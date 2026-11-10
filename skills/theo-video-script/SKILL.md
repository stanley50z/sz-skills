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
- **Disclosures.** Money, access, or products of their own that touch the topic.
- **Logistics.** Target runtime, speaking rate if known, their sign-off.

Done when every first-person line the script will need traces to the intake or a supplied source. Where the user has nothing to give, the script carries `[NEED: what would fill this]` in that spot.

### 2. Read the sources

Read each source in full. For each one, list the passages worth reading aloud, every number, and the user's reaction to each passage: agrees, doubts, or contradicts it with a named piece of their evidence.

Done when every source has that list.

### 3. Frame

Pick the video type from the sample table in `PATTERNS.md`, read its body order, and read the breakdown of the one or two nearest videos. Then write one line each:

- **Thesis.** The central claim.
- **Turn.** What the viewer expects against what the user will argue.
- **Axis.** A two-sided model the subject gets judged on.
- **Hidden variable.** The number or factor everyone else is looking past.
- **Verdict.** A placement: who should use it, for which job, at what cost.

Run the four topic tests in `PATTERNS.md`. When one fails, tell the user which and what would fix it, and wait for their answer.

### 4. Outline

Build a segment table with start time, job, one-line content and word count. Jobs are hook, lead-in, source, show, zoom out, honesty block, verdict, close. The word budget is runtime times the user's speaking rate, or 150 words per minute when unknown. Shares of runtime follow the skeleton table in `PATTERNS.md`.

- Body blocks alternate between source, show and zoom out, each one to six minutes.
- Each open loop is written next to the segment that pays it off.
- The honesty block sits at 75 to 90% of runtime, before the verdict.
- A video over 40 minutes gets a spoken roadmap and one long story with a twist in its second half.

Done when the word counts sum to the budget and every open loop has a payoff segment.

### 5. Write

Write the full script in the output format below, in this order: hook, lead-in, body, honesty block, verdict, close. Write every spoken line out. For a passage the user will read from a source, write a `[READ]` cue and then the reaction lines that follow it.

### 6. Check

Every line below holds before the script goes to the user. Fix the script where one fails.

1. The first 30 seconds name the subject and state the stance.
2. The hook carries one hard number or concrete surprise from the intake and the user's personal stake.
3. The hook withholds one thing (the why, the method or the verdict) and a later segment pays it off.
4. Where the title overclaims, the first two minutes say so.
5. Disclosures come before the first argument.
6. Every claim read from a source is followed by the user's own number, experience, or explicit agreement.
7. One hidden-variable moment exists.
8. A concession comes before each major criticism, and a limit follows each major praise.
9. The user's own mistake or change of mind appears, when the intake has one.
10. Every open loop is paid off.
11. Each segment ends on a verdict line of 12 words or fewer.
12. The verdict is a placement, split by viewer type where viewers differ.
13. The close has a question for the comments and the user's sign-off.
14. Every first-person fact traces to the intake. Gaps are `[NEED]` cues.
15. Read aloud, each sentence can be said in one breath or breaks at a natural pause.

## Output format

```
# <working title>

Titles: five options, each a different shape from PATTERNS.md
Type: <type> · <runtime> · <word budget> words
Thesis: ...
Turn: ...
Axis: ...
Hidden variable: ...
Verdict: ...

| Time | Job | Content | Words |
|---|---|---|---|

## 00:00 Hook

[SCREEN: what the viewer sees]
Spoken lines.

## 01:40 Source: <name>

[READ: <source>, from "first words" to "last words"]
Reaction lines.
[DEMO: what to run, what to watch for, what to say if it fails]
[NEED: what would fill this]
```

## Other requests

- **One part only** (titles, a hook, a topic shortlist). Run intake and frame, then deliver that part in the same format.
- **Critique of an existing script.** Run the step 6 checklist against it. Report each failed line with the offending passage and a rewrite.
