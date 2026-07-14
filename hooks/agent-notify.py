#!/usr/bin/env python3
"""Show a desktop notification. Used as a Claude Code / Codex / T3 Code hook.

Usage: agent-notify.py [TITLE] [BODY]
Reads optional hook JSON from stdin (uses `cwd` / `message` fields if present).
Cross-platform: Windows (WinRT toast via PowerShell), macOS (osascript),
Linux (notify-send).

The notification process is spawned detached and this script exits
immediately, so the hook never blocks turn end even when run synchronously
(T3 Code has no async hooks yet).
"""

import json
import os
import platform
import subprocess
import sys
from xml.sax.saxutils import escape


def read_stdin_json():
    try:
        if sys.stdin is None or sys.stdin.isatty():
            return {}
        data = sys.stdin.read()
        return json.loads(data) if data.strip() else {}
    except Exception:
        return {}


def spawn_detached(cmd, env=None):
    kwargs = {
        "stdin": subprocess.DEVNULL,
        "stdout": subprocess.DEVNULL,
        "stderr": subprocess.DEVNULL,
        "env": env,
    }
    if platform.system() == "Windows":
        kwargs["creationflags"] = (
            subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        )
    else:
        kwargs["start_new_session"] = True
    subprocess.Popen(cmd, **kwargs)


def notify_windows(title, body):
    ps = (
        "$null = [Windows.UI.Notifications.ToastNotificationManager, "
        "Windows.UI.Notifications, ContentType = WindowsRuntime];"
        "$null = [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, "
        "ContentType = WindowsRuntime];"
        "$xml = New-Object Windows.Data.Xml.Dom.XmlDocument;"
        "$xml.LoadXml($env:AGENT_TOAST_XML);"
        "$toast = New-Object Windows.UI.Notifications.ToastNotification $xml;"
        "$appId = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe';"
        "[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($appId).Show($toast)"
    )
    toast_xml = (
        '<toast><visual><binding template="ToastGeneric">'
        f"<text>{escape(title)}</text><text>{escape(body)}</text>"
        "</binding></visual></toast>"
    )
    env = dict(os.environ, AGENT_TOAST_XML=toast_xml)
    spawn_detached(
        ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps],
        env=env,
    )


def notify_macos(title, body):
    script = f"display notification {json.dumps(body)} with title {json.dumps(title)}"
    spawn_detached(["osascript", "-e", script])


def notify_linux(title, body):
    spawn_detached(["notify-send", title, body])


def main():
    args = sys.argv[1:]
    title = args[0] if args else "Agent"
    body = args[1] if len(args) > 1 else ""
    payload = read_stdin_json()
    if not body:
        body = payload.get("message") or "Finished a turn"
    cwd = payload.get("cwd")
    if cwd:
        body = f"{body} — {cwd}"

    system = platform.system()
    if system == "Windows":
        notify_windows(title, body)
    elif system == "Darwin":
        notify_macos(title, body)
    else:
        notify_linux(title, body)


if __name__ == "__main__":
    main()
