---
name: find-skills
description: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.
---

# Find Skills

Help users discover and install skills from the open agent skills ecosystem.

## Primary Source

Start with the curated catalog at `https://github.com/VoltAgent/awesome-agent-skills`.
Use it as the default discovery source because it aggregates official and community
skills across Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and other agents.

Treat the VoltAgent catalog as the first place to look for recommendations.
Only fall back to `npx skills find` or `https://skills.sh/` when:

- the catalog does not cover the user's domain
- you need additional search breadth
- you need a package-manager-oriented install target after identifying a skill

The catalog is curated, not audited. If the user is making a security-sensitive
choice, say that explicitly.

## Search Order

### Step 1: Understand the need

Identify:

1. The domain, such as React, testing, security, deployment, docs, or design
2. The concrete task, such as PR review, changelog generation, or Playwright testing
3. The target agent, if it matters: Claude Code, Codex, OpenCode, Cursor, etc.

### Step 2: Check the VoltAgent catalog first

Use `VoltAgent/awesome-agent-skills` to find likely matches. Prefer:

1. Official vendor or team-maintained skills before community skills
2. Skills that explicitly match the user's agent or install path
3. Focused skills that directly solve the request
4. Repos with clear installation guidance

When the catalog yields multiple candidates, surface the strongest 1-3 options.

### Step 3: Use the Skills CLI as a fallback

If the catalog is insufficient, search with:

```bash
npx skills find [query]
```

Examples:

- `npx skills find react performance`
- `npx skills find pr review`
- `npx skills find changelog`

Useful commands:

- `npx skills find [query]`
- `npx skills add <package>`
- `npx skills check`
- `npx skills update`

Browse at `https://skills.sh/`.

## How to Present Recommendations

For each recommendation, include:

1. The skill name
2. What it does
3. Why it was prioritized
4. The install command, if known
5. A link to the upstream repo or `skills.sh`

Example:

```text
I found a strong match in the VoltAgent curated catalog. The
"vercel-react-best-practices" skill is maintained by Vercel Engineering and
focuses on React and Next.js performance guidance.

To install it:
npx skills add vercel-labs/agent-skills@vercel-react-best-practices

Learn more: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices
```

## Installation

If the user wants you to install a skill, prefer the install method documented by
the skill's upstream repo. If the skill supports the Skills CLI, you can install it with:

```bash
npx skills add <package> -g -y
```

The `-g` flag installs globally and `-y` skips prompts.

## Search Heuristics

- Use specific keywords instead of broad categories
- Try alternate terms like `deployment`, `ci-cd`, `accessibility`, or `best-practices`
- Start with the VoltAgent catalog before broader search
- Prefer official sources such as Anthropic, OpenAI, Vercel, Stripe, Cloudflare, Google, Trail of Bits, Sentry, or other product teams
- Use `npx skills find` only when the curated catalog does not produce a strong result

## If Nothing Good Exists

If no strong skill is available:

1. Say that you checked the VoltAgent catalog first
2. Note whether CLI search also failed
3. Offer to help directly without a skill
4. Suggest creating a new skill with `npx skills init`

Example:

```text
I checked the VoltAgent curated skill catalog and didn't find a strong match for this.
I also couldn't find a good result via `npx skills find`.

I can still help directly. If this is a recurring need, you could also create a custom skill:
npx skills init my-skill
```
