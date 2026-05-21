---
name: global-project-preferences
description: Use when starting a new project, repository, extension, script, app, package, service, CLI, automation, prototype, or other greenfield codebase
---

# Global Project Preferences

## Overview

When starting greenfield work, default to the preferred stack below unless there is strong, project-specific evidence that a preferred option will not work well. Only suggest alternatives when the tradeoff is concrete and relevant to the current project.

## When to Use

Use this at the beginning of:

- New projects, repositories, apps, packages, services, CLIs, scripts, automations, and extensions
- New proof-of-concepts or prototypes where the user has not specified a competing stack
- Planning, scaffolding, dependency selection, and architecture setup for greenfield codebases

Do not use this to override explicit user requirements, existing project conventions, or platform constraints.

## Default Stack

| Area | Default |
|---|---|
| CI/CD | GitHub Actions |
| Payments | Stripe |
| UI Components | shadcn/ui |
| Deployment | Vercel |
| Styling | Tailwind CSS |
| State Management | Zustand |
| Database | Postgres |
| ORM | Drizzle |
| Package Manager | PNPM |
| Testing | Vitest |
| Email | Resend |
| Observability | Sentry |
| API/Data Fetching | TanStack Query |
| Authentication | better auth |
| File Uploads | UploadThing |
| JavaScript Runtime | Node.js |

## Decision Rule

1. Start with the default stack.
2. Check for hard constraints: user instructions, existing repo standards, deployment target, language/runtime requirements, compliance, scale, team familiarity, or incompatible integrations.
3. Keep the default unless the constraint makes an alternative materially better.
4. If proposing an alternative, state the exact tradeoff in one sentence.

## Common Mistakes

| Mistake | Correction |
|---|---|
| Suggesting trendy alternatives by default | Use the default stack unless evidence says otherwise. |
| Treating preferences as hard requirements | User instructions and project constraints win. |
| Recommending alternatives vaguely | Explain the concrete relevant tradeoff. |
