---
name: to-tickets
description: Break a plan, spec, or the current conversation into tracer-bullet tickets with blocking edges, published to the configured tracker.
disable-model-invocation: true
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets** — tracer-bullet vertical slices, each declaring the tickets that **block** it.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

If the work came through `/to-spec`, fetch the published spec from the tracker and read it.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests) — vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

Give each ticket its **blocking edges** — the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change — rename a column, retype a shared symbol — whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket — green is promised only there.

### 4. Review the breakdown when there is one

First verify that every requirement maps to at least one ticket. None may be silently dropped.

A **direct single-ticket request** is a self-contained request supplied with this skill invocation that clearly maps to one ticket with no blocking edges. Treat the invocation as approval: publish that ticket immediately and skip breakdown review. Scope or acceptance-criteria ambiguity that prevents a complete ticket is the only reason to ask a clarifying question.

For specs, plans, conversations with multiple requirements, or any proposal producing multiple tickets, present the breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct — does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Publish the tickets to the configured tracker

Publish the direct ticket or approved breakdown as GitHub issues, following `docs/agents/issue-tracker.md`, in the staged sequence below. The graph must become visible before any ticket enters an automated implementation queue.

1. Create every implementation ticket without `ready-for-agent` and without an assignee. Create blockers first so later ticket bodies can reference real identifiers.
2. Wire the complete graph. Link each implementation ticket to the spec parent with the platform's native parent/sub-issue relationship. Add every native blocking dependency.
3. Read the graph back from the tracker. Verify that every ticket has the intended parent and blocker set. If any relationship is missing or wrong, leave every new ticket outside the implementation queue and report the mismatch.
4. Apply `ready-for-agent` to the implementation tickets only after the graph passes verification. Apply any category labels required by the tracker at the same time.

The spec parent remains the central reference and progress tracker. Preserve its body and open/closed state. Remove `ready-for-agent` from the spec parent if a legacy `/to-spec` run added it, and apply the configured non-executable spec label when available.

Work the **frontier**: any implementation ticket whose blockers are all done. For a purely linear chain, that means top to bottom. Blocked implementation tickets may carry `ready-for-agent`; native dependencies keep them out of the live frontier.

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue, otherwise omit this section).

## Requirement

Which spec item this implements.

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective — not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None — can start immediately".

</issue-template>

Avoid specific file paths or code snippets — they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

For UI work, write acceptance criteria along both tdd-skill axes — visual checks (viewport, state, what must not clip, overflow, or misalign) and end-to-end behavior walkthroughs (the workflow to click through in the browser and the result that must appear, on real data when available) — not component tests, DOM assertions, or snapshots.

## When the User Requests a Change During Ticketing

A user change during ticketing is a new requirement: propagate it to the spec first, then the tickets, following [`../implement/REQUIREMENT-CHANGES.md`](../implement/REQUIREMENT-CHANGES.md).

## HTML Plan Companion

For a large or hard-to-review breakdown, create an optional HTML Plan Companion (linked from the spec parent issue, e.g. `docs/plans/<artifact-id>/plan.html`). The published tickets remain the source of truth; the HTML file is a review aid.

Use an HTML Plan Companion when it would make the breakdown easier to understand through:

- ticket dependency maps
- file-change maps
- requirement-to-ticket traceability
- plan overview dashboards
- risk or blocker summaries

Do not create HTML for small breakdowns, short ticket lists, or anything where Markdown is clearer. Do not replace ticket bodies or acceptance criteria with HTML-only content.

## Handoff

Offer the user both execution routes; the user chooses and invokes one:

- `/implement`: work the frontier one ticket at a time, clearing context between tickets.
- `/implement-spec`: orchestrate the whole spec on one integration branch, for an approved multi-ticket spec.
