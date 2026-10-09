# sz-skills

My personal collection of AI agent skills, synced across devices.

## My Skills

| Skill | Description |
|---|---|
| [download-online-video](skills/download-online-video/) | Download YouTube and Bilibili videos, audio, and subtitles with a cross-platform `yt-dlp` helper |
| [global-project-preferences](skills/global-project-preferences/) | Default tech stack preferences for new projects, extensions, scripts, and other greenfield work |
| [repo-visualizer](skills/repo-visualizer/) | Generate a human-readable interactive HTML codebase structure report with Mermaid, inputs/outputs, and clickable file details |
| [commit](skills/commit/) | Fast, bounded Git closure workflow — reviews and stages all changes, commits, applies checkout-specific push rules, and verifies |
| [openwiki](skills/openwiki/) | Generate the project's wiki directly in its ignored `openwiki/` GitHub Wiki clone using the CLI's default output and sync that same folder to GitHub |
| [setup-git-repo](skills/setup-git-repo/) | Bootstrap a local and remote GitHub repository, add the engineering-skills config, generate and publish its Wiki from `openwiki/`, and install a bundled post-commit hook that pulls, regenerates, commits, and pushes the Wiki automatically in a detached background job |
| [t3code-file-links](skills/t3code-file-links/) | Hand off local files in T3 Code with copyable native paths, valid in-project links, and rendered image previews |

## Vendor Skills (customized)

Skills sourced from other projects with local edits. These are skipped by `update.py` — update manually when needed.

| Skill | Description | Source | Customization |
|---|---|---|---|
| **[mattpocock/skills suite](https://github.com/mattpocock/skills)** | | | Locally adapted development-cycle skills |
| [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/) | One-time GitHub repo configuration — GitHub Issues, triage labels, docs layout | ↳ `skills/engineering/setup-matt-pocock-skills` | Requires a reachable GitHub remote and stops before writing when one is missing; uses GitHub Issues exclusively; keeps canonical triage labels, `AGENTS.md` when no agent file exists, and write-then-report behavior; model-invocable so `setup-git-repo` can invoke it; writes the v1.3 `GLOSSARY.md` layout and renames a repo's legacy `CONTEXT.md` domain glossary when rerun |
| [wayfinder](skills/wayfinder/) | Plan multi-session work as a map of decision tickets | ↳ `skills/engineering/wayfinder` | Persists every grilling-round exchange as an issue checkpoint so interrupted sessions can resume without the original chat transcript |
| [to-spec](skills/to-spec/) | Synthesize the current conversation into a published spec | ↳ `skills/engineering/to-spec` | Non-executable spec parents, Structured HTML Companion review aid, and explicit handoff to `/to-tickets` |
| [to-tickets](skills/to-tickets/) | Break a spec into tracer-bullet tickets with blocking edges | ↳ `skills/engineering/to-tickets` | Direct single-ticket requests publish without a granularity quiz; staged graph publication before queue labels, native parent/dependency verification, `Requirement:` trace fields, UI acceptance criteria, cross-phase change propagation, HTML plan companion |
| [implement](skills/implement/) | Implement a direct request or ticket with TDD, code review, commit, and a review-ready PR | ↳ `skills/engineering/implement` | Direct work gets a tracker record without entering the Automode implementation queue; also adds the no-fallback hard gate, suggest-don't-auto-apply, version-upgrade test cleanup, visual + end-to-end UI checks with close-out e2e pass, cross-phase change propagation, review-ready PR creation, and local skill names |
| [tdd](skills/tdd/) | Test-driven development with seam-based red-green loops | ↳ `skills/engineering/tdd` | Reapplies local rules: command timeouts, user-requirement hierarchy, required end-to-end pass (real-data full run, live browser walkthrough for web apps) on top of visual UI checks, no silent fallbacks, stale v1/v2 test cleanup, and review-stage refactoring (renamed from local `test-driven-development` to the upstream name) |
| [prototype](skills/prototype/) | Throwaway logic/UI prototypes to answer design questions | ↳ `skills/engineering/prototype` | UI options shown together on one static HTML comparison page kept until the user decides; a dev server only when genuinely needed, bound for Tailscale and stopped before handoff unless the user asks to keep it |
| [handoff](skills/handoff/) | Compact the current conversation into a handoff document for another agent to pick up | ↳ `skills/productivity/handoff` | Saves the handoff doc to the workspace root instead of the OS temp dir, and stays model-invocable |
| [grilling](skills/grilling/) | Shared interview loop used by the grill skills | ↳ `skills/productivity/grilling` | Bounds the design tree to requested behavior; excludes speculative recovery and preventable concurrency branches |
| [grill-me](skills/grill-me/) | Deep interview on any plan or design decision | ↳ `skills/productivity/grill-me` | Harness-correct loading of `grilling` |
| [grill-with-docs](skills/grill-with-docs/) | Interview + domain modeling to build shared language before speccing | ↳ `skills/engineering/grill-with-docs` | Harness-correct loading of `grilling` and `domain-modeling` |
| [triage](skills/triage/) | Move issues through the triage state machine | ↳ `skills/engineering/triage` | Harness-correct loading of `grilling` and `domain-modeling` |
| [improve-codebase-architecture](skills/improve-codebase-architecture/) | Find architecture improvements and deeper module boundaries | ↳ `skills/engineering/improve-codebase-architecture` | Harness-correct loading of its reference skills; architecture vocabulary keeps real identifiers and glossary terms |
| [ask-matt](skills/ask-matt/) | Router for picking the right skill/workflow for a request | ↳ `skills/engineering/ask-matt` | GitHub-only routing, user-directed `/retro`, summaries defer to the skill definitions |
| [retro](skills/retro/) | Propose environment improvements from a coding-session retrospective (user-invoked) | ↳ `skills/engineering/retro` | Harness-correct loading; finds Pi, Codex, and Claude Code session logs; reads only the named session and changes nothing without approval |
| [implement-spec](skills/implement-spec/) | Implement a whole spec's ticket graph on one integration branch (user-invoked) | ↳ `skills/engineering/implement-spec` | Workers share the local tdd policy; the orchestrator owns integration validation, the final code review, and the aggregate PR; see the rationale |
| [code-review](skills/code-review/) | Review diffs against repo standards and originating specs | ↳ `skills/engineering/code-review` | Reviews working-tree changes before commit; see the rationale |
| [codebase-design](skills/codebase-design/) | Shared vocabulary for designing deep modules at clean seams | ↳ `skills/engineering/codebase-design` | Vocabulary rules apply to architectural discussion; real names stay exact |
| [unslop](skills/unslop/) | Cut AI tells from user-facing writing | [cursor/plugins pstack by Lauren Tan](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop) | Scoped to user-facing prose; exact technical terms and quotations are preserved; punctuation is judgment, not a ban |

> The customization rationale for the mattpocock/skills suite lives in [docs/mattpocock-customization-rationale.md](docs/mattpocock-customization-rationale.md). This repo previously vendored the [obra/superpowers](https://github.com/obra/superpowers) suite, fully retired in favor of the mattpocock/skills development cycle (v1.3 since 2026-10); the superpowers-era rationale and migration history are preserved in git history (`docs/superpowers-customization-rationale.md`).

## Vendor Skills

Skills sourced from other projects. Run `python update.py` to pull latest versions.

Anthropic's `frontend-design` is the sole visual-design skill. Architecture, prototyping, and video tooling remain separate. UI testing defaults to desktop; other devices require an explicit user request.

Vendor skill directories use the official upstream skill name from `SKILL.md` unchanged. Do not rename them to match a simplified repo folder name.

| Skill | Description | Source |
|---|---|---|
| [frontend-design](skills/frontend-design/) | Anthropic's guidance for visual direction, typography, layout, and UI copy | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| [browser-harness](skills/browser-harness/) | Control local or remote browsers through Browser Harness using CDP | [browser-use/browser-harness](https://github.com/browser-use/browser-harness/blob/main/SKILL.md) |
| **[mattpocock/skills suite](https://github.com/mattpocock/skills)** | | |
| [pr](skills/pr/) | Shape a PR body: smallest visual, before/after evidence, merge danger (model-invoked) | ↳ `skills/engineering/pr` |
| [diagnosing-bugs](skills/diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions | ↳ `skills/engineering/diagnosing-bugs` |
| [domain-modeling](skills/domain-modeling/) | Build and sharpen a project's domain model, glossary, and ADRs | ↳ `skills/engineering/domain-modeling` |
| [research](skills/research/) | Investigate a question against primary sources, capture findings | ↳ `skills/engineering/research` |
| [wizard](skills/wizard/) | Interactive bash walkthroughs for procedures only a human can perform | ↳ `skills/engineering/wizard` |
| [teach](skills/teach/) | Teach one concept across sessions in a stateful learning workspace | ↳ `skills/productivity/teach` |
| [to-questionnaire](skills/to-questionnaire/) | Turn an unanswerable decision into a questionnaire for the person who can answer it | ↳ `skills/productivity/to-questionnaire` |
| [wait-what](skills/wait-what/) | One-word corrective that re-pitches a message that didn't land | ↳ `skills/productivity/wait-what` |
| [writing-for-agents](skills/writing-for-agents/) | Reference for writing and editing skills — vocabulary and principles for predictable skills | ↳ `skills/productivity/writing-for-agents` |
| [remotion-best-practices](skills/remotion-best-practices/) | Best practices for Remotion-based video creation in React, including preview and render workflows | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion-best-practices) |

## Setup

Requires: Python 3.8+, [gh CLI](https://cli.github.com/) (authenticated)

```sh
git clone https://github.com/stanley50z/sz-skills ~/sz-skills
cd ~/sz-skills
python setup.py
```

`setup.py` installs every skill in this repo, installs the repo-managed global instructions under `global/`, and registers the local `sz-skills` plugins for Codex and Claude Code. Their agent-hook manifests are intentionally empty.
The installed global instructions read the detailed UI checklist from `~/sz-skills/global/UI-GUIDELINES.md`; keep the source checkout at `~/sz-skills`. That reference is not copied separately. If the checkout moves, update the source pointer and rerun setup.
It prepends the current user's GitHub username to the `AGENTS.md` files installed for Codex, Pi, and Opencode. Pass `--github-username <name>` to set it explicitly, set `SZ_GITHUB_USERNAME`, or let setup read the authenticated account from `gh`. If none is available, setup installs the generic instructions and prints a warning.
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

`setup.py` also installs:

- `global/AGENTS.md` => generated `~/.codex/AGENTS.md`, with a local GitHub identity header when resolved
- `global/AGENTS.md` => generated `~/.pi/agent/AGENTS.md`, with the same identity header for Pi
- `global/AGENTS.md` => generated `~/.config/opencode/AGENTS.md`, with the same identity header for Opencode
- `global/CLAUDE.md` -> `~/.claude/CLAUDE.md`

It also registers the local `sz-skills` plugins:

- Codex: adds the hook-only `.codex-hook-plugin` package as the `sz-skills` local marketplace and enables `sz-skills@sz-skills` in `~/.codex/config.toml`.
- Claude Code: enables `sz-skills@sz-skills` in `~/.claude/settings.json` and records the repo path in Claude's plugin install state.

`hooks/` is the source of truth for every hook file. `setup.py` mirrors the Codex-relevant files (everything except the Claude-only `hooks.json` and `session-start`) into `.codex-hook-plugin/hooks/`, adding new files and deleting stale ones, so edit hooks only under `hooks/` and re-run `python setup.py`.

`setup.py` also points `core.hooksPath` at the repo-managed `githooks/` directory. The `githooks/post-commit` hook re-runs `setup.py` after any commit that touches `skills/` or `global/`, while `githooks/post-merge` runs it after successful merge-based pulls. Together they keep the installed skill copies in sync with the repo.

The Codex plugin package does not contain a `skills/` directory; Codex loads skills through the copied/mirrored directories above. Both plugins register no agent hooks. The old browser-context, Chrome DevTools tracking/reminder, and desktop-notification registrations were removed on 2026-10-08. Keep these manifests empty so setup does not restore them. Herdr manages its own integrations separately and is the only agent-hook integration retained on this machine.

The same cleanup removed Claude's permission toast, the installed Superpowers startup hook (without removing its skills), and Codex's native `notify` command. A Superpowers plugin update can restore its vendor hook; check its installed `hooks/hooks.json` after updates. Git hooks and Pi extension callbacks were not changed.

Cleanup backups, verification results, and test logs are under `C:/Users/13982/.codex/diagnostics/hook-failure-2026-10-08/`.

## Updating Vendor Skills

Always pull the latest repo state before updating vendor skills. In this repo, "update skills" means:

```sh
cd ~/sz-skills
git pull --ff-only
python update.py
python setup.py
git diff              # review changes
git add -A && git commit -m "chore: update vendor skills"
```
