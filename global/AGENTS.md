For plain local `file://` HTML pages, prefer Chrome DevTools MCP for visual inspection, screenshots, and simulated button/key presses.

For other browser verification and control tasks, prefer tools in this order:

1. Codex Chrome Plugin, when the harness is Codex and the plugin is available.
2. Chrome DevTools MCP connected to the existing user profile and session.
3. Chrome DevTools MCP in a new session/window.

After finishing Chrome DevTools MCP work, close the entire DevTools-controlled browser/window only when it was launched by Chrome DevTools MCP with an owned isolated profile or unique `user-data-dir`. If MCP attached to an existing browser via `browser-url`, `ws-endpoint`, `autoConnect`, or a normal user profile, do not close the browser automatically; close only task tabs when appropriate.

## Web Search

When unsure about a fact involving real-world products, use web search before answering.

## Scripting Defaults

When asked to write a script and no language is specified, use Python by default. Keep cross-platform compatibility in mind, especially for paths, shell invocation, filesystem behavior, and environment assumptions.

## Encoding on Windows

When reading, writing, or verifying files/command output that may contain Chinese or other non-ASCII text in PowerShell, use UTF-8 explicitly.
