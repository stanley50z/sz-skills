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

**Problem:** The TDD skill enforced "write a failing test for every piece of code," which led to:

- **Too many tests** — the agent tests every internal function, not just the features the user asked for.
- **Tests that mirror implementation** — tests assert what the code does (tautologies like testing `2 + 2 = 4`) instead of what the feature should do from the user's perspective.
- **Tests that miss real problems** — because they verify internal plumbing, not user-facing behavior. The feature could be broken while all tests pass.

**Solution:** Reframed TDD around a test hierarchy:

1. **User-requirement tests** — verify features as the user described them, from the outside. These are the primary tests.
2. **Edge case / error tests** — cover failure modes of the above.
3. **Implementation tests** — only when internal behavior is complex enough to warrant direct verification. The gate question: "would the user care if this worked differently internally?"

The task template in the plan now includes a `Requirement:` field tracing each task back to the spec, and the test step shows behavioral test examples instead of internal function tests.

**Files changed:** `test-driven-development/SKILL.md`, `test-driven-development/testing-anti-patterns.md`, `writing-plans/SKILL.md`

## 4. No Fallbacks, No Silent Failure

**Problem:** Three related failure modes:

1. **Fallback code to pass tests** — the agent writes implementation code that returns a default value, catches and ignores errors, or adds a fallback path. The test passes. The feature doesn't actually work. This is the most damaging pattern because it's invisible — everything looks green.

2. **Auto-applying alternatives** — when the planned approach doesn't work, the agent silently switches to an alternative instead of asking the user which direction to take.

3. **Version upgrade fallbacks** — when replacing v1 with v2, the agent creates `if v2 fails, fall back to v1` code, even though the user explicitly asked for v2. Worse, stale v1 tests remain in the test suite, and when they fail (because v2 intentionally changed the behavior), the agent re-implements v1 as a "fallback" to make them pass. The stale tests are the root cause of the loop.

**Solution:**

- **Hard gate** against fallback code: if the feature can't be implemented, let the test fail. Don't fake success with try/catch, default returns, or `?? fallbackValue`.
- **Suggest, don't auto-apply**: when the planned approach keeps failing, stop and present alternatives to the user. The user decides.
- **Version upgrade rules**: when upgrading v1 → v2, remove or rewrite v1 tests *before* implementing v2. Never create v1 fallback code unless the user explicitly asks for backward compatibility.
- **New anti-patterns** added: "Fallback Code to Pass Tests" (anti-pattern 6), "Testing Implementation Instead of Requirements" (anti-pattern 7), "Stale Tests From Previous Version" (anti-pattern 8).

**Files changed:** `test-driven-development/SKILL.md`, `test-driven-development/testing-anti-patterns.md`, `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md`

## 5. Simplified Finishing Workflow

**Problem:** The upstream finishing skill presents 4 options after tests pass (merge locally, create PR, keep as-is, discard). This is more ceremony than needed — the typical workflow is just to commit the work. More importantly, the skill proceeds to finishing as soon as automated tests pass, without giving the user a chance to test the feature manually.

**Solution:**

- **User testing gate**: after automated tests pass, the agent asks the user to test the feature themselves and waits for confirmation before proceeding. Automated tests passing does not mean the feature works as the user expected.
- **Always commit**: instead of the 4-option menu, the skill always creates a commit using the `commit` skill. Merge, PR, and cleanup decisions are left to the user.

**Files changed:** `finishing-a-development-branch/SKILL.md`

## 6. Cross-Phase User Change Propagation

**Problem:** The user-requirement tracking from customization #1 only covers the brainstorming phase. But users give feedback and request changes at every stage — during planning, during execution, during manual testing. When a user says "change A to B" mid-execution, the agent would typically just patch the current code without updating the spec, plan, or tests. The change is scoped to the current phase, and upstream/downstream artifacts become stale.

**Solution:** Every skill in the pipeline now has the same rule: when the user requests a change at any stage, treat it as a new User Requirement and propagate it to all artifacts:

1. **Spec** — update the User Requirements section
2. **Plan** — update or add `[USER-REQ]` tasks, remove stale ones
3. **Tests** — remove/rewrite tests for old behavior, write tests for new
4. **Implementation** — update code

A mid-execution change from the user has the same authority as an initial requirement stated during brainstorming. The user's request steers the entire process, not just the current phase.

**Files changed:** `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md`, `finishing-a-development-branch/SKILL.md`, `writing-plans/SKILL.md`

## Structural Change: Flattened Layout

The upstream repo organizes all 14 skills under a `skills/` subdirectory. Initially these were kept nested under `superpowers/` in this repo, but OpenCode requires each skill to have its own `SKILL.md` at the directory root to discover them. All 14 skills were flattened into the repo's `skills/` directory as independent sibling directories, matching the same flat structure as the ui-ux-pro-max suite.

**Files changed:** `setup.py` (discovers skills from `skills/` subdirectory), `update.py` (14 individual upstream entries instead of one bundle entry)
