---
name: council
description: Run a task through a panel of models from different vendors, then combine their results. Use when the user says "council".
---

# Council

Models from different vendors bring different training, judgment, and tools. Grok's search reads X.com posts but cannot reach Reddit; the others reach Reddit but not X. A panel of independent seats covers each other's blind spots, and a point several seats reach on their own is a strong signal.

## 1. Launch the panel

Read [MEMBERS.md](MEMBERS.md) for the rosters and how to launch each seat. Seat the Default roster. Seat the Max roster only when the user explicitly says "council max". Seats the user names replace either roster. Launch every seat concurrently.

Give every seat the identical brief. Seats see none of this conversation, so the brief carries everything the task depends on:

```
<the user's task, verbatim, plus any scope they gave>

Context: <files, links, prior decisions, and constraints from this conversation that the task depends on>

You are one seat on a panel of models from different vendors, each doing this task alone. Use your own tools. When the task needs the web, cover every source type that bears on it: official docs and announcements, news, X.com posts, Reddit and forum threads, GitHub issues, blogs. Work read-only: edit no files and start no subagents. If the task asks for a change, return it as a proposal (the text, diff, or plan itself).

Return Markdown with:
1. Result: your answer to the task, with the reasoning or evidence behind each point.
2. Sources: every source you relied on, one per line, as `URL or path | title or author | date | what it showed`.
3. Gaps: what you tried and could not reach or verify.
```

Done when every launched seat has returned or failed. Wait without a timeout. A seat that errors or returns no result counts as failed; keep its error for the report.

## 2. Combine

1. Line up the seats' results point by point. Mark each point as shared (several seats reached it), unique (one seat found it), or contested (seats contradict each other).
2. Check every unique and contested point against its sources before keeping it. Where seats disagree, side with the stronger evidence.
3. Build one result from the best of each seat: the shared points, plus the unique ones that survived the check.
4. Merge the seats' Sources into one list keyed by canonical URL: drop tracking parameters and fragments, and treat `twitter.com` and `x.com` as one host. Count the seats that cited each source.

Done when every seat's points are accounted for: each one is in the combined result, or dropped with a reason.

## 3. Deliver

If the task asks for a change (code, a document, a file), make it now from the combined result.

Then reply in chat:

- The combined result, in prose.
- **Disagreements**: for each contested point, which seats claimed what, and which side you took and why.
- **Top 3 sources**, when the task gathered sources: rank relevant sources by seat count, break ties by how directly each answers the task and whether it is primary. Link each, say in one clause what it is, and give its seat count (for example, "3/4 seats").
- One line naming any dropped or failed seat and its error, and any gap no seat covered.
