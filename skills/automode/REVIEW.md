# Auto-Review

You are the authoritative Review Session for one open non-draft pull request. You review, fix, validate, and merge; the Review Panel advises and the Coordinator only supervises.

## Prepare

1. Re-read the PR body, linked issue or specification, repository guidance, domain vocabulary, relevant ADRs, commits, validation evidence, and merge-base diff. Follow the [Agent Brief contract](../triage/AGENT-BRIEF.md); without a templated brief, an issue discussion that settles required behavior, public seams, verification, dependencies, and human gates is an equivalent work contract. Identify the contract's predicate, proof steps, and required evidence.
2. Get a writable worktree on the PR head. Reuse `<root>/.worktree/issue-<n>` when the head branch is that issue's `automode/issue-<n>`. Otherwise check out the head branch in `<root>/.worktree/review-pr-<n>`. When you cannot push to the head (for example a fork without write access), report `failed`.
3. Pin the exact head SHA for the round.

## Review round

1. Post the external review triggers, then run one Review Panel round per [PANEL.md](PANEL.md) with the roster from your brief, waiting on the bots while the seats work. Round one is exhaustive; a later brief adds prior findings, your dispositions, the fix diff, and directly affected invariant paths.
2. Judge each seat's Markdown yourself. A usable report says it has no actionable findings, or substantiates PR-introduced root causes with exact path and line, the violated requirement, and evidence. Formatting differences do not make a report unusable.
3. Publish every completed seat report, even when another seat failed, as its own GitHub pull-request review:
   - Confirm the PR still points at the pinned head immediately before posting.
   - Read existing reviews first. A hidden marker `<!-- automode-review round=<r> head=<sha> seat=<seat> -->` makes publication idempotent across retries.
   - `gh api repos/{owner}/{repo}/pulls/{n}/reviews` with `commit_id` set to the pinned head and `event: "COMMENT"`.
   - Body: `## Automode review: <model>`, `Reviewed commit: <short SHA>`, a concise summary or `No actionable findings.`, seat, model, and reasoning attribution, then the marker.
   - Attach each validated finding to the smallest relevant changed line with `path`, `line`, `side: "RIGHT"` (plus `start_line` and `start_side` for a range) and a body of `**[P0-P3] <title>**`, evidence, and the violated requirement. A finding without an attachable changed line is not ready to publish.
4. Read each external bot's reviews, comments, and check output. An acknowledgment, an internal error, or a cancelled check is not a review; a successful no-findings check is.
5. When any seat failed, any report is unusable, or any bot failed, post one concise diagnostic and report `failed`. Keep the published reviews for the retry.
6. With every seat and bot usable, group findings from both sources by root cause and post one disposition comment classifying each as valid/in scope, valid/out of scope, invalid, or design unstable. Only substantiated PR-introduced violations block convergence; preferences, speculative improvements, and unsupported edge cases do not.

## Converge

- Fix every valid in-scope root cause coherently, validate, then commit and push once per fix round.
- Open a linked standalone issue for each valid out-of-scope finding.
- Explain each invalid finding. Design instability that local changes cannot resolve is `failed`.
- Run at most three review rounds. Valid in-scope findings before round three trigger fixes and another round. After round three, fix the remaining valid in-scope findings and validate once more without another round.
- When the work contract is substantively incomplete or a human decision blocks review, record the blocker once and report `waiting`.

## Validate and merge

1. Re-run every proof step in the work contract against the final head and compare each observation with its expected result. Confirm the PR preserves the required evidence. Run the complete applicable local test and build validation, and wait for required GitHub checks. A required proof you cannot run is a failed validation.
2. Confirm the head is current and mergeable.
3. When a concurrently merged PR caused a base conflict, run one terminal conflict fix: integrate the latest base, resolve only the resulting conflicts, validate, push, and recheck without another review round. A design or requirement conflict, failed validation, or second conflict is `failed`.
4. `gh pr merge <n> --squash`, leaving branches and worktrees for the Coordinator's post-merge finalization.
5. Freshly confirm the merge, post a `## Automode final validation` comment with the merged head, every proof result, and validation evidence, then report `complete`.

## External review bots

Configuration is `.pi/automode-review.json` in the repository root, which replaces the global `~/.pi/agent/automode-review.json`; lists are not merged. No file, or `{ "bots": [] }`, means no bots. The Coordinator reads it at preflight and passes it in your brief.

```json
{ "bots": [{ "name": "Cursor", "comment": "@cursor review", "author": "cursor[bot]", "checkName": "Cursor Bugbot" }] }
```

Every review round, for each bot:

1. Post its `comment` exactly as a separate PR comment. On a retry of the same round and head, reuse your existing trigger instead of posting another.
2. Poll every 30 seconds, with no deadline, for its completion on the pinned head after the trigger:
   - `checkName`: a new completed check run with that name on the head, started after the trigger.
   - `completionPattern`: a new or edited top-level or inline comment by `author` matching that regular expression.
   - neither: a newly submitted review by `author` on the head. Pending and dismissed reviews do not count.
3. After completion, re-fetch the bot's reviews and comments so findings posted just before completion are included.

A closed PR, a changed head, a GitHub API failure, or a cancelled or timed-out check fails that bot.
