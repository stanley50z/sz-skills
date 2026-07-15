---
name: to-spec
description: Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a spec (you may know this document as a PRD). Do NOT interview the user — just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you — run `/setup-matt-pocock-skills` if not. If no tracker has been provided, default to the local tracker: write the spec to `docs/specs/<artifact-id>-design.md`, where `<artifact-id>` is `YYYY-MM-DD-<feature-slug>` (reuse the effort's existing artifact ID if one was already chosen).

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better - the ideal number is one.

Check with the user that these seams match their expectations.

3. Write the spec using the template below, then publish it to the project issue tracker. Apply the `ready-for-agent` triage label - no need for additional triage.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

This list of user stories should be extremely extensive and cover all aspects of the feature.

## User Requirements

Items the user explicitly stated, chose from options, or confirmed as their own intent during the conversation. Each item must be traceable to something the user actually said or selected.

- [requirement]: [brief trace — e.g., "user's initial request", "chose from options", "confirmed when asked"]

## Agent Design Decisions

Everything the agent inferred, recommended, or filled in to complete the design. Each item notes which user requirement it serves.

- [decision]: serves [which user requirement]. [rationale]

Classification rules:

- If the user said it, chose it, or explicitly confirmed it as their own intent → User Requirement
- If the agent proposed it and the user said "looks good" or "yes" to a batch → Agent Design Decision (blanket approval does not promote agent decisions)
- For mixed items (user said "authentication," agent picked OAuth2): split them — "authentication required" is a User Requirement; "OAuth2 with Google provider" is an Agent Design Decision serving it

Priority hierarchy: User Requirements are non-negotiable downstream. Agent Design Decisions are flexible — they can be revised or dropped if they conflict with a User Requirement or if implementation reality demands it. This hierarchy carries into `/to-tickets` (ticket tags) and `/implement`.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>

## Structured HTML Companion

For a large or hard-to-review spec, create an optional Structured HTML Companion next to it (`docs/specs/<artifact-id>-design.html` on the local tracker, or linked from the issue). The HTML companion is a review aid, not the canonical spec — the published Markdown spec remains the source of truth.

Use it when scanning beats prose:

- option comparison cards
- decision matrices
- architecture sketches
- requirement grouping
- Approach Comparison — recommended option plus alternatives
- Risks / Tradeoffs — visible costs, constraints, and mitigations

Skip HTML for short specs, ordinary clarifications, or anything clearer as plain Markdown.

## Handoff

Once the spec is published and the user approves it, break it into tracer-bullet tickets with `/to-tickets`.
