For plain local `file://` HTML pages, prefer Chrome DevTools MCP for visual inspection, screenshots, and simulated button/key presses.

For other browser verification and control tasks, prefer tools in this order:

1. Codex Chrome Plugin, when the harness is Codex and the plugin is available.
2. Chrome DevTools MCP connected to the existing user profile and session.
3. Chrome DevTools MCP in a new session/window.

After DevTools MCP work, close the browser only if MCP launched it with its own isolated profile or `user-data-dir`. If it attached to an existing browser (`browser-url`, `ws-endpoint`, `autoConnect`, or a normal profile), close only task tabs.

## File Links

When operating inside T3 Code and referencing local files, use T3 Code-compatible Markdown links formatted as `[label](/C:/absolute/path/to/file.ext:line)` (line number optional); use forward slashes and never `file://` URLs or backticks.

## Question Dialogs and Hidden Text

Harnesses like T3 Code collapse assistant text that precedes a tool call into the Work Log, so the user never sees it. Never ask a question (via AskUserQuestion or any dialog tool) that refers to content living only in that hidden text — e.g. "does this summary match your understanding?" when the summary itself is invisible.

- Make every question dialog self-contained: put the summary, plan, or recommendation being confirmed into the question text and option descriptions.
- If the content is too long to fit in the dialog, don't use the dialog tool: end the turn with the content plus the question as plain visible text, and wait for the reply.

## Web Search

When unsure about a fact involving real-world products, use web search before answering.

## Localhost Ports

Before picking a localhost port, read `C:\Users\13982\LOCALHOST_PORTS.md` (create it if missing). Don't reuse ports assigned to other projects unless verified safe. Register any new fixed port there in the same change.

## Scripting Defaults

Scripts default to Python unless a language is specified. Write cross-platform code (paths, shell invocation, filesystem behavior, environment).

## Shell Commands on Windows

Commands execute via `powershell.exe -Command "<string>"` (Windows PowerShell 5.1) unless the harness says otherwise. The command is embedded in an extra quoting layer you cannot see.

- Never use POSIX-only syntax: no heredocs (`<<'EOF'`), no `&&`/`||` chaining, no `$(...)`, no `export VAR=x`.
- Never use PowerShell here-strings (`@'...'@`) inside a `-Command` string — the outer quoting layer breaks them.
- For multiline Python or scripts: write the code to a temp file with the file-write tool, run `python tempfile.py`, then delete it. Do NOT pipe multiline code via stdin.
- For one-liners: `python -c "..."` with double quotes outside and single quotes inside.
- On a parse or quoting error, switch to the temp-file approach immediately — don't retry with different quoting.

## Encoding on Windows

In PowerShell, use explicit UTF-8 when reading, writing, or verifying anything that may contain non-ASCII (e.g. Chinese) text.

## Notes and Memory

Record durable facts and decisions directly in the project's relevant doc files and/or agent files (AGENTS.md / CLAUDE.md), DO NOT USE memory.

## Incidental Fixes

When you notice a small issue or flaw while working on the main task, fix it in passing — don't ask whether to fix it, just do it.

## Installing Dependencies

When you need a library or tool (e.g. openpyxl), just install it with whatever tool you know best — don't take detours.
