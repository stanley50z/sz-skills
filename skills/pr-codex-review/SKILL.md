---
name: pr-codex-review
description: Run a convergent, user-invoked Codex review loop on a pull request — use custom prompts to front-load findings, verify fixes, escalate unstable designs, merge a clean head, and remove the merged branch.
disable-model-invocation: true
---

# PR Codex Review Loop

Run a prompt-driven, manually triggered Codex review loop on the current PR (or the PR the user names). Assume automatic Codex reviews are disabled.

Use `gh` for all PR, review, comment, reaction, and issue operations. Track requested head SHAs, the previous reviewed SHA, prior findings, and their root causes.

## Review requests

Use the review comment itself as the custom reviewer prompt. Keep the cycle contract in these review comments instead of global repository review instructions, so it applies only when this skill is invoked. Never send a bare `@codex review` request. Post exactly one custom review request for each head SHA.

Post the initial request immediately:

```text
@codex review current head <HEAD_SHA>.

Treat this as the complete initial review pass for this PR. Report only P0/P1 correctness regressions introduced by this PR. Report all independent P0/P1 root causes you can substantiate now; do not hold findings for later rounds. Review the PR's stated invariants and failure modes as a whole. Group every manifestation of the same missing invariant into one root-cause finding, cite the strongest concrete manifestation, and state the invariant that must hold.

If a local fix cannot make an invariant hold across the full affected path, write `DESIGN STOP: <root cause and why redesign is required>` instead of proposing another piecemeal patch.

Focus especially on: <TWO_OR_THREE_PR_SPECIFIC_RISKS>.

When no P0/P1 root cause remains, return no findings so the review closes cleanly.
```

Derive the focus risks from the PR description, linked issue, applicable repository guidance, and changed code. For concurrency or state-machine work, ask Codex to examine the relevant transition and failure matrix.

Post the follow-up request immediately after pushing:

```text
@codex review current head <HEAD_SHA>. The previous reviewed head was <PREVIOUS_REVIEWED_SHA>.

This is a verification pass, not a fresh review. Check each prior root-cause finding against the current code. Report only:
1. a prior finding that is not actually fixed; or
2. a P0/P1 regression introduced by the fix within a directly affected invariant path.

Do not report unrelated defects from untouched original code. Do not split or rename a previously grouped root cause into new variants. If verification shows that a local fix cannot make the invariant hold across the full affected path, write `DESIGN STOP: <root cause and why redesign is required>`.

If all prior findings are resolved and no fix-induced P0/P1 remains, return no findings now so this review closes cleanly.
```

## Convergence contract

- Use the initial review for the complete PR-wide search. Use every later review only to verify prior root causes and their fixes.
- Only an unresolved prior root cause or a P0/P1 caused by its fix may keep the cycle open after the initial review.
- Treat a valid follow-up finding in untouched original code as out of scope: file an issue, reply with the link, and do not let it trigger another fix/review round.
- Treat `DESIGN STOP` or equivalent evidence that no local fix can close the invariant as design unstable. Stop and present redesign or split options.
- When a round has no valid in-cycle findings and every prior root cause is resolved, treat the head as clean even if the review also contains invalid or explicitly out-of-scope comments.

## The loop

1. **Request the review.** Resolve the current head SHA. Post the initial or follow-up custom prompt above immediately unless that exact head has already been requested. Never post a duplicate request for the same head.
2. **Wait for the requested review.** Schedule one 10-minute wait or delayed wake-up, then continue to step 3. Prefer the runtime's non-blocking delayed-continuation or monitoring mechanism over a foreground shell sleep. Do not implement the wait as repeated one-minute sleeps, narrate each elapsed minute, or query GitHub before the interval closes.

   An acknowledgement is not a completed round; wait another interval without posting again. If Codex reports a usage limit, permission failure, or service failure, treat the loop as blocked. Stop immediately and report the blocker. Do not retry until the user explicitly resumes.
3. **Check for a completed round.** Fetch reactions on the PR, reviews, review comments, and review-thread replies, and identify which activity came from Codex. Match reviews and review comments to the exact current head SHA; do not use timestamp alone. A PR-level 👍 counts only when it was posted after the request for the current head and the head has not changed. Coalesce findings for that head that arrive before acting into one substantive round. Process at most one completed substantive round per head SHA. If there is no completed round, return to step 2 without posting again.
4. **Read the round and classify.**
   - **Clean review**: the exact current head receives a qualifying 👍 reaction or approval with no requested changes. Before merging, confirm the head SHA has not changed since the clean review, no unresolved P0/P1 findings remain in the review cycle, and required validation is green. Merge, then continue to step 7.
   - **Substantive review**: evaluate every point on its merits, group manifestations by root cause, and sort each root cause into exactly one bucket:
     - **Valid, in scope** — fix it in this PR.
     - **Valid, out of scope** — better handled separately. Open a GitHub issue for it with enough context to stand alone, and reply on the review thread linking the issue.
     - **Valid, design unstable** — Codex returns `DESIGN STOP`, or the finding otherwise shows that a local fix cannot close the invariant. Stop and present the root cause and redesign/split options.
     - **Invalid / wrong** — the review misreads the code or asks for something incorrect.
5. **Stop or close gate.** Stop and report if the review is broadly invalid or any root cause is design unstable. If the round has no valid in-cycle findings and all prior root causes are resolved, apply the clean-review checks, merge, and continue to step 7.
6. **Fix and push.** Apply all valid in-cycle fixes, verify they build/test, and push one new commit for the round. Every root cause must be accounted for as fixed, issue-filed, design-stopped, or invalid. Record the reviewed SHA, findings, and root causes, then return to step 1 so the verification prompt is posted immediately.
7. **Remove the merged branch.** After confirming the merge succeeded, delete the PR head branch from the remote and the local repository. Never delete the base or default branch. If the head branch is checked out locally, switch to the base branch before deleting it. Confirm both copies are gone before finishing.

The loop ends after merge and branch cleanup, an invalid or design-unstable review, a reviewer blocker, or the user calling it off.
