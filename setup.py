#!/usr/bin/env python3
"""sz-skills setup script — create links from agent skill directories into this repo.

Run this after cloning on a new device:
    git clone https://github.com/stanley50z/sz-skills ~/.sz-skills
    cd ~/.sz-skills
    python setup.py

On Windows: creates NTFS junctions (no admin / developer-mode required).
On macOS / Linux: creates symlinks.
"""

import os
import platform
import shutil
import stat
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
HOME = Path.home()

# Directories where AI tools look for skills
TARGET_ROOTS = [
    HOME / ".agents" / "skills",
    HOME / ".claude" / "skills",
]

# ── Colours (ANSI) ───────────────────────────────────────────────────────

def _cyan(s):   return f"\033[36m{s}\033[0m"
def _green(s):  return f"\033[32m{s}\033[0m"
def _yellow(s): return f"\033[33m{s}\033[0m"
def _red(s):    return f"\033[31m{s}\033[0m"

# ── Helpers ──────────────────────────────────────────────────────────────

def discover_skills() -> list[str]:
    """Return names of top-level directories that contain a SKILL.md."""
    return sorted(
        d.name
        for d in REPO_ROOT.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    )


# Skill bundles: directories that don't have their own SKILL.md but contain
# subdirectories that do. These are linked as a single junction/symlink.
BUNDLES = ["superpowers"]


def discover_bundles() -> list[str]:
    """Return names of known bundle directories that exist in the repo."""
    return sorted(
        name for name in BUNDLES
        if (REPO_ROOT / name).is_dir()
    )


def _is_link_or_junction(path: Path) -> bool:
    """Check if path is a symlink or NTFS junction."""
    if path.is_symlink():
        return True
    if platform.system() == "Windows":
        try:
            return bool(os.lstat(path).st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)
        except (OSError, AttributeError):
            pass
    return False


def make_link(source: Path, target: Path):
    """Create a directory junction (Windows) or symlink (Unix) at target -> source."""
    if target.exists() or target.is_symlink():
        if _is_link_or_junction(target):
            # Remove junction/symlink without following into target contents
            os.rmdir(target)
        elif target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()

    if platform.system() == "Windows":
        # NTFS junction — no admin required
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(target), str(source)],
            capture_output=True, check=True,
        )
    else:
        target.symlink_to(source)


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    skills = discover_skills()
    bundles = discover_bundles()
    all_entries = skills + bundles

    if not all_entries:
        print(_red("No skills or bundles found."))
        sys.exit(1)

    print(_cyan(f"Creating links for: {', '.join(all_entries)}"))

    for root in TARGET_ROOTS:
        root.mkdir(parents=True, exist_ok=True)
        for entry in all_entries:
            source = REPO_ROOT / entry
            target = root / entry
            try:
                make_link(source, target)
                print(f"  {_green(f'{target} -> {source}')}")
            except Exception as e:
                print(f"  {_red(f'FAILED: {target} — {e}')}")

    print(f"\n{_cyan('Done. All skills are linked.')}")


if __name__ == "__main__":
    main()
