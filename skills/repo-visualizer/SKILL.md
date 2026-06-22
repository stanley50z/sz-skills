---
name: repo-visualizer
description: Use when asked to update docs, visualize a codebase, map repository structure, generate repo_structure.htmnel, document code dependencies, inputs, outputs, call graphs, or script internals.
---

# Repo Visualizer

## Overview

Create a navigable architecture snapshot of the non-test code in the current repository. The output is a self-contained HTML page at `doc/repo_structure.htmnel` that future maintainers can scan and click through.

## When to Use

- User says "update docs", "visualize codebase", "show repo structure", "map codebase", "document how files connect", or asks for `repo_structure.htmnel`.
- Use for source-code repositories where file relationships and script internals matter.
- Do not use for test-only reviews, generated/vendor code, or broad architecture refactoring recommendations.

## Workflow

1. Inspect repo orientation files first: README, package/project manifests, build/config files, and existing docs.
2. Inventory non-test source code. Exclude `test`, `tests`, `__tests__`, `spec`, `e2e`, fixtures, snapshots, coverage, build/dist, vendored dependencies, caches, and generated output unless they are the product being documented.
3. Read the code files, prioritizing entry points, config, scripts, and modules imported by other files. Do not infer details from filenames alone.
4. Build a file graph from imports/requires/includes, CLI or config entry references, and obvious runtime calls. Label uncertain or dynamic edges as `dynamic/indirect` instead of inventing certainty.
5. For each code file, identify purpose, inputs, outputs, key functions/classes, and key module-level variables/constants/state.
6. Generate `doc/repo_structure.htmnel`, creating `doc/` if needed. Regenerate from source when updating; do not patch stale facts by hand.
7. Open the local HTML page and verify Mermaid renders, file clicks change the details panel, text is readable, and there are no script errors. Prefer Chrome DevTools MCP for `file://` verification when available; close that browser session afterward.

## File Details

For every included code file, capture:

| Field | What to Record |
|---|---|
| Purpose | One sentence describing the file's role |
| Inputs | CLI args, env vars, files, network/DB/user input, imported APIs |
| Outputs | Files, stdout/logs, network/DB writes, exports, rendered UI, side effects |
| Functions/classes | Name, purpose, important params, return value or effect |
| Variables/constants | Module-level config, exported state, flags, and values that shape behavior |

## HTML Requirements

- Self-contained HTML/CSS/JS except Mermaid may load from CDN.
- Include a Mermaid graph showing code files and links. Use compact file labels and edge labels for import/call/config relationships.
- Make each script/code file clickable from both the graph and a file list. Clicking shows that file's details in a side panel or main panel.
- For Mermaid callbacks, initialize Mermaid with `securityLevel: "loose"` and expose the handler on `window`, for example `window.selectFile = selectFile`.
- Include a summary section with project inputs, project outputs, main entry points, and omitted test/generated paths.
- Use stable element IDs derived from paths, escape all code text for HTML/JS, and keep the page usable without a build step.

## Mermaid Pattern

```mermaid
flowchart LR
  app_py["app.py\ninput: HTTP/env\noutput: routes/logs"] --> db_py["db.py\ninput: queries\noutput: records"]
  click app_py call selectFile("app.py") "Show app.py details"
```

Pair it with JavaScript data:

```js
const files = {
  "app.py": {
    purpose: "...",
    inputs: ["..."],
    outputs: ["..."],
    functions: [{ name: "main", purpose: "..." }],
    variables: [{ name: "CONFIG", purpose: "..." }]
  }
};
```

## Quality Bar

- Prefer accurate partial coverage over broad invented coverage.
- Keep tests out of the main graph; mention excluded test areas only in the omitted paths section.
- If a file is large, summarize stable public behavior before private helpers.
- If the repo uses multiple languages, document each by its actual dependency mechanism.
- If verification cannot run, state exactly what was generated and what was not verified.
