---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

# Implement

Implement the work described by the user in the spec or tickets.

Work one ticket at a time from the frontier (tickets whose blockers are all done). Read the ticket's **Requirement** and its `[USER-REQ]` / `[AGENT-DECISION]` tag before coding.

Use `/tdd` where possible, at pre-agreed seams. For UI layout, styling, responsive behavior, visual hierarchy, and interaction states, use the visual RED/GREEN checks from the tdd skill — no component tests, DOM assertions, or snapshot tests.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

## Hard Rules

- **No fallbacks, no silent failure.** Implement the feature for real — no default returns, no swallowed errors, no `?? fallbackValue` to make a test pass. If it can't be implemented, let the test fail and say so.
- **Suggest, don't auto-apply.** When the planned approach keeps failing, stop and present alternatives to the user. The user decides which direction to take.
- **`[USER-REQ]` is non-negotiable.** If a user requirement cannot be met as specified, stop and ask. `[AGENT-DECISION]` items can be adapted when implementation reality demands it.
- **Version upgrades:** when replacing v1 with v2, remove or rewrite stale v1 tests *before* implementing v2. Never add v1 fallback paths unless the user explicitly asks for backward compatibility.

## When the User Requests a Change Mid-Implementation

Treat it as a new User Requirement and propagate it to every artifact, not just the code in front of you:

1. **Spec** (`docs/specs/`) — update the User Requirements section
2. **Tickets** (`docs/plans/`) — update or add `[USER-REQ]` tickets, remove stale ones
3. **Tests** — remove/rewrite tests for old behavior, write tests for new
4. **Implementation** — update the code

A mid-implementation change has the same authority as an initial requirement stated during grilling.

## Close Out

Once done, use `/code-review` to review the work, address what it finds, then commit to the current branch with the commit skill. When the whole feature branch is complete, the finishing-a-development-branch skill handles the user-testing gate before final wrap-up.
