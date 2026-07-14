---
name: openwiki
description: Generate and maintain OpenWiki repository documentation (the openwiki/ directory) and publish it to the repo's native GitHub Wiki. Use when the user asks to set up OpenWiki in a repository, update the generated docs, or publish them to the GitHub Wiki — or when work touches the openwiki CLI, an openwiki/ directory, or an OPENWIKI block in AGENTS.md/CLAUDE.md.
---

# OpenWiki

OpenWiki is a CLI that generates and maintains agent-facing repository documentation under `openwiki/` — its **code mode**. Always invoke the `code` subcommand explicitly: bare `openwiki --update` targets the personal-mode wiki in `~/.openwiki/wiki`, which is unrelated to repository work. For CLI capabilities beyond this skill (personal mode, connectors, other providers), read the installed README at `<npm root -g>/openwiki/README.md`.

## Durable decisions

- OpenWiki runs **local-only**, on the saved ChatGPT-subscription login: set `OPENWIKI_PROVIDER` to `openai-chatgpt` for every run. The upstream README recommends a scheduled CI workflow, but that path needs a metered API key, so repositories stay free of OpenWiki CI: delete `.github/workflows/openwiki-update.yml` (or the GitLab equivalent) whenever a run recreates it.
- Generated docs publish to the repository's **native GitHub Wiki**, not MkDocs or GitHub Pages.
- Pages under `openwiki/` change by rerunning OpenWiki, never by hand-editing (unless explicitly asked).

## Where things live

| Location | Purpose |
| --- | --- |
| `openwiki/` in the repo | Generated docs; `quickstart.md` is the entry page; `INSTRUCTIONS.md` is the generation prompt, never published |
| `<!-- OPENWIKI:START/END -->` blocks in `AGENTS.md` / `CLAUDE.md` | Rewritten by OpenWiki on each code run; leave their contents to OpenWiki |
| `~/.openwiki/.env` | Provider and model selection plus ChatGPT OAuth tokens |
| Sibling `..\<repo>.wiki` clone | Git repository backing the GitHub Wiki tab |
| `~/.openwiki/wiki` | Personal-mode wiki — unrelated to repository docs |

Treat every value in `~/.openwiki/.env` as a password, the refresh token above all: if you must inspect the file, read variable names only — never print, copy, or commit a value.

## Update the generated docs

```powershell
$env:OPENWIKI_PROVIDER = 'openai-chatgpt'
openwiki code --update --print
```

Review `git status --short`, `git diff --check`, and `git diff`. A run may touch the `AGENTS.md`/`CLAUDE.md` blocks or recreate the CI workflow even when the docs are already current.

Done when every touched file is explained by the review and no OpenWiki CI workflow exists in the tree.

## Publish to the GitHub Wiki

The GitHub Wiki is a separate git repository, cloned as a **sibling** at `..\<repo>.wiki` (clone missing or wiki not yet created → [references/setup.md](references/setup.md)). The Wiki **flattens** all pages into one namespace, so publishing is copy + rename + link rewrite.

Map each source page to a wiki file:

- An existing wiki's pages are the mapping — match each source page to its established wiki page and keep names stable.
- On first publication, `openwiki/quickstart.md` becomes `Home.md`; give every other page a short readable flattened title (`architecture/overview.md` → `Architecture-overview.md`) free of `\ / : * ? " < > |`.
- Every page gets a `_Sidebar.md` entry; the sidebar's source of truth is the clone itself.

Rewrite links in the copied pages for the flattened namespace:

- Internal links → flattened page names without `.md`: `architecture/overview.md` becomes `Architecture-overview`.
- Links to main-repository files → absolute `https://github.com/<owner>/<repo>/blob/<branch>/...` (or `tree/...`) URLs. A relative `../` path cannot reach the main repository from the wiki repo.

Done when every page under `openwiki/` except `INSTRUCTIONS.md` has exactly one wiki page and a sidebar entry, and a search of the clone for `](../` and for relative links ending in `.md)` returns nothing (absolute `https://github.com/...` URLs are exempt).

Validate and push from the clone (the wiki's default branch — the one GitHub renders — is typically `master`):

```powershell
git -C ..\<repo>.wiki status --short
git -C ..\<repo>.wiki diff --check
git -C ..\<repo>.wiki add --all
git -C ..\<repo>.wiki commit -m "docs: sync OpenWiki pages"
git -C ..\<repo>.wiki push origin master
```

Done when the clone's local `HEAD`, upstream, and remote branch agree, and the Wiki tab renders `Home` with the sidebar.

## First-time setup

Installing the CLI, the ChatGPT login, initializing a repository's docs, and creating/cloning its GitHub Wiki: [references/setup.md](references/setup.md).
