# Visual UI Tests

All UI testing is visual testing. Do not write code tests for UI layout,
styling, responsive behavior, visual hierarchy, or interaction states.

## Tool Priority

1. Codex agents use the Chrome plugin first when it is available.
2. If Chrome plugin is unavailable or insufficient, use Chrome DevTools MCP.
3. If neither is available, use the best available browser/screenshot tool and
   state the fallback.

Project instructions may name a more specific browser tool for a target. Follow
those instructions when they are more specific than this default order.

## Visual RED/GREEN

For UI work, the TDD cycle becomes:

```text
RED:   Open the current UI and capture/inspect the broken or missing state
GREEN: Implement the smallest change
VERIFY: Reopen, interact, screenshot, and inspect the relevant viewports/states
```

The evidence is a screenshot or live browser observation plus concise notes.
Do not replace visual inspection with DOM assertions, snapshot tests, component
unit tests, or "it should render" tests.

## Required Checks

Inspect each relevant screen/state for:

- Text clipping, unintended truncation, overflow, or hidden text.
- Labels, button text, badges, and table cells fitting inside their containers.
- UI components aligned to a coherent grid.
- Balanced horizontal and vertical visual weight.
- Clear hierarchy, grouping, and spacing.
- No incoherent overlap between adjacent sections, controls, cards, modals, or
  navigation.
- Responsive behavior at realistic desktop and mobile viewports.
- Hover, focus, active, disabled, selected, loading, empty, and error states
  when those states exist.
- No unexpected scrollbars, layout jumps, or off-screen controls.

## Visual Quality Rules

- Text must remain readable and fully visible.
- Controls must have enough space for their longest expected labels.
- Repeated components should line up consistently.
- Dense UIs should still scan cleanly; spacious UIs should not feel empty.
- Primary actions and current state should be visually obvious.
- Visual decisions should serve the product workflow, not decoration.
