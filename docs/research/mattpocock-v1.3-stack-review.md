# Matt Pocock v1.3 review against the sz-skills stack

> Superseded by [the revised HTML report](mattpocock-v1.3-stack-review.html) on 2026-10-08. The user clarified that Automode provides first-class support and adapts to the chosen skills. Automode compatibility is not an adoption criterion. The revised recommendation adds all three v1.3 skills, including `implement-spec`; this earlier analysis is retained as research history.

Reviewed 2026-10-08. Research only. No skill, updater, installer, or global instruction changes were made.

## Recommendation

Add `retro` and `pr`, remove `resolving-merge-conflicts`, and migrate the glossary convention coherently. Keep `implement-spec` optional rather than making it the default or replacing Automode. The most useful pruning is inside the existing instructions, especially `tdd` and its callers, rather than deleting useful skills to reduce the catalog count.

## Evidence and scope

Primary sources:

- [Matt's video, New Skills! v1.3 brings /pr, /implement-spec, and /retro](https://www.youtube.com/watch?v=BsJGo1wFTvQ). Read the English auto-caption transcript of the full 14:34 video, not just its description. Auto-captions contain transcription errors; the tagged source controls exact names and behavior.
- [v1.3.1 changelog](https://github.com/mattpocock/skills/blob/v1.3.1/CHANGELOG.md), including the v1.3.0 changes.
- [v1.3.1 router](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/ask-matt/SKILL.md).
- Tagged `pr`, `retro`, and `implement-spec` source linked below.
- Local `README.md`, `update.py`, `setup.py`, `global/AGENTS.md`, relevant skill definitions and supporting files, `tests/test_mattpocock_skills.py`, and `docs/mattpocock-customization-rationale.md`.

The local source catalog contains 36 top-level skills. Manual-entry skills and model-invoked skills are not interchangeable overhead. A large manual-entry catalog does not imply that every skill body is loaded on every turn. Harness support for invocation metadata must be verified rather than assumed.

The upstream reference checkout already existed at `C:\Users\13982\github repo ref\skills` and was pulled with `git pull --ff-only`. Release conclusions use the v1.3.0/v1.3.1 tags. Current main was inspected separately for useful unreleased fixes; those are not attributed to v1.3.

## What the video changes about the recommendation

### Deterministic orchestration remains Matt's preference

At [1:49](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=109s), Matt recommends a script that reads tickets and runs implementation. At [3:05](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=185s), he explicitly describes agent orchestration as worse than a deterministic loop, but easier to get started with. Around 4:23 he explains that he reaches for `implement-spec` where those scripts have not been set up.

This is an argument for an optional orchestrator, not for replacing an existing deterministic runner merely because a newer skill exists. Your local `implement`, `to-spec`, and `to-tickets` already distinguish manual sessions from Automode ownership and queue publication.

### `pr` improves the human review input

At [4:54](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=294s), Matt introduces a PR-body template. It is not another code reviewer. It asks for a small visual explanation, before/after evidence, and merge risk. At 8:07 he suggests borrowing its useful parts if a PR-body skill already exists.

### `retro` should remain human-directed

At [9:37](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=577s), Matt introduces session retrospectives. At [12:36](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=756s), he stresses human judgment and warns against automatically applying retrospective findings. His concern is a loop of false-positive improvements that gradually steers the repository away from its intended behavior.

## Additions

### Add `retro` first

Source: [v1.3.1 retro](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/retro/SKILL.md).

This fills a real gap. `code-review` checks changes; `diagnosing-bugs` diagnoses failures; `improve-codebase-architecture` surveys code structure. None has the same job as reading session evidence to find inefficient tools, missing information, weak navigation, unwired checks, or ineffective steering instructions.

Use it on a troublesome session or a small sample of recent sessions. Keep it user-invoked and proposal-only. Mechanical mistakes should produce a deterministic-check proposal; judgment calls can become reviewer standards. Keep execution safety and authorization instructions in the implementation context even when style guidance moves to review.

For this stack, make sure its session-reading instructions can find Pi, Codex, and Claude logs. Do not inspect unrelated sessions by default, publish raw transcripts, or auto-edit global instructions. These are integration recommendations, not behaviors proven by running the skill here.

### Add `pr`, with one ownership boundary

Source: [v1.3.1 pr](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/pr/SKILL.md).

Your `commit` owns Git closure. `implement` owns branch creation, feature validation, pushing, and ready-to-review PR creation. `pr` should own only the body format. It adds a distinct useful result without introducing a competing shipping workflow.

Have `implement` explicitly load it when writing the body. Preserve links and closing references to the spec and implementation issue. Choose screenshots for visual changes and exact execution evidence for nonvisual work; do not manufacture a before state or treat an agent's risk label as permission to merge.

The expected shape is:

```text
Summary: the smallest diagram, diff sketch, or tree that explains the change
Evidence: observed before and after
Merge danger: reversibility and affected consumers
```

`pr` should not replace `code-review`, the browser walkthrough, or the user testing gate.

### Keep `implement-spec` optional, or defer it

Source: [v1.3.1 implement-spec](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/implement-spec/SKILL.md).

It runs the ready frontier of a ticket dependency graph through background implementers in separate worktrees, merges work onto an integration branch, then reviews the combined diff. It can be useful for a bounded multi-ticket spec in a repo without an established runner.

It is not a drop-in wrapper around your local `implement`:

- Your `implement` starts from the remote default branch and closes out with its own ready PR. Workers here must start from the integration branch and leave aggregate PR ownership to the orchestrator.
- Your published implementation tickets carry `ready-for-agent`. A second orchestrator needs explicit ownership coordination so Automode does not implement the same tickets concurrently. The stock skill does not express your local queue rules.
- Your TDD can ask the user about seams. For unattended execution, the approved ticket must already define the relevant behavior and interface; an unresolved human decision should pause rather than be answered by a worker.
- Preserve your requirement trace, no-silent-fallback policy, browser verification, final end-to-end pass, and default-branch awareness.
- Multiple workers can each test successfully while their combination fails. The integrated result needs validation before PR readiness. Ignored data, fixtures, or credentials may not exist in new worktrees; verify that tests actually ran rather than skipped.
- GitHub blockers may remain open until the aggregate PR merges. Advance the in-run frontier from tickets integrated and validated on the branch, not only from closed GitHub issues. The [tagged implementation docs](https://github.com/mattpocock/skills/blob/v1.3.1/docs/engineering/implement-spec.md) acknowledge this distinction.
- Confirm actual subagent nesting support in each harness; do not assume the video's claim about recursive subagents applies identically everywhere.
- Stock worker wording includes resetting onto the integration branch. Any local adaptation must protect existing changes and keep worktree cleanup limited to resources created for the run.

Do not remove your current `implement` or deterministic runner to make room for this skill.

## Removal

### Remove `resolving-merge-conflicts`

The [v1.3 changelog](https://github.com/mattpocock/skills/blob/v1.3.1/CHANGELOG.md) explicitly retires it with no replacement. Your local copy is only a short generic procedure, but includes unconditional "never --abort" and "stage everything" instructions. Those are unnecessary commitments for a general conflict-resolution task.

Keep conflict resolution as ordinary Git work. Preserve intent, understand both sides, verify the result, and let the user's requested operation determine whether to continue or abort. No replacement skill is needed.

Actual retirement must update `README.md`, `update.py`, `setup.py`'s retired names, `ask-matt`, and the migration tests. Merely stopping upstream synchronization would leave installed copies active.

## Required migration and wiring fixes

### Migrate CONTEXT to GLOSSARY coherently

Sources: [v1.3 changelog](https://github.com/mattpocock/skills/blob/v1.3.1/CHANGELOG.md), [domain-modeling](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/domain-modeling/SKILL.md), video [8:10](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=490s).

Upstream now expects `GLOSSARY.md` and `GLOSSARY-MAP.md`. The local catalog still contains old references in domain modeling, diagnosis, architecture, triage, the router, and customized setup templates. Updating only unpatched skills would produce readers and writers using different names.

Migrate readers, writers, templates, tests, and existing project consumer docs together. Rename only domain-glossary files, not every arbitrary file called `CONTEXT.md`. Existing project migrations should be deliberate and repository-scoped.

`update.py` downloads files but does not prune files removed upstream. A renamed supporting file such as `CONTEXT-FORMAT.md` will remain unless deliberately retired. It also skips every `PATCHED` skill, so running update is not a complete migration. Its GitHub Contents requests do not specify a version ref, so it tracks current upstream main rather than installing an exact v1.3 release.

### Make skill loading explicit and harness-correct

Source: [v1.3 changelog invocation fixes](https://github.com/mattpocock/skills/blob/v1.3.1/CHANGELOG.md).

Your seven-line `grill-me` and `grill-with-docs` wrappers still say to run `/grilling` in prose. The release changes this to an explicit tool call because naming a skill did not reliably load it. Preserve the principle across harnesses: load and follow the skill body using the harness's actual mechanism. In Pi, that mechanism is reading the supplied `SKILL.md`; do not invent a nonexistent Skill tool.

### Fix precommit review coverage

Local evidence: `skills/implement/SKILL.md` Close Out invokes review before commit. `skills/code-review/SKILL.md` pins `git diff <fixed-point>...HEAD`, which includes committed changes, not outstanding working-tree edits.

The written workflow can therefore miss the very implementation it is supposed to review. This is a static instruction inconsistency, not a demonstrated session failure. Define a working-tree review mode covering tracked and relevant untracked changes, or explicitly change the sequencing while preserving the intended review-before-final-closure policy.

### Bring the router in line with your stack

Your `ask-matt` still mentions the local `.scratch` tracker, the retired conflict skill, and the old diagnosis post-mortem handoff. Your setup skill is GitHub-only. Upstream v1.3.1 fixes the stale diagnosis route, but the local GitHub-only routing still needs to remain consistent with your customization.

## What to prune rather than delete

### Shorten the loaded TDD path

Your `skills/tdd/SKILL.md` is 401 lines. Tagged upstream v1.3.1 is 38 lines. The difference is not automatically wrong: your timeouts, visual checks, browser walkthroughs, and final end-to-end pass are substantive requirements.

But the local file repeats end-to-end rules in several sections, carries broad examples, and embeds branch-specific UI instructions even for non-UI tasks. It already has supporting files. Keep the common execution path and hard gates in `SKILL.md`; move UI-only reference and extended examples behind explicit pointers. Make `implement` reference the canonical TDD rules instead of duplicating their full policy.

Retain the safeguards. Reduce repeated text and branch-irrelevant reading.

### Keep safety global, disclose detailed style guidance

`global/AGENTS.md` contains both cross-task operational rules and narrow style guidance. Authorization, secret handling, shell correctness, port ownership, and process cleanup need to be available during execution. Some language-specific style and detailed UI checklists can be reached through targeted pointers or reviewer standards instead.

Treat this as a proposal to validate against sessions, not a license to erase guardrails because a file is long.

### Consider narrowing unslop's enforcement

Keep its useful plain-language discipline. Its current mandatory use, absolute punctuation bans, and blacklist of legitimate technical terms such as "primitive" or "harness" can compete with precise technical explanation.

A possible change is to target user-facing prose and allow exact technical terminology and source quotations. That would revise an existing preference and requires your approval; no such change was made. This is my recommendation, not a v1.3 release requirement.

## Skills I would keep

- `grilling`, `grill-me`, and `grill-with-docs`: shared interview behavior plus stateless and documented entry points. The wrappers are tiny and manual-entry. Fix loading rather than deleting the distinction.
- `research` plus Ketch and Firecrawl: research owns delegation and a cited artifact; the tools own retrieval. Keep Firecrawl as the difficult-extraction fallback rather than a second default research workflow.
- `repo-visualizer` and `improve-codebase-architecture`: the former documents code structure for humans; the latter proposes structural improvements.
- `commit` and `pr`: Git closure and PR presentation have separate jobs.
- `teach`, `to-questionnaire`, `wait-what`: optional manual-entry tools. No evidence from this source audit that deleting them would improve coding reliability.
- `frontend-design`, `prototype`, and browser tooling: retain the sole visual-design skill and mock-before-real-component policy.
- Personal media, document, spreadsheet, Wiki, and handoff tools: no v1.3 evidence that they need retirement. Keep them task-specific rather than forcing them into every coding workflow.

Do not restore retired Superpowers skills, add a second visual-design skill, or import upstream experimental/in-progress skills merely to complete a set.

## Suggested order if approved

1. Retire the conflict skill; add original-vendor `retro` and `pr` with upstream provenance and correct invocation metadata.
2. Migrate glossary producers and consumers, preserving the custom GitHub setup and project conventions.
3. Fix working-tree review coverage and explicit skill loading; align the router with local workflows.
4. Disclose long TDD reference sections and remove duplicated policy from callers without weakening requirements.
5. Trial `retro` on selected sessions. Approve individual findings, preferably backed by repeatable evidence.
6. Add `implement-spec` only when a concrete spec needs it and queue ownership is defined.

Installation changes would require the repo's documented pull-first update workflow, preservation of existing work, classification updates, focused regression tests, `python setup.py`, and verification in all four managed harness targets. None of that was run for this research request.

## Artifacts

- This report: `C:\Users\13982\sz-skills\docs\research\mattpocock-v1.3-stack-review.md`.
- Independent source audit: `docs/research/mattpocock-v1.3-source-audit.md`.
- Video caption evidence and yt-dlp log: `C:\Users\13982\.tmp\mattpocock-v1.3-audit\video-transcript.txt`, `BsJGo1wFTvQ.en.vtt`, and `ytdlp.log`.
- The caption-normalization script was removed after use. No browser tabs or temporary test/dev servers were opened.
