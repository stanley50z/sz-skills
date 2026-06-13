# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [global-project-preferences](skills/global-project-preferences/) | Default tech stack preferences for new projects, extensions, scripts, and other greenfield work |
| [restart-stale-docker](skills/restart-stale-docker/) | Check whether Docker Desktop is stale and restart the Windows/WSL2 engine safely |
| [commit](skills/commit/) | Git commit workflow — stages files, drafts message, and runs git commit |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.py` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| [find-skills](skills/find-skills/) | Discover and install agent skills from the open ecosystem | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Prefers [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) catalog |
| [slides](skills/slides/) | Slide creation — copywriting formulas, layout patterns, strategies | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/slides) | Renames invalid upstream skill name `ckm:slides` to `slides` for harness compatibility |
| [test-driven-development](skills/test-driven-development/) | Test-driven development with red-green-refactor loop | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) | Keeps Superpowers-compatible skill name and reapplies local rules: command timeouts, user-requirement hierarchy, visual-only UI checks, no silent fallbacks, and stale v1/v2 test cleanup |
| **ui-ux-pro-max suite** | | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Harness-compatible plain skill names |
| [banner-design](skills/banner-design/) | Banner design with sizes, styles, and layout references | ↳ `.claude/skills/banner-design` | Renames invalid upstream skill name `ckm:banner-design` to `banner-design` |
| [brand](skills/brand/) | Brand identity system — guidelines, voice, typography, color, logo rules | ↳ `.claude/skills/brand` | Renames invalid upstream skill name `ckm:brand` to `brand` |
| [design](skills/design/) | Design routing — logos, icons, CIP, slides, social photos | ↳ `.claude/skills/design` | Renames invalid upstream skill name `ckm:design` to `design` |
| [design-system](skills/design-system/) | Design tokens, component specs, slide generation | ↳ `.claude/skills/design-system` | Renames invalid upstream skill name `ckm:design-system` to `design-system` |
| [ui-styling](skills/ui-styling/) | UI styling — Tailwind, shadcn/ui, canvas design system, bundled fonts | ↳ `.claude/skills/ui-styling` | Renames invalid upstream skill name `ckm:ui-styling` to `ui-styling` |
| **superpowers suite** | | [obra/superpowers](https://github.com/obra/superpowers) | [Tailored workflow](docs/superpowers-customization-rationale.md) |
| [brainstorming](skills/brainstorming/) | Explore intent, requirements, and design before creative work | ↳ `skills/brainstorming` |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/) | Dispatch 2+ independent tasks to parallel agents | ↳ `skills/dispatching-parallel-agents` |
| [executing-plans](skills/executing-plans/) | Execute implementation plans with review checkpoints | ↳ `skills/executing-plans` |
| [finishing-a-development-branch](skills/finishing-a-development-branch/) | Guide branch completion — merge, PR, or cleanup | ↳ `skills/finishing-a-development-branch` |
| [receiving-code-review](skills/receiving-code-review/) | Receive code review with technical rigor | ↳ `skills/receiving-code-review` |
| [requesting-code-review](skills/requesting-code-review/) | Request code review before merging | ↳ `skills/requesting-code-review` |
| [subagent-driven-development](skills/subagent-driven-development/) | Execute plans with independent sub-agents | ↳ `skills/subagent-driven-development` |
| [systematic-debugging](skills/systematic-debugging/) | Debug bugs and test failures systematically | ↳ `skills/systematic-debugging` |
| [using-git-worktrees](skills/using-git-worktrees/) | Create isolated git worktrees for feature work | ↳ `skills/using-git-worktrees` |
| [using-superpowers](skills/using-superpowers/) | Establish skill discovery and usage conventions | ↳ `skills/using-superpowers` |
| [verification-before-completion](skills/verification-before-completion/) | Run verification before claiming work is complete | ↳ `skills/verification-before-completion` |
| [writing-plans](skills/writing-plans/) | Write implementation plans before touching code | ↳ `skills/writing-plans` |
| [writing-skills](skills/writing-skills/) | Create, edit, and verify agent skills | ↳ `skills/writing-skills` |

## Vendor Skills

Skills sourced from other projects. Run `python update.py` to pull latest versions.

Vendor skill directories use the official upstream skill name from `SKILL.md` unchanged. Do not rename them to match a simplified repo folder name.

| Skill | Description | Source |
|---|---|---|
| [docker-expert](skills/docker-expert/) | Docker containerization expertise for optimization, hardening, multi-stage builds, Compose, and production deployment | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/docker-expert) |
| [grill-with-docs](skills/grill-with-docs/) | Deeper planning review against project language, documented decisions, and inline docs updates | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) |
| [improve-codebase-architecture](skills/improve-codebase-architecture/) | Find architecture improvements, refactoring opportunities, and deeper module boundaries | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) |
| [supabase-postgres-best-practices](skills/supabase-postgres-best-practices/) | Postgres best practices for Supabase projects, including schema design, RLS, migrations, and query performance | [supabase/agent-skills](https://github.com/supabase/agent-skills/tree/main/skills/supabase-postgres-best-practices) |
| [remotion-best-practices](skills/remotion-best-practices/) | Best practices for Remotion-based video creation in React, including preview and render workflows | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [revealjs](skills/revealjs/) | Create polished reveal.js presentations, decks, and slideshows with HTML and CSS | [ryanbbrown/revealjs-skill](https://github.com/ryanbbrown/revealjs-skill/tree/main/skills/revealjs) |
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

`setup.py` installs every skill in this repo. To choose specific skills from a terminal menu instead, run:

```sh
python interactive_setup.py
```

Both setup scripts create junctions (Windows) or symlinks (macOS/Linux) for coding harness skill directories:

- `~/.claude/skills/` — Claude Code
- `~/.codex/skills/` — OpenAI Codex
- `~/.config/opencode/skills/` — Opencode
- `~/.agents/skills/` — Pi coding agent

The script creates those directories if they do not exist yet. For each skill in this repo, it adds the skill if missing and replaces the target only when a skill with the same name already exists. Unrelated skills in those directories are left alone.

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
