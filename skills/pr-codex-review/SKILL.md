---
name: pr-codex-review
description: Loop on a PR's automated Codex review — fix valid points, spin off out-of-scope ones as issues, merge on thumbs-up, and remove the merged branch.
disable-model-invocation: true
---

# PR Codex Review Loop

Work the review loop on the current PR (or the PR the user names) until it earns a thumbs-up, merges, and its branch is removed, or until the review is wrong.

Use `gh` for all PR, review, comment, reaction, and issue operations.

## The loop

1. **Check for a new round.** Fetch reviews and review comments on the PR. A round is *new* only if it was posted after the latest push to the PR branch. If there is nothing new yet, wait and re-check (step 5's cadence).
2. **Read the round and classify.**
   - **Thumbs-up**: the round is just a 👍 reaction on the PR (or an approval with no requested changes). The PR is good — merge it, then continue to step 6.
   - **Substantive review**: evaluate every point on its merits before acting. Sort each point into exactly one bucket:
     - **Valid, in scope** — fix it in this PR.
     - **Valid, out of scope** — better handled separately. Open a GitHub issue for it with enough context to stand alone, and reply on the review thread linking the issue.
     - **Invalid / wrong** — the review misreads the code or asks for something incorrect.
3. **Stop gate.** If the review as a whole is invalid or wrong, stop the loop and report to the user why, point by point. Push nothing.
4. **Fix and push.** Apply all in-scope fixes, verify they build/test, and push a new commit to the PR branch. Every point from the round must be accounted for: fixed, issue-filed, or explained as invalid.
5. **Wait for the next round.** After pushing, wait 10 minutes (`sleep 600`) for the reviewer to respond, then return to step 1.
6. **Remove the merged branch.** After confirming the merge succeeded, delete the PR head branch from the remote and the local repository. Never delete the base or default branch. If the head branch is checked out locally, switch to the base branch before deleting it. Confirm both copies are gone before finishing.

The loop ends only after merge and branch cleanup (thumbs-up), the stop gate (invalid review), or the user calling it off.
