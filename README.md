# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [commit](commit/) | Git commit workflow — stages files, drafts message, and runs git commit |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.ps1` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| [find-skills](find-skills/) | Discover and install agent skills from the open ecosystem | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Prefers [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) catalog |

## Vendor Skills

Skills sourced from other projects. Run `.\update.ps1` to pull latest versions.

| Skill | Description | Source |
|---|---|---|
| [gh-cli](gh-cli/) | Comprehensive GitHub CLI (gh) reference for repos, issues, PRs, Actions, and more | [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/gh-cli) |
| [ui-ux-pro-max](ui-ux-pro-max/) | UI/UX design intelligence — 50+ styles, 161 palettes, 57 font pairings, 25 chart types across 10 stacks | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |

## Setup

```powershell
git clone https://github.com/stanley50z/sz-skills ~/.sz-skills
cd ~/.sz-skills
.\setup.ps1
```

`setup.ps1` creates junctions from `~\.agents\skills\` and `~\.claude\skills\` into this repo.

## Updating Vendor Skills

```powershell
cd ~/.sz-skills
.\update.ps1
git diff              # review changes
git add -A && git commit -m "update vendor skills"
```
