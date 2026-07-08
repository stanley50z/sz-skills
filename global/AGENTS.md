For plain local `file://` HTML pages, prefer Chrome DevTools MCP for visual inspection, screenshots, and simulated button/key presses.

For other browser verification and control tasks, prefer tools in this order:

1. Codex Chrome Plugin, when the harness is Codex and the plugin is available.
2. Chrome DevTools MCP connected to the existing user profile and session.
3. Chrome DevTools MCP in a new session/window.

After finishing Chrome DevTools MCP work, close the entire DevTools-controlled browser/window only when it was launched by Chrome DevTools MCP with an owned isolated profile or unique `user-data-dir`. If MCP attached to an existing browser via `browser-url`, `ws-endpoint`, `autoConnect`, or a normal user profile, do not close the browser automatically; close only task tabs when appropriate.

## Web Search

When unsure about a fact involving real-world products, use web search before answering.

## Localhost Ports

Before choosing or starting a localhost dev-server port, read `C:\Users\13982\LOCALHOST_PORTS.md`; if it does not exist, create it first. Avoid ports already assigned there unless you are intentionally working on that project or have verified that reusing the port is safe. When adding a new fixed localhost port for any project, update that registry in the same change.

## Scripting Defaults

When asked to write a script and no language is specified, use Python by default. Keep cross-platform compatibility in mind, especially for paths, shell invocation, filesystem behavior, and environment assumptions.

## Shell Commands on Windows

Commands execute via `powershell.exe -Command "<string>"` (Windows PowerShell 5.1) unless the harness says otherwise. The command is embedded in an extra quoting layer you cannot see.

- Never use POSIX-only syntax: no heredocs (`<<'EOF'`), no `&&`/`||` chaining, no `$(...)`, no `export VAR=x`.
- Never use PowerShell here-strings (`@'...'@`) inside a `-Command` string — the outer quoting layer breaks them.
- For multiline Python or scripts: write the code to a temp file with the file-write tool, run `python tempfile.py`, then delete it. Do NOT pipe multiline code via stdin.
- For one-liners: `python -c "..."` with double quotes outside and single quotes inside.
- If a command fails with a parse or quoting error, switch to the temp-file approach immediately. Do not retry the same idiom with different quoting.

## Encoding on Windows

When reading, writing, or verifying files/command output that may contain Chinese or other non-ASCII text in PowerShell, use UTF-8 explicitly.
