---
name: pr-codex-review
description: Run a bounded, user-invoked Codex review loop on a pull request — request focused reviews, fix valid findings, escalate unstable designs, merge a clean head, and remove the merged branch.
disable-model-invocation: true
---

# PR Codex Review Loop

Run a bounded, manually triggered Codex review loop on the current PR (or the PR the user names). Assume automatic Codex reviews are disabled.

Use `gh` for all PR, review, comment, reaction, and issue operations. Track the initial head and base SHAs, changed-line count, start time, requested head SHAs, previous reviewed SHA, substantive-round count, and finding root causes.

## Review requests

Only post `@codex review` once for each exact head SHA. Never post a duplicate request for the same head.

Post the initial request immediately:

```text
@codex review current head <HEAD_SHA>. Report only P0/P1 correctness regressions introduced by this PR. Review the PR's stated invariants and failure modes as a whole. Group manifestations of the same missing invariant into one root-cause finding. If correctness requires architectural redesign rather than a bounded patch, say so explicitly. Focus especially on: <TWO_OR_THREE_PR_SPECIFIC_RISKS>.
```

Derive the focus risks from the PR description, linked issue, applicable repository guidance, and changed code. For concurrency or state-machine work, ask Codex to examine the relevant transition and failure matrix.

Post the follow-up request immediately after pushing:

```text
@codex review current head <HEAD_SHA>. The previous reviewed head was <PREVIOUS_REVIEWED_SHA>. Verify the previous findings and report only P0/P1 regressions introduced by their fixes, or defects in directly affected invariant paths. Do not start a fresh search of unrelated untouched parts of the original diff. Group manifestations of the same missing invariant into one root-cause finding. If a bounded patch cannot close the invariant, say that redesign is required.
```

## Convergence guard

Group findings by root cause before changing code. Treat repeated symptoms of one missing invariant as one design problem, not an invitation to stack local patches.

- After 3 substantive rounds, pause and give the user a convergence checkpoint: root causes found, PR growth, elapsed time, remaining risks, and a recommendation to continue, redesign, or split follow-up work.
- Hard-stop after 5 substantive rounds, the same missing invariant or core area in two consecutive rounds, 2 hours of wall-clock loop time, or growth beyond `max(500 changed lines, 25% of the initial changed-line count)`.
- After a checkpoint or hard stop, do not modify or push more code unless the user explicitly authorizes continuation with a new budget.

## The loop

1. **Request the review.** Resolve the current head SHA. Post the initial or follow-up request above immediately unless that exact head has already been requested.
2. **Wait for the requested review.** Schedule one 10-minute wait or delayed wake-up, then check the convergence guard and continue to step 3. Prefer the runtime's non-blocking delayed-continuation or monitoring mechanism over a foreground shell sleep. Do not implement the wait as repeated one-minute sleeps, narrate each elapsed minute, or query GitHub before the interval closes.

   An acknowledgement is not a completed round; wait another interval without posting again. If Codex reports a usage limit, permission failure, or service failure, treat the loop as blocked. Stop immediately and report the blocker. Do not retry until the user explicitly resumes.
3. **Check for a completed round.** Fetch reactions on the PR, reviews, review comments, and review-thread replies, and identify which activity came from Codex. Match reviews and review comments to the exact current head SHA; do not use timestamp alone. A PR-level 👍 counts only when it was posted after the request for the current head and the head has not changed. Coalesce findings for that head that arrive before acting into one substantive round. Process at most one completed substantive round per head SHA. If there is no completed round, return to step 2 without posting again.
4. **Read the round and classify.**
   - **Clean review**: the exact current head receives a qualifying 👍 reaction or approval with no requested changes. Before merging, confirm the head SHA has not changed since the clean review, no unresolved P0/P1 findings remain, and required validation is green. Merge, then continue to step 7.
   - **Substantive review**: increment the substantive-round count, evaluate every point on its merits, and sort each point into exactly one bucket:
     - **Valid, in scope** — fix it in this PR.
     - **Valid, out of scope** — better handled separately. Open a GitHub issue for it with enough context to stand alone, and reply on the review thread linking the issue.
     - **Valid, design unstable** — the point reveals a repeated missing invariant, architectural flaw, or material scope expansion that is unsafe to repair piecemeal. Stop and present the root cause and redesign/split options.
     - **Invalid / wrong** — the review misreads the code or asks for something incorrect.
5. **Stop gate.** Group findings by root cause and apply the convergence guard before changing code. Stop if the review is broadly invalid or wrong, any point is classified as design unstable, or a checkpoint/hard-stop threshold is reached. Report point by point and push nothing.
6. **Fix and push.** Apply all in-scope fixes, verify they build/test, and push one new commit for the round. Every point must be accounted for as fixed, issue-filed, or invalid. Record the reviewed SHA and root causes, then return to step 1 so the focused follow-up request is posted immediately.
7. **Remove the merged branch.** After confirming the merge succeeded, delete the PR head branch from the remote and the local repository. Never delete the base or default branch. If the head branch is checked out locally, switch to the base branch before deleting it. Confirm both copies are gone before finishing.

The loop ends after merge and branch cleanup, a convergence checkpoint/hard stop, an invalid or design-unstable review, a reviewer blocker, or the user calling it off.
