#!/usr/bin/env python3
"""Claude Code PreToolUse hook that blocks shell syntax sent to the wrong shell.

Registered in ~/.claude/settings.json with matcher "Bash|PowerShell":
    python C:/Users/13982/sz-skills/hooks/shell-syntax-guard.py

Blocks (exit 2, reason on stderr, which Claude Code shows to the model):
- bash heredocs (`python - <<'PY'`) in the PowerShell tool
- PowerShell cmdlets (`Get-ChildItem ...`) at the start of a Bash command
Any other input, including malformed input, is allowed (exit 0).
"""

from __future__ import annotations

import json
import logging
import re
import shlex
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

HEREDOC = re.compile(r"<<-?\s*['\"]?[A-Za-z_]\w*['\"]?")
CMDLET = re.compile(
    r"((?:Get|Set|Select|Where|ForEach|Write|Remove|New|Test|Out|Start|Stop|Invoke|Copy|Move"
    r"|Format|Measure|Sort|Group|Import|Export|ConvertTo|ConvertFrom|Add|Clear|Join|Split|Resolve"
    r"|Rename)-[A-Z][A-Za-z]+)\b"
)


def bash_cmdlet(command: str) -> str | None:
    """Find a cmdlet in command position, leaving quoted arguments and heredoc bodies alone."""
    head = command.split("<<", 1)[0]
    lexer = shlex.shlex(head, posix=True, punctuation_chars=";&|()\n")
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    command_start = True
    try:
        for token in lexer:
            if token and all(char in ";&|()\n" for char in token):
                command_start = True
            elif command_start:
                if CMDLET.fullmatch(token):
                    return token
                command_start = False
    except ValueError:
        # An unfinished quote is a shell parse error, not evidence of the wrong shell.
        return None
    return None


def check(tool_name: str, command: str) -> str | None:
    """Return a block reason, or None to allow the command."""
    if tool_name == "PowerShell" and HEREDOC.search(command):
        return (
            "Blocked: this is the PowerShell tool, which has no heredocs (`<<'EOF'`). "
            "Write the script to a temp file with the Write tool and run it, or use the Bash tool."
        )
    if tool_name == "Bash":
        cmdlet = bash_cmdlet(command)
        if cmdlet:
            return (
                f"Blocked: `{cmdlet}` is a PowerShell cmdlet, but this is the Bash tool "
                "(Git Bash). Use the PowerShell tool, call `powershell.exe -NoProfile -Command '...'`, "
                "or use the bash equivalent."
            )
    return None


def main() -> int:
    """Read one PreToolUse event and return Claude's blocking exit code when needed."""
    try:
        payload = json.loads(sys.stdin.read() or "{}")
        tool_name = payload.get("tool_name") or ""
        command = (payload.get("tool_input") or {}).get("command") or ""
    except (ValueError, AttributeError):
        return 0
    if not isinstance(command, str):
        return 0
    reason = check(tool_name, command)
    if reason:
        logging.warning("%s: %s", tool_name, reason)
        print(reason, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    log_dir = Path.home() / ".sz-skills" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        handlers=[RotatingFileHandler(log_dir / "shell-syntax-guard.log", maxBytes=1_000_000,
                                      backupCount=2, encoding="utf-8")],
        level=logging.WARNING, format="%(asctime)s %(levelname)s %(message)s",
    )
    try:
        sys.exit(main())
    except Exception:
        logging.exception("Shell syntax guard crashed")
        raise
