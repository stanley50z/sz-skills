#!/usr/bin/env python3
"""Codex PreToolUse hook that nudges broad searches toward Graphify first."""

import json
import os
import re
import sys
from pathlib import Path


SEARCH_COMMAND_RE = re.compile(
    r"(^|[\s;&|()])(?:rg|grep|ripgrep|find|fd|ack|ag)(?:\s|$)",
    re.IGNORECASE,
)


def _load_payload() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def _command_from_payload(payload: dict) -> str:
    tool_input = payload.get("tool_input") or payload.get("toolInput") or {}
    if isinstance(tool_input, dict):
        return str(tool_input.get("command") or "")
    return ""


def _find_graph_root(start: Path) -> Path | None:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / "graphify-out" / "graph.json").is_file():
            return candidate
    return None


def main() -> int:
    payload = _load_payload()
    tool_name = str(payload.get("tool_name") or payload.get("toolName") or "")
    if tool_name and tool_name != "Bash":
        return 0

    command = _command_from_payload(payload)
    if not SEARCH_COMMAND_RE.search(command):
        return 0

    cwd = Path(str(payload.get("cwd") or os.getcwd()))
    graph_root = _find_graph_root(cwd)
    if graph_root is None:
        return 0

    rel_graph = "graphify-out/graph.json"
    message = (
        f"MANDATORY: {rel_graph} exists. Before broad search or source "
        "inventory, run `graphify query \"<question>\"` to orient from the "
        "existing graph. Use `graphify explain \"<concept>\"` for a focused "
        "component and `graphify path \"<A>\" \"<B>\"` for relationships. "
        "Use raw search only after Graphify has oriented you, or when editing "
        "and verifying specific lines."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "additionalContext": message,
                }
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
