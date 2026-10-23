# Automode Panel

A Panel is a set of independent advisory subagents, its **seats**, that the authoritative Ticket Session consults. Auto-Grilling calls it a Deliberation Panel; Auto-Review calls it a Review Panel. Seats advise; the Ticket Session judges and acts.

## Roster

The Coordinator resolves the roster once at preflight and passes it in every grilling and review Ticket brief. Default seats:

| Seat | Model | Reasoning |
|---|---|---|
| Codex | GPT-6 Astra | high |
| Claude | Claude Opus 5.5 | high |
| Kimi | Kimi K3 | max |
| Grok | Grok 4.7 | high |

Add the Coordinator's own model as an extra seat when it matches none of these; a reasoning difference alone adds no seat. Launch each seat through the route your harness supports for that model with explicit reasoning options. In T3 Code, resolve provider instances and option names through `orchestrator_capabilities` and launch with `delegate_task`. Drop a seat your harness cannot reach and name it in the preflight report. With fewer than two reachable seats, ask the user before starting.

## Running a round

1. Build one context and give every seat the identical copy.
2. Launch every seat concurrently. A seat never sees another seat's answer.
3. Each seat is read-only and advisory: it reads, searches, and lists files, then answers. Its brief says it cannot edit files, run git writes, touch the tracker, merge, launch subagents, or ask a human.
4. Wait for every seat to finish, with no timeout, retry, or substitute seat. An empty or malformed answer counts as a failed seat; record its diagnostic.

## Grilling seats

Context: all user prompts on the ticket, every prior Grilling Round, the Grilling Session's final answers to those rounds, and the complete current round of numbered questions with their options.

Each seat answers every question with a proposed answer, rationale, material trade-offs, assumptions and uncertainties, and sources for consequential factual claims. A seat that skips a question has failed. The round proceeds when at least one seat succeeds.

## Review seats

Context: the round number, the pinned head SHA, and a prose brief carrying the PR body, work contract, repository guidance, diff, commits, validation evidence, and, after round one, the prior findings, dispositions, and fix diff.

Each seat inspects the pinned head and returns Markdown: either `No actionable findings.` or findings that each give a priority `P0`–`P3`, the exact changed path and line or range, the violated requirement, rule, or invariant, and concrete evidence. Round one is exhaustive. Every seat must succeed before disposition.
