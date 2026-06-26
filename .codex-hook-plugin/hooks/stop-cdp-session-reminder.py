#!/usr/bin/env python3
"""Stop hook that reminds Codex to close only owned Chrome DevTools sessions."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterable


DEVTOOLS_TOOL_PREFIXES = (
    "mcp__chrome_devtools__",
    "mcp__chrome-devtools__",
)

REMINDER = (
    "Before finishing, check whether this turn used a Chrome DevTools MCP "
    "browser/window that was launched with an owned isolated profile or unique "
    "user-data-dir. Close the entire DevTools-controlled browser/window only "
    "when it is owned. If it was attached through browser-url, ws-endpoint, "
    "autoConnect, or a normal user profile, do not close the browser "
    "automatically; close only task tabs when appropriate. Then give the final "
    "answer."
)


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False))


def read_input() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    return json.loads(raw)


def get_turn_id(entry: dict[str, Any]) -> str | None:
    payload = entry.get("payload")
    if not isinstance(payload, dict):
        return None
    metadata = payload.get("internal_chat_message_metadata_passthrough")
    if not isinstance(metadata, dict):
        return None
    turn_id = metadata.get("turn_id")
    return turn_id if isinstance(turn_id, str) else None


def iter_transcript_entries(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as transcript:
        for line in transcript:
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(entry, dict):
                yield entry


def iter_current_turn_tool_names(path: Path, turn_id: str) -> Iterable[str]:
    for entry in iter_transcript_entries(path):
        if get_turn_id(entry) != turn_id:
            continue
        payload = entry.get("payload")
        if not isinstance(payload, dict):
            continue
        if payload.get("type") != "function_call":
            continue
        name = payload.get("name")
        if isinstance(name, str):
            yield name


def used_chrome_devtools(transcript_path: str | None, turn_id: str | None) -> bool:
    if not transcript_path or not turn_id:
        return False
    path = Path(transcript_path)
    if not path.is_file():
        return False
    for tool_name in iter_current_turn_tool_names(path, turn_id):
        normalized = tool_name.lower()
        if normalized.startswith(DEVTOOLS_TOOL_PREFIXES):
            return True
    return False


def has_cleanup_decision(message: Any) -> bool:
    if not isinstance(message, str):
        return False
    text = message.lower()
    mentions_devtools = (
        "chrome devtools" in text
        or "devtools-controlled" in text
        or "cdp" in text
    )
    mentions_ownership = any(
        term in text
        for term in (
            "owned",
            "isolated profile",
            "user-data-dir",
            "attached",
            "browser-url",
            "ws-endpoint",
            "autoconnect",
            "normal user profile",
            "user-owned",
        )
    )
    mentions_disposition = any(
        term in text
        for term in (
            "close",
            "closed",
            "left open",
            "leave open",
            "kept open",
            "keep open",
        )
    )
    return mentions_devtools and mentions_ownership and mentions_disposition


def main() -> int:
    hook_input = read_input()
    if hook_input.get("stop_hook_active") or hook_input.get("stopHookActive"):
        emit({"continue": True})
        return 0

    transcript_path = hook_input.get("transcript_path") or hook_input.get("transcriptPath")
    turn_id = hook_input.get("turn_id") or hook_input.get("turnId")
    last_assistant_message = (
        hook_input.get("last_assistant_message")
        or hook_input.get("lastAssistantMessage")
        or ""
    )

    if used_chrome_devtools(transcript_path, turn_id) and not has_cleanup_decision(last_assistant_message):
        emit({"decision": "block", "reason": REMINDER})
        return 0

    emit({"continue": True})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
