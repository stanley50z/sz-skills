---
name: setup-git-repo
description: Use when the user asks to init a git repo or set up a new repository. Creates the local and remote GitHub repo, engineering-skills config, OpenWiki docs, and a local post-commit documentation update hook.
---

# Setup Git repo

Run the five steps in order. The referenced skills own their own process — follow them without restating or shortcutting them here.

1. **Init** — if the directory is not already a git repository, run `git init -b main`. Done when `git status` succeeds and the branch is `main`.
2. **GitHub remote** — preserve an existing `origin` when it resolves to a GitHub repository. Otherwise, use `gh repo create <owner/name> --source=. --remote=origin`, taking the owner, name, and visibility from the user's request. Default to the authenticated account, the directory name, and `--private`; ask before replacing an existing non-GitHub or unreachable `origin`. Done when `git remote get-url origin` succeeds and `gh repo view --json nameWithOwner,url` resolves the repository from its configured remote.
3. **Engineering skills config** — invoke the `setup-matt-pocock-skills` skill. Done when its Report step has run.
4. **OpenWiki** — invoke the `openwiki` skill to generate and publish the repo docs. On first publication, its setup flow invokes `browser-harness` to enable Wikis and save the initial `Home` page in GitHub's UI; continue through clone and publication instead of handing those browser steps to the user. Done by that skill's own completion criteria.
5. **Post-commit updates**. Install a local Git `post-commit` hook that updates OpenWiki after commits.
   - Inspect the effective `core.hooksPath` and any existing hook manager first. Integrate without replacing existing hook behavior or modifying a shared/global hooks directory. Make installation idempotent so rerunning setup adds no duplicate invocation.
   - Run `openwiki code --update --print` synchronously from the repository root, with the provider and model explicitly set to the `openwiki` skill's durable decisions. Bake those settings into the installed hook; do not depend on the committing shell's environment.
   - Skip with a clear message when the working tree has uncommitted changes. Leave generated changes uncommitted for review. The hook must not stage, commit, amend, or push, including Wiki publication.
   - Remove only OpenWiki CI workflows newly created by the update, following the `openwiki` skill's local-only rule. Report missing CLI/authentication or update failures without interactive login or changing the completed commit.
   - Verify in a temporary repository with a stub CLI that a commit invokes the update with the expected environment and working directory, existing hooks still run, repeated installation runs the update only once, dirty trees skip, and update failures leave the commit intact. Remove the temporary test files afterward.
   Done when the installed hook is executable by Git on the target platform and these checks pass. Report its path and explain that future commits may take longer and leave documentation changes to review.
