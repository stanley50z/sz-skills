#!/usr/bin/env python3
"""sz-skills setup script — create links from coding harness skill directories into this repo.

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
SKILLS_DIR = REPO_ROOT / "skills"
HOME = Path.home()

# Directories where coding harnesses look for skills
TARGET_ROOTS = [
    HOME / ".claude" / "skills",
    HOME / ".codex" / "skills",
    HOME / ".config" / "opencode" / "skills",
]

# ── Colours (ANSI) ───────────────────────────────────────────────────────

def _cyan(s):   return f"\033[36m{s}\033[0m"
def _green(s):  return f"\033[32m{s}\033[0m"
def _yellow(s): return f"\033[33m{s}\033[0m"
def _red(s):    return f"\033[31m{s}\033[0m"

# ── Helpers ──────────────────────────────────────────────────────────────

def discover_skills() -> list[str]:
    """Return names of directories under skills/ that contain a SKILL.md."""
    if not SKILLS_DIR.is_dir():
        return []
    return sorted(
        d.name
        for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
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
    if target.exists() or target.is_symlink() or _is_link_or_junction(target):
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

    if not skills:
        print(_red("No skills found."))
        sys.exit(1)

    print(_cyan(f"Creating links for: {', '.join(skills)}"))

    for root in TARGET_ROOTS:
        root.mkdir(parents=True, exist_ok=True)
        for skill in skills:
            source = SKILLS_DIR / skill
            target = root / skill
            try:
                make_link(source, target)
                print(f"  {_green(f'{target} -> {source}')}")
            except Exception as e:
                print(f"  {_red(f'FAILED: {target} — {e}')}")

    print(f"\n{_cyan('Done. All skills are linked.')}")


if __name__ == "__main__":
    main()
