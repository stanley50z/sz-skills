# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [commit](commit/) | Git commit workflow — stages files, drafts message, and runs git commit |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.py` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| [find-skills](find-skills/) | Discover and install agent skills from the open ecosystem | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Prefers [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) catalog |

## Vendor Skills

Skills sourced from other projects. Run `python update.py` to pull latest versions.

| Skill | Description | Source |
|---|---|---|
| [gh-cli](gh-cli/) | Comprehensive GitHub CLI (gh) reference for repos, issues, PRs, Actions, and more | [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/gh-cli) |
| **ui-ux-pro-max suite** | | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| [ui-ux-pro-max](ui-ux-pro-max/) | UI/UX design intelligence — styles, palettes, font pairings, chart types across 10+ stacks | ↳ `.claude/skills/ui-ux-pro-max` + `src/ui-ux-pro-max` |
| [banner-design](banner-design/) | Banner design with sizes, styles, and layout references | ↳ `.claude/skills/banner-design` |
| [brand](brand/) | Brand identity system — guidelines, voice, typography, color, logo rules | ↳ `.claude/skills/brand` |
| [design](design/) | Design routing — logos, icons, CIP, slides, social photos | ↳ `.claude/skills/design` |
| [design-system](design-system/) | Design tokens, component specs, slide generation | ↳ `.claude/skills/design-system` |
| [slides](slides/) | Slide creation — copywriting formulas, layout patterns, strategies | ↳ `.claude/skills/slides` |
| [ui-styling](ui-styling/) | UI styling — Tailwind, shadcn/ui, canvas design system, bundled fonts | ↳ `.claude/skills/ui-styling` |

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

`setup.py` creates junctions (Windows) or symlinks (macOS/Linux) from `~/.agents/skills/` and `~/.claude/skills/` into this repo.

## Updating Vendor Skills

```sh
cd ~/.sz-skills
python update.py
git diff              # review changes
git add -A && git commit -m "chore: update vendor skills"
```
