## Working Values

Build complex things as simple as possible. Understand the real constraint, then fight for the smallest change that makes the correct behavior unsurprising — measure twice, cut once; YAGNI. Fight scope creep: honor the task's intent in a minimal, realistic fashion.

## General Coding Preferences

- Type safety is useful; lean on it.
- Propose bold ideas when they can meaningfully benefit the work.
- Limit destructive actions to targets explicitly authorized by the user.
- Write focused regression tests for real behavior.
- Comment how a function or class is used, above its definition — not every line — and update comments when the code changes.

## Debugging artifacts

Always provide persistent log and crash dump paths for debugging. Configure the application to write to them and document their locations in the project. If the runtime cannot produce native crash dumps, persist crash reports with stack traces instead.

## TypeScript

- Write idiomatic TypeScript; if it reads like a Python dev wrote it, rewrite it.
- Prefer inferred types over annotations. Use `any` only when no reasonable typed alternative exists or the user requests it.
- Skip one-liner wrappers that exist only to cast.

## Questions Are Read-Only

When the user asks how something works or why, investigate and answer. Start editing only when the user requests a change.

## Match Ceremony to the Task

Work a single agent finishes in one pass gets a single agent. Delegate to sub-agents only for breadth or adversarial review.

## T3 Code model and subagent preferences

These preferences apply inside T3 Code; standalone Pi keeps its own configuration.

- Prefer native Codex for OpenAI models, native Claude Code for Anthropic models, and Pi for third-party models. Apply the same routing to subagents, regardless of the parent's harness. Respect the user's explicitly selected model.
- Prefer Opus 5.5 with high effort for front-end design, code review, daily coding, exploration, and everyday use unless the user requests another model or effort.
- Resolve provider instances, model IDs, and supported options through T3's `orchestrator_capabilities`. Use `delegate_task` for cross-provider work or explicit model options; native same-provider subagents are suitable when they support the selected model and no model options are needed.
- For Opus 5.5 subagents, explicitly pass high effort in the delegation options, not just the task prompt. Use the provider's advertised option names and confirm the returned provider, model, and options match the request.
- When the user dictates a child's prompt, pass it word for word and omit the optional `role` field. Add no length target, format, or skill instructions unless asked. Otherwise, give each child a self-contained brief.
- If the requested provider, model, or option is unavailable or fails, report the failure and stop that delegation. Switch providers, models, or routes only when the user authorizes it. Retry authentication failures only after the user confirms access is restored.

## Visual and Design Work

- Use Anthropic's `frontend-design` as the sole visual-design skill.
- UI testing targets desktop unless the user explicitly requests another device or viewport.
- Mock first: explore directions in throwaway mocks, and touch real components only after the user picks one.
- For UI design choices, prefer one self-contained HTML comparison page containing every option, clearly labeled to match the question. Images are acceptable when every option has a visible preview, either in a labeled comparison sheet or as individually linked images. Before asking the user to choose, provide access to all previews in the preceding message. Agent-side image inspection does not count as showing the user. Keep the comparison available until the user decides.
- When building or reviewing UI, apply `~/sz-skills/global/UI-GUIDELINES.md`.

## File handoff

In T3 Code, use `t3code-file-links` whenever returning or displaying a local file. In other harnesses, link files as `file:///C:/path/to/file` URLs with forward slashes so the terminal makes them ctrl-clickable, and include the native absolute path when the user needs a copyable location.

## HTML Reports

- Answer explanations, summaries, and ordinary questions in chat. Length alone does not require a file. Create an HTML report when the user requests one or the task explicitly calls for a saved visual artifact, such as the UI comparisons above.
- Subagents return findings as text to the parent unless their assigned task explicitly requests a report artifact.
- Link reports according to File handoff and include the main finding in the reply. In T3 Code, when asked to show the report here, use `html_preview` then `html_render`. Open a report in the host's default app only when the user requests it; the user may be viewing T3 remotely.

## Global Agent Instructions

`~/sz-skills` is the source of truth for these global instructions and for global skills. Edit `~/sz-skills/global/AGENTS.md` (or `global/CLAUDE.md`), then run `python setup.py` there to regenerate the installed copies. Never edit `~/.pi/agent/AGENTS.md`, `~/.codex/AGENTS.md`, `~/.config/opencode/AGENTS.md`, or `~/.claude/CLAUDE.md` directly; `setup.py` overwrites them.

## Loading Skills

When an instruction says to load or use a named skill, call the harness's native skill tool if it has one; otherwise read that skill's `SKILL.md` from the location the harness lists. A skill marked `disable-model-invocation: true` runs only when the user names it; never load it on your own or from another skill.

Keep Claude Code's retired `superpowers` plugin and duplicate `frontend-design` plugin disabled. Use the repo-installed Anthropic `frontend-design` skill.

## Question Dialogs and Hidden Text

Give context in plain text before asking a question.

## Web Search

When unsure about a fact involving real-world products/news/repositories, use web search before answering.

In Codex and Claude Code, prefer the harness's native web-search tools; Ketch and Firecrawl skills are not required for ordinary web research. Pi keeps its configured Ketch and specialist research skills. Browser automation follows the separate Browser Use policy.

## Browser Use

For browser exploration, automation, scraping, testing, or site/app interaction, invoke the `browser-harness` skill.

After browser exploration or testing, close every browser tab opened for the task and delete every temporary script created for it.

## Specific GitHub Repository Questions

When the user writes `@owner/repo`, interpret it as the GitHub repository `https://github.com/owner/repo`, including in installation requests. For example, `@trycua/cua` means `https://github.com/trycua/cua`. Treat it as a scoped npm package only when the user explicitly identifies it as an npm package.

When the user asks about a specific GitHub repository, compare its owner with the user's GitHub account. For a repository owned by the user, inspect the existing first-party checkout at its default location, `~\<repo-name>`; ask for its location if absent. For a repository owned by another account, use `~\github repo ref\<repo-name>`. If that checkout already exists, run `git pull --ff-only` before inspecting it. Otherwise, clone it there. Treat the source code as the primary evidence instead of relying on documentation or web search. This workflow applies only when the repository itself is the subject of the user's question.

After every answer about a repository newly cloned under `~\github repo ref\` for the current request, report that repository folder's current size and ask whether to keep or delete it. Do not ask about deleting a checkout that existed before the request. If the user continues asking about a newly cloned repository without answering, answer the new question and repeat the size and retention question. Delete the clone only with explicit user authorization.

## Machines

`mac`, `pc`, and `razor` are the user's machines. Each name is also a configured SSH alias, so `ssh <name>` reaches that machine.

## Tool Boundaries

Never use computer use unless the user explicitly requests it.

## Localhost Ports

Before picking a localhost port, read `~\LOCALHOST_PORTS.md` and create it if missing. Choose an unassigned port, verify it is available, and register any new fixed port there in the same change.

## Test server cleanup

Stop every temporary test or dev server you start once testing finishes, including on failure and before handing off or completing the task, unless the user explicitly asks to leave it running. Track their PIDs and ports, stop their child processes too, and verify the processes have exited and their ports are released. Target only processes started for the task; preserve existing apps and agent sessions, and never kill processes by runtime name alone, such as all `node` processes.

## Utility Scripts

For projects requiring a repeatable launch command, provide cross-platform `start.py` and `stop.py` scripts. Both scripts must run without opening a terminal window, and `start.py` must leave long-running processes in the background. Default utility scripts to Python unless another language is specified.

## Shell Commands on macOS / zsh

- Quote patterns intended for a tool, such as `rg -g '*.ts'` or `grep --include='*.ts'`, so zsh does not expand them. Quote literal arguments beginning with `=` to avoid zsh's command-path expansion.
- Check command exit status and stderr before treating empty output as a finding. After a quoting error, move complex logic into a temporary script and remove it after use.
- macOS does not ship GNU `timeout`. Use the execution tool's timeout option when available, or Python's `subprocess.run(..., timeout=...)` for a command deadline. A tool's yield/wait interval only controls when output returns; it does not terminate the command.

## Shell Commands on Windows

The shell depends on the tool that runs your commands:

- **A tool named `bash`/`Bash`** (Pi, Claude Code): Git Bash (MSYS2). Use Bash syntax; `&&`, `$(...)`, and heredocs work. `C:\Users\13982` is `/c/Users/13982` or `~`. Call Windows-only commands explicitly, e.g. `powershell.exe -NoProfile -Command '...'`.
- **A tool named `powershell`, or Codex's shell tool**: Windows PowerShell 5.1 via `powershell.exe -Command "<string>"`, inside an extra quoting layer you cannot see. Use no POSIX-only syntax: no heredocs, no `&&`/`||` chaining, no `$(...)`, no `export VAR=x`, and no here-strings (`@'...'@`).

In either shell:

- For multiline Python or scripts: write the code to a temp file with the file-write tool, run `python tempfile.py`, then delete it. Do NOT pipe multiline code via stdin.
- On a parse or quoting error, switch to the temp-file approach immediately — don't retry with different quoting.

## Windows UAC approval

- When an authorized task requires administrator privileges, launch the elevated script immediately. The user expects the Windows UAC prompt and is usually nearby to approve it.
- Keep the agent running: wait 10 seconds, then check process status, logs, or the intended system change to determine whether elevation succeeded. Never ask the user whether they approved UAC or end the turn waiting for a chat reply.
- If approval has not gone through, reissue the UAC request and repeat the 10-second check automatically. Keep only one live approval attempt at a time; retire any stale pending attempt before replacing it.
- Once the elevated operation starts, monitor it rather than relaunching it. Verify the result and continue the task. A missing result alone does not mean approval failed.
- Continue this loop until approval succeeds or the user tells you to stop. Diagnose actual launch or command failures from logs rather than treating every failure as missing approval. UAC approval remains a Windows interaction; never bypass it.

## Encoding on Windows

Use explicit UTF-8 when reading, writing, or verifying anything that may contain non-ASCII (e.g. Chinese) text, especially in PowerShell or when passing text to `powershell.exe`.

## Notes and Memory

Record durable facts and decisions in the relevant project or agent documentation.

WHEN THE USER MAKES A DECISION THAT OVERRIDES A PREVIOUS DECISION, REVISIT AND RECONFIRM THE OVERRIDDEN DECISION AND ALL PREVIOUS RELATED DECISIONS IN LIGHT OF THE NEW DECISION BEFORE PROCEEDING.

## Scope

Keep changes within the user's requested scope.

## Installing Dependencies

Install required dependencies with the project's preferred package manager. When the project has no preference, use pnpm, then Bun, then other appropriate package managers.
