param(
    [string]$RepoRoot = "C:\Users\13982\sz-video",
    [string]$Worktree = "",
    [int]$ServerPort = 5174,
    [int]$WebPort = 5173,
    [string]$LogDir = (Join-Path $env:TEMP "sz-video-start"),
    [switch]$Restart,
    [switch]$NoVerify
)

$ErrorActionPreference = "Stop"

function Test-SzVideoWorkspace {
    param([string]$Path)

    return (
        (Test-Path -LiteralPath (Join-Path $Path "package.json")) -and
        (Test-Path -LiteralPath (Join-Path $Path "apps\server\package.json")) -and
        (Test-Path -LiteralPath (Join-Path $Path "apps\web\package.json"))
    )
}

function Resolve-SzVideoWorkspace {
    if ($Worktree -and (Test-SzVideoWorkspace -Path $Worktree)) {
        return (Resolve-Path -LiteralPath $Worktree).Path
    }

    $operatorWorktree = Join-Path $RepoRoot ".worktrees\video-workflow-operator-ui"
    if (Test-SzVideoWorkspace -Path $operatorWorktree) {
        return (Resolve-Path -LiteralPath $operatorWorktree).Path
    }

    if (Test-SzVideoWorkspace -Path $RepoRoot) {
        return (Resolve-Path -LiteralPath $RepoRoot).Path
    }

    throw "Could not find a sz-video PNPM workspace under '$RepoRoot'. Expected apps\server and apps\web packages."
}

function Resolve-Corepack {
    $nodeCorepack = "C:\Program Files\nodejs\corepack.cmd"
    if (Test-Path -LiteralPath $nodeCorepack) {
        return $nodeCorepack
    }

    $command = Get-Command corepack.cmd, corepack -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($command) {
        return $command.Source
    }

    throw "corepack was not found. Install Node.js with Corepack enabled before starting sz-video."
}

function Get-PortProcesses {
    param([int]$Port)

    Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
        ForEach-Object {
            $process = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue
            [pscustomobject]@{
                Port = $Port
                Pid = $_.OwningProcess
                ProcessName = $process.ProcessName
                Path = $process.Path
            }
        }
}

function Stop-PortListeners {
    param([int[]]$Ports)

    foreach ($port in $Ports) {
        Get-PortProcesses -Port $port | ForEach-Object {
            if ($_.Pid -and $_.Pid -ne $PID) {
                Stop-Process -Id $_.Pid -Force -ErrorAction SilentlyContinue
            }
        }
    }
}

function Wait-HttpOk {
    param(
        [string]$Url,
        [int]$TimeoutSeconds = 30
    )

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    $lastError = $null
    while ((Get-Date) -lt $deadline) {
        try {
            $response = Invoke-WebRequest -UseBasicParsing -Uri $Url -TimeoutSec 5
            if ($response.StatusCode -ge 200 -and $response.StatusCode -lt 500) {
                return $true
            }
        } catch {
            $lastError = $_.Exception.Message
        }
        Start-Sleep -Milliseconds 500
    }

    throw "Timed out waiting for $Url. Last error: $lastError"
}

function Start-PnpmPackage {
    param(
        [string]$Workspace,
        [string]$Corepack,
        [string]$PackageName,
        [string]$StdoutPath,
        [string]$StderrPath
    )

    Start-Process `
        -FilePath $Corepack `
        -ArgumentList @("pnpm", "--filter", $PackageName, "dev") `
        -WorkingDirectory $Workspace `
        -WindowStyle Hidden `
        -RedirectStandardOutput $StdoutPath `
        -RedirectStandardError $StderrPath `
        -PassThru
}

$workspace = Resolve-SzVideoWorkspace
$corepack = Resolve-Corepack
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

if ($Restart) {
    Stop-PortListeners -Ports @($ServerPort, $WebPort)
    Start-Sleep -Milliseconds 500
}

$serverOut = Join-Path $LogDir "sz-video-server.out.log"
$serverErr = Join-Path $LogDir "sz-video-server.err.log"
$webOut = Join-Path $LogDir "sz-video-web.out.log"
$webErr = Join-Path $LogDir "sz-video-web.err.log"

$serverProcesses = @(Get-PortProcesses -Port $ServerPort)
$webProcesses = @(Get-PortProcesses -Port $WebPort)

$serverProcess = $null
$webProcess = $null

if ($serverProcesses.Count -eq 0) {
    Remove-Item -LiteralPath $serverOut, $serverErr -Force -ErrorAction SilentlyContinue
    $serverProcess = Start-PnpmPackage -Workspace $workspace -Corepack $corepack -PackageName "@sz-video/server" -StdoutPath $serverOut -StderrPath $serverErr
}

if ($webProcesses.Count -eq 0) {
    Remove-Item -LiteralPath $webOut, $webErr -Force -ErrorAction SilentlyContinue
    $webProcess = Start-PnpmPackage -Workspace $workspace -Corepack $corepack -PackageName "@sz-video/web" -StdoutPath $webOut -StderrPath $webErr
}

if (-not $NoVerify) {
    Wait-HttpOk -Url "http://127.0.0.1:$WebPort/" | Out-Null
    Wait-HttpOk -Url "http://127.0.0.1:$ServerPort/api/preflight?folderPath=E:%5CVideos" | Out-Null
}

$currentServer = @(Get-PortProcesses -Port $ServerPort)
$currentWeb = @(Get-PortProcesses -Port $WebPort)

[pscustomobject]@{
    Workspace = $workspace
    WebUrl = "http://127.0.0.1:$WebPort/"
    ApiUrl = "http://127.0.0.1:$ServerPort"
    ServerPid = if ($currentServer.Count -gt 0) { ($currentServer | Select-Object -First 1).Pid } elseif ($serverProcess) { $serverProcess.Id } else { $null }
    WebPid = if ($currentWeb.Count -gt 0) { ($currentWeb | Select-Object -First 1).Pid } elseif ($webProcess) { $webProcess.Id } else { $null }
    LogDir = (Resolve-Path -LiteralPath $LogDir).Path
    StartedServer = [bool]$serverProcess
    StartedWeb = [bool]$webProcess
} | Format-List
