---
name: to-tickets
description: Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges — one Markdown file per ticket under docs/plans/ by default, or native blocking links on a real issue tracker.
disable-model-invocation: true
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets** — tracer-bullet vertical slices, each declaring the tickets that **block** it.

**Default medium is local ticket files under `docs/plans/`.** Publish to a real issue tracker only when the project or the user explicitly configures one. (User preferences for ticket location override this default.)

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

If the work came through `/to-spec`, read the spec (`docs/specs/<artifact-id>-design.md` on the local tracker). Its **User Requirements** and **Agent Design Decisions** sections are the requirement sources for every ticket.

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

Tag every ticket title with its requirement source from the spec:

- `[USER-REQ]` — implements a user requirement (non-negotiable)
- `[AGENT-DECISION]` — implements an agent design decision (flexible, can be revised)

If a ticket serves both, tag it `[USER-REQ]` — the user requirement takes priority. Every user requirement in the spec must map to at least one ticket; none may be silently dropped.

Give each ticket its **blocking edges** — the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change — rename a column, retype a shared symbol — whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket — green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name with its `[USER-REQ]` / `[AGENT-DECISION]` tag
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct — does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Also verify yourself: does every User Requirement from the spec map to at least one ticket?

Iterate until the user approves the breakdown.

### 5. Publish the tickets

Publish the approved tickets. The tickets are the same either way, only the shape of the blocking edges changes:

- **Local files (default)** → write one file per ticket under `docs/plans/<artifact-id>/<NN>-<slug>.md`, numbered from `01` in dependency order (blockers first). Reuse the effort's existing artifact ID when one exists; otherwise create one as `YYYY-MM-DD-<feature-slug>`. Each file's "Blocked by" lists the numbers/titles it depends on. Use the per-ticket file template below — one ticket per file, never a single combined file.
- **A real issue tracker (GitHub, Linear, …)** → publish one issue per ticket in dependency order (blockers first) so each ticket's blocking edges can reference real identifiers. Use the platform's native blocking / sub-issue relationship where it has one; otherwise set each ticket's "Blocked by" to the blocking issues. Apply the project's agent-ready triage label if one exists.

Work the **frontier**: any ticket whose blockers are all done. For a purely linear chain that means top to bottom.

Do NOT close or modify any parent issue.

<local-ticket-template>

# <NN> — <Ticket title> [USER-REQ | AGENT-DECISION]

**Requirement:** which spec item this implements, quoted or paraphrased — or the agent decision it realizes and which user requirement that serves.

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective — not a layer-by-layer implementation list.

**Blocked by:** the numbers/titles of the tickets that gate this one, or "None — can start immediately".

**Status:** ready

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue, otherwise omit this section).

## Requirement

Which spec item this implements (`[USER-REQ]`) or the agent decision it realizes (`[AGENT-DECISION]`).

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective — not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None — can start immediately".

</issue-template>

In either form, avoid specific file paths or code snippets — they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

For UI behaviour, write acceptance criteria as visual checks (viewport, state, what must not clip, overflow, or misalign) per the tdd skill's visual tests — not component tests, DOM assertions, or snapshots.

## When the User Requests a Change During Ticketing

**A user change during ticketing is a new User Requirement — not a footnote.**

If the user says "change A to B" while reviewing the breakdown, do not just edit the tickets. Propagate the change back to the spec first:

1. **Spec**: Update the User Requirements section — add B, remove or update A
2. **Tickets**: Update or add `[USER-REQ]` tickets for B, remove tickets for old A

The user's request at any stage has the same authority as an initial requirement stated during grilling.

## HTML Plan Companion

For a large or hard-to-review breakdown, create an optional HTML Plan Companion at `docs/plans/<artifact-id>/plan.html`. The Markdown ticket files remain the source of truth; the HTML file is a review aid.

Use an HTML Plan Companion when it would make the breakdown easier to understand through:

- ticket dependency maps
- file-change maps
- requirement-to-ticket traceability
- plan overview dashboards
- risk or blocker summaries

Do not create HTML for small breakdowns, short ticket lists, or anything where Markdown is clearer. Do not replace ticket bodies or acceptance criteria with HTML-only content.

## Handoff

Work the frontier one ticket at a time with the implement skill (`/implement`), clearing context between tickets.
