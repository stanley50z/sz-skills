---
name: graphify
description: Use when asked to visualize or map a codebase, document repository structure, inspect architecture or file relationships, generate codebase graph reports, or answer questions from an existing graphify-out graph.
---

# Graphify

## Overview

Use the upstream Graphify CLI as the codebase map engine instead of hand-writing a repository visualization. The Python package is `graphifyy`; the command is `graphify`.

This is a local wrapper skill, not Graphify's full platform-specific skill. Prefer the CLI outputs and keep this repo's skill/hook installation model separate from Graphify's own installers.

## When to Use

- The user asks to visualize a codebase, map repository structure, document file relationships, inspect architecture, or generate a repo graph.
- The user asks questions that can be answered from an existing `graphify-out/graph.json`.
- The user asks for the old repo visualizer output, `repo_structure`, or `docs/repo_structure.*`.

Do not use Graphify for ordinary code edits where direct source inspection is faster, unless an existing `graphify-out/graph.json` can orient the work first.

## Workflow

1. Check whether Graphify is available:

```sh
graphify --version
```

If missing, install the official package:

```sh
uv tool install graphifyy
```

If `uv` is not available, use `pipx install graphifyy`. Avoid plain `pip install` unless there is already an active project environment intended to own the CLI.

2. Build or update the graph:

```sh
graphify .
```

On Windows PowerShell, use `graphify .`; do not type `/graphify .`.

3. Use the generated outputs:

```text
graphify-out/graph.html
graphify-out/GRAPH_REPORT.md
graphify-out/graph.json
```

4. For architecture HTML, generate a call-flow report:

```sh
graphify export callflow-html --output docs/repo_structure.html
```

If the user asked for the old `docs/repo_structure.htmnel` name, prefer the corrected `docs/repo_structure.html` and mention the filename change.

5. For questions against an existing graph, query the graph before reading many source files:

```sh
graphify query "how does authentication reach the database?"
graphify path "UserService" "DatabasePool"
graphify explain "RateLimiter"
```

Use source files afterward to verify details before editing code.

## Guardrails

- Distinguish Graphify's install surfaces:
  - `graphify install --platform claude` and `graphify install --platform codex` install user-scope skill files.
  - `graphify claude install` and `graphify codex install` add project-level always-on instructions and tool hooks.
  - `graphify hook install` adds git hooks for graph refresh.
- Do not run `graphify claude install`, `graphify codex install`, or `graphify hook install` unless the user explicitly asks for always-on project integration or git hooks. This repo manages its own skills and hooks through `setup.py`.
- Do not vendor Graphify's platform-specific `SKILL.md` variants into this wrapper.
- Do not invent graph edges or architecture facts. If Graphify marks an edge `INFERRED` or `AMBIGUOUS`, preserve that uncertainty.
- For large repos, use Graphify's narrowing suggestions instead of forcing a whole-repo run.
- For `file://` HTML verification, follow the project browser-tool preference and inspect the generated page visually.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Installing a PyPI package named `graphify` | Install `graphifyy`; the command is still `graphify`. |
| Running `/graphify .` in PowerShell | Run `graphify .`. |
| Hand-patching stale architecture HTML | Re-run Graphify and regenerate the HTML from `graphify-out/graph.json`. |
| Letting Graphify overwrite repo instruction files | Skip Graphify installers unless the user asked for that integration. |
