---
name: theo-video-script
description: Write or critique a tech video script built the way Theo (t3.gg) builds his.
disable-model-invocation: true
---

# Theo-style video script

A Theo video is a stance backed by first-hand evidence, delivered in a fixed skeleton. Take the skeleton and the moves from [`PATTERNS.md`](PATTERNS.md). The facts, the opinions and the voice come from the user.

Write in the language the user will speak. The quotes in `PATTERNS.md` show how a move works; write fresh lines in the user's language and in their own words.

## Steps

### 1. Intake

Read what the user gave, then ask once for whatever is missing:

- **Trigger.** What happened and when, with the sources (links, posts, docs).
- **Stance.** Their view in one sentence, and what they believed before.
- **First-hand evidence.** What they ran, built, measured, paid for or broke, with numbers and units.
- **Screen material.** What they can show, including runs that failed.
- **Logistics.** Target runtime, speaking rate if known, their sign-off.

Done when every first-person line the script will need traces to the intake or a supplied source. Where the user has nothing to give, the script carries `[NEED: what would fill this]` in that spot.

### 2. Read the sources

Read each source in full. For each one, list the passages worth reading aloud, every number, and the user's reaction to each passage: agrees, doubts, or contradicts it with a named piece of their evidence.

Then pull the b-roll out of the sources, so the script carries the material itself instead of a note about it:

- **Screenshots.** For each passage, chart, table or tweet the script will show, open the source with the `browser-harness` skill and screenshot that part. Save it as a PNG with a descriptive name (`aa-2025-12-29-gpqa-diamond.png`) in the folder the script goes in, or in the attachments folder the user names.
- **Links.** Record the exact URL of each page, post or video the script points at. Add `&t=<seconds>` to a YouTube link at the moment you cite. For a page that may change, use its web.archive.org snapshot.

Done when every source has its passage list, and every visual the script will need is a saved screenshot or an exact link.

### 3. Frame

Pick the video type from the sample table in `PATTERNS.md`, read its body order, and read the breakdown of the one or two nearest videos. The breakdowns record Theo's sponsor reads and his money and access disclosures. Leave both out of the user's script. Then write one line each:

- **Thesis.** The central claim.
- **Turn.** What the viewer expects against what the user will argue.
- **Axis.** A two-sided model the subject gets judged on.
- **Hidden variable.** The number or factor everyone else is looking past.
- **Verdict.** A placement: who should use it, for which job, at what cost.

Run the four topic tests in `PATTERNS.md`. When one fails, tell the user which and what would fix it, and wait for their answer.

### 4. Outline

Build a segment table with job, one-line content and word count. Jobs are hook, lead-in, source, show, zoom out, honesty block, verdict, close. The table is a working note for planning and stays out of the script. The word budget is runtime times the user's speaking rate, or 150 words per minute when unknown. Shares of runtime follow the skeleton table in `PATTERNS.md`.

- Body blocks alternate between source, show and zoom out, each one to six minutes.
- Each open loop is written next to the segment that pays it off.
- The honesty block sits at 75 to 90% of runtime, before the verdict.
- A video over 40 minutes gets a spoken roadmap and one long story with a twist in its second half.

Done when the word counts sum to the budget and every open loop has a payoff segment.

### 5. Write

Write the full script in the output format below, in this order: hook, lead-in, body, honesty block, verdict, close. Write every spoken line out. For a passage the user will read from a source, embed its screenshot, then write the spoken version of the passage (translated into the user's language when the source is in another) and the reaction lines that follow it.

### 6. Check

Every line below holds before the script goes to the user. Fix the script where one fails.

1. The first 30 seconds name the subject and state the stance.
2. The hook carries one hard number or concrete surprise from the intake and the user's personal stake.
3. The hook withholds one thing (the why, the method or the verdict) and a later segment pays it off.
4. Where the title overclaims, the first two minutes say so.
5. Every claim read from a source is followed by the user's own number, experience, or explicit agreement.
6. One hidden-variable moment exists.
7. A concession comes before each major criticism, and a limit follows each major praise.
8. The user's own mistake or change of mind appears, when the intake has one.
9. Every open loop is paid off.
10. Each segment ends on a verdict line of 12 words or fewer.
11. The verdict is a placement, split by viewer type where viewers differ.
12. The close has a question for the comments and the user's sign-off.
13. Every first-person fact traces to the intake. Gaps are `[NEED]` cues.
14. Every visual taken from a source is an embedded screenshot or an exact link. No bracket note describes a source that could have been extracted.
15. Read aloud, each sentence can be said in one breath or breaks at a natural pause.

## Output format

The script is plain text the user will say, in paragraphs, the way their past scripts read. It has no title, metadata header, headings, segment table or timestamps. Put the five title options (each a different shape from `PATTERNS.md`) and the one-line frame in your reply, outside the script.

Only three kinds of non-spoken material appear inside the script:

- An embedded screenshot on its own line, between paragraphs, where it goes on screen: `![|300](aa-2025-12-29-gpqa-diamond.png)`. Images shown together share one line.
- A link, either inline on the words that cite it (`a [report](https://...) counted`) or as a link card on its own line (`[!Page title](https://...)`).
- A short bracket note for what has no source to extract: a sound cue (`[TV beep]`), the user's own demo or a visual they will make, or a `[NEED: what would fill this]` gap.

```
Hook line.

Spoken paragraph.
![|300](source-chart.png)![|300](source-table.png)
Spoken paragraph that cites a [post](https://...) inline.
[!Video title](https://www.youtube.com/watch?v=...&t=384s)
Spoken paragraph.

Closing question for the comments. Sign-off.
```

The user adds their own images and links to the script afterwards.

## Other requests

- **One part only** (titles, a hook, a topic shortlist). Run intake and frame, then deliver that part in the same format.
- **Critique of an existing script.** Run the step 6 checklist against it. Report each failed line with the offending passage and a rewrite.
