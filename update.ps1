# Update all vendor skills to latest upstream versions
#
# Usage:
#   cd ~/.sz-skills
#   .\update.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $MyInvocation.MyCommand.Path

Write-Host "Updating vendor submodules..." -ForegroundColor Cyan
git -C $repoRoot submodule update --remote --depth 1

Write-Host "Done. Vendor skills are now at latest upstream." -ForegroundColor Green
Write-Host "Run 'git diff' to see what changed, then commit if you want to pin the new versions." -ForegroundColor Yellow
