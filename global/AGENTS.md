## Working Values

Build complex things as simple as possible. Understand the real constraint, then fight for the smallest change that makes the correct behavior unsurprising — measure twice, cut once; YAGNI. Fight scope creep: honor the task's intent in a minimal, realistic fashion.

## General Coding Preferences

- Type safety is useful; lean on it.
- Propose bold ideas when they can meaningfully benefit the work.
- Be careful with destructive actions the user didn't explicitly request.
- Keep tests focused: regression tests for real bugs and real behavior, not endless smoke tests.
- Comment how a function or class is used, above its definition — not every line — and update comments when the code changes.

## TypeScript

- Write idiomatic TypeScript; if it reads like a Python dev wrote it, rewrite it.
- Prefer inferred types over annotations. Use `any` only when no reasonably typed alternative exists or the user asks for it.
- Skip one-liner wrappers that exist only to cast.

## Questions Are Read-Only

When the user asks how something works or why, investigate and answer. Start editing only when the user requests a change.

## Match Ceremony to the Task

Work a single agent finishes in one pass gets a single agent. Delegate to sub-agents only for breadth or adversarial review.

## Visual and Design Work

- Mock first: explore directions in throwaway mocks, and touch real components only after the user picks one.
- Use strong contrast; follow the project's existing design tokens.

## File links

Only link files inside the current thread's project. Use absolute paths, forward slashes, and optional `:line:column`:

- Windows: `[app.ts](/C:/Users/name/project/src/app.ts:12:3)`
- macOS/Linux: `[app.ts](/Users/name/project/src/app.ts:12:3)`

Percent-encode special characters in link targets.

For files outside the current project—even in another T3 project—print the native absolute path as plain text without backticks.

## Question Dialogs and Hidden Text

Harnesses like T3 Code collapse assistant text that precedes a tool call into the Work Log, so the user never sees it. Never ask a question (via AskUserQuestion or any dialog tool) that refers to content living only in that hidden text — e.g. "does this summary match your understanding?" when the summary itself is invisible.

- Make every question dialog self-contained: put the summary, plan, or recommendation being confirmed into the question text and option descriptions.
- If the content is too long to fit in the dialog, don't use the dialog tool: end the turn with the content plus the question as plain visible text, and wait for the reply.

## Web Search

When unsure about a fact involving real-world products/news/repositories, use web search before answering.

## Localhost Ports

Before picking a localhost port, read `~\LOCALHOST_PORTS.md` (create it if missing). Don't reuse ports assigned to other projects unless verified safe. Register any new fixed port there in the same change.

## Utility Scripts
For any project that needs to launch sth, make a start.py script to do it.
Utility scripts default to Python unless a language is specified. Write cross-platform code (paths, shell invocation, filesystem behavior, environment).

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
