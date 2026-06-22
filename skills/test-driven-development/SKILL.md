---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development

This skill is based on Matt Pocock's `tdd` skill, kept under the
Superpowers-compatible `test-driven-development` name. It retains the local
requirements for command timeouts, user-requirement test priority, explicit
failure over fallback behavior, stale v1/v2 test cleanup, and visual-only UI
testing.

## Philosophy

**Core principle**: Tests should verify behavior through public interfaces,
not implementation details. Code can change entirely; tests shouldn't.

**Good tests** are integration-style: they exercise real code paths through
public APIs. They describe what the system does, not how it does it. A good
test reads like a specification - "user can checkout with valid cart" tells
you exactly what capability exists. These tests survive refactors because they
don't care about internal structure.

**Bad tests** are coupled to implementation. They mock internal collaborators,
test private methods, or verify through external means (like querying a
database directly instead of using the interface). The warning sign: your test
breaks when you refactor, but behavior hasn't changed. If you rename an
internal function and tests fail, those tests were testing implementation, not
behavior.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking
guidelines.

For UI work, see [visual-tests.md](visual-tests.md). UI tests are visual
checks, not code tests.

## Timeout Rule

Every test run MUST have a command-level timeout. This is a first-class TDD
rule, not an optional safety net.

If a test command can hang, the agent can hang with it. Never run bare
`npm test`, `pytest`, `go test`, `cargo test`, `vitest`, `jest`, `bun test`,
`deno test`, or similar commands without a timeout around the process.

Use an external timeout that kills the stuck process, not just an in-test
assertion timeout. Runner-level test timeouts help, but they do not replace a
command-level timeout.

Reasonable defaults:

- Single test or focused RED/GREEN check: 30-60 seconds
- Small package or file-level suite: 2-5 minutes
- Full project suite: 5-15 minutes

If a command times out, treat that as a failure that must be debugged. Do not
re-run the same hanging command without changing anything.

## What to Test First

Tests should be derived from user requirements, not implementation details.

If the spec has "User Requirements" and "Agent Design Decisions" sections, the
user requirements drive the primary test suite. Each user requirement should
have at least one behavioral test that verifies the feature works as the user
described it, from the outside.

Agent design decisions get lighter testing. They're often covered implicitly by
the user-requirement tests. Don't write separate tests for internal functions
just because they exist.

Test hierarchy:

1. User-requirement tests - verify features the user asked for, from the user's
   perspective.
2. Edge case / error tests - cover failure modes and boundaries of the
   user-facing behavior.
3. Implementation tests - only when the internal behavior is complex enough to
   warrant direct verification. Ask: "would the user care if this worked
   differently internally?" If no, skip the dedicated internal test.

The test for "login redirects to dashboard" is not
`expect(generateToken()).toBeString()`. It is
`expect(afterLogin().currentPage).toBe('/dashboard')`. Test the feature, not
the plumbing.

## UI Tests Are Visual

<HARD-GATE>
All UI testing is visual testing. Do not write code tests for UI layout,
styling, responsive behavior, visual hierarchy, or interaction states.
</HARD-GATE>

For UI work, the RED/GREEN loop is still one behavior at a time, but the test
artifact is visual evidence and inspection notes. Use [visual-tests.md](visual-tests.md)
for the checklist.

Tool priority:

1. Use the strongest available real-browser inspection tool that supports
   screenshots, live inspection, and simulated clicks/keys.
2. For local `file://` pages, prefer Chrome DevTools MCP when it is available.
3. In Codex, the Chrome plugin may satisfy this role; in Claude Code, t3code,
   or other harnesses, use Chrome DevTools MCP or the harness's equivalent
   DevTools/browser MCP.
4. If no DevTools-capable browser tool is available, use the best available
   browser/screenshot tool and state the fallback.

Project instructions may name a more specific browser tool for a target. Follow
those instructions when they are more specific than this default order.

Visual checks must cover:

- Text is not clipped, truncated unexpectedly, overflowing its container, or
  hidden behind other elements.
- UI components align to a coherent grid and do not drift by a few pixels.
- Horizontal and vertical visual weight feel balanced; the screen should not
  feel lopsided, crowded in one area, or empty in another.
- Spacing, grouping, and hierarchy make the primary workflow obvious.
- Interactive states are visible and usable: hover, focus, active, disabled,
  selected, loading, empty, and error states when relevant.
- Responsive layouts work at realistic desktop and mobile viewports.
- The inspection is based on screenshots or live browser observation, not DOM
  guesses or implementation details.

## Anti-Pattern: Horizontal Slices

**DO NOT write all tests first, then all implementation.** This is "horizontal
slicing" - treating RED as "write all tests" and GREEN as "write all code."

This produces poor tests:

- Tests written in bulk test imagined behavior, not actual behavior
- You end up testing the shape of things (data structures, function signatures)
  rather than user-facing behavior
- Tests become insensitive to real changes - they pass when behavior breaks,
  fail when behavior is fine
- You outrun your headlights, committing to test structure before understanding
  the implementation

**Correct approach**: Vertical slices via tracer bullets. One test -> one
implementation -> repeat. Each test responds to what you learned from the
previous cycle. Because you just wrote the code, you know exactly what behavior
matters and how to verify it.

```text
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED->GREEN: test1->impl1
  RED->GREEN: test2->impl2
  RED->GREEN: test3->impl3
  ...
```

## Workflow

### 1. Planning

When exploring the codebase, use the project's domain glossary so that test
names and interface vocabulary match the project's language, and respect ADRs
in the area you're touching.

Before writing any code:

- [ ] Confirm with user what interface changes are needed
- [ ] Confirm with user which user-facing behaviors to test first
- [ ] For UI changes, define the visual states and viewports to inspect
- [ ] Identify opportunities for [deep modules](deep-modules.md)
- [ ] Design interfaces for [testability](interface-design.md)
- [ ] List the behaviors to test, not implementation steps
- [ ] Confirm whether existing v1 behavior is being preserved or replaced

Ask: "What should the public interface look like? Which behaviors are most
important to test?"

You can't test everything. Focus testing effort on user requirements, critical
paths, and complex logic, not every possible edge case.

### 2. Tracer Bullet

Write ONE test that confirms ONE thing about the system:

```text
RED:   Write test for first behavior -> test fails
GREEN: Write minimal code to pass -> test passes
```

This is your tracer bullet - it proves the path works end-to-end.

Verify RED with a timeout. Confirm the test fails for the expected reason
(feature missing), not because of a typo, setup error, or hang.

### 3. Incremental Loop

For each remaining behavior:

```text
RED:   Write next test -> fails
GREEN: Minimal code to pass -> passes
```

Rules:

- One test at a time
- Only enough code to pass the current test
- Don't anticipate future tests
- Keep tests focused on observable behavior
- Run every RED and GREEN check with a timeout
- For UI, use visual inspection instead of code tests

### 4. No Fallbacks, No Silent Failure

<HARD-GATE>
Never write fallback code, default returns, or silent error swallowing to make a
test pass. If the feature doesn't work, the code must fail explicitly.
</HARD-GATE>

Bad:

```typescript
function search(query: string): Result[] {
  try {
    return database.search(query);
  } catch {
    return [];
  }
}
```

That code can make a test green while hiding a broken feature.

Good:

```typescript
function search(query: string): Result[] {
  return database.search(query);
}
```

Rules:

- If you can't implement the feature, let the test fail. Don't fake it.
- Error handling is for expected user-facing error cases, not for masking
  incomplete implementation.
- If you're adding a `try/catch`, default return, or `?? fallbackValue` to make
  a test green, stop and ask whether the code works correctly in production.
- If the planned approach keeps failing, stop and present alternatives to the
  user instead of silently switching approaches.

### 5. Version Upgrades

When the user asks to upgrade, expand, or replace existing behavior (v1) with a
new version (v2):

- Remove or update stale v1 tests first. Tests asserting intentionally replaced
  behavior will pull the implementation back toward v1.
- Never create `if v2 fails, fall back to v1` code unless the user explicitly
  asks for backward compatibility.
- Write new tests for v2 behavior. The test suite should reflect what the user
  wants now, not what existed before.
- If v2 can't be implemented as described, surface the problem. Don't silently
  preserve v1.

### 6. Refactor

After all tests pass, look for [refactor candidates](refactoring.md):

- [ ] Extract duplication
- [ ] Deepen modules by moving complexity behind simple interfaces
- [ ] Apply SOLID principles where natural
- [ ] Consider what new code reveals about existing code
- [ ] Run tests after each refactor step, with a timeout

**Never refactor while RED.** Get to GREEN first.

## Checklist Per Cycle

```text
[ ] Test is driven by a user requirement, edge case, or justified internal complexity
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] RED run failed for the expected reason
[ ] RED and GREEN commands used command-level timeouts
[ ] UI changes were verified visually, not with code tests
[ ] Visual check covered clipping/overflow, alignment, visual balance, states, and responsive viewports
[ ] Code is minimal for this test
[ ] No speculative features added
[ ] No fallback/default/silent failure added to make the test pass
[ ] Stale v1 tests were removed or updated before implementing v2 behavior
```
