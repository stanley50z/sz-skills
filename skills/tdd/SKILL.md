---
name: tdd
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development

TDD is the red → green loop. This skill keeps Matt Pocock's upstream `tdd`
core (agreed seams, independent expected values, vertical slices) plus local
requirements: command timeouts, user-requirement test priority, explicit
failure over fallbacks, stale-version cleanup, and a final end-to-end run on
real data.

When exploring the codebase, use the project's domain glossary so test names
match its language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details.
A good test reads like a specification ("user can checkout with valid cart")
and survives refactors because it ignores internal structure. See
[tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking.

Derive tests from what the user asked for, in this order:

1. User-requirement tests: each requested behavior, checked from the outside.
2. Edge case and error tests at the boundaries of that behavior.
3. Implementation tests only when internal logic is complex enough that the
   user would care if it worked differently.

Expected values come from an independent source of truth: a spec example, a
known literal, a fixture, a worked scenario. An assertion that recomputes the
value the way the code does (`expect(add(a, b)).toBe(a + b)`) is tautological
and passes by construction.

## Seams

A **seam** is the public boundary you test at. Every test sits at an agreed
seam: write down the seams under test and confirm them with the user before
the first test, unless the spec already pins them. No test targets an
unconfirmed internal helper because it is convenient.

When the shape of the interface itself is in question (module depth, seam
placement, what to expose), load `codebase-design` for the vocabulary: use
the native Skill tool when the harness has one, otherwise read its
`SKILL.md`. It is a reference to consult, not a session to run. See also
[deep-modules.md](deep-modules.md) and [interface-design.md](interface-design.md).

## Timeouts

Every test command runs under a **command-level timeout** that kills the
process: `timeout 60 pytest ...`, the tool's own timeout parameter, or the
platform equivalent. Runner-level test timeouts help but do not replace it.

- Focused RED/GREEN check: 30-60 seconds
- File or package suite: 2-5 minutes
- Full project suite: 5-15 minutes

A timeout is a failure to debug; change something before rerunning.

## UI changes

When the change touches anything a user sees in a browser, read
[visual-tests.md](visual-tests.md) before the first cycle. It is the
canonical policy for checking UI look-and-feel visually on desktop and for
the live browser walkthrough of UI behavior; it replaces the code-test
artifact for look-and-feel in the loop below.

## The loop

Plan first: confirm the seams, list behaviors (not implementation steps),
identify the real entry point and available real data for the final run, and
confirm whether existing behavior is being kept or replaced.

Then work in **vertical slices**, one tracer bullet at a time. Writing all
tests first and all code after tests imagined behavior and commits to test
structure before you understand the implementation.

```text
RED:   one test for the next behavior, run with a timeout -> fails for the expected reason
GREEN: the minimal code to pass it, run with a timeout -> passes
```

Repeat per behavior. A RED that fails from a typo, setup error, or hang does
not count. Write only enough code for the current test; no speculative
features.

## Explicit failure

<HARD-GATE>
Never write fallback code, default returns, or silent error swallowing to make
a test pass. If the feature doesn't work, the code fails explicitly.
</HARD-GATE>

- Handle errors only for expected, user-facing error cases the requirements
  name. A `try/catch`, default return, or `?? fallbackValue` added to turn a
  test green hides a broken feature.
- If you can't implement the feature, let the test stay red and say so.
- If the planned approach keeps failing, stop and present alternatives to the
  user instead of silently switching approaches.

## Replacing existing behavior

When the user asks to upgrade or replace existing behavior with a new version:

- Remove or update stale tests for the replaced behavior first; they pull the
  implementation back toward the old version.
- Add backward compatibility only when the user explicitly asks for it. No
  `if new fails, fall back to old` paths.
- If the new version can't be built as described, surface the problem rather
  than silently keeping the old one.

## After green: review, then refactor

Refactoring is not part of the loop; never refactor while RED. Once behavior
is green, review the diff: for non-trivial independent work load `code-review`
(native Skill tool when the harness has one, otherwise read its `SKILL.md`).
Use its findings and [refactoring.md](refactoring.md) to clean up, rerunning
tests with a timeout after each step.

When the caller owns the review phase (`implement`, `implement-spec`), skip
this review and defer review-driven refactoring to the caller, which reviews
from its resolved comparison point.

## Done gate

Before calling the work done:

- [ ] Every user requirement has at least one end-to-end test or verified run
      through the real entry point (CLI, HTTP request, browser workflow),
      full stack, no mocked internals.
- [ ] The final end-to-end run used real data when real or production-like
      data exists; report explicitly when only synthetic data was available.
- [ ] UI changes passed the checks in [visual-tests.md](visual-tests.md),
      including the live browser walkthrough.
- [ ] The full test suite passed once, under a timeout. A required test
      that was unexpectedly skipped or uncollected counts as failed.

If the end-to-end pass exposes a failure, return to the loop; do not patch
around it or declare partial success.
