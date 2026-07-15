# Superpowers Suite Customization Rationale

This document explains why and how the [obra/superpowers](https://github.com/obra/superpowers) skill suite was customized for this repo. The upstream superpowers skills provide a solid development workflow (brainstorm → plan → execute → review → finish), but in practice, several patterns emerged where AI coding agents would produce work that drifted from what the user actually asked for. These customizations address those patterns.

## 1. User Requirements vs Agent Design Decisions

**Problem:** When the brainstorming skill produces a spec document, everything in it looks equally "decided." There is no distinction between what the user explicitly asked for and what the agent inferred or assumed on its own. As the spec flows into the plan and then into execution, the agent treats all items with equal weight. When trade-offs arise, the agent has no basis for knowing which items are negotiable and which are not. The user's original intent gets diluted.

**Solution:** The spec document now has two clearly separated sections:

- **User Requirements** — items the user explicitly stated, chose from options, or confirmed. Each traces back to something the user said.
- **Agent Design Decisions** — everything the agent inferred or filled in. Each notes which user requirement it serves.

This distinction carries forward through the entire pipeline:

- During **brainstorming**, the agent tracks which items come from the user vs which it assumed. Blanket approval ("looks good") does not promote agent decisions to user requirements.
- During **planning**, each task is tagged `[USER-REQ]` or `[AGENT-DECISION]`. Every user requirement must map to at least one task.
- During **execution**, if a `[USER-REQ]` task can't be met, the agent stops and asks. `[AGENT-DECISION]` tasks can be adapted.
- **Reviewers** (spec and plan) verify that user requirements are properly separated, not silently dropped, and not contradicted by agent decisions.

**Files changed:** `brainstorming/SKILL.md`, `brainstorming/spec-document-reviewer-prompt.md`, `writing-plans/SKILL.md`, `writing-plans/plan-document-reviewer-prompt.md`, `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md`

## 2. Doc File Paths Simplified

**Problem:** The upstream skills default to saving specs under `docs/superpowers/specs/` and plans under `docs/superpowers/plans/`. The "superpowers" intermediate folder adds no meaningful organization — it just makes paths longer.

**Solution:** Changed all default paths to `docs/specs/` and `docs/plans/`.

**Files changed:** `brainstorming/SKILL.md`, `brainstorming/spec-document-reviewer-prompt.md`, `writing-plans/SKILL.md`, `subagent-driven-development/SKILL.md`, `requesting-code-review/SKILL.md`

## 3. Requirement-Driven Testing

**Problem:** The original Superpowers TDD skill enforced "write a failing test for every piece of code," which led to:

- **Too many tests** — the agent tests every internal function, not just the features the user asked for.
- **Tests that mirror implementation** — tests assert what the code does (tautologies like testing `2 + 2 = 4`) instead of what the feature should do from the user's perspective.
- **Tests that miss real problems** — because they verify internal plumbing, not user-facing behavior. The feature could be broken while all tests pass.

**Solution:** Replaced the local TDD skill body with Matt Pocock's vertical-slice `tdd` workflow, while keeping the Superpowers-compatible `test-driven-development` skill name. Reapplied the local test hierarchy:

1. **User-requirement tests** — verify features as the user described them, from the outside. These are the primary tests.
2. **Edge case / error tests** — cover failure modes of the above.
3. **Implementation tests** — only when internal behavior is complex enough to warrant direct verification. The gate question: "would the user care if this worked differently internally?"

The task template in the plan includes a `Requirement:` field tracing each task back to the spec, and the TDD skill prioritizes behavioral tests over internal function tests.

**Files changed:** `test-driven-development/SKILL.md`, `test-driven-development/tests.md`, `test-driven-development/mocking.md`, `test-driven-development/deep-modules.md`, `test-driven-development/interface-design.md`, `test-driven-development/refactoring.md`, `writing-plans/SKILL.md`

## 4. No Fallbacks, No Silent Failure

**Problem:** Three related failure modes:

1. **Fallback code to pass tests** — the agent writes implementation code that returns a default value, catches and ignores errors, or adds a fallback path. The test passes. The feature doesn't actually work. This is the most damaging pattern because it's invisible — everything looks green.

2. **Auto-applying alternatives** — when the planned approach doesn't work, the agent silently switches to an alternative instead of asking the user which direction to take.

3. **Version upgrade fallbacks** — when replacing v1 with v2, the agent creates `if v2 fails, fall back to v1` code, even though the user explicitly asked for v2. Worse, stale v1 tests remain in the test suite, and when they fail (because v2 intentionally changed the behavior), the agent re-implements v1 as a "fallback" to make them pass. The stale tests are the root cause of the loop.

**Solution:**

- **Hard gate** against fallback code: if the feature can't be implemented, let the test fail. Don't fake success with try/catch, default returns, or `?? fallbackValue`.
- **Suggest, don't auto-apply**: when the planned approach keeps failing, stop and present alternatives to the user. The user decides.
- **Version upgrade rules**: when upgrading v1 → v2, remove or rewrite v1 tests *before* implementing v2. Never create v1 fallback code unless the user explicitly asks for backward compatibility.
- **Main workflow placement**: these checks stay in `SKILL.md` so stale v1 tests are removed or rewritten before v2 implementation starts.

**Files changed:** `test-driven-development/SKILL.md`, `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md`

## 5. Visual-Only UI Testing

**Problem:** Agents tend to treat UI work like ordinary code by adding component tests, DOM assertions, or snapshot tests. Those checks can pass while the real interface has clipped text, overflowing labels, awkward spacing, misaligned controls, weak hierarchy, or unbalanced visual weight.

**Solution:** The TDD skill now treats UI tests as visual inspections only:

- No code tests for UI layout, styling, responsive behavior, visual hierarchy, or interaction states.
- Agents use the strongest available real-browser inspection tool; local `file://` pages prefer Chrome DevTools MCP when available, including Claude Code, t3code, and other harnesses with DevTools/browser MCP support.
- Visual checks explicitly cover clipping, overflow, alignment, horizontal and vertical visual balance, interaction states, and responsive viewports.
- A dedicated `visual-tests.md` reference keeps the visual inspection checklist out of the main workflow.
- `writing-plans`, `executing-plans`, and the subagent implementer prompt now tell UI work to use visual checks instead of generating or expecting code-test tasks.

**Files changed:** `test-driven-development/SKILL.md`, `test-driven-development/visual-tests.md`, `writing-plans/SKILL.md`, `executing-plans/SKILL.md`, `subagent-driven-development/implementer-prompt.md`

## 6. Simplified Finishing Workflow

**Problem:** The upstream finishing skill presents 4 options after tests pass (merge locally, create PR, keep as-is, discard). This is more ceremony than needed — the typical workflow is just to commit the work. More importantly, the skill proceeds to finishing as soon as automated tests pass, without giving the user a chance to test the feature manually.

**Solution:**

- **User testing gate**: after automated tests pass, the agent asks the user to test the feature themselves and waits for confirmation before proceeding. Automated tests passing does not mean the feature works as the user expected.
- **Always commit**: instead of the 4-option menu, the skill always creates a commit using the `commit` skill. Merge, PR, and cleanup decisions are left to the user.

**Files changed:** `finishing-a-development-branch/SKILL.md`

## 7. Cross-Phase User Change Propagation

**Problem:** The user-requirement tracking from customization #1 only covers the brainstorming phase. But users give feedback and request changes at every stage — during planning, during execution, during manual testing. When a user says "change A to B" mid-execution, the agent would typically just patch the current code without updating the spec, plan, or tests. The change is scoped to the current phase, and upstream/downstream artifacts become stale.

**Solution:** Every skill in the pipeline now has the same rule: when the user requests a change at any stage, treat it as a new User Requirement and propagate it to all artifacts:

1. **Spec** — update the User Requirements section
2. **Plan** — update or add `[USER-REQ]` tasks, remove stale ones
3. **Tests** — remove/rewrite tests for old behavior, write tests for new
4. **Implementation** — update code

A mid-execution change from the user has the same authority as an initial requirement stated during brainstorming. The user's request steers the entire process, not just the current phase.

**Files changed:** `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md`, `finishing-a-development-branch/SKILL.md`, `writing-plans/SKILL.md`

## 8. Optional Deep Planning Pass

**Problem:** The brainstorming skill is the main entry point for the superpowers pipeline, but some designs need a deeper pass against project language, existing docs, and ADR-level decisions before implementation planning. Running a separate prompt after the spec review creates extra ceremony and makes the escalation easy to miss.

**Solution:** Added `grill-with-docs` as an optional escalation in the brainstorming handoff. After the spec review loop passes, the agent asks the user to review the written spec and, in the same prompt, decide whether to run `grill-with-docs` before writing the implementation plan. If the user opts in, `grill-with-docs` runs before `writing-plans`; otherwise the normal superpowers pipeline continues directly to `writing-plans`.

**Files changed:** `brainstorming/SKILL.md`

## 9. Structured HTML Companions

**Problem:** Some brainstorming and planning outputs are difficult to review as linear Markdown. Dense option comparisons, requirement groupings, architecture sketches, dependency maps, and traceability matrices lose clarity when buried in prose.

**Solution:** Added targeted HTML companion guidance to `brainstorming` and `writing-plans`. HTML is not a universal response format and does not replace canonical Markdown specs or plans. It is a review aid for cases where visual hierarchy, scanning, or structured comparison improves human understanding.

- **brainstorming** may create structured HTML companions for option comparison cards, decision matrices, architecture sketches, requirement grouping, approach comparisons, and risks/tradeoffs.
- **writing-plans** may create HTML plan companions for task dependency maps, file-change maps, requirement-to-task traceability, and plan overview dashboards.

**Files changed:** `brainstorming/SKILL.md`, `writing-plans/SKILL.md`

## Migration (2026-07): Execution Half Replaced by mattpocock/skills

The Superpowers execution pipeline (`writing-plans`, `executing-plans`, `subagent-driven-development`, `requesting-code-review`, `receiving-code-review`, `verification-before-completion`) was retired in favor of [mattpocock/skills](https://github.com/mattpocock/skills) v1.1 `to-tickets` + `implement` (vendored as customized vendor skills).

**Why:** The working split is Claude for brainstorming/spec, GPT (Codex) for implementation. The Superpowers execution skills assume cheap Claude Code subagent dispatch for their spec-reviewer, plan-reviewer, per-task implementer/reviewer, and verification loops; on Codex these serialize into slow single-threaded ceremony around micro-steps. Matt Pocock's v1.1 flow (spec → tracer-bullet tickets → implement one ticket per fresh session → one code review at close-out) is model-agnostic and matches the intended split.

**The pipeline is now:** `brainstorming` (customized, Claude side) → spec in `docs/specs/` → optional `grill-with-docs` → `to-tickets` → tickets in `docs/plans/<artifact-id>/` → `implement` per ticket (drives `test-driven-development`, closes with `code-review` + `commit`) → `finishing-a-development-branch` (user testing gate).

**Where the customizations above moved:**

| Customization | Old home | New home |
|---|---|---|
| #1 User Requirements vs Agent Design Decisions | writing-plans, executing-plans, subagent-driven-development | `to-tickets` (`[USER-REQ]`/`[AGENT-DECISION]` ticket tags, spec traceability), `implement` (USER-REQ stop-and-ask rule) |
| #2 Simplified doc paths | writing-plans | `to-tickets` (tickets under `docs/plans/<artifact-id>/`) |
| #4 No fallbacks, no silent failure | executing-plans, subagent-driven-development | `implement` (hard gate, suggest-don't-auto-apply, version-upgrade rules); TDD-level rules remain in `test-driven-development` |
| #5 Visual-only UI testing | writing-plans, executing-plans, subagent prompts | `to-tickets` (visual acceptance criteria), `implement` (visual RED/GREEN); reference remains in `test-driven-development/visual-tests.md` |
| #7 Cross-phase user change propagation | writing-plans, executing-plans, subagent-driven-development | `to-tickets` and `implement` (both propagate changes back to spec/tickets/tests/code) |
| #9 HTML plan companion | writing-plans | `to-tickets` (`docs/plans/<artifact-id>/plan.html`) |

Customizations #3 (requirement-driven testing, in `test-driven-development`), #6 (finishing workflow), and #8 (grill-with-docs escalation, in `brainstorming`) were unaffected. `brainstorming`'s terminal state changed from invoking `writing-plans` to invoking `to-tickets`. Upstream review-ceremony pieces intentionally not ported: plan/spec reviewer subagent loops around tickets, per-task subagent code review, and the exact-file-paths/complete-code-in-plan style — tickets describe end-to-end behaviour and stay path-light per upstream guidance. The non-patched `code-review` vendor skill was verified against v1.1 in the same migration (its content, including the Martin Fowler code-smell vocabulary, was already current; only the upstream `agents/openai.yaml` was new).

## Migration (2026-07, part 2): Full Adoption of mattpocock/skills v1.1

The first migration replaced only the execution half. This second step adopts the full v1.1 development cycle as shown in Matt Pocock's v1.1 announcement, retiring the remaining Superpowers development-cycle skills. Only Superpowers harness glue remains (`using-superpowers`, `dispatching-parallel-agents`, `using-git-worktrees`, `finishing-a-development-branch`).

**The cycle:** `grill-with-docs` (or `wayfinder` for work too big for one session) → `to-spec` → `to-tickets` → `implement` per ticket (drives `tdd`, closes with `code-review` + `commit`) → `finishing-a-development-branch`. `diagnosing-bugs` replaces `systematic-debugging`; `research` and `prototype` support any stage; `domain-modeling`/`codebase-design`/`grilling` are the shared reference skills; `triage`, `ask-matt`, `resolving-merge-conflicts`, `grill-me`, and `setup-matt-pocock-skills` round out the suite.

**Changes:**

- **Retired** `brainstorming` (role split across `grill-with-docs`/`wayfinder` + `to-spec`) and `systematic-debugging` (replaced by `diagnosing-bugs`).
- **`to-spec` customized**: carries forward customization #1 — the spec template gains User Requirements vs Agent Design Decisions sections with the classification rules and priority hierarchy — plus the `docs/specs/<artifact-id>-design.md` local default (#2) and the Structured HTML Companion (#9).
- **`setup-matt-pocock-skills` customized**: the local-markdown tracker doc maps to this repo's committed `docs/specs/` + `docs/plans/<artifact-id>/` conventions (#2) instead of upstream `.scratch/`, so `to-spec`, `to-tickets`, and `wayfinder` all follow the same paths without per-skill edits.
- **`grill-with-docs` and `improve-codebase-architecture` restored to pure upstream** and made auto-updatable: their customizations existed only to stay standalone while `grilling`, `domain-modeling`, and `codebase-design` were not vendored — those dependencies are now vendored, and upstream v1.1 `grilling` natively includes the confirmation gates and facts-vs-decisions rules that had been cherry-picked locally.
- **`test-driven-development` renamed to upstream `tdd`** (customizations kept): the Superpowers-compatible name existed only for `superpowers:test-driven-development` references in skills that are now retired.
- **`using-superpowers` updated**: the pre-plan gate routes to `grill-with-docs`/`wayfinder` instead of `brainstorming`, and the skill now documents the development cycle.
- **Intentionally not vendored:** `teach` (course-teaching workflow, unrelated to the development cycle).

**What was consciously dropped with `brainstorming`:** the spec-document-reviewer subagent loop and the one-question-at-a-time interview checklist. The grilling skills cover the interview; spec quality control is now the user review plus `code-review`'s spec axis at implementation time. The requirement-source tracking (#1), path conventions (#2), and HTML companions (#9) all live on in the customized `to-spec`/`to-tickets`/`implement`.

## Migration (2026-07, part 3): Superpowers Fully Retired

The last four Superpowers skills — `using-superpowers`, `dispatching-parallel-agents`, `using-git-worktrees`, `finishing-a-development-branch` — were dropped without vendored replacements. This document is the only Superpowers artifact that remains, kept as the historical record of the customizations and the migration.

- **`using-superpowers`** was injected wholesale into every session by the SessionStart hooks and overrode harness behavior ("invoke a skill before ANY response"). That hijacking is gone: the hooks now inject only the Chrome DevTools MCP browser-ownership guidance, and skill selection is left to each harness's native skill discovery.
- **`dispatching-parallel-agents`** and **`using-git-worktrees`**: harnesses now provide native subagent dispatch and worktree isolation; a process skill on top added ceremony, not capability.
- **`finishing-a-development-branch`**: its customized user-testing gate (#6) moved into `implement`'s close-out ("ask the user to test the feature themselves before wrapping up"); merge/PR/cleanup decisions stay with the user. The `commit` skill's linked-worktree gate no longer routes through it — commits happen in place and worktree merge/cleanup stays with the user.

## Structural Change: Flattened Layout

The upstream repo organizes all 14 skills under a `skills/` subdirectory. Initially these were kept nested under `superpowers/` in this repo, but OpenCode requires each skill to have its own `SKILL.md` at the directory root to discover them. All 14 skills were flattened into the repo's `skills/` directory as independent sibling directories, matching the same flat structure as the ui-ux-pro-max suite.

**Files changed:** `setup.py` (discovers skills from `skills/` subdirectory), `update.py` (14 individual upstream entries instead of one bundle entry)
