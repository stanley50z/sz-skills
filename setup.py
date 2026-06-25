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
import json
import shutil
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SKILLS_DIR = REPO_ROOT / "skills"
GLOBAL_DIR = REPO_ROOT / "global"
HOME = Path.home()

# Directories where coding harnesses look for skills
TARGET_ROOTS = [
    HOME / ".claude" / "skills",    # Claude Code
    HOME / ".codex" / "skills",      # OpenAI Codex
    HOME / ".config" / "opencode" / "skills",  # Opencode
    HOME / ".agents" / "skills",     # Pi coding agent
]

# Global instruction files for harnesses that support user-level memory.
GLOBAL_INSTRUCTION_LINKS = [
    (GLOBAL_DIR / "AGENTS.md", HOME / ".codex" / "AGENTS.md"),
    (GLOBAL_DIR / "CLAUDE.md", HOME / ".claude" / "CLAUDE.md"),
]

# Local plugin registration used only for hook-based bootstrap. Skills are
# still installed through TARGET_ROOTS to avoid duplicated plugin skill names.
PLUGIN_NAME = "sz-skills"
PLUGIN_ID = f"{PLUGIN_NAME}@{PLUGIN_NAME}"
PLUGIN_VERSION = "1.0.0"
CODEX_HOOK_PLUGIN_DIR = ".codex-hook-plugin"
CODEX_CONFIG_PATH = HOME / ".codex" / "config.toml"
CLAUDE_SETTINGS_PATH = HOME / ".claude" / "settings.json"
CLAUDE_INSTALLED_PLUGINS_PATH = HOME / ".claude" / "plugins" / "installed_plugins.json"
CLAUDE_KNOWN_MARKETPLACES_PATH = HOME / ".claude" / "plugins" / "known_marketplaces.json"

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
        if target.is_symlink():
            target.unlink()
        elif _is_link_or_junction(target):
            # Remove Windows junction without following into target contents
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


def make_file_link(source: Path, target: Path):
    """Create a file symlink at target -> source, falling back to a hard link on Windows."""
    if not source.is_file():
        raise FileNotFoundError(source)

    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink() or _is_link_or_junction(target):
        if target.is_symlink():
            target.unlink()
        elif _is_link_or_junction(target):
            os.rmdir(target)
        elif target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()

    if platform.system() == "Windows":
        try:
            target.symlink_to(source)
        except OSError:
            os.link(source, target)
    else:
        target.symlink_to(source)


def _toml_literal(value: str) -> str:
    """Return a TOML literal string for paths we control."""
    if "'" in value:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return f"'{value}'"


def _replace_or_append_toml_table(text: str, header: str, body_lines: list[str]) -> str:
    block_lines = [header, *body_lines]
    lines = text.splitlines()

    start = None
    for index, line in enumerate(lines):
        if line.strip() == header:
            start = index
            break

    if start is None:
        if lines and lines[-1].strip():
            lines.append("")
        lines.extend(block_lines)
        return "\n".join(lines) + "\n"

    end = start + 1
    while end < len(lines):
        if lines[end].startswith("["):
            break
        if not lines[end].strip():
            lookahead = end + 1
            while lookahead < len(lines) and not lines[lookahead].strip():
                lookahead += 1
            if lookahead == len(lines) or lines[lookahead].startswith("["):
                break
        end += 1

    lines[start:end] = block_lines
    return "\n".join(lines) + "\n"


def install_codex_plugin_config(
    *,
    config_path: Path = CODEX_CONFIG_PATH,
    repo_root: Path = REPO_ROOT,
) -> bool:
    """Register the hook-only Codex plugin package and enable it."""
    repo_root = repo_root.resolve()
    codex_plugin_root = (repo_root / CODEX_HOOK_PLUGIN_DIR).resolve()
    text = config_path.read_text(encoding="utf-8") if config_path.exists() else ""

    text = _replace_or_append_toml_table(
        text,
        f"[marketplaces.{PLUGIN_NAME}]",
        [
            'source_type = "local"',
            f"source = {_toml_literal(str(codex_plugin_root))}",
        ],
    )
    updated = _replace_or_append_toml_table(
        text,
        f'[plugins."{PLUGIN_ID}"]',
        ["enabled = true"],
    )

    if config_path.exists() and config_path.read_text(encoding="utf-8") == updated:
        return False

    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(updated, encoding="utf-8")
    return True


def _load_json_file(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json_if_changed(path: Path, data) -> bool:
    rendered = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == rendered:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    return True


def _current_git_commit(repo_root: Path = REPO_ROOT) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            capture_output=True,
            check=True,
            text=True,
        )
    except Exception:
        return None
    commit = result.stdout.strip()
    return commit or None


def install_claude_plugin_config(
    *,
    settings_path: Path = CLAUDE_SETTINGS_PATH,
    installed_plugins_path: Path = CLAUDE_INSTALLED_PLUGINS_PATH,
    known_marketplaces_path: Path = CLAUDE_KNOWN_MARKETPLACES_PATH,
    repo_root: Path = REPO_ROOT,
    now_iso: str | None = None,
    git_commit_sha: str | None = None,
) -> bool:
    """Register this repo as an enabled Claude Code local plugin."""
    repo_root = repo_root.resolve()
    now_iso = now_iso or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    git_commit_sha = git_commit_sha if git_commit_sha is not None else _current_git_commit(repo_root)

    changed = False

    settings = _load_json_file(settings_path, {})
    enabled_plugins = settings.setdefault("enabledPlugins", {})
    if enabled_plugins.get(PLUGIN_ID) is not True:
        enabled_plugins[PLUGIN_ID] = True
        changed = True
    changed = _write_json_if_changed(settings_path, settings) or changed

    installed = _load_json_file(installed_plugins_path, {"version": 2, "plugins": {}})
    installed.setdefault("version", 2)
    installed_plugins = installed.setdefault("plugins", {})
    existing_records = installed_plugins.get(PLUGIN_ID, [])
    existing_record = existing_records[0] if existing_records else {}
    install_record = {
        "scope": "user",
        "installPath": str(repo_root),
        "version": PLUGIN_VERSION,
        "installedAt": existing_record.get("installedAt", now_iso),
        "lastUpdated": existing_record.get("lastUpdated", now_iso),
    }
    if git_commit_sha:
        install_record["gitCommitSha"] = git_commit_sha
    if existing_record.get("installPath") != str(repo_root) or existing_record.get("version") != PLUGIN_VERSION:
        install_record["lastUpdated"] = now_iso
    if existing_records != [install_record]:
        installed_plugins[PLUGIN_ID] = [install_record]
        changed = True
    changed = _write_json_if_changed(installed_plugins_path, installed) or changed

    known = _load_json_file(known_marketplaces_path, {})
    existing_marketplace = known.get(PLUGIN_NAME, {})
    marketplace = {
        "source": {
            "source": "local",
            "path": str(repo_root),
        },
        "installLocation": str(repo_root),
        "lastUpdated": existing_marketplace.get("lastUpdated", now_iso),
    }
    if existing_marketplace.get("source", {}).get("path") != str(repo_root):
        marketplace["lastUpdated"] = now_iso
    if existing_marketplace != marketplace:
        known[PLUGIN_NAME] = marketplace
        changed = True
    changed = _write_json_if_changed(known_marketplaces_path, known) or changed

    return changed


def install_plugin_hooks() -> int:
    """Enable the local hook plugin for Codex and Claude Code."""
    installed = 0
    try:
        if install_codex_plugin_config():
            installed += 1
        print(f"  {_green(f'Codex plugin enabled: {PLUGIN_ID}')}")
    except Exception as e:
        print(f"  {_red(f'FAILED: Codex plugin config — {e}')}")

    try:
        if install_claude_plugin_config():
            installed += 1
        print(f"  {_green(f'Claude Code plugin enabled: {PLUGIN_ID}')}")
    except Exception as e:
        print(f"  {_red(f'FAILED: Claude Code plugin config — {e}')}")
    return installed


def install_skills(
    skills: list[str],
    *,
    skills_dir: Path = SKILLS_DIR,
    target_roots: list[Path] = TARGET_ROOTS,
) -> int:
    """Link selected skills into each coding harness root and return success count."""
    installed = 0
    for root in target_roots:
        root.mkdir(parents=True, exist_ok=True)
        for skill in skills:
            source = skills_dir / skill
            target = root / skill
            try:
                make_link(source, target)
                installed += 1
                print(f"  {_green(f'{target} -> {source}')}")
            except Exception as e:
                print(f"  {_red(f'FAILED: {target} — {e}')}")
    return installed


def install_global_instructions(
    links: list[tuple[Path, Path]] = GLOBAL_INSTRUCTION_LINKS,
) -> int:
    """Link repo-managed global instruction files into harness locations."""
    installed = 0
    for source, target in links:
        try:
            make_file_link(source, target)
            installed += 1
            print(f"  {_green(f'{target} -> {source}')}")
        except Exception as e:
            print(f"  {_red(f'FAILED: {target} — {e}')}")
    return installed


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    skills = discover_skills()

    if not skills:
        print(_red("No skills found."))
        sys.exit(1)

    print(_cyan(f"Creating links for: {', '.join(skills)}"))

    install_skills(skills)

    print(f"\n{_cyan('Creating global instruction links')}")
    install_global_instructions()

    print(f"\n{_cyan('Enabling plugin hooks')}")
    install_plugin_hooks()

    print(f"\n{_cyan('Done. Skills, global instructions, and plugin hooks are linked.')}")


if __name__ == "__main__":
    main()
