For plain local `file://` HTML pages, prefer Chrome DevTools MCP for visual inspection, screenshots, and simulated button/key presses.

For other browser verification and control tasks, prefer tools in this order:

1. Codex Chrome Plugin, when the harness is Codex and the plugin is available.
2. Chrome DevTools MCP connected to the existing user profile and session.
3. Chrome DevTools MCP in a new session/window.

After finishing Chrome DevTools MCP work, close the Chrome DevTools session window so its profile is not left locked for the next turn.
