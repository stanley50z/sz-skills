#!/usr/bin/env python3
"""Claude Code SessionStart hook that tells the session to load the unslop skill.

Claude Code rarely calls the Skill tool for a writing-style skill on its own, so
setup.py registers this in ~/.claude/settings.json with matcher
"startup|clear|compact":
    python C:/Users/13982/sz-skills/hooks/unslop-context.py

Prints a one-line instruction as SessionStart additionalContext; the skill body
itself loads only through the Skill tool. On any failure it logs the stack trace
to ~/.sz-skills/logs/unslop-context.log and prints nothing, so a broken hook
never blocks a session.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

LOG_PATH = Path.home() / ".sz-skills" / "logs" / "unslop-context.log"
INSTRUCTION = (
    "Before your first reply, load the `unslop` skill with the Skill tool, "
    "then apply it to every reply and document you write for the user."
)


def main() -> int:
    try:
        output = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": INSTRUCTION}}
        sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(output, ensure_ascii=False))
    except Exception:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(filename=LOG_PATH, encoding="utf-8", format="%(asctime)s %(message)s")
        logging.exception("unslop-context hook failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
