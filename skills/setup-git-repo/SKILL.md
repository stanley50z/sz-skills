---
name: setup-git-repo
description: Bootstrap a Git repository — git init plus the standard repo tooling (engineering-skills config, OpenWiki docs). Use when the user asks to init a git repo or set up a new repository.
---

# Setup Git repo

Run the three steps in order. The referenced skills own their own process — follow them without restating or shortcutting them here.

1. **Init** — if the directory is not already a git repository, run `git init`. Done when `git status` succeeds.
2. **Engineering skills config** — invoke the `setup-matt-pocock-skills` skill. Done when its Report step has run.
3. **OpenWiki** — invoke the `openwiki` skill to generate the repo docs. Done by that skill's own completion criteria.
