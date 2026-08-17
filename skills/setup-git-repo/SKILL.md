---
name: setup-git-repo
description: Use when the user asks to init a git repo or set up a new repository — bootstraps the local and remote GitHub repo with the standard tooling (engineering-skills config, OpenWiki docs).
---

# Setup Git repo

Run the four steps in order. The referenced skills own their own process — follow them without restating or shortcutting them here.

1. **Init** — if the directory is not already a git repository, run `git init -b main`. Done when `git status` succeeds and the branch is `main`.
2. **GitHub remote** — preserve an existing `origin` when it resolves to a GitHub repository. Otherwise, use `gh repo create <owner/name> --source=. --remote=origin`, taking the owner, name, and visibility from the user's request. Default to the authenticated account, the directory name, and `--private`; ask before replacing an existing non-GitHub or unreachable `origin`. Done when `git remote get-url origin` succeeds and `gh repo view --json nameWithOwner,url` resolves the repository from its configured remote.
3. **Engineering skills config** — invoke the `setup-matt-pocock-skills` skill. Done when its Report step has run.
4. **OpenWiki** — invoke the `openwiki` skill to generate and publish the repo docs. On first publication, its setup flow invokes `browser-harness` to enable Wikis and save the initial `Home` page in GitHub's UI; continue through clone and publication instead of handing those browser steps to the user. Done by that skill's own completion criteria.
