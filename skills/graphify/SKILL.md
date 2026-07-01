---
name: graphify
description: Use when answering any question about a codebase, architecture, file relationships, dependency links, data-flow, or project content, especially when graphify-out/graph.json exists, or when asked to build, refresh, query, explain, path, init, or initialize Graphify.
---

# Graphify

## Overview

Use the upstream Graphify CLI as a codebase knowledge graph engine. The Python package is `graphifyy`; the command is `graphify`.

This is a local wrapper skill, not Graphify's full platform-specific skill. Prefer the CLI outputs and keep this repo's skill/hook installation model separate from Graphify's own installers.

## When to Use

- The user explicitly asks for Graphify.
- The user asks to "init graphify" or "initialize Graphify" in a project.
- The user asks to build or refresh a `graphify-out` knowledge graph.
- The user asks any question about a codebase, architecture, file relationship, dependency, data-flow, or project content and `graphify-out/graph.json` exists.
- The user asks questions that can be answered from an existing `graphify-out/graph.json`, `GRAPH_REPORT.md`, or Graphify wiki.

Do not use Graphify when the task is about stale or incorrect graph output, or when the user explicitly says not to use it. For ordinary code edits, use Graphify only when an existing `graphify-out/graph.json` can orient the work first. Do not treat Graphify's node graph as a replacement for a human-readable architecture document.

## Fast Path for Existing Graphs

If `graphify-out/graph.json` exists and the user asks a natural-language question about codebase structure, architecture, file relationships, dependencies, data flow, call paths, ownership, or project content, first run `graphify query "<question>"` before broad `rg`, `grep`, or multi-file reads.

Use `graphify path "<A>" "<B>"` when the question asks how two concepts connect. Use `graphify explain "<concept>"` when the question asks what a specific component, module, file, or concept does. Use source files afterward to verify details before editing code.

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

3. If the user asked to "init graphify" or "initialize Graphify", treat that as an explicit request for repo-local git hooks too. From the target project repo, install Graphify's git hooks:

```sh
graphify hook install
```

This installs or appends Graphify-managed `post-commit` and `post-checkout` hooks for that project so `graphify-out` refreshes after commits and checkouts.

4. Use the generated outputs:

```text
graphify-out/graph.html
graphify-out/GRAPH_REPORT.md
graphify-out/graph.json
```

In a repo, treat `graphify-out/` as generated local output and add it to `.gitignore` unless the user explicitly asks to version graph snapshots.

5. For questions against an existing graph, query the graph before broad source inspection:

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
- Do not run `graphify claude install`, `graphify codex install`, or `graphify hook install` unless the user explicitly asks for always-on project integration, git hooks, or to "init graphify" / "initialize Graphify". This repo manages its own skills and hooks through `setup.py`.
- Do not vendor Graphify's platform-specific `SKILL.md` variants into this wrapper. Keep this skill compact and wrapper-focused.
- Do not invent graph edges or architecture facts. If Graphify marks an edge `INFERRED` or `AMBIGUOUS`, preserve that uncertainty.
- For large repos, use Graphify's narrowing suggestions instead of forcing a whole-repo run.
- For `file://` HTML verification, follow the project browser-tool preference and inspect the generated page visually.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Installing a PyPI package named `graphify` | Install `graphifyy`; the command is still `graphify`. |
| Running `/graphify .` in PowerShell | Run `graphify .`. |
| Hand-patching stale graph output | Re-run Graphify and use the refreshed `graphify-out/graph.json`. |
| Letting Graphify overwrite repo instruction files | Skip Graphify installers unless the user asked for that integration. |
