#!/usr/bin/env python3
"""PostToolUse hook that records Chrome DevTools MCP usage for the active turn."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any


DEVTOOLS_TOOL_PREFIXES = (
    "mcp__chrome_devtools__",
    "mcp__chrome-devtools__",
)
STATE_ENV = "SZ_SKILLS_CODEX_HOOK_STATE_DIR"


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False))


def read_input() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    return json.loads(raw)


def is_chrome_devtools_tool(tool_name: Any) -> bool:
    if not isinstance(tool_name, str):
        return False
    normalized = tool_name.lower()
    return normalized.startswith(DEVTOOLS_TOOL_PREFIXES)


def state_dir() -> Path:
    explicit = os.environ.get(STATE_ENV)
    if explicit:
        return Path(explicit)

    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "hook-state" / "sz-skills"

    return Path.home() / ".codex" / "hook-state" / "sz-skills"


def marker_path(turn_id: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", turn_id).strip("._-") or "turn"
    digest = hashlib.sha256(turn_id.encode("utf-8")).hexdigest()[:16]
    return state_dir() / "chrome-devtools-turns" / f"{safe[:80]}-{digest}.json"


def cleanup_old_markers(root: Path, max_age_seconds: int = 7 * 24 * 60 * 60) -> None:
    cutoff = time.time() - max_age_seconds
    marker_root = root / "chrome-devtools-turns"
    if not marker_root.is_dir():
        return
    for marker in marker_root.glob("*.json"):
        try:
            if marker.stat().st_mtime < cutoff:
                marker.unlink()
        except OSError:
            pass


def main() -> int:
    try:
        payload = read_input()
        tool_name = payload.get("tool_name") or payload.get("toolName")
        turn_id = payload.get("turn_id") or payload.get("turnId")

        if not is_chrome_devtools_tool(tool_name) or not isinstance(turn_id, str) or not turn_id:
            emit({})
            return 0

        root = state_dir()
        cleanup_old_markers(root)
        path = marker_path(turn_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "turn_id": turn_id,
                    "tool_name": tool_name,
                    "recorded_at": int(time.time()),
                },
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )
    except Exception:
        # Hook state is advisory. Never break the completed tool call if marking fails.
        pass

    emit({})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
