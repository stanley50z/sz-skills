---
name: start-sz-video
description: Use when the user wants to start, relaunch, open, or verify the local sz-video non-Docker operator UI, Vite web app, or local API server.
---

# Start sz-video

Start the local `sz-video` operator UI stack without starting Docker containers. This skill is for the non-Docker web/API layer that controls and inspects the existing workflow.

## Quick Start

Run the bundled launcher from any working directory:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\13982\.sz-skills\skills\start-sz-video\scripts\start-sz-video.ps1"
```

Bundled script: `scripts/start-sz-video.ps1`.

The script prefers `C:\Users\13982\sz-video\.worktrees\video-workflow-operator-ui` because that worktree contains the PNPM workspace with `@sz-video/server` and `@sz-video/web`. It starts:

| Part | URL |
|---|---|
| Operator UI | `http://127.0.0.1:5173/` |
| Local API | `http://127.0.0.1:5174` |

## Rules

- Do not run Docker startup commands for this skill. Avoid `docker compose up` and `docker-compose up`.
- Do not use root `pnpm dev` directly in this Windows environment; it can recurse into bare `pnpm` and fail when `pnpm` is not on `cmd.exe` PATH.
- Use the script, which launches server and web separately through `corepack.cmd`.
- Keep logs outside the repo unless the user asks otherwise.
- If ports are already occupied, reuse them by default. Pass `-Restart` only when the user asks for a relaunch or stale dev server fix.

## Useful Options

```powershell
# Stop listeners on 5173/5174, then start fresh.
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\13982\.sz-skills\skills\start-sz-video\scripts\start-sz-video.ps1" -Restart

# Use a different checkout or worktree.
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\13982\.sz-skills\skills\start-sz-video\scripts\start-sz-video.ps1" -RepoRoot "C:\Users\13982\sz-video"
```

After launch, report the UI URL, API URL, process IDs, and log directory.
