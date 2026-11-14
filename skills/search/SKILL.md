---
name: search
description: Search a topic with a panel of models from different vendors, then merge their findings and rank the top 3 sources.
disable-model-invocation: true
---

# Search

Each vendor's search reaches different corners of the web. Grok reads X.com posts but cannot reach Reddit; the others reach Reddit but not X. A panel of independent seats covers each other's blind spots, and a source several seats find on their own is a strong signal.

## 1. Launch the panel

Seats:

| Seat | Model | Reasoning |
|---|---|---|
| Codex | GPT-6.1 Sol | high |
| Claude | Claude Opus 5.5 | high |
| Grok | Grok 4.7 | high |
| Muse | Muse Wonder Full 1.0 | high |

In T3 Code, resolve provider instances and option names through `orchestrator_capabilities`, then launch every seat concurrently with `delegate_task`, passing the reasoning level in `target.options`. Launch the Muse seat through Muse Code. Elsewhere, use the route your harness supports for each model. Drop a seat your harness cannot reach and name it in the report.

Give every seat the identical brief:

```
Search the web for: <the user's topic, verbatim, plus any scope they gave>

Use your own web and search tools. Cover every source type that bears on the topic: official docs and announcements, news, X.com posts, Reddit and forum threads, GitHub issues, blogs. You work alone and read-only: search, read, and answer; edit no files and start no subagents.

Return Markdown with:
1. Findings: the answer to the topic as concrete claims, each citing the sources behind it.
2. Sources: every source you relied on, one per line, as `URL | title or author | date | what it says about the topic`.
3. Unreachable: source types or sites you tried and could not reach.
```

Done when every launched seat has returned or failed. Wait without a timeout. A seat that errors or returns no sources counts as failed; keep its error for the report.

## 2. Compile

1. Merge the seats' Sources into one list keyed by canonical URL: drop tracking parameters and fragments, and treat `twitter.com` and `x.com` as one host.
2. For each source, count the seats that cited it and judge its relevance: how directly it answers the topic, and whether it is a primary source (the author, vendor, or person the claim is about).
3. Pick the top 3: sort the relevant sources by seat count, break ties by relevance, and leave out any source that does not address the topic even if many seats cited it.
4. Write the answer from the merged Findings. Where seats disagree, say which seats claimed what, and side with the claim the stronger sources back.

Done when every seat's sources are in the merged list and every claim in the answer traces to a source.

## 3. Report

Reply in chat:

- The answer, in prose.
- **Top 3 sources**: link each, say in one clause what it is, and give its seat count (for example, "3/4 seats").
- One line naming any dropped or failed seat and its error, and any source type no seat reached.
