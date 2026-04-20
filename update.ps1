# Update vendor skills to latest upstream versions.
# Requires: gh CLI (authenticated)
#
# Usage:
#   cd ~/.sz-skills
#   .\update.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $MyInvocation.MyCommand.Path

# Define upstream sources: local_dir -> (repo, path_in_repo)
$upstream = @{
    "gh-cli" = @{
        repo = "github/awesome-copilot"
        path = "skills/gh-cli"
    }
    "ui-ux-pro-max" = @{
        repo = "nextlevelbuilder/ui-ux-pro-max-skill"
        path = ".claude/skills/ui-ux-pro-max"
    }
}

foreach ($skill in $upstream.Keys) {
    $src = $upstream[$skill]
    $localDir = Join-Path $repoRoot $skill
    Write-Host "Updating $skill from $($src.repo)..." -ForegroundColor Cyan

    # Get file listing from GitHub API
    $files = gh api "repos/$($src.repo)/contents/$($src.path)" --jq '.[].name' 2>$null
    if (-not $files) {
        # Single file (not a directory listing) - try as single item
        $files = @(gh api "repos/$($src.repo)/contents/$($src.path)" --jq '.name' 2>$null)
    }

    # Fetch each file
    foreach ($file in $files) {
        $remotePath = "$($src.path)/$file"
        $localPath = Join-Path $localDir $file

        # Check if it's a directory
        $type = gh api "repos/$($src.repo)/contents/$remotePath" --jq '.type' 2>$null
        if ($type -eq "dir") {
            Write-Host "  Skipping directory: $file (nested dirs not supported by this script)" -ForegroundColor Yellow
            continue
        }

        $content = gh api "repos/$($src.repo)/contents/$remotePath" --jq '.content' 2>$null
        if ($content) {
            $decoded = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($content -replace "`n",""))
            Set-Content -Path $localPath -Value $decoded -NoNewline -Encoding UTF8
            Write-Host "  Updated $file" -ForegroundColor Green
        }
    }
}

Write-Host "`nDone. Run 'git diff' to see changes, then commit to pin the new versions." -ForegroundColor Yellow
