---
name: implement-spec
description: "Implement the result of /to-spec and /to-tickets in code."
disable-model-invocation: true
---

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

The goal is the entire spec implemented on a single **integration branch**, delivered as one pull request that resolves every implementation ticket.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed. A ticket counts as done for the frontier once it lands on the integration branch. Its issue stays open until the pull request merges, so track progress from landed work, not from issue state.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Shared policy

This skill orchestrates; it does not run the single-ticket `/implement` close-out, which branches and opens its own pull request. Workers reuse the approved policy instead:

- **Tests**: every implementer subagent and the review-fix subagent load the `tdd` skill and build at the seams the spec and tickets pin. This orchestrator's caller owns the review phase, so workers skip tdd's per-change review; step 8 reviews the integrated result.
- **Requirement changes**: follow [`../implement/REQUIREMENT-CHANGES.md`](../implement/REQUIREMENT-CHANGES.md). Pause affected workers until the spec and tickets are updated.
- **Human decisions**: a worker that hits a decision the spec and tickets do not pin (a product choice, a seam change, ambiguous acceptance criteria) stops and reports the question. Ask the user, record the answer on the ticket, then resume that ticket. Other frontier tickets keep going.

## Steps

1. Read the spec and tickets to understand the task graph.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Resolve the repository's default branch from Git or hosting metadata; for a fork, use the default branch of the repository that will receive the pull request. Fetch it, create the integration branch from its latest remote tip, and keep that start commit for review.

4. Use **implementer subagents** to implement each frontier ticket, each in a task-owned worktree outside the repo checkout, on its own ticket branch created from the latest integration tip. Each implementer subagent:
   - confirms its worktree is based on the integration branch before starting;
   - installs dependencies and provides the gitignored test inputs and data the tests need, copying or linking local files without committing them or exposing secrets; an unexpectedly skipped or uncollected required test fails verification under the [tdd done gate](../tdd/SKILL.md);
   - builds the ticket under the shared policy;
   - commits only its ticket's changes on its ticket branch, staging exact paths and leaving secrets unstaged;
   - merges the latest integration tip into its branch and reruns the ticket's tests before reporting done.

5. Land completed work with a **merger subagent**, one landing at a time. Before each landing, confirm the ticket branch contains the latest integration tip; if another ticket landed meanwhile, merge the new tip and rerun the ticket's tests first. Push the integration branch after each landing. After the first landing, open a draft pull request that targets the default branch.

6. If a landing changes the **frontier**, kick off more **implementer subagents** for the new tickets. This allows for maximum concurrency.

7. Once every ticket has landed, run the aggregate validation on the integration branch: the full test suite and the tdd done gate's end-to-end run through the real entry point, covering every requirement in the spec. Treat failures as review findings for step 8.

8. Load the `code-review` skill with the integration branch's start commit as the resolved comparison point, plus the spec and ticket references. Fix everything it and the aggregate validation raised in a single **implementer subagent**, landed like any ticket. Then rerun the aggregate validation; repeat until it passes.

9. Load the `pr` skill to write the body. Add a line that links the spec and a closing reference for every implementation ticket. Mark the pull request ready for review.

10. Keep the integration branch and its open pull request. Remove only the task-owned ticket and fix worktrees and their ticket and fix branches, after their work has landed. Report the pull request and integration branch, then ask the user to test the feature themselves.
