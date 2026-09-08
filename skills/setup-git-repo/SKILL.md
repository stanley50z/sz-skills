---
name: setup-git-repo
description: Use when the user asks to init a git repo or set up a new repository. Creates the local and remote GitHub repo, engineering-skills config, OpenWiki docs, and a local post-commit documentation update hook.
---

# Setup Git repo

Run the five steps in order. The referenced skills own their own process — follow them without restating or shortcutting them here.

1. **Init** — if the directory is not already a git repository, run `git init -b main`. Done when `git status` succeeds and the branch is `main`.
2. **GitHub remote** — preserve an existing `origin` when it resolves to a GitHub repository. Otherwise, use `gh repo create <owner/name> --source=. --remote=origin`, taking the owner, name, and visibility from the user's request. Default to the authenticated account, the directory name, and `--private`; ask before replacing an existing non-GitHub or unreachable `origin`. Done when `git remote get-url origin` succeeds and `gh repo view --json nameWithOwner,url` resolves the repository from its configured remote.
3. **Engineering skills config** — invoke the `setup-matt-pocock-skills` skill. Done when its Report step has run.
4. **OpenWiki**. Invoke the `openwiki` skill to clone the native GitHub Wiki into `<project>/wiki/`, generate directly into that same folder, and publish it. Its setup flow owns Wiki initialization through `browser-harness`. Complete its output-directory support check before generation; if blocked, report the blocker and stop before installing the update hook. Done by that skill's own completion criteria.
5. **Post-commit updates**. Install a local Git `post-commit` hook that updates OpenWiki after commits.
   - Inspect the effective `core.hooksPath` and any existing hook manager first. Integrate without replacing existing hook behavior or modifying a shared/global hooks directory. Make installation idempotent so rerunning setup adds no duplicate invocation.
   - Run `openwiki code --update --print` synchronously from the main project root with the `openwiki` skill's verified output-directory configuration targeting `<project>/wiki/`. Bake that configuration and the skill's provider/model settings into the hook; do not depend on the committing shell's environment. Confirm that `wiki/` is the correct separate Wiki repository before running. Never fall back to a project-root `openwiki/` tree.
   - Skip with a clear message when either repository has uncommitted changes. Check the Wiki clone separately because the main repository ignores it. Leave generated changes inside `wiki/` uncommitted for review and later GitHub Wiki synchronization. Review any project agent-file changes separately. The hook must not stage, commit, amend, or push either repository.
   - Remove only OpenWiki CI workflows newly created by the update, following the `openwiki` skill's local-only rule. Report missing CLI/authentication or update failures without interactive login or changing the completed commit.
   - Verify in temporary project and Wiki repositories with a stub CLI that a commit invokes the update with the expected environment, source root, and output root. Confirm no `openwiki/` tree appears, Wiki Git metadata stays intact, existing hooks still run, repeated installation invokes the update only once, either dirty tree causes a skip, and failures leave the commit intact. Remove temporary test files afterward.
   Done when the installed hook is executable by Git on the target platform and these checks pass. Report its path and explain that future commits may take longer and leave Wiki changes for review and a separate sync.
