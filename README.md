# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [download-online-video](skills/download-online-video/) | Download YouTube and Bilibili videos, audio, and subtitles with a cross-platform `yt-dlp` helper |
| [global-project-preferences](skills/global-project-preferences/) | Default tech stack preferences for new projects, extensions, scripts, and other greenfield work |
| [repo-visualizer](skills/repo-visualizer/) | Generate a human-readable interactive HTML codebase structure report with Mermaid, inputs/outputs, and clickable file details |
| [commit](skills/commit/) | Git commit workflow — stages files, drafts message, and runs git commit |
| [pr-codex-review](skills/pr-codex-review/) | Loop on a PR's automated Codex review — fix valid points, spin off out-of-scope ones as issues, merge on thumbs-up, and remove the merged branch (user-invoked only) |
| [openwiki](skills/openwiki/) | Maintain OpenWiki repository docs locally on the ChatGPT-subscription login and publish them to the native GitHub Wiki |
| [setup-git-repo](skills/setup-git-repo/) | Bootstrap a local and remote GitHub repository, then add the setup-matt-pocock-skills config and OpenWiki docs |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.py` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| [ketch](skills/ketch/) | Route live research across web search, OSS code search, library docs, page scraping, and site crawling with bounded output and cited synthesis | [1broseidon/ketch](https://github.com/1broseidon/ketch/tree/main/skills/ketch) | Pi defaults to ketch; harnesses with native web tools retain their native search default unless ketch is explicitly requested or specifically better suited |
| **[mattpocock/skills suite](https://github.com/mattpocock/skills)** | | | Locally adapted development-cycle skills |
| [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/) | One-time GitHub repo configuration — GitHub Issues, triage labels, docs layout | ↳ `skills/engineering/setup-matt-pocock-skills` | Requires a reachable GitHub remote and stops before writing when one is missing; uses GitHub Issues exclusively; keeps canonical triage labels, `AGENTS.md` when no agent file exists, and write-then-report behavior; model-invocable so `setup-git-repo` can invoke it |
| [to-spec](skills/to-spec/) | Synthesize the current conversation into a published spec | ↳ `skills/engineering/to-spec` | Structured HTML Companion review aid and explicit handoff to `/to-tickets` |
| [to-tickets](skills/to-tickets/) | Break a spec into tracer-bullet tickets with blocking edges | ↳ `skills/engineering/to-tickets` | `Requirement:` spec-trace field, visual + behavior-walkthrough UI acceptance criteria, cross-phase change propagation, HTML plan companion |
| [implement](skills/implement/) | Implement one ticket at a time with TDD, code review, commit, and a review-ready PR | ↳ `skills/engineering/implement` | No-fallback hard gate, suggest-don't-auto-apply, version-upgrade test cleanup, visual + end-to-end UI checks with close-out e2e pass, cross-phase change propagation, review-ready PR creation, local skill names |
| [tdd](skills/tdd/) | Test-driven development with seam-based red-green loops | ↳ `skills/engineering/tdd` | Reapplies local rules: command timeouts, user-requirement hierarchy, required end-to-end pass (real-data full run, live browser walkthrough for web apps) on top of visual UI checks, no silent fallbacks, stale v1/v2 test cleanup, and review-stage refactoring (renamed from local `test-driven-development` to the upstream name) |
| [prototype](skills/prototype/) | Throwaway logic/UI prototypes to answer design questions | ↳ `skills/engineering/prototype` | UI prototype dev server binds to all interfaces so the preview is reachable over Tailscale as well as localhost |
| [handoff](skills/handoff/) | Compact the current conversation into a handoff document for another agent to pick up | ↳ `skills/productivity/handoff` | Saves the handoff doc to the workspace root instead of the OS temp dir, and stays model-invocable |
| **[ui-ux-pro-max suite](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** | | | Harness-compatible plain skill names |
| [slides](skills/slides/) | Slide creation — copywriting formulas, layout patterns, strategies | ↳ `.claude/skills/slides` | Renames invalid upstream skill name `ckm:slides` to `slides` for harness compatibility |
| [banner-design](skills/banner-design/) | Banner design with sizes, styles, and layout references | ↳ `.claude/skills/banner-design` | Renames invalid upstream skill name `ckm:banner-design` to `banner-design` |
| [brand](skills/brand/) | Brand identity system — guidelines, voice, typography, color, logo rules | ↳ `.claude/skills/brand` | Renames invalid upstream skill name `ckm:brand` to `brand` |
| [design](skills/design/) | Design routing — logos, icons, CIP, slides, social photos | ↳ `.claude/skills/design` | Renames invalid upstream skill name `ckm:design` to `design` |
| [design-system](skills/design-system/) | Design tokens, component specs, slide generation | ↳ `.claude/skills/design-system` | Renames invalid upstream skill name `ckm:design-system` to `design-system` |
| [ui-styling](skills/ui-styling/) | UI styling — Tailwind, shadcn/ui, canvas design system, bundled fonts | ↳ `.claude/skills/ui-styling` | Renames invalid upstream skill name `ckm:ui-styling` to `ui-styling` |

> The customization rationale for the mattpocock/skills suite lives in [docs/mattpocock-customization-rationale.md](docs/mattpocock-customization-rationale.md). This repo previously vendored the [obra/superpowers](https://github.com/obra/superpowers) suite, fully retired in favor of the mattpocock/skills v1.1 development cycle; the superpowers-era rationale and migration history are preserved in git history (`docs/superpowers-customization-rationale.md`).

## Vendor Skills

Skills sourced from other projects. Run `python update.py` to pull latest versions.

Vendor skill directories use the official upstream skill name from `SKILL.md` unchanged. Do not rename them to match a simplified repo folder name.

| Skill | Description | Source |
|---|---|---|
| [browser-harness](skills/browser-harness/) | Control local or remote browsers through Browser Harness using CDP | [browser-use/browser-harness](https://github.com/browser-use/browser-harness/blob/main/SKILL.md) |
| **[mattpocock/skills suite](https://github.com/mattpocock/skills)** | | |
| [ask-matt](skills/ask-matt/) | Router for picking the right skill/workflow for a request | ↳ `skills/engineering/ask-matt` |
| [code-review](skills/code-review/) | Review diffs against repo standards and originating specs | ↳ `skills/engineering/code-review` |
| [codebase-design](skills/codebase-design/) | Shared vocabulary for designing deep modules at clean seams | ↳ `skills/engineering/codebase-design` |
| [diagnosing-bugs](skills/diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions | ↳ `skills/engineering/diagnosing-bugs` |
| [domain-modeling](skills/domain-modeling/) | Build and sharpen a project's domain model, glossary, and ADRs | ↳ `skills/engineering/domain-modeling` |
| [grill-with-docs](skills/grill-with-docs/) | Interview + domain modeling to build shared language before speccing | ↳ `skills/engineering/grill-with-docs` |
| [improve-codebase-architecture](skills/improve-codebase-architecture/) | Find architecture improvements and deeper module boundaries | ↳ `skills/engineering/improve-codebase-architecture` |
| [research](skills/research/) | Investigate a question against primary sources, capture findings | ↳ `skills/engineering/research` |
| [resolving-merge-conflicts](skills/resolving-merge-conflicts/) | Intent-traced merge/rebase conflict resolution | ↳ `skills/engineering/resolving-merge-conflicts` |
| [triage](skills/triage/) | Move issues through the triage state machine | ↳ `skills/engineering/triage` |
| [wayfinder](skills/wayfinder/) | Plan work too big for one session as a shared map of decision tickets | ↳ `skills/engineering/wayfinder` |
| [grilling](skills/grilling/) | Shared interview loop used by the grill skills | ↳ `skills/productivity/grilling` |
| [grill-me](skills/grill-me/) | Deep interview on any plan or design decision | ↳ `skills/productivity/grill-me` |
| [writing-great-skills](skills/writing-great-skills/) | Reference for writing and editing skills — vocabulary and principles for predictable skills | ↳ `skills/productivity/writing-great-skills` |
| [remotion-best-practices](skills/remotion-best-practices/) | Best practices for Remotion-based video creation in React, including preview and render workflows | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion-best-practices) |
| [revealjs](skills/revealjs/) | Create polished reveal.js presentations, decks, and slideshows with HTML and CSS | [ryanbbrown/revealjs-skill](https://github.com/ryanbbrown/revealjs-skill/tree/main/skills/revealjs) |
| **[ui-ux-pro-max suite](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** | | |
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

The Codex plugin package is context-only and does not contain a `skills/` directory, so Codex should load these skills through the copied/mirrored skill directories above instead of as plugin-bundled skills. The SessionStart hook injects Chrome DevTools MCP ownership guidance so the browser cleanup rules are available before the model chooses any browser behavior. A Codex PostToolUse hook records Chrome DevTools MCP usage for the active turn, and the Stop hook checks that marker plus transcript evidence. Only when needed, it blocks finalization with a reminder to close only owned isolated DevTools browser sessions. It does not run cleanup scripts.

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
