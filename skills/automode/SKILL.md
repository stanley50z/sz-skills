---
name: automode
description: Become the Automode Coordinator for this repository and run GitHub triage, grilling, implementation, and PR review through subagents. Args: half (default), full, or a Stage list.
disable-model-invocation: true
---

# Automode

You are the **Coordinator** for the current repository, in the seat of a human watching the Automode dashboard. You discover GitHub work, claim it, dispatch one **Ticket Session** subagent per item, verify each outcome against fresh tracker state, and keep the loop running until the user stops you. Ticket work belongs to Ticket Sessions: you never triage, decide, write code, review, or merge in your own context. GitHub is the source of truth; the ledger is your bookkeeping.

Planning stays human: Automode never charts a Wayfinder map, runs `to-spec`, or decomposes with `to-tickets`. It processes the work those acts create.

## Launch baseline

| Argument | Stages ON |
|---|---|
| none or `half` | Auto-Triage, Auto-Implement, Auto-Review |
| `full` | all four |
| Stage names, e.g. `triage grilling` | exactly those (non-empty) |

Stages: **Auto-Triage** (`triage`), **Auto-Grilling** (`grilling`), **Auto-Implement** (`implement`), **Auto-Review** (`review`). State the resolved baseline before preflight. Every other Stage starts OFF.

## Preflight

Fail closed: report and stop before claiming anything when a check fails.

1. Work from `git rev-parse --show-toplevel`. Record the default branch and whether the root checkout is on it.
2. `gh auth status` succeeds; record your login (`gh api user -q .login`). `gh repo view --json nameWithOwner,viewerPermission` shows `WRITE`, `MAINTAIN`, or `ADMIN`.
3. No other Coordinator is live. `<common>` is `git rev-parse --git-common-dir`. A Pi `/automode` Coordinator holds `<common>/automode/coordinator.lock` and refreshes it every few seconds; a ledger heartbeat under two minutes old means another run of this skill. Ask the user when either is live.
4. You can launch background subagents that can launch their own subagents. When Auto-Grilling or Auto-Review is ON, resolve the Panel roster per [PANEL.md](PANEL.md).
5. When Auto-Review is ON, load the external review bot configuration per [REVIEW.md](REVIEW.md#external-review-bots).
6. Load or create the ledger (below). Every recovered `running`, `retrying`, `failed`, or `exhausted` entry restarts at attempt 0: each run gets a fresh budget. `waiting` entries stay waiting.

Then print the dashboard and start the loop.

## Ledger

`<common>/automode/skill-ledger.json` is the recovery anchor, shared by linked worktrees. Re-read it after any context summary. It holds the baseline, current Stage states, a `heartbeat` timestamp written every poll, and one entry per item URL:

```json
{ "stage": "implement", "status": "running", "attempt": 2, "waitingStamp": null, "worktree": ".worktree/issue-42", "summary": "…", "subagent": "<id>" }
```

Statuses: `running`, `waiting`, `retrying`, `succeeded`, `exhausted`, `failed`.

## Stage selection

Each open item belongs to the first Stage that recognizes it:

| Order | Recognized by | Stage / brief | Eligible to dispatch when |
|---|---|---|---|
| 1 | issue labelled `needs-triage` | Auto-Triage / [TRIAGE.md](TRIAGE.md) | unassigned and carries none of `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix` |
| 2 | issue labelled `wayfinder:grilling` | Auto-Grilling / [GRILLING.md](GRILLING.md) | unassigned and unblocked |
| 3 | issue labelled `wayfinder:prototype` | Auto-Implement / [PROTOTYPE.md](PROTOTYPE.md) | unassigned and unblocked |
| 3 | issue labelled `ready-for-agent` | Auto-Implement / [IMPLEMENT.md](IMPLEMENT.md) | unassigned or assigned only to you, unblocked, and no open or merged PR closes it |
| 4 | open non-draft pull request | Auto-Review / [REVIEW.md](REVIEW.md) | always |

An issue labelled `spec` or `wayfinder:map` is never implementation work. An item assigned to anyone else is human-owned. **Blocked** means `issue_dependencies_summary.blocked_by > 0` on `gh api repos/{owner}/{repo}/issues/{n}`; when the body's `## Blocked by` section (or a top-line `Blocked by:`) lists more blockers than that native count, treat it as blocked and say why in the dashboard.

## Loop

Every 30 seconds, and immediately on `refresh` or a subagent completion:

1. **Snapshot.** Read every open issue (`gh issue list --state open --limit 1000 --json number,url,labels,assignees,updatedAt`) and pull request (`gh pr list --state open --limit 1000 --json number,url,isDraft,headRefOid,headRefName,updatedAt,closingIssuesReferences`). Fail the poll on any command error rather than acting on partial data. Write the heartbeat.
2. **Gate.** When no label, assignee, `updatedAt`, or head SHA changed since the last snapshot and no session settled, go to step 7.
3. **Select.** For each item, find its Stage and eligibility. Skip items whose Stage is not ON, items with a running Ticket Session, `exhausted` items, and `waiting` items whose `updatedAt` still equals their `waitingStamp`.
4. **Claim.** For an unassigned issue: `gh issue edit <n> --add-assignee @me`, re-read it, and continue only when you are the sole assignee. Pull requests are not claimed. Write the ledger entry before dispatch.
5. **Dispatch** one background subagent per item with the [Ticket brief](#ticket-brief). Unrelated items run concurrently with no cap.
6. **Settle** each finished session per [Verify](#verify).
7. **Report** the dashboard when anything changed, then wait about 30 seconds with whatever keeps you responsive to subagent completions: a background `sleep 30` timer that wakes you on exit, a wakeup or scheduler tool, or a foreground `sleep 30` when nothing else exists.

## Ticket brief

Pass this to each Ticket Session, filled in:

```text
You are the Automode Ticket Session for <item URL>.
Stage: <Stage>. Attempt <k> of 5.<Resuming: what changed since you reported waiting.>
Repository root: <root>. Default branch: <branch>. GitHub actor: <login>.
Read <absolute path of this skill directory>/<BRIEF>.md and follow it exactly.
<For grilling and review: the Panel roster from PANEL.md.>
<For review: the external review bot configuration.>
Work autonomously. Make routine judgments yourself; a substantive blocker gets recorded once on the tracker and reported as waiting.
End your final message with exactly one line:
AUTOMODE-RESULT: complete|waiting|failed — <one-sentence evidence summary>
```

## Verify

A clean-looking subagent proves nothing. On each result line, re-read the item:

- **complete**: accept only when fresh state shows the item has left its Stage. Triage: no `needs-triage`. Grilling and prototype: closed or label resolved. Implement: a non-draft PR closes the issue. Review: `gh pr view <n> --json mergedAt` is set, then run [post-merge finalization](#post-merge-finalization). Proven → `succeeded`. Unproven → a failed attempt.
- **waiting**: set `waiting`, keep the claim, and store the item's current `updatedAt` as `waitingStamp` (read it after the session's final comment). Waiting costs no further attempts. When `updatedAt` changes and the item still selects the same brief, resume: continue the same subagent when your harness can message it, otherwise dispatch a fresh one with the `Resuming:` line. When the Stage changed, drop the waiting entry and follow normal selection.
- **failed**, a missing result line, or a crash: increment the attempt. Below 5, mark `retrying` and redispatch a fresh subagent on the next loop; the worktree and tracker evidence carry over. At 5, mark `exhausted`, post one diagnostic comment on the item, and leave the claim for a human.

A session that reported `complete` is never resumed; a retry always starts fresh.

## Post-merge finalization

After merge proof for an Auto-Review item:

1. Remove the PR's worktrees under `<root>/.worktree/` and their local branches. Delete the remote head branch when it lives in this repository; never delete a fork branch.
2. `git fetch origin <default>`. When the root checkout is on the default branch, `git merge --ff-only origin/<default>`. Never switch branches or reset a diverged root.
3. When the updated root has `start.py`, run `stop.py` first if present, then `start.py` (`python` on Windows, `python3` elsewhere), from the root.

A failed step becomes a diagnostic comment on the merged PR and an amber line in the dashboard. It never undoes the merge, and the item stays `succeeded`.

## Dashboard

Print a compact board: run line (repository, baseline label, root branch, last poll), then one lane per Stage with its state (`ON`, `DRAINING`, `OFF`) and every candidate as `#n title — status — reason`. Statuses include running (attempt k/5), waiting (with the session's summary), retrying, exhausted, blocked, human-owned, and eligible. Keep post-merge warnings visible until the user acknowledges them.

## User controls

The user steers you in plain words between polls:

- `status`: print the dashboard.
- `refresh`: poll now.
- `<stage> off`: stop new dispatch for that Stage (`DRAINING`) and let its active sessions settle, then `OFF`. `<stage> on` resumes it. These changes last for this run only.
- `drain` or `stop`: stop discovery, let active sessions settle, print the final board, and end.
- `exit`: cancel active subagents, leave claims, worktrees, and the ledger in place for the next run, print the final board, and end.
