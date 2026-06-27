---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and development work should be finalized
---

# Finishing a Development Branch

## Overview

Finalize development work without presenting integration choices.

**Core principle:** Verify tests -> create a branch if the worktree is detached -> commit remaining changes -> merge to `main` -> verify on `main` -> clean up owned worktree.

**Announce at start:** "I'm using the finishing-a-development-branch skill to complete this work."

## The Process

### Step 1: Verify Tests On The Feature Branch

Run the project's normal test suite before finishing:

```bash
npm test / cargo test / pytest / go test ./...
```

If tests fail, stop and fix the failures. Do not commit or merge failing work.

### Step 2: Commit Remaining Changes

Check status:

```bash
git status --short
```

If there are uncommitted changes, confirm you are on a development branch before invoking the `commit` skill:

```bash
git branch --show-current
```

If the current branch is empty/detached, check whether this is a linked worktree:

```bash
git rev-parse --git-dir
git rev-parse --git-common-dir
git worktree list --porcelain
```

If it is a linked worktree, create a development branch in the current worktree before invoking the `commit` skill. Use the default `codex/` prefix, derive a short slug from the task or changed files, and make it unique if needed:

```bash
git switch -c codex/<short-task-slug>
```

Do not ask the user for confirmation just to create this branch. This is the normal Codex app worktree finish path because app-created worktrees start detached by default.

If the current branch is empty/detached and this is not a linked worktree, stop and report that the working tree is not on a development branch. Do not commit.

If the current branch is `main`, `master`, or `trunk`, stop and report that the working tree is not on a development branch. Do not commit.

If you are on a development branch, use the `commit` skill to stage and commit all visible non-secret modified and untracked files, including files outside the current task or session. If the branch is already clean because the implementation plan made task-level commits, continue.

Do not ask the user whether to commit once you have confirmed you are on a development branch.

### Step 3: Detect Branch And Worktree State

Collect:

```bash
git rev-parse --git-dir
git rev-parse --git-common-dir
git rev-parse --show-toplevel
git branch --show-current
git merge-base HEAD main
```

If there is no current branch, create a named branch using the default `codex/` prefix before merging. This should only be a safety net for already-clean detached worktrees; uncommitted detached worktrees should have been branched in Step 2 before committing.

### Step 4: Merge Back To `main`

Do not present merge/PR/keep/discard options. The default final action is always a local merge to `main`.

Before switching to `main`, verify the main checkout is clean enough to merge:

```bash
git -C <main-worktree-root> status --short
```

If `main` has unrelated uncommitted changes, stop and report the blocker. Do not overwrite or stash user changes unless explicitly instructed.

Merge from the main worktree root:

```bash
git -C <main-worktree-root> checkout main
git -C <main-worktree-root> pull
git -C <main-worktree-root> merge <feature-branch>
```

If the merge conflicts, stop and report the conflict. Do not guess through conflict resolution.

### Step 5: Verify On `main`

Run the project's normal test suite again on `main`.

If tests fail after merge, fix them on `main`, commit the fix, and rerun tests. Do not report completion until the merged `main` passes.

### Step 6: Clean Up Owned Worktree And Branch

Only clean up worktrees created under `.worktrees/`, `worktrees/`, or `~/.config/superpowers/worktrees/`.

From the main worktree root:

```bash
git worktree remove <feature-worktree-path>
git worktree prune
git branch -d <feature-branch>
```

If the worktree is harness-owned or outside those directories, leave it in place and report its path.

## Common Mistakes

**Asking for integration choice**
- Problem: User has already set the policy.
- Fix: Always commit and merge back to `main` locally.

**Overwriting dirty `main`**
- Problem: User changes can be lost.
- Fix: Stop if `main` has uncommitted changes that would interfere with merge.

**Stopping on Codex app detached worktrees**
- Problem: Codex app worktrees start on detached HEAD, so there may be no branch yet.
- Fix: In a linked worktree, create a `codex/` branch before invoking the commit skill.

**Skipping post-merge tests**
- Problem: Feature branch passes but merged `main` breaks.
- Fix: Always verify again after merge.

## Red Flags

**Never:**
- Present merge/PR/keep/discard options
- Push or create a PR as the default finish action
- Delete or overwrite user changes on `main`
- Merge failing tests
- Remove a worktree before the merge and post-merge verification succeed

**Always:**
- Commit remaining work
- Merge back to `main` locally
- Verify tests before and after merge
- Clean up only owned worktrees
