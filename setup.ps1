# sz-skills setup script
# Run this after cloning on a new device to set up submodules and junctions.
#
# Usage:
#   git clone https://github.com/stanley50z/sz-skills ~/.sz-skills
#   cd ~/.sz-skills
#   .\setup.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $MyInvocation.MyCommand.Path

# 1. Initialize and update submodules
Write-Host "Initializing submodules..." -ForegroundColor Cyan
git -C $repoRoot submodule init
git -C $repoRoot submodule update --depth 1

# 2. Configure sparse-checkout for each submodule
Write-Host "Configuring sparse-checkout..." -ForegroundColor Cyan

$awesomeCopilot = Join-Path $repoRoot "vendor/awesome-copilot"
git -C $awesomeCopilot sparse-checkout init --cone
git -C $awesomeCopilot sparse-checkout set skills/gh-cli

$uiUxProMax = Join-Path $repoRoot "vendor/ui-ux-pro-max-skill"
git -C $uiUxProMax sparse-checkout init --cone
git -C $uiUxProMax sparse-checkout set .claude/skills/ui-ux-pro-max

# 3. Create junctions for all skills
Write-Host "Creating junctions..." -ForegroundColor Cyan

$junctions = @{
    # [target_dir] = [source_in_repo]
    # Own skills
    "$HOME\.agents\skills\commit"       = "$repoRoot\commit"
    "$HOME\.agents\skills\find-skills"  = "$repoRoot\find-skills"
    "$HOME\.claude\skills\commit"       = "$repoRoot\commit"
    "$HOME\.claude\skills\find-skills"  = "$repoRoot\find-skills"
    "$HOME\.config\opencode\skills\find-skills" = "$repoRoot\find-skills"
    # Vendor skills
    "$HOME\.agents\skills\gh-cli"       = "$repoRoot\vendor\awesome-copilot\skills\gh-cli"
    "$HOME\.agents\skills\ui-ux-pro-max"= "$repoRoot\vendor\ui-ux-pro-max-skill\.claude\skills\ui-ux-pro-max"
    "$HOME\.claude\skills\gh-cli"       = "$repoRoot\vendor\awesome-copilot\skills\gh-cli"
    "$HOME\.claude\skills\ui-ux-pro-max"= "$repoRoot\vendor\ui-ux-pro-max-skill\.claude\skills\ui-ux-pro-max"
}

foreach ($target in $junctions.Keys) {
    $source = $junctions[$target]
    $parentDir = Split-Path $target
    if (-not (Test-Path $parentDir)) {
        New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
    }
    if (Test-Path $target) {
        Remove-Item $target -Recurse -Force
    }
    cmd /c mklink /J "$target" "$source" | Out-Null
    Write-Host "  $target -> $source" -ForegroundColor Green
}

Write-Host "`nSetup complete!" -ForegroundColor Cyan
