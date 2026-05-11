---
name: restart-stale-docker
description: Use when Docker Desktop on Windows appears open but Docker CLI commands hang, time out, return Server null, cannot find docker engine named pipes, or report the daemon is not running.
---

# Restart Stale Docker

## Overview

Use this skill to distinguish a healthy Docker Desktop session from a stale Windows/WSL2 session, then restart only the Docker Desktop stack needed to recover the engine.

The stale pattern is: Desktop UI processes exist, but `docker version` does not return server info quickly, Docker engine named pipes are missing or unresponsive, or CLI probes hang.

## Diagnosis

Run bounded probes first. Never let Docker CLI commands run without a timeout.

```powershell
Get-Process -Name 'Docker Desktop','com.docker.backend','com.docker.proxy','vpnkit','dockerd','docker' -ErrorAction SilentlyContinue |
  Select-Object ProcessName,Id,CPU,StartTime,Responding

Get-ChildItem -Path '\\.\pipe\' -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -match 'docker|Docker' } |
  Select-Object -ExpandProperty Name

wsl.exe -l -v

Get-Service -Name 'com.docker.service','LxssManager' -ErrorAction SilentlyContinue |
  Select-Object Name,Status,StartType
```

For the CLI probe, use a job timeout so a stale daemon cannot block the turn:

```powershell
$job = Start-Job -ScriptBlock { docker version --format '{{json .}}' 2>&1 }
if (Wait-Job $job -Timeout 15) {
  Receive-Job $job
} else {
  Stop-Job $job -ErrorAction SilentlyContinue
  'docker version timed out after 15 seconds'
}
Remove-Job $job -Force -ErrorAction SilentlyContinue
```

Interpretation:

- Healthy: `docker version` returns both `Client` and `Server`; verify with `docker ps`.
- Down: no Docker Desktop/backend processes and no engine pipes.
- Stale: Desktop or `docker-desktop` WSL is running, but `docker version` has `Server: null`, cannot open `dockerDesktopLinuxEngine` or `docker_engine`, or times out.

## Recovery

First clear hung CLI probes and stale Desktop/backend processes:

```powershell
Get-Process -Name 'Docker Desktop','com.docker.backend','com.docker.proxy','vpnkit','dockerd','docker' -ErrorAction SilentlyContinue |
  Stop-Process -Force -ErrorAction SilentlyContinue
```

Terminate only Docker Desktop's WSL distro, not the user's normal Linux distro:

```powershell
wsl.exe --terminate docker-desktop 2>$null
Start-Sleep -Seconds 5
```

Relaunch Docker Desktop:

```powershell
$desktop = Join-Path $Env:ProgramFiles 'Docker\Docker\Docker Desktop.exe'
if (-not (Test-Path -LiteralPath $desktop)) {
  $desktop = Join-Path ${Env:ProgramFiles(x86)} 'Docker\Docker\Docker Desktop.exe'
}
if (-not (Test-Path -LiteralPath $desktop)) {
  throw 'Docker Desktop.exe not found in Program Files.'
}
Start-Process -FilePath $desktop -WindowStyle Hidden
```

Poll for readiness with short CLI timeouts:

```powershell
$deadline = (Get-Date).AddSeconds(120)
$attempt = 0
while ((Get-Date) -lt $deadline) {
  $attempt++
  $job = Start-Job -ScriptBlock { docker version --format '{{json .}}' 2>&1 }
  if (Wait-Job $job -Timeout 10) {
    $text = (Receive-Job $job) -join "`n"
    Remove-Job $job -Force -ErrorAction SilentlyContinue
    if ($text -match '"Server"\s*:\s*\{') {
      "READY attempt=$attempt"
      $text
      break
    }
    "NOT_READY attempt=$attempt"
    $text
  } else {
    Stop-Job $job -ErrorAction SilentlyContinue
    Remove-Job $job -Force -ErrorAction SilentlyContinue
    "TIMEOUT attempt=$attempt"
  }
  Start-Sleep -Seconds 5
}
```

## Verification

After `docker version` returns server info, run:

```powershell
docker ps --format 'table {{.ID}}\t{{.Names}}\t{{.Status}}'
```

Report whether Docker is healthy and list any running containers. If `docker version` still times out after the deep restart, report that Docker Desktop remains stale and include the current process, pipe, WSL, and service state.

## Guardrails

- Use this workflow for local Windows Docker Desktop/WSL2 only.
- Do not run `wsl --shutdown` unless the user explicitly asks; it stops all WSL distros.
- Do not remove containers, images, volumes, or Docker data.
- Do not kill unrelated WSL distros such as `Ubuntu-22.04`.
- Always use command timeouts or job-based timeouts around Docker CLI probes.
