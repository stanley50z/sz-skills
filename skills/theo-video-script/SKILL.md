---
name: theo-video-script
description: Help the user write their own tech video script the way Theo (t3.gg) builds his, with guiding questions and a placeholder scaffold, or check a draft they wrote.
disable-model-invocation: true
---

# Theo-style video script helper

A Theo video is a stance backed by first-hand evidence, delivered in a fixed skeleton. The skeleton and the moves are in [`PATTERNS.md`](PATTERNS.md). The user writes every spoken line. You build what surrounds those lines: questions that draw out what the user knows, and placeholders that say what each spot in the script needs, so the user can write it in their own voice.

Ask your questions and write placeholders in the language the user will speak. The quotes in `PATTERNS.md` show how a move works. When the user is stuck on a move, point them to the matching quote and ask the question that gets their version of it.

## Placeholders

A placeholder marks one spot the user will fill:

```
[Move · length: guiding question or instruction. What the intake already gives.]
```

- **Move.** The job of the spot, named after `PATTERNS.md`: segment, hook number, stance, stake, read and react, concession, own mistake, hidden variable, emotion, segment verdict, open loop, payoff, comment question, sign-off.
- **Length.** In lines or words, taken from the segment's word budget: "1 line", "2 to 3 sentences", "~250 words".
- **Guiding question or instruction.** One question whose answer is the line, asking for something concrete the user saw, ran, paid for or felt. Use an instruction when the move needs one, such as which loop to tease.
- **What the intake gives.** The user's own facts that fit this spot, quoted from their answers or sources. Leave it off when nothing fits, so the question alone shows the gap.

```
[Segment · Source: the pricing post · ~400 words]
[Hook number · 1 line: Which figure from your test made you stop? You told me the run cost $412 over 3 days.]
[Emotion · 1 line: How did you feel when the agent deleted the branch?]
[Open loop · 1 line: Tease the webhook bug here. It pays off in the honesty block.]
[Segment verdict · 12 words max: If a viewer remembers one thing from this block, what is it?]
```

The user deletes each placeholder as they fill it. What remains is the script.

## Steps

### 1. Intake

Read what the user gave, then ask once for whatever is missing:

- **Trigger.** What happened and when, with the sources (links, posts, docs).
- **Stance.** Their view in one sentence, and what they believed before.
- **First-hand evidence.** What they ran, built, measured, paid for or broke, with numbers and units.
- **Screen material.** What they can show, including runs that failed.
- **Logistics.** Target runtime, speaking rate if known, their sign-off.

Done when each item has the user's answer or the user has said they have nothing for it. A missing item becomes a placeholder with no intake facts.

### 2. Read the sources

Read each source in full. For each one, list the passages worth reading aloud and every number in it.

Then pull the b-roll out of the sources, so the scaffold carries the material itself instead of a note about it:

- **Screenshots.** For each passage, chart, table or tweet the script will show, open the source with the `browser-harness` skill and screenshot that part. Save it as a PNG with a descriptive name (`aa-2025-12-29-gpqa-diamond.png`) in the folder the script goes in, or in the attachments folder the user names.
- **Links.** Record the exact URL of each page, post or video the script points at. Add `&t=<seconds>` to a YouTube link at the moment you cite. For a page that may change, use its web.archive.org snapshot.

Done when every source has its passage list, and every visual the script will need is a saved screenshot or an exact link.

### 3. Frame

Pick the video type from the sample table in `PATTERNS.md`, read its body order, and read the breakdown of the one or two nearest videos. The breakdowns record Theo's sponsor reads and his money and access disclosures. Leave both out of the user's scaffold.

Ask the user these five questions in one message. Under each, list the candidates the intake and sources point to (two numbers that could be the hidden variable, say), and let the user pick one or answer in their own words:

- **Thesis.** What is the one claim the video makes?
- **Turn.** What does the viewer expect, and what will you argue instead?
- **Axis.** What two-sided model will you judge the subject on?
- **Hidden variable.** Which number or factor is everyone else looking past?
- **Verdict.** Who should use it, for which job, at what cost?

Run the four topic tests in `PATTERNS.md` against the answers. When one fails, tell the user which and ask what would fix it.

Done when the user has answered all five and every topic test passes.

### 4. Outline

Build a segment table with job, what the segment needs from the user, and word count. Jobs are hook, lead-in, source, show, zoom out, honesty block, verdict, close. The word budget is runtime times the user's speaking rate, or 150 words per minute when unknown. Shares of runtime follow the skeleton table in `PATTERNS.md`.

- Body blocks alternate between source, show and zoom out, each one to six minutes.
- Each open loop is written next to the segment that pays it off.
- The honesty block sits at 75 to 90% of runtime, before the verdict.
- A video over 40 minutes gets a spoken roadmap and one long story with a twist in its second half.

Done when the word counts sum to the budget and every open loop has a payoff segment.

### 5. Scaffold

Write the scaffold to a file in the folder the script goes in, in segment order: hook, lead-in, body, honesty block, verdict, close. Each segment opens with a segment placeholder naming its job, content and word count, then holds, in the order they will be said:

- Placeholders for every line of the step 6 checklist that applies to the segment. The hook gets the subject, hook number, stance, stake and withheld thing; every segment ends on a segment verdict placeholder.
- For each source passage the user will read: its screenshot or link, the passage quoted word for word as the source has it, then a read and react placeholder that asks whether the user's evidence agrees, doubts or contradicts it.
- The visuals and links from step 2, where they go on screen.

Done when every checklist line has a placeholder in the segment that owns it, every open loop placeholder names its payoff, and the placeholder lengths sum to the word budget.

### 6. Check the draft

When the user brings back a filled or partly filled draft, run this checklist. For each line that fails, quote the passage and answer with a guiding question or a placeholder showing what the spot needs. The user writes the fix.

1. The first 30 seconds name the subject and state the stance.
2. The hook carries one hard number or concrete surprise and the user's personal stake.
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
13. Every placeholder is filled or deleted.
14. Every visual taken from a source is an embedded screenshot or an exact link. No bracket note describes a source that could have been extracted.
15. Read aloud, each sentence can be said in one breath or breaks at a natural pause.

## Output format

The finished script is plain text the user will say, in paragraphs, the way their past scripts read, with no title, headings or timestamps. Besides the spoken lines it holds only:

- An embedded screenshot on its own line, between paragraphs, where it goes on screen: `![|300](aa-2025-12-29-gpqa-diamond.png)`. Images shown together share one line.
- A link, either inline on the words that cite it (`a [report](https://...) counted`) or as a link card on its own line (`[!Page title](https://...)`).
- A short bracket note for what has no source to extract: a sound cue (`[TV beep]`) or the user's own demo or a visual they will make.

The scaffold uses the same format, with placeholders standing where the spoken lines will go:

```
[Segment · Hook · ~200 words]
[Hook number · 1 line: Which figure made you stop? You told me $412 over 3 days.]
[Stake · 1 to 2 sentences: Why does this hit you personally?]

[Segment · Source: the launch post · ~400 words]
![|300](source-chart.png)
> "Passage quoted word for word from the source."
[Read and react · 1 to 3 sentences: Does your own run agree with this? Your intake says 24 of 36 claims failed.]
[Segment verdict · 12 words max: What should the viewer take from this block?]
```

Your reply carries the segment table, the five-question frame as the user answered it, and title prompts: the two or three title shapes from `PATTERNS.md` that fit the frame, each with the question that would fill it.

## Other requests

- **One part only** (titles, a hook, a topic shortlist). Run intake and frame, then scaffold that part.
- **Critique of an existing script.** Run step 6 against it.
