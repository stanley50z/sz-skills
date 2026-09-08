---
name: setup-git-repo
description: Use when the user asks to init a git repo or set up a new repository. Creates the local and remote GitHub repo, engineering-skills config, OpenWiki docs, and an automatic post-commit Wiki synchronization hook.
---

# Setup Git repo

Run the five steps in order. The referenced skills own their own process — follow them without restating or shortcutting them here.

1. **Init** — if the directory is not already a git repository, run `git init -b main`. Done when `git status` succeeds and the branch is `main`.
2. **GitHub remote** — preserve an existing `origin` when it resolves to a GitHub repository. Otherwise, use `gh repo create <owner/name> --source=. --remote=origin`, taking the owner, name, and visibility from the user's request. Default to the authenticated account, the directory name, and `--private`; ask before replacing an existing non-GitHub or unreachable `origin`. Done when `git remote get-url origin` succeeds and `gh repo view --json nameWithOwner,url` resolves the repository from its configured remote.
3. **Engineering skills config** — invoke the `setup-matt-pocock-skills` skill. Done when its Report step has run.
4. **OpenWiki**. Invoke the `openwiki` skill to clone the native GitHub Wiki into `<project>/openwiki/`, generate directly into that same folder using the CLI's default output, and publish it. Its setup flow owns Wiki initialization through `browser-harness`. Complete setup before installing the update hook. Done by that skill's own completion criteria.
5. **Automatic Wiki synchronization**. Install the bundled [scripts/openwiki-sync](scripts/openwiki-sync) launcher and [scripts/openwiki_post_commit.py](scripts/openwiki_post_commit.py) runner by following [references/post-commit.md](references/post-commit.md). Copy the implementation instead of writing a new one. The hook must pull the Wiki, run OpenWiki, validate pages, commit changes, and push the Wiki automatically. Only the nested `openwiki/` repository is committed and pushed; preserve the main project commit and existing hooks. Done when the reference's installation checks pass and the installed paths and automatic workflow have been reported.
