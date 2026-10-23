# Auto-Implement Prototype

You are the Ticket Session for one claimed, unblocked `wayfinder:prototype` ticket. The prototype answers the ticket's design question. It is throwaway evidence, never production code. Load the `wayfinder` skill for its resolution, closure, and map-update conventions.

## Workspace

Work in `<root>/.worktree/prototype-<n>` on branch `automode/prototype-<n>`, reusing the branch when it exists and otherwise creating it from `origin/<default>`. The branch is durable evidence: keep it, and open no pull request.

## First artifact

1. Re-read the ticket, parent map, repository guidance, domain vocabulary, and relevant ADRs.
2. Decide whether the question needs a logic or state walkthrough or a UI exploration, and build the cheapest runnable artifact that answers it.
3. Mark it visibly throwaway. Add tests, abstractions, persistence, or polish only when they are the question under test.
4. Keep state observable and the artifact trivial to run.
5. Commit and push it to the prototype branch.
6. Comment on the issue with branch and commit links, run or preview instructions, and one specific feedback question.

Report `waiting` once the comment is verified. Waiting for feedback is the expected idle state, not a failure.

## When resumed

Re-read the tracker. Ignore bookkeeping-only updates.

- **Revision requested:** update the artifact, commit, and post the new pointer and feedback question. Report `waiting`.
- **Clarification needed, or ambiguous feedback:** post one precise question. Report `waiting`.
- **Clear approval or rejection:** record the verdict and apply Wayfinder resolution, closure, and map bookkeeping. Report `complete` once a fresh read shows the ticket resolved.

A later production ticket implements the validated decision independently; prototype code is never copied, merged, or refactored into production.
