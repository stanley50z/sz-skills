# mattpocock/skills Suite Customization Rationale

This document explains why and how the [mattpocock/skills](https://github.com/mattpocock/skills) v1.2 suite was customized for this repo. The suite is this repo's development cycle: `grill-with-docs` (or `wayfinder`) → `to-spec` → `to-tickets` → `implement` per ticket (drives `tdd`, closes with `code-review` + `commit`), with `diagnosing-bugs`, `research`, `prototype`, `triage`, and the reference skills alongside.

Most of the suite is vendored unmodified and auto-updated by `update.py`. Seven skills carry local edits and are listed in `update.PATCHED`, so updates skip them: `setup-matt-pocock-skills`, `to-spec`, `to-tickets`, `implement`, `tdd`, `prototype`, and `handoff`. Each customization below records the problem it solves, the change, and the files it touches.

**Origin:** the suite replaced the [obra/superpowers](https://github.com/obra/superpowers) suite in 2026-07. Several customizations below (requirement-driven testing, no-fallback rules, visual UI testing, change propagation, HTML companions, the user testing gate) were carried over from that era because the failure modes they guard against are model- and suite-independent. The superpowers-era rationale document and its migration history were removed with the suite; both are preserved in git history (`docs/superpowers-customization-rationale.md`, deleted 2026-07).

## 1. Requirement-Driven Testing

**Problem:** Left alone, agents write a failing test for every piece of code, which produces too many tests, tests that mirror implementation (tautologies that pass by construction), and tests that miss real problems — the feature can be broken while everything is green, because the tests verify internal plumbing rather than user-facing behavior.

**Solution:** The tdd skill derives tests from user requirements and applies a hierarchy:

1. **User-requirement tests** — verify features as the user described them, from the outside. These are the primary tests.
2. **Edge case / error tests** — cover failure modes and boundaries of the user-facing behavior.
3. **Implementation tests** — only when internal behavior is complex enough to warrant direct verification. The gate question: "would the user care if this worked differently internally?"

Tickets carry a **`Requirement:`** field tracing each ticket back to the spec item it implements, so the implementing session knows which behavior the tests must prove.

**Files changed:** `tdd/SKILL.md`, `to-tickets/SKILL.md`

## 2. Command-Level Test Timeouts

**Problem:** If a test command can hang, the agent hangs with it. Runner-level assertion timeouts don't help when the process itself is stuck.

**Solution:** Every test run must have an external, command-level timeout that kills the stuck process — never bare `npm test` / `pytest` / `go test` and similar. Defaults: 30–60s for a focused RED/GREEN check, 2–5min for a file-level suite, 5–15min for the full suite. A timeout is a failure to debug, not a command to blindly re-run.

**Files changed:** `tdd/SKILL.md`

## 3. No Fallbacks, No Silent Failure

**Problem:** Three related failure modes:

1. **Fallback code to pass tests** — default returns, swallowed errors, or `?? fallbackValue` make a test green while the feature doesn't actually work. The most damaging pattern because it's invisible.
2. **Auto-applying alternatives** — when the planned approach fails, the agent silently switches direction instead of asking.
3. **Version upgrade fallbacks** — when replacing v1 with v2, stale v1 tests fail (because v2 intentionally changed behavior) and the agent re-implements v1 as a "fallback" to make them pass. The stale tests are the root cause of the loop.

**Solution:**

- **Hard gate** against fallback code in both `tdd` and `implement`: if the feature can't be implemented, let the test fail. Don't fake success.
- **Suggest, don't auto-apply**: when the planned approach keeps failing, stop and present alternatives. The user decides.
- **Version upgrade rules**: remove or rewrite stale v1 tests *before* implementing v2; never add v1 fallback paths unless the user explicitly asks for backward compatibility.

**Files changed:** `tdd/SKILL.md`, `implement/SKILL.md`

## 4. Visual UI Testing

**Problem:** Agents treat UI work like ordinary code by adding component tests, DOM assertions, or snapshot tests. Those can pass while the real interface has clipped text, overflowing labels, misaligned controls, weak hierarchy, or unbalanced visual weight.

**Solution:** UI look-and-feel is tested visually, never with code tests:

- No code tests for UI layout, styling, responsive behavior, visual hierarchy, or interaction-state appearance.
- Agents use the strongest available real-browser inspection tool (Chrome DevTools MCP preferred for local `file://` pages), full-screen unless a viewport is specified.
- Visual checks explicitly cover clipping, overflow, alignment, horizontal/vertical visual balance, interaction states, and responsive viewports.
- A dedicated `visual-tests.md` reference keeps the inspection checklist out of the main workflow.
- `to-tickets` writes UI acceptance criteria along the same axes; `implement` repeats the no-component-test rule.

**Files changed:** `tdd/SKILL.md`, `tdd/visual-tests.md`, `to-tickets/SKILL.md`, `implement/SKILL.md`

## 5. End-to-End Tests on Real Data (2026-07)

**Problem:** A green unit/integration suite — and even a visually clean UI — doesn't prove the feature works. Agents declare success without ever running the real thing: no full-stack run, synthetic toy inputs instead of the project's actual data, and web app changes verified by looking at the page rather than using it.

**Solution:** The suite biases toward end-to-end coverage, and every feature ends with a mandatory end-to-end pass:

- Every user requirement gets at least one end-to-end test or verified run through the real entry point (CLI invocation, HTTP request, browser workflow) with no mocked internals.
- The final run uses **real or production-like data** when available (sample files, fixture dumps, a dev database, a live dev API). Synthetic input is a fallback that must be called out in the report.
- For web apps, end-to-end means the **real browser**: open the app, click the actual buttons, type real input, and review the result the user would see — on top of the visual checks, not instead of them. The walkthrough covers the full workflow, the rendered result (correct data, state changes, redirects, persistence across reload), and reachable error flows.
- Scripted e2e suites (Playwright, Cypress, etc.) count as end-to-end tests where the project has them, but they do not replace the live walkthrough of the changed flow.
- The tdd workflow gains a final **End-to-End Pass** step; a failure there returns to the RED/GREEN loop — no patching around it, no partial success.
- `implement` runs the end-to-end pass before closing any ticket that changes user-facing behavior; `to-tickets` writes behavior-walkthrough acceptance criteria alongside the visual ones.

**Files changed:** `tdd/SKILL.md`, `tdd/visual-tests.md`, `implement/SKILL.md`, `to-tickets/SKILL.md`

## 6. Review-Stage Refactoring

**Problem:** Refactoring mid-implementation-loop churns code while behavior is still unproven, and cleanup decisions made one test at a time miss duplication that only shows up across the whole diff.

**Solution:** Refactoring is not part of the RED/GREEN loop. Get the behavior green first, then review the diff — running or requesting `code-review` for non-trivial diffs — and refactor deliberately from its Standards findings, re-running tests (with timeouts) after each step. Never refactor while RED.

**Files changed:** `tdd/SKILL.md`

## 7. Cross-Phase Change Propagation

**Problem:** Users request changes at every stage — during ticketing, during implementation, during manual testing. Agents typically patch the code in front of them, leaving the spec, tickets, and tests stale.

**Solution:** `to-tickets` and `implement` share the same rule: a user change at any stage has the same authority as an initial requirement and propagates to every artifact — spec (on the tracker), tickets (update/add/remove), tests (remove/rewrite old, write new), and implementation.

**Files changed:** `to-tickets/SKILL.md`, `implement/SKILL.md`

## 8. Structured HTML Companions

**Problem:** Dense specs and plans are hard to review as linear Markdown — option comparisons, dependency maps, and traceability matrices lose clarity in prose.

**Solution:** Targeted HTML-companion guidance. HTML never replaces the canonical Markdown/tracker artifact; it is a review aid for cases where scanning beats prose.

- **to-spec** may create a Structured HTML Companion for option comparison cards, decision matrices, architecture sketches, requirement grouping, Approach Comparison, and Risks / Tradeoffs. Skipped for short specs.
- **to-tickets** may create an HTML Plan Companion (`docs/plans/<artifact-id>/plan.html` on a local tracker) for ticket dependency maps, file-change maps, requirement-to-ticket traceability, and plan overview dashboards.

**Files changed:** `to-spec/SKILL.md`, `to-tickets/SKILL.md`

## 9. Explicit Spec → Tickets Handoff

**Problem:** Upstream `to-spec` ends at the published spec; the next step of the cycle is implicit, so sessions stall or jump straight to code.

**Solution:** `to-spec` ends with an explicit handoff: once the spec is published and approved, break it into tracer-bullet tickets with `/to-tickets`.

**Files changed:** `to-spec/SKILL.md`

## 10. GitHub-Required Non-Interactive Setup, Model-Invocable

**Problem:** Upstream `setup-matt-pocock-skills` interviews the user section by section and shows drafts for approval. The answers are always the same for this user, so the interview is pure ceremony. It is also slash-command-only (`disable-model-invocation: true`), so no other skill can reach it.

**Solution:** The skill is model-invocable, so `setup-git-repo` can invoke it as part of repo bootstrap. It requires a configured, reachable GitHub remote before writing anything; once that prerequisite passes, setup is non-interactive — explore, apply the standing defaults, write, then report:

- **Issue tracker is always GitHub Issues**. Missing, unreachable, and non-GitHub remotes stop setup instead of falling back to local Markdown or another tracker.
- **Triage labels are always the five canonical defaults** (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`), created on the tracker when missing — and skipped entirely when the `triage` skill isn't installed.
- **Agent instructions file**: edit `CLAUDE.md` if present, else `AGENTS.md`; create `AGENTS.md` only when neither exists. Never create a second agent file.
- **Domain docs**: single-context by default; multi-context only on real monorepo signals.

**Files changed:** `setup-matt-pocock-skills/SKILL.md`

## 11. Close-Out User Testing Gate

**Problem:** Skills proceed to finishing as soon as automated tests pass, without the user ever trying the feature. Automated tests passing does not mean the feature works as the user expected.

**Solution:** `implement`'s close-out reviews with `/code-review`, commits with the `commit` skill, and — when the feature branch is complete — asks the user to test the feature themselves before wrapping up. Merge, PR, and cleanup decisions stay with the user.

**Files changed:** `implement/SKILL.md`

## 12. Handoff Saved to the Workspace, Model-Invocable

**Problem:** Upstream `handoff` writes the handoff document to the OS temp directory, where it is invisible to the next session and never committed, and it is slash-command-only.

**Solution:** The handoff doc is saved as `handoff-<topic>.md` in the workspace root, and the skill stays model-invocable so an agent can proactively hand off when a session needs to end.

**Files changed:** `handoff/SKILL.md`

## 13. Tailscale-Reachable UI Prototype Preview

**Problem:** Upstream `prototype` hands over a UI prototype via a localhost URL only, so the preview is unreachable when reviewing from another device over Tailscale.

**Solution:** The UI branch's hand-over step runs the dev server bound to all interfaces (`--host` / `0.0.0.0`) and surfaces both the localhost and Tailscale URLs.

**Files changed:** `prototype/UI.md`

**v1.2 rebase note (2026-08):** v1.2 reshaped the logic branch from a terminal app into a single shareable HTML file (free-play buttons + guided walkthroughs) and made prototypes primary sources captured on a `prototype/<name>` throwaway branch instead of deleted. The reshape was adopted wholesale — a self-contained HTML file serves the multi-device review case behind this customization even better than a bound dev server — so the only surviving local edit is the Tailscale hand-over line in `prototype/UI.md` (`SKILL.md` and `LOGIC.md` are stock v1.2).

## 14. Naming and Suite Wiring

- **`tdd` uses the upstream name.** The local skill was previously named `test-driven-development` for superpowers compatibility; those references are retired, so the skill was renamed to match upstream while keeping the local customizations.
- **`implement` references local skill names** (`/tdd`, `/code-review`, the `commit` skill) so its handoffs resolve in this repo's flattened skill layout.
- **`writing-for-agents` tracks the upstream rename.** v1.2 renamed `writing-great-skills` to `writing-for-agents`; the local directory, `update.py`, `README.md`, and `setup.py`'s retired list follow upstream (the skill itself is vendored unmodified).
- **Flattened layout**: upstream nests skills under `skills/engineering/` and `skills/productivity/`; this repo vendors each as an independent sibling directory under `skills/` because OpenCode discovers skills by a root-level `SKILL.md`. `update.py` maps each skill to its upstream path individually.
- **Codex metadata follows local invocation policy.** v1.2 added `agents/openai.yaml` beside every skill. For skills this repo makes model-invocable against upstream's user-invoked default (`setup-matt-pocock-skills`, `handoff`), the local yaml omits upstream's `policy.allow_implicit_invocation: false` block so Codex does not hide them from model invocation.

**Files changed:** `tdd/SKILL.md`, `implement/SKILL.md`, `update.py`, `setup.py`

## Retired Customizations

- **User Requirements vs Agent Design Decisions / `[USER-REQ]` tagging** (removed 2026-07): the requirement-source split was designed for the superpowers pipeline, where specs passed through several agent hands. The Pocock cycle front-loads user intent through the grilling interview and keeps the user in the loop at each stage (seam check, ticket quiz, close-out testing), so the tag machinery added ceremony without pulling its weight. Cross-phase change propagation (#7) and the ticket `Requirement:` trace (#1) carry the surviving intent.
- **Skill-level `docs/` path defaults in `to-spec`/`to-tickets`** (removed 2026-07): both skills are tracker-first per upstream design; the committed-`docs/` conventions survive only in the local tracker template (#11).
