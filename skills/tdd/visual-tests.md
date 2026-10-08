# Visual and End-to-End UI Tests

The canonical UI testing policy for [the TDD loop](SKILL.md). Two checks, both
required, neither replacing the other:

- **Look-and-feel is verified visually.** Layout, styling, visual hierarchy,
  and interaction-state appearance are checked by looking at the rendered UI.
  Write no component, DOM, or snapshot code tests for them.
- **Behavior is verified with a live browser walkthrough** of every changed
  flow. Scripted e2e suites (Playwright, Cypress, etc.) still run where the
  project has them, but they do not replace the walkthrough.

## Browser

Drive the browser through the `browser-harness` skill: use the native Skill
tool when the harness has one, otherwise read its `SKILL.md`. It owns tool
choice, tab ownership, and cleanup. Use a full-screen desktop browser unless
the user explicitly requests another device or viewport.

## Visual RED/GREEN

```text
RED:    open the current UI and capture the broken or missing state
GREEN:  implement the smallest change
VERIFY: reopen, interact, screenshot, and inspect the relevant screens and states
```

The evidence is a screenshot or live observation plus concise notes, never a
DOM guess.

Inspect each relevant screen and state for:

- Text fully visible: no clipping, unintended truncation, overflow, or text
  hidden behind other elements; controls fit their longest expected labels.
- Components aligned to a coherent grid, repeated components lined up.
- Balanced horizontal and vertical visual weight; no lopsided, crowded, or
  empty regions.
- Clear hierarchy, grouping, and spacing; the primary action and current
  state are obvious.
- No incoherent overlap between sections, controls, cards, modals, or
  navigation; no unexpected scrollbars, layout jumps, or off-screen controls.
- Hover, focus, active, disabled, selected, loading, empty, and error states
  where they exist.

## Behavior walkthrough

For every changed flow, drive the real UI:

- Perform the actual user workflow: navigate, click the real controls, type
  into the real fields, submit.
- Use real data when it is available (dev database, sample files, live dev
  API) rather than placeholder input.
- Review the result the user would see: correct data rendered, state changes
  applied, navigation and redirects landing where expected, persistence across
  a reload when relevant.
- Exercise reachable error and edge flows, not just the happy path.
- Capture evidence of the result state, not just the initial screen.
