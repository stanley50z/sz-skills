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
SKILLS_DIR = REPO_ROOT / "skills"

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
    "browser-harness": [
        {"repo": "browser-use/browser-harness", "path": "", "only": ["SKILL.md"]},
    ],
    "unslop": [
        {"repo": "cursor/plugins", "path": "pstack/skills/unslop"},
    ],
    "code-review": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/code-review"},
    ],
    "grill-with-docs": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/grill-with-docs"},
    ],
    "handoff": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/handoff"},
    ],
    "ask-matt": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/ask-matt"},
    ],
    "codebase-design": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/codebase-design"},
    ],
    # Replaces the superpowers `systematic-debugging` skill.
    "diagnosing-bugs": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/diagnosing-bugs"},
    ],
    "domain-modeling": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/domain-modeling"},
    ],
    "prototype": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/prototype"},
    ],
    "research": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/research"},
    ],
    "resolving-merge-conflicts": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/resolving-merge-conflicts"},
    ],
    # Customized: local tracker doc maps to docs/specs/ + docs/plans/ instead of .scratch/.
    "setup-matt-pocock-skills": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/setup-matt-pocock-skills"},
    ],
    # Replaces the superpowers `brainstorming` spec output (customized:
    # non-executable spec parents, structured HTML companion, handoff to to-tickets).
    "to-spec": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/to-spec"},
    ],
    "triage": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/triage"},
    ],
    "wayfinder": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/wayfinder"},
    ],
    # New in v1.2: interactive bash walkthroughs for human-only procedures.
    "wizard": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/wizard"},
    ],
    "grilling": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/grilling"},
    ],
    "grill-me": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/grill-me"},
    ],
    "teach": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/teach"},
    ],
    # New in v1.2: questionnaire for the one person who can answer a decision.
    "to-questionnaire": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/to-questionnaire"},
    ],
    # New in v1.2: one-word verbosity corrective.
    "wait-what": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/wait-what"},
    ],
    # Replaces the superpowers `writing-skills` skill (renamed upstream from
    # writing-great-skills in v1.2).
    "writing-for-agents": [
        {"repo": "mattpocock/skills", "path": "skills/productivity/writing-for-agents"},
    ],
    "improve-codebase-architecture": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/improve-codebase-architecture"},
    ],
    # Replaces the superpowers `writing-plans` skill (customized: staged graph
    # publication, requirement trace field, UI criteria, change propagation,
    # HTML plan companion).
    "to-tickets": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/to-tickets"},
    ],
    # Replaces the superpowers `executing-plans` / `subagent-driven-development`
    # execution loop (customized: no-fallback gates, visual-only UI checks,
    # cross-phase change propagation).
    "implement": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/implement"},
    ],
    # Customized fork of Matt Pocock's `tdd` skill (command timeouts,
    # user-requirement test priority, no fallbacks, stale v1/v2 test cleanup,
    # visual-only UI testing).
    "tdd": [
        {"repo": "mattpocock/skills", "path": "skills/engineering/tdd"},
    ],
    "remotion-best-practices": [
        {"repo": "remotion-dev/skills", "path": "skills/remotion-best-practices"},
    ],
    "revealjs": [
        {"repo": "ryanbbrown/revealjs-skill", "path": "skills/revealjs"},
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
}

# Skills with local customizations — skip during auto-update
PATCHED = {
    "handoff",
    "setup-matt-pocock-skills",
    "to-spec",
    "slides",
    "banner-design",
    "brand",
    "design",
    "design-system",
    "tdd",
    "to-tickets",
    "implement",
    "prototype",
    "wayfinder",
    "grilling",
    "ui-styling",
}

# ── Colours (ANSI) ───────────────────────────────────────────────────────

def _cyan(s):    return f"\033[36m{s}\033[0m"
def _green(s):   return f"\033[32m{s}\033[0m"
def _yellow(s):  return f"\033[33m{s}\033[0m"
def _red(s):     return f"\033[31m{s}\033[0m"
def _dim(s):     return f"\033[90m{s}\033[0m"

def _log(*args, **kwargs):
    """Print with immediate flush so progress is visible even via pipes."""
    print(*args, **kwargs, flush=True)

# ── Helpers ──────────────────────────────────────────────────────────────

def gh_api(endpoint: str) -> list | dict | None:
    """Call gh api and return parsed JSON, or None on failure."""
    _log(_dim(f"  ⏳ gh api repos/{endpoint}"))
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
        _log(f"{indent}{_red('WARNING: could not list ' + remote_path)}")
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
            _log(f"{indent}{_dim('Skipping binary: ' + name)}")
            continue

        content = decode_content(entry, repo, remote_full)
        if content is not None:
            local_full.write_bytes(content)
            _log(f"{indent}{_green('Updated ' + name)}")
        else:
            _log(f"{indent}{_red('WARNING: no content for ' + name)}")


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    skills_list = list(UPSTREAM.items())
    total = len(skills_list)
    for idx, (skill, sources) in enumerate(skills_list, 1):
        if skill in PATCHED:
            _log(_yellow(f"[{idx}/{total}] Skipping {skill} (has local customizations)"))
            continue

        local_dir = SKILLS_DIR / skill
        _log(_cyan(f"[{idx}/{total}] Updating {skill}..."))

        for src in sources:
            repo = src["repo"]
            remote_path = src["path"]
            only_filter = src.get("only")  # None means "everything"

            data = gh_api(f"{repo}/contents/{remote_path}")
            if data is None:
                _log(f"  {_red('WARNING: could not list ' + remote_path + ' from ' + repo)}")
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
                    _log(f"  {_dim('Skipping symlink: ' + name)}")
                    continue

                remote_full = f"{remote_path}/{name}"
                local_full = local_dir / name

                if entry_type == "dir":
                    sync_remote_dir(repo, remote_full, local_full)
                    continue

                ext = Path(name).suffix.lower()
                if ext in BINARY_EXTS:
                    _log(f"  {_dim('Skipping binary: ' + name)}")
                    continue

                content = decode_content(entry, repo, remote_full)
                if content is not None:
                    ensure_dir(local_full.parent)
                    local_full.write_bytes(content)
                    _log(f"  {_green('Updated ' + name)}")
                else:
                    _log(f"  {_red('WARNING: no content for ' + name)}")

    _log(f"\n{_yellow('Done. Run `git diff` to see changes, then commit to pin the new versions.')}")


if __name__ == "__main__":
    main()
