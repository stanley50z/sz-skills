---
name: global-project-preferences
description: Use when starting greenfield work — a new project, app, script, or prototype where no competing stack is specified
---

# Global Project Preferences

For greenfield work — planning, scaffolding, dependency selection, architecture setup — default to the stack below.

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
2. Check for hard constraints: user instructions, existing repo standards, deployment target, language/runtime requirements, compliance, scale, team familiarity, or incompatible integrations. These always win over the defaults.
3. Keep the default unless a constraint makes an alternative materially better.
4. If proposing an alternative, state the exact tradeoff in one sentence.
