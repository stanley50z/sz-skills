# Council members

The seats of every Council. Change a roster here and every skill that seats it follows.

## Default roster

Seated by the `council` skill and Automode's Deliberation and Review Councils.

| Seat | Model | Reasoning |
|---|---|---|
| Codex | GPT-6.2 Sol | high |
| Claude | Claude Opus 5.5 | high |
| Grok | Grok 4.7 | high |
| Muse | Muse Wonder Full 1.0 | high |

## Max roster

Seated by the `council` skill only when the user explicitly says "council max".

| Seat | Model | Reasoning |
|---|---|---|
| Codex | GPT-6.2 Astra | medium |
| Claude | Claude Fable 5.2 | medium |
| Grok | Grok 4.7 | high |
| Muse | Muse Wonder Full 1.0 | high |

## Launching seats

Launch each seat through the route your harness supports for its model, with the reasoning level set explicitly. In T3 Code, resolve provider instances and option names through `orchestrator_capabilities`, then launch with `delegate_task`, passing the reasoning level in `target.options`. Launch the Muse seat through Muse Code, not Pi. Drop a seat your harness cannot reach and name it in your report.
