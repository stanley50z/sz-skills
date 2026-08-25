## Working Values

Build complex things as simple as possible. Understand the real constraint, then fight for the smallest change that makes the correct behavior unsurprising — measure twice, cut once; YAGNI. Fight scope creep: honor the task's intent in a minimal, realistic fashion.

## General Coding Preferences

- Type safety is useful; lean on it.
- Propose bold ideas when they can meaningfully benefit the work.
- Limit destructive actions to targets explicitly authorized by the user.
- Write focused regression tests for real behavior.
- Comment how a function or class is used, above its definition — not every line — and update comments when the code changes.

## TypeScript

- Write idiomatic TypeScript; if it reads like a Python dev wrote it, rewrite it.
- Prefer inferred types over annotations. Use `any` only when no reasonable typed alternative exists or the user requests it.
- Skip one-liner wrappers that exist only to cast.

## Questions Are Read-Only

When the user asks how something works or why, investigate and answer. Start editing only when the user requests a change.

## Match Ceremony to the Task

Work a single agent finishes in one pass gets a single agent. Delegate to sub-agents only for breadth or adversarial review.

## Visual and Design Work

- Mock first: explore directions in throwaway mocks, and touch real components only after the user picks one.
- Use strong contrast; follow the project's existing design tokens.

## File handoff

In T3 Code, use `t3code-file-links` whenever returning or displaying a local file. In other harnesses, use that harness's native file-link syntax and include the native absolute path when the user needs a copyable location.

## Question Dialogs and Hidden Text

Give context in plain text before asking a question.

## Web Search

When unsure about a fact involving real-world products/news/repositories, use web search before answering.

## Localhost Ports

Before picking a localhost port, read `~\LOCALHOST_PORTS.md` and create it if missing. Choose an unassigned port, verify it is available, and register any new fixed port there in the same change.

## Utility Scripts

For projects requiring a repeatable launch command, provide a cross-platform `start.py`. Default utility scripts to Python unless another language is specified.

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

Record durable facts and decisions in the relevant project or agent documentation.

## Scope

Keep changes within the user's requested scope.

## Installing Dependencies

Install required dependencies with the project's preferred package manager. When the project has no preference, use pnpm, then Bun, then other appropriate package managers.
