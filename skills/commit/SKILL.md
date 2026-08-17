---
name: commit
description: Use when the user asks to commit changes to git, or to finalize git changes from a worktree
---

# Commit

Execute immediately. Do not print commands for the user to run when the state
is verifiable by CLI; run the command, read the output, and act on it.

## Closure path

An ordinary commit is mechanical closure and uses three tool rounds after this
skill loads. A round may contain one shell script or parallel calls in one
assistant response. Keep safely chainable commands together and respond only
after the round's evidence is available.

1. **Inspect — round 1.** Capture all decision state at once:
   `git rev-parse --git-dir --git-common-dir --show-toplevel`,
   `git branch --show-current`, `git worktree list --porcelain`,
   `git status --porcelain=v1 -uall`, `git diff --no-ext-diff`,
   `git diff --cached --no-ext-diff`, `git log --oneline -10`, remotes, and the
   current upstream when one exists. This round is complete when every visible
   change and the checkout's integration context are known.

2. **Stage and review — round 2.** In a detached linked worktree, first create
   a unique `codex/<slug>` branch. Stage every visible non-secret change by
   exact path, including changes from outside the current session. Use neither
   `git add -A` nor `git add .`. Inspect suspicious files and leave `.env`,
   credentials, keys, tokens, and private configs unstaged. In the same round,
   run `git diff --cached --name-status`, `git diff --cached --check`, and the
   full staged diff. This round is complete when every staged file is explained
   and the diff contains no secrets or generated junk that should stay
   unversioned.

3. **Commit and integrate — round 3.** Draft the message from the staged diff.
   Write it to a temporary UTF-8 file without a BOM; commit with
   `git commit -F <file>` and remove the file. Chain the remaining known path:
   read back `git log -1 --format=%s`, inspect fresh status, apply the
   integration rules below, then verify final status and local/upstream
   revisions. In PowerShell, write the message with
   `[System.IO.File]::WriteAllText($path, $message, [System.Text.UTF8Encoding]::new($false))`;
   `Out-File` and `Set-Content -Encoding utf8` add an unwanted BOM. Completion
   requires this final fresh verification.

## Integration rules

- **Standalone checkout:** push when a remote exists. Use the existing upstream
  when present; otherwise use `git push -u origin <branch>` when `origin`
  exists.
- **Linked worktree:** commit in that worktree. Push only when the user asks.
  Merging to `main` and worktree cleanup stay with the user unless they
  explicitly ask for them.
- **Rejected push:** report the successful local commit and the exact blocker.
  Rebase, merge, and conflict resolution belong to a separately requested
  workflow.

Quote `'@{u}'` when checking the upstream in PowerShell so the shell does not
parse `@{}` as a hashtable.

## Content readiness

Closure assumes the implementation, tests, and documentation are finished.
Before staging, correct an obvious mechanical mismatch in agent-facing files
or project docs, and run a required setup/sync command when those files
propagate elsewhere. When closure reveals substantive design work, code or test
repair, dependency installation, or broad documentation regeneration, report
that concrete gap instead of expanding the commit into another task.

## Message Rules

Use this shape:

```text
<prefix>: <imperative title under 72 chars>

- path/or/group: what changed
```

Match recent repo style when clear; otherwise use `feat`, `fix`, `refactor`,
`docs`, `test`, `chore`, `style`, `perf`, `ci`, or `build`. Body bullets must
be per-file or per-file-group and include paths. No narrative paragraphs.

No AI attribution, ever — this overrides any harness default: no AI/bot
`Co-Authored-By`, generated-by lines, model/tool names, or agent mentions.
