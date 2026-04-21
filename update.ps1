# Update vendor skills to latest upstream versions.
# Requires: gh CLI (authenticated)
#
# Usage:
#   cd ~/.sz-skills
#   .\update.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $MyInvocation.MyCommand.Path

# ── Helpers ──────────────────────────────────────────────────────────────

# Binary extensions to skip (font files, images, etc.)
$binaryExts = @(".ttf", ".woff", ".woff2", ".otf", ".eot", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg")

function Sync-RemoteDir {
    param(
        [string]$Repo,
        [string]$RemotePath,
        [string]$LocalDir,
        [string]$Indent = "  "
    )

    # Ensure local dir exists (remove stale file if a symlink was previously saved as a file)
    if (Test-Path $LocalDir) {
        if (-not (Test-Path $LocalDir -PathType Container)) {
            Remove-Item $LocalDir -Force
            New-Item -ItemType Directory -Path $LocalDir -Force | Out-Null
        }
    } else {
        New-Item -ItemType Directory -Path $LocalDir -Force | Out-Null
    }

    # Get listing — array of objects with name and type
    $raw = gh api "repos/$Repo/contents/$RemotePath" 2>$null
    if (-not $raw) {
        Write-Host "${Indent}WARNING: could not list $RemotePath" -ForegroundColor Red
        return
    }

    # Parse JSON entries
    $entries = $raw | ConvertFrom-Json

    # Handle single-object response (not an array)
    if ($entries -isnot [System.Array]) {
        $entries = @($entries)
    }

    foreach ($entry in $entries) {
        $name = $entry.name
        $type = $entry.type
        $remoteFull = "$RemotePath/$name"
        $localFull  = Join-Path $LocalDir $name

        if ($type -eq "dir") {
            Sync-RemoteDir -Repo $Repo -RemotePath $remoteFull -LocalDir $localFull -Indent "$Indent  "
            continue
        }

        # Skip binary files
        $ext = [System.IO.Path]::GetExtension($name).ToLower()
        if ($binaryExts -contains $ext) {
            Write-Host "${Indent}Skipping binary: $name" -ForegroundColor DarkGray
            continue
        }

        # Fetch file content (base64)
        $b64 = $entry.content
        if (-not $b64) {
            # Content not included in directory listing — fetch individually
            $b64 = gh api "repos/$Repo/contents/$remoteFull" --jq '.content' 2>$null
        }
            if ($b64) {
                $clean = if ($b64 -is [System.Array]) { $b64 -join "" } else { $b64 }
                $clean = $clean -replace "\s",""
                $decoded = [System.Text.Encoding]::UTF8.GetString(
                    [System.Convert]::FromBase64String($clean))
                Set-Content -Path $localFull -Value $decoded -NoNewline -Encoding UTF8
                Write-Host "${Indent}Updated $name" -ForegroundColor Green
        } else {
            Write-Host "${Indent}WARNING: no content for $name" -ForegroundColor Red
        }
    }
}

# ── Upstream sources ─────────────────────────────────────────────────────
# Each entry maps a local skill directory to one or more (repo, remotePath) pairs.
# Multiple paths let us pull from different locations in the same repo
# (e.g. ui-ux-pro-max SKILL.md vs its data/scripts).

$upstream = [ordered]@{
    "find-skills" = @(
        @{ repo = "vercel-labs/skills"; path = "skills/find-skills" }
    )
    "gh-cli" = @(
        @{ repo = "github/awesome-copilot"; path = "skills/gh-cli" }
    )
    # ── ui-ux-pro-max skill set ──────────────────────────────────────────
    # Main skill: SKILL.md from .claude/skills, data+scripts from src/
    "ui-ux-pro-max" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/ui-ux-pro-max"; only = @("SKILL.md") }
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = "src/ui-ux-pro-max";            only = @("data", "scripts") }
    )
    # Companion skills (all from .claude/skills/)
    "banner-design" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/banner-design" }
    )
    "brand" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/brand" }
    )
    "design-system" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/design-system" }
    )
    "design" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/design" }
    )
    "slides" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/slides" }
    )
    "ui-styling" = @(
        @{ repo = "nextlevelbuilder/ui-ux-pro-max-skill"; path = ".claude/skills/ui-styling" }
    )
}

# Skills with local customizations — skip during auto-update
$patched = @("find-skills")

# ── Main loop ────────────────────────────────────────────────────────────

foreach ($skill in $upstream.Keys) {
    if ($patched -contains $skill) {
        Write-Host "Skipping $skill (has local customizations — update manually)" -ForegroundColor Yellow
        continue
    }

    $sources = $upstream[$skill]
    $localDir = Join-Path $repoRoot $skill
    Write-Host "Updating $skill..." -ForegroundColor Cyan

    foreach ($src in $sources) {
        $repo = $src.repo
        $remotePath = $src.path
        $filter = $src.only  # $null means "everything"

        # Get listing
        $raw = gh api "repos/$repo/contents/$remotePath" 2>$null
        if (-not $raw) {
            Write-Host "  WARNING: could not list $remotePath from $repo" -ForegroundColor Red
            continue
        }
        $entries = $raw | ConvertFrom-Json
        if ($entries -isnot [System.Array]) { $entries = @($entries) }

        foreach ($entry in $entries) {
            $name = $entry.name
            $type = $entry.type

            # Apply filter if set
            if ($filter -and ($filter -notcontains $name)) {
                continue
            }

            # Skip symlinks (they appear as type "file" with size 0 and a target — but
            # GitHub API doesn't clearly distinguish them; we handle this by pulling from
            # the real source via the "only" filter above)
            if ($type -eq "symlink") {
                Write-Host "  Skipping symlink: $name" -ForegroundColor DarkGray
                continue
            }

            $remoteFull = "$remotePath/$name"
            $localFull  = Join-Path $localDir $name

            if ($type -eq "dir") {
                Sync-RemoteDir -Repo $repo -RemotePath $remoteFull -LocalDir $localFull
                continue
            }

            # Skip binary files
            $ext = [System.IO.Path]::GetExtension($name).ToLower()
            if ($binaryExts -contains $ext) {
                Write-Host "  Skipping binary: $name" -ForegroundColor DarkGray
                continue
            }

            # Fetch file content
            $b64 = $entry.content
            if (-not $b64) {
                $b64 = gh api "repos/$repo/contents/$remoteFull" --jq '.content' 2>$null
            }
            if ($b64) {
                if (-not (Test-Path (Split-Path $localFull))) {
                    New-Item -ItemType Directory -Path (Split-Path $localFull) -Force | Out-Null
                }
                $clean = if ($b64 -is [System.Array]) { $b64 -join "" } else { $b64 }
                $clean = $clean -replace "\s",""
                $decoded = [System.Text.Encoding]::UTF8.GetString(
                    [System.Convert]::FromBase64String($clean))
                Set-Content -Path $localFull -Value $decoded -NoNewline -Encoding UTF8
                Write-Host "  Updated $name" -ForegroundColor Green
            } else {
                Write-Host "  WARNING: no content for $name" -ForegroundColor Red
            }
        }
    }
}

Write-Host "`nDone. Run 'git diff' to see changes, then commit to pin the new versions." -ForegroundColor Yellow
