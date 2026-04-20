# sz-skills setup script
# Run this after cloning on a new device to create junctions.
#
# Usage:
#   git clone https://github.com/stanley50z/sz-skills ~/.sz-skills
#   cd ~/.sz-skills
#   .\setup.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $MyInvocation.MyCommand.Path

# All skills in this repo (each top-level directory with a SKILL.md)
$skills = Get-ChildItem $repoRoot -Directory |
    Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } |
    Select-Object -ExpandProperty Name

# Where to create junctions
$targetRoots = @(
    "$HOME\.agents\skills",
    "$HOME\.claude\skills"
)

Write-Host "Creating junctions for: $($skills -join ', ')" -ForegroundColor Cyan

foreach ($root in $targetRoots) {
    if (-not (Test-Path $root)) {
        New-Item -ItemType Directory -Path $root -Force | Out-Null
    }
    foreach ($skill in $skills) {
        $target = Join-Path $root $skill
        $source = Join-Path $repoRoot $skill
        if (Test-Path $target) {
            Remove-Item $target -Recurse -Force
        }
        cmd /c mklink /J "$target" "$source" | Out-Null
        Write-Host "  $target -> $source" -ForegroundColor Green
    }
}

Write-Host "`nDone. All skills are linked." -ForegroundColor Cyan
