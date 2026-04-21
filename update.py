#!/usr/bin/env python3
"""Update vendor skills to latest upstream versions.

Requires: gh CLI (authenticated), Python 3.8+

Usage:
    cd ~/.sz-skills
    python update.py
"""

import base64
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

# Binary extensions to skip (font files, images, etc.)
BINARY_EXTS = frozenset([
    ".ttf", ".woff", ".woff2", ".otf", ".eot",
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
])

# ── Upstream sources ─────────────────────────────────────────────────────
# Each entry maps a local skill directory to a list of (repo, path, only?) dicts.
# Multiple paths pull from different locations in the same repo
# (e.g. ui-ux-pro-max SKILL.md from .claude/skills vs data/scripts from src/).

UPSTREAM = {
    "find-skills": [
        {"repo": "vercel-labs/skills", "path": "skills/find-skills"},
    ],
    "gh-cli": [
        {"repo": "github/awesome-copilot", "path": "skills/gh-cli"},
    ],
    # ── ui-ux-pro-max skill set ──────────────────────────────────────────
    "ui-ux-pro-max": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/ui-ux-pro-max", "only": ["SKILL.md"]},
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": "src/ui-ux-pro-max", "only": ["data", "scripts"]},
    ],
    # Companion skills
    "banner-design": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/banner-design"},
    ],
    "brand": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/brand"},
    ],
    "design-system": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/design-system"},
    ],
    "design": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/design"},
    ],
    "slides": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/slides"},
    ],
    "ui-styling": [
        {"repo": "nextlevelbuilder/ui-ux-pro-max-skill", "path": ".claude/skills/ui-styling"},
    ],
    # ── superpowers skill bundle ─────────────────────────────────────────
    "superpowers": [
        {"repo": "obra/superpowers", "path": "skills"},
    ],
}

# Skills with local customizations — skip during auto-update
PATCHED = {"find-skills", "superpowers"}

# ── Colours (ANSI) ───────────────────────────────────────────────────────

def _cyan(s):    return f"\033[36m{s}\033[0m"
def _green(s):   return f"\033[32m{s}\033[0m"
def _yellow(s):  return f"\033[33m{s}\033[0m"
def _red(s):     return f"\033[31m{s}\033[0m"
def _dim(s):     return f"\033[90m{s}\033[0m"

# ── Helpers ──────────────────────────────────────────────────────────────

def gh_api(endpoint: str) -> list | dict | None:
    """Call gh api and return parsed JSON, or None on failure."""
    result = subprocess.run(
        ["gh", "api", f"repos/{endpoint}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def decode_content(entry: dict, repo: str, remote_path: str) -> bytes | None:
    """Extract and decode base64 content from a GitHub Contents API entry."""
    b64 = entry.get("content")
    if not b64:
        # Content not included in directory listing — fetch individually
        data = gh_api(f"{repo}/contents/{remote_path}")
        if data:
            b64 = data.get("content")
    if not b64:
        return None
    cleaned = re.sub(r"\s", "", b64)
    return base64.b64decode(cleaned)


def ensure_dir(path: Path):
    """Create directory, removing a stale file at the same path if needed."""
    if path.exists() and not path.is_dir():
        path.unlink()
    path.mkdir(parents=True, exist_ok=True)


def sync_remote_dir(repo: str, remote_path: str, local_dir: Path, indent: str = "  "):
    """Recursively download a remote directory."""
    ensure_dir(local_dir)

    data = gh_api(f"{repo}/contents/{remote_path}")
    if data is None:
        print(f"{indent}{_red('WARNING: could not list ' + remote_path)}")
        return

    entries = data if isinstance(data, list) else [data]

    for entry in entries:
        name = entry["name"]
        entry_type = entry["type"]
        remote_full = f"{remote_path}/{name}"
        local_full = local_dir / name

        if entry_type == "dir":
            sync_remote_dir(repo, remote_full, local_full, indent + "  ")
            continue

        ext = Path(name).suffix.lower()
        if ext in BINARY_EXTS:
            print(f"{indent}{_dim('Skipping binary: ' + name)}")
            continue

        content = decode_content(entry, repo, remote_full)
        if content is not None:
            local_full.write_bytes(content)
            print(f"{indent}{_green('Updated ' + name)}")
        else:
            print(f"{indent}{_red('WARNING: no content for ' + name)}")


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    for skill, sources in UPSTREAM.items():
        if skill in PATCHED:
            print(_yellow(f"Skipping {skill} (has local customizations — update manually)"))
            continue

        local_dir = REPO_ROOT / skill
        print(_cyan(f"Updating {skill}..."))

        for src in sources:
            repo = src["repo"]
            remote_path = src["path"]
            only_filter = src.get("only")  # None means "everything"

            data = gh_api(f"{repo}/contents/{remote_path}")
            if data is None:
                print(f"  {_red('WARNING: could not list ' + remote_path + ' from ' + repo)}")
                continue

            entries = data if isinstance(data, list) else [data]

            for entry in entries:
                name = entry["name"]
                entry_type = entry["type"]

                # Apply filter if set
                if only_filter and name not in only_filter:
                    continue

                # Skip symlinks
                if entry_type == "symlink":
                    print(f"  {_dim('Skipping symlink: ' + name)}")
                    continue

                remote_full = f"{remote_path}/{name}"
                local_full = local_dir / name

                if entry_type == "dir":
                    sync_remote_dir(repo, remote_full, local_full)
                    continue

                ext = Path(name).suffix.lower()
                if ext in BINARY_EXTS:
                    print(f"  {_dim('Skipping binary: ' + name)}")
                    continue

                content = decode_content(entry, repo, remote_full)
                if content is not None:
                    ensure_dir(local_full.parent)
                    local_full.write_bytes(content)
                    print(f"  {_green('Updated ' + name)}")
                else:
                    print(f"  {_red('WARNING: no content for ' + name)}")

    print(f"\n{_yellow('Done. Run `git diff` to see changes, then commit to pin the new versions.')}")


if __name__ == "__main__":
    main()
