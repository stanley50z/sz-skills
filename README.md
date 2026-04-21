# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [commit](skills/commit/) | Git commit workflow — stages files, drafts message, and runs git commit |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.py` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| [find-skills](skills/find-skills/) | Discover and install agent skills from the open ecosystem | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Prefers [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) catalog |
| **superpowers suite** | | [obra/superpowers](https://github.com/obra/superpowers) | [Tailored workflow](docs/superpowers-customization-rationale.md) |
| [brainstorming](skills/brainstorming/) | Explore intent, requirements, and design before creative work | ↳ `skills/brainstorming` |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/) | Dispatch 2+ independent tasks to parallel agents | ↳ `skills/dispatching-parallel-agents` |
| [executing-plans](skills/executing-plans/) | Execute implementation plans with review checkpoints | ↳ `skills/executing-plans` |
| [finishing-a-development-branch](skills/finishing-a-development-branch/) | Guide branch completion — merge, PR, or cleanup | ↳ `skills/finishing-a-development-branch` |
| [receiving-code-review](skills/receiving-code-review/) | Receive code review with technical rigor | ↳ `skills/receiving-code-review` |
| [requesting-code-review](skills/requesting-code-review/) | Request code review before merging | ↳ `skills/requesting-code-review` |
| [subagent-driven-development](skills/subagent-driven-development/) | Execute plans with independent sub-agents | ↳ `skills/subagent-driven-development` |
| [systematic-debugging](skills/systematic-debugging/) | Debug bugs and test failures systematically | ↳ `skills/systematic-debugging` |
| [test-driven-development](skills/test-driven-development/) | Write tests before implementation code | ↳ `skills/test-driven-development` |
| [using-git-worktrees](skills/using-git-worktrees/) | Create isolated git worktrees for feature work | ↳ `skills/using-git-worktrees` |
| [using-superpowers](skills/using-superpowers/) | Establish skill discovery and usage conventions | ↳ `skills/using-superpowers` |
| [verification-before-completion](skills/verification-before-completion/) | Run verification before claiming work is complete | ↳ `skills/verification-before-completion` |
| [writing-plans](skills/writing-plans/) | Write implementation plans before touching code | ↳ `skills/writing-plans` |
| [writing-skills](skills/writing-skills/) | Create, edit, and verify agent skills | ↳ `skills/writing-skills` |

## Vendor Skills

Skills sourced from other projects. Run `python update.py` to pull latest versions.

| Skill | Description | Source |
|---|---|---|
| [gh-cli](skills/gh-cli/) | Comprehensive GitHub CLI (gh) reference for repos, issues, PRs, Actions, and more | [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/gh-cli) |
| **ui-ux-pro-max suite** | | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| [ui-ux-pro-max](skills/ui-ux-pro-max/) | UI/UX design intelligence — styles, palettes, font pairings, chart types across 10+ stacks | ↳ `.claude/skills/ui-ux-pro-max` + `src/ui-ux-pro-max` |
| [banner-design](skills/banner-design/) | Banner design with sizes, styles, and layout references | ↳ `.claude/skills/banner-design` |
| [brand](skills/brand/) | Brand identity system — guidelines, voice, typography, color, logo rules | ↳ `.claude/skills/brand` |
| [design](skills/design/) | Design routing — logos, icons, CIP, slides, social photos | ↳ `.claude/skills/design` |
| [design-system](skills/design-system/) | Design tokens, component specs, slide generation | ↳ `.claude/skills/design-system` |
| [slides](skills/slides/) | Slide creation — copywriting formulas, layout patterns, strategies | ↳ `.claude/skills/slides` |
| [ui-styling](skills/ui-styling/) | UI styling — Tailwind, shadcn/ui, canvas design system, bundled fonts | ↳ `.claude/skills/ui-styling` |

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

`setup.py` creates junctions (Windows) or symlinks (macOS/Linux) from `~/.agents/skills/` and `~/.claude/skills/` into this repo's `skills/` directory.

## Updating Vendor Skills

```sh
cd ~/.sz-skills
python update.py
git diff              # review changes
git add -A && git commit -m "chore: update vendor skills"
```
