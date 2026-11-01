#!/usr/bin/env python3
"""Claude Code SessionStart hook that preloads the unslop skill into context.

Claude Code rarely calls the Skill tool for a writing-style skill on its own, so
setup.py registers this in ~/.claude/settings.json with matcher
"startup|clear|compact":
    python C:/Users/13982/sz-skills/hooks/unslop-context.py

Prints the skill body as SessionStart additionalContext. On any failure it logs
the stack trace to ~/.sz-skills/logs/unslop-context.log and prints nothing, so a
broken hook never blocks a session.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parent.parent / "skills" / "unslop" / "SKILL.md"
LOG_PATH = Path.home() / ".sz-skills" / "logs" / "unslop-context.log"
PREAMBLE = (
    "The unslop skill is preloaded below; do not call the Skill tool for it. "
    "Apply it to every reply and document you write for the user."
)


def skill_body(text: str) -> str:
    """Drop the YAML frontmatter so only the instructions remain."""
    if text.startswith("---"):
        _, _, rest = text[3:].partition("\n---")
        text = rest.partition("\n")[2]
    return text.strip()


def main() -> int:
    try:
        body = skill_body(SKILL_PATH.read_text(encoding="utf-8"))
        context = f"{PREAMBLE}\n\n{body}"
        output = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}
        sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(output, ensure_ascii=False))
    except Exception:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(filename=LOG_PATH, encoding="utf-8", format="%(asctime)s %(message)s")
        logging.exception("unslop-context hook failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
