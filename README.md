# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [download-online-video](skills/download-online-video/) | Download YouTube and Bilibili videos, audio, and subtitles with a cross-platform `yt-dlp` helper |
| [global-project-preferences](skills/global-project-preferences/) | Default tech stack preferences for new projects, extensions, scripts, and other greenfield work |
| [repo-visualizer](skills/repo-visualizer/) | Generate a human-readable interactive HTML codebase structure report with Mermaid, inputs/outputs, and clickable file details |
| [commit](skills/commit/) | Git commit workflow — stages files, drafts message, and runs git commit |
| [openwiki](skills/openwiki/) | Maintain OpenWiki repository docs locally on the ChatGPT-subscription login and publish them to the native GitHub Wiki |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.py` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| [find-skills](skills/find-skills/) | Discover and install agent skills from the open ecosystem | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Prefers [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) catalog |
| [handoff](skills/handoff/) | Compact the current conversation into a handoff document for another agent to pick up | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) | Saves the handoff doc to the workspace root instead of the OS temp dir, and stays model-invocable |
| [slides](skills/slides/) | Slide creation — copywriting formulas, layout patterns, strategies | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/slides) | Renames invalid upstream skill name `ckm:slides` to `slides` for harness compatibility |
| [tdd](skills/tdd/) | Test-driven development with seam-based red-green loops | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) | Reapplies local rules: command timeouts, user-requirement hierarchy, visual-only UI checks, no silent fallbacks, stale v1/v2 test cleanup, and review-stage refactoring (renamed from local `test-driven-development` to the upstream name) |
| [to-spec](skills/to-spec/) | Synthesize the current conversation into a published spec | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec) | Adds User Requirements vs Agent Design Decisions sections with classification rules, `docs/specs/<artifact-id>-design.md` local default, and the Structured HTML Companion review aid |
| [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/) | One-time repo configuration — tracker, triage labels, docs layout | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills) | Local-markdown tracker doc maps to this repo's `docs/specs/` + `docs/plans/<artifact-id>/` conventions instead of `.scratch/` |
| [to-tickets](skills/to-tickets/) | Break a spec into tracer-bullet tickets with blocking edges | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets) | Replaces superpowers `writing-plans`: `[USER-REQ]`/`[AGENT-DECISION]` source tags, local ticket files under `docs/plans/<artifact-id>/` by default (no tracker setup required), visual-only UI acceptance criteria, cross-phase change propagation, HTML plan companion |
| [implement](skills/implement/) | Implement one ticket at a time with TDD, code review, and commit | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement) | Replaces superpowers `executing-plans`/`subagent-driven-development`: no-fallback hard gate, suggest-don't-auto-apply, USER-REQ hierarchy, version-upgrade test cleanup, visual-only UI checks, cross-phase change propagation, local skill names |
| **ui-ux-pro-max suite** | | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Harness-compatible plain skill names |
| [banner-design](skills/banner-design/) | Banner design with sizes, styles, and layout references | ↳ `.claude/skills/banner-design` | Renames invalid upstream skill name `ckm:banner-design` to `banner-design` |
| [brand](skills/brand/) | Brand identity system — guidelines, voice, typography, color, logo rules | ↳ `.claude/skills/brand` | Renames invalid upstream skill name `ckm:brand` to `brand` |
| [design](skills/design/) | Design routing — logos, icons, CIP, slides, social photos | ↳ `.claude/skills/design` | Renames invalid upstream skill name `ckm:design` to `design` |
| [design-system](skills/design-system/) | Design tokens, component specs, slide generation | ↳ `.claude/skills/design-system` | Renames invalid upstream skill name `ckm:design-system` to `design-system` |
| [ui-styling](skills/ui-styling/) | UI styling — Tailwind, shadcn/ui, canvas design system, bundled fonts | ↳ `.claude/skills/ui-styling` | Renames invalid upstream skill name `ckm:ui-styling` to `ui-styling` |
| **superpowers suite** (harness glue only) | | [obra/superpowers](https://github.com/obra/superpowers) | [Tailored workflow](docs/superpowers-customization-rationale.md); the development cycle (brainstorming, writing-plans, executing-plans, subagent-driven-development, requesting/receiving-code-review, verification-before-completion, systematic-debugging) was retired in favor of the [mattpocock/skills](https://github.com/mattpocock/skills) v1.1 suite |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/) | Dispatch 2+ independent tasks to parallel agents | ↳ `skills/dispatching-parallel-agents` |
| [finishing-a-development-branch](skills/finishing-a-development-branch/) | Guide branch completion — user testing gate, then commit | ↳ `skills/finishing-a-development-branch` |
| [using-git-worktrees](skills/using-git-worktrees/) | Create isolated git worktrees for feature work | ↳ `skills/using-git-worktrees` |
| [using-superpowers](skills/using-superpowers/) | Establish skill discovery conventions; routes feature work into the mattpocock development cycle | ↳ `skills/using-superpowers` |

## Vendor Skills

Skills sourced from other projects. Run `python update.py` to pull latest versions.

Vendor skill directories use the official upstream skill name from `SKILL.md` unchanged. Do not rename them to match a simplified repo folder name.

| Skill | Description | Source |
|---|---|---|
| [code-review](skills/code-review/) | Review diffs against repo standards and originating specs | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review) |
| [ask-matt](skills/ask-matt/) | Router for picking the right skill/workflow for a request | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt) |
| [codebase-design](skills/codebase-design/) | Shared vocabulary for designing deep modules at clean seams | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) |
| [diagnosing-bugs](skills/diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions (replaces superpowers `systematic-debugging`) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) |
| [domain-modeling](skills/domain-modeling/) | Build and sharpen a project's domain model, glossary, and ADRs | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) |
| [grill-with-docs](skills/grill-with-docs/) | Interview + domain modeling to build shared language before speccing | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) |
| [grilling](skills/grilling/) | Shared interview loop used by the grill skills | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) |
| [grill-me](skills/grill-me/) | Deep interview on any plan or design decision | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) |
| [improve-codebase-architecture](skills/improve-codebase-architecture/) | Find architecture improvements and deeper module boundaries | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) |
| [prototype](skills/prototype/) | Throwaway logic/UI prototypes to answer design questions | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [research](skills/research/) | Investigate a question against primary sources, capture findings | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/research) |
| [resolving-merge-conflicts](skills/resolving-merge-conflicts/) | Intent-traced merge/rebase conflict resolution | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts) |
| [triage](skills/triage/) | Move issues through the triage state machine | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) |
| [wayfinder](skills/wayfinder/) | Plan work too big for one session as a shared map of decision tickets | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder) |
| [docker-expert](skills/docker-expert/) | Docker containerization expertise for optimization, hardening, multi-stage builds, Compose, and production deployment | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/docker-expert) |
| [supabase-postgres-best-practices](skills/supabase-postgres-best-practices/) | Postgres best practices for Supabase projects, including schema design, RLS, migrations, and query performance | [supabase/agent-skills](https://github.com/supabase/agent-skills/tree/main/skills/supabase-postgres-best-practices) |
| [remotion-best-practices](skills/remotion-best-practices/) | Best practices for Remotion-based video creation in React, including preview and render workflows | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [revealjs](skills/revealjs/) | Create polished reveal.js presentations, decks, and slideshows with HTML and CSS | [ryanbbrown/revealjs-skill](https://github.com/ryanbbrown/revealjs-skill/tree/main/skills/revealjs) |
| [writing-great-skills](skills/writing-great-skills/) | Reference for writing and editing skills — vocabulary and principles for predictable skills (replaces superpowers `writing-skills`) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills) |
| **ui-ux-pro-max suite** | | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| [ui-ux-pro-max](skills/ui-ux-pro-max/) | UI/UX design intelligence — styles, palettes, font pairings, chart types across 10+ stacks | ↳ `.claude/skills/ui-ux-pro-max` + `src/ui-ux-pro-max` |

> **Note:** `ui-styling` includes font license files (OFL) but binary `.ttf` files are skipped during
> `update.py` to keep the repo lightweight. If you need the actual font files, download them from the
> upstream repo or use Google Fonts.

## Setup

Requires: Python 3.8+, [gh CLI](https://cli.github.com/) (authenticated)

```sh
git clone https://github.com/stanley50z/sz-skills ~/.sz-skills
cd ~/.sz-skills
python setup.py
```

`setup.py` installs every skill in this repo, links the repo-managed global instruction files under `global/`, and enables the local `sz-skills` plugin hooks for Codex and Claude Code.
To choose specific skills from a terminal menu instead, run:

```sh
python interactive_setup.py
```

Both setup scripts install skills into these coding harness skill directories:

- `~/.claude/skills/` — Claude Code
- `~/.codex/skills/` — OpenAI Codex, copied so Codex keeps plain skill names
- `~/.config/opencode/skills/` — Opencode
- `~/.agents/skills/` — Pi coding agent and Codex-compatible agents, mirrored to the copied Codex skills

The Claude Code and Opencode targets use junctions (Windows) or symlinks (macOS/Linux) into this repo. The Codex target uses real copied directories because Codex scans both `~/.codex/skills` and `~/.agents/skills`; when either target is a junction into this repo, Codex exposes those entries as `sz-skills:<skill>`. The Agents target points to the copied Codex skill directories so Codex-compatible scanners see one canonical plain skill source instead of duplicate entries.

The script creates those directories if they do not exist yet. For each skill in this repo, it adds the skill if missing and replaces the target only when a skill with the same name already exists. Retired repo-managed skill names are removed; unrelated skills in those directories are left alone.

`setup.py` also links:

- `global/AGENTS.md` -> `~/.codex/AGENTS.md`
- `global/CLAUDE.md` -> `~/.claude/CLAUDE.md`

It also registers local `sz-skills` plugin hooks:

- Codex: adds the hook-only `.codex-hook-plugin` package as the `sz-skills` local marketplace and enables `sz-skills@sz-skills` in `~/.codex/config.toml`.
- Claude Code: enables `sz-skills@sz-skills` in `~/.claude/settings.json` and records the repo path in Claude's plugin install state.

`hooks/` is the source of truth for every hook file. `setup.py` mirrors the Codex-relevant files (everything except the Claude-only `hooks.json` and `session-start`) into `.codex-hook-plugin/hooks/`, adding new files and deleting stale ones, so edit hooks only under `hooks/` and re-run `python setup.py`.

`setup.py` also points `core.hooksPath` at the repo-managed `githooks/` directory. The `githooks/post-commit` hook re-runs `setup.py` after any commit that touches `skills/` or `global/`, while `githooks/post-merge` runs it after successful merge-based pulls. Together they keep the installed skill copies in sync with the repo.

The Codex plugin package is context-only and does not contain a `skills/` directory, so Codex should load these skills through the copied/mirrored skill directories above instead of as plugin-bundled skills. The SessionStart hook injects `using-superpowers` and Chrome DevTools MCP ownership guidance so rules are available before the model chooses which skill or browser cleanup behavior applies. A Codex PostToolUse hook records Chrome DevTools MCP usage for the active turn, and the Stop hook checks that marker plus transcript evidence. Only when needed, it blocks finalization with a reminder to close only owned isolated DevTools browser sessions. It does not run cleanup scripts.

Both plugins also register an `agent-notify` Stop hook that fires a desktop notification (Windows toast / macOS / Linux) when the agent finishes a turn, titled "Claude Code" or "Codex" plus the working directory. The script (`hooks/agent-notify.py`) spawns the notifier detached and exits immediately, so it never delays turn end. This covers Claude Code and Codex wherever they run — including inside T3 Code, which loads user-level Claude settings and spawns `codex app-server` with the user's `CODEX_HOME`. Codex prompts once to trust the new hook after it changes.

## Updating Vendor Skills

Always pull the latest repo state before updating vendor skills. In this repo, "update skills" means:

```sh
cd ~/.sz-skills
git pull --ff-only
python update.py
python setup.py
git diff              # review changes
git add -A && git commit -m "chore: update vendor skills"
```
