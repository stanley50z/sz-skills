# Theo (t3.gg) structural reading, group A

Five videos, read end to end from auto-captions. Timestamps are the `[mm:ss]` paragraph starts in the transcript, so a quote may fall up to ~30 s after the stamp. Chapter times come from the file headers. "Inferred" marks anything about the picture that I deduced from speech.

Caption fixes used throughout (applied lightly inside quotes):

- Sponsor links appear as "swyd.link", "soy.link", "selective.link", "swyx.io", "soda.link". All are `soydev.link/<sponsor>` per the descriptions.
- "codeex / codecs" = Codex; "cloud code / Quad Coder" = Claude Code; "Soul" = Sol (GPT-5.6 Sol); "Grock" = Grok; "Hebo / Tibo" = Tibo (the OpenAI Codex lead Theo usually names). "Jeff aka FaZe" is probably his editor, credited as @Ph4seon3 ("Phase"); that one is a guess.
- Bleeped profanity shows up as `[\h__\h]` or as a missing word ("grill the out of me"). I mark those `[bleep]`.

Speaking rate across all five is ~200-220 words per minute (7,686 words in 38:21; 9,665 in 44:12; 14,419 in 66:36; 6,876 in 31:47; 5,035 in 25:27).

---

## 1. "So I tried Matt's skills..." (0oXOOlqVu5M, 38:21, uploaded 2026-08-19)

### Topic and angle

He reviews two published sets of agent skills: Matt Pocock's `mattpocock/skills` (200k+ stars) and "pstack" by Lauren, aka "Potato", a former React core member now at Cursor. Captions spell it "Pee Stack / P stack / P-Skill / Pystock". The description links `cursor/plugins/tree/main/pstack`. "Potato" is almost certainly the handle "poteto", which is my guess. What triggered it was long-running audience demand ("my whole Twitch chat is freaking out... Long overdue", 00:31) plus a week of his own use. The angle is "I dismissed these, then actually used them". The stance: never install skill packs blindly, read them and keep the parts that fit you. The surprise is that the best win was pstack's tiny `unslop` skill, not Matt's.

Title vs content: the title promises a verdict on Matt's skills, and the ellipsis signals ambivalence. The description admits the twist ("the biggest wins came from somewhere unexpected"). Matt's skills don't get serious attention until 12:17. The first ~9 minutes of real content are about pstack and unslop. The payoff for Matt lands at 28:01 ("I don't necessarily want this much prescription"). At 34:01 he says plainly that he is "much more philosophically aligned with what potato is cooking". He delivers on the title, but the verdict tilts toward the competitor.

### Hook (00:02-01:58)

> "There is one particular GitHub repo that I've been eyeing for a long time and just never took the time to dive into. It's by a person that I've interacted with a bunch in the past who, if you've been around for a while, I am sure you're familiar with. I've often called myself the second best TypeScript YouTuber, and the reason is because of this individual, the number one, Matt Pocock."

Mechanism:

1. It withholds the name for three sentences, then reveals it with a self-deprecating rank joke ("second best TypeScript YouTuber").
2. A number stake follows: "racked up over 200,000 stars on GitHub, making it one of the 10 most starred projects on all of GitHub. Truly insane. All for markdown files."
3. A confession sets up the "did my mind change?" arc: "I honestly kind of dismissed initially".
4. It widens to a second subject with a strong opinion: "The vast majority of these skill repos are absolute slop and should be ignored, but there is one other I'm excited about" (01:01).
5. Credential of effort: "I installed a bunch of the skills... I have went through and audited the majority of the skills in both of these suites".

What it withholds: which skills won, and what the "one other" verdict is.

### Lead-in

- Sponsor bridge (01:32): "I cannot wait to show show everything I've learned after a real quick break for today's sponsor."
- Depot read, chapter 01:58-03:14 (~76 s). It opens with a thematic framing that ties into the video ("Let's be honest with ourselves. We've moved past the era of doing one thing at a time."). Numbers follow ("up to 55 times faster", "up to 10 times faster"), then a self-correcting pivot inside the ad: "But that's not what I promised. I was talking about working in parallel, not just building in parallel." It closes on "Ship faster and unblock yourself at soydev.link/depot."
- Exit line (03:00): "Couple things I want to say up front before we go too deep into all of these skills". A ~60 s philosophy disclaimer follows: "you do not get anything out of blindly copying other people's setups... It's cringe and bad. It means you suck at engineering, period."
- Method disclosure (04:00-05:00): he reads out the prompt he used to have an agent audit his usage history across "this MacBook, left book [machine name, unclear], and BB1" and rank pstack skills. He admits a resource bias: "I had a bunch of Opus 5 to burn at the time".
- There is no formal roadmap. The tease "P stack is going to be the underrated gem in this" (04:00) does that job.

### Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:02-01:58 | Hook | Matt rank joke, star count, pstack introduced |
| 01:58-03:14 | Sponsor | Depot |
| 03:14-04:16 | Framing/thesis preview | Don't copy setups |
| 04:16-05:12 | Method | Agent-generated fit ranking of pstack skills |
| 05:12-09:23 | Read-and-react | Reads `unslop` SKILL.md aloud nearly in full. Tangent at 05:31: a skill description is "a trigger", like a YouTube thumbnail |
| 09:23-12:31 | Demo (A/B) | Same "what is this project" question with unslop (Codex/Sol in T3 Code) vs ChatGPT without skills; reads both aloud |
| 12:31-13:23 | Transition | "rabbit hole" explanation; runs the same audit on Matt's repo |
| 13:23-17:02 | Read-and-react | Lists Matt's engineering skills; explains `disable-model-invocation`; personal experience with diagnosing-bugs; reads grilling skill; m-dash rant |
| 17:02-19:50 | Demo | Grilling skill on his Lakebed project, Opus 5 vs Sol (low, then high), answering questions on camera |
| 19:50-21:47 | Read-and-react | teach, ask-matt, improve-codebase-architecture, wayfinder, wizard |
| 21:47-27:17 | Demo + workflow | Has his "fleet" repo agent install wizard on all machines; reads Matt's README flow; answers more grilling questions; reads an old sloppy agent thread aloud as contrast; T3 Code skill-manager idea |
| 27:17-31:16 | Critique | Matt's skills "prescribe mental workflows"; writing-for-agents read and judged "unreadable"; runs a text through an AI detector (inferred) |
| 31:16-35:01 | Read-and-react | pstack Arena, the "bro" skill credited to Dillon Mulroy ("bro" is a caption guess), blast-radius, show-me-your-work |
| 35:01-36:04 | Meta | "what you're getting instead is my actual process" |
| 36:04-38:21 | Recommendations + outro | Step list, don't fear editing `.claude`, sign-off |

Rough split: read-and-react on skill markdown ~45%, live demos ~30%, opinion/framing/recommendations ~15%, sponsor ~3%, hook ~5%.

### Thesis and arguments

Central claim: skill collections are worth mining, but you get value by reading them and taking the few that fit you. For him that was pstack's `unslop` first and Matt's grilling and wizard second.

Arguments in order:

1. Copying setups makes you a worse engineer (03:14). Supported by an analogy to copying a code template.
2. Small markdown can change agent output a lot. Supported by the unslop A/B, read aloud ("It's insane these both came from the same model for adding one markdown file", 12:00).
3. Some of Matt's skills are useful. Supported by the grilling demo producing questions he hadn't considered, and by diagnosing-bugs "over the last few days".
4. Matt's set is over-prescriptive and written in AI-sounding prose. Supported by an m-dash count and by reading writing-for-agents aloud.
5. pstack fits his day-to-day better, with one concession: "very much tied to cursor specifically, which is the biggest issue with P Stack" (32:30).

Concessions and admissions: "I honestly kind of dismissed initially"; "Okay, I'm seeing the light. This is useful. I should have tried this before" (19:30); "I should have been reading the docs the whole time. My bad" (22:31); "I feel like I am not going through this the right way" (20:02, on teach). He also finds that his preferred unslop skill is "allegedly AI" too (31:31). Bias disclosure: a long friendly history with Matt, and an "old favorite" relationship with Lauren. He frames it explicitly as not a contest: "I didn't want this to be like a one or the other thing" (34:01).

### Evidence

- Skill markdown read aloud line by line, with interjections ("Don't call me out like this", "No mention of load bearing sadly").
- Agent output read aloud as before/after comparison: an App Store Connect thread, the T3 Code description, and an old thread full of m-dashes ("Oh god, the M-dash how", 26:32).
- Live agent runs: grilling questions are read and answered.
- A counted figure: "There's nine m-dashes in this page" (15:31).
- An AI-detector result: "Cool, I passed 100% human written" (31:30). The detector is inferred; he seems to test his own text first.
- Personal usage claims: Arena "has cost me hundreds of dollars of inference"; blast-radius "caught a couple of things".
- His own products as test beds: T3 Code, Lakebed, the "fleet" repo.

About 45% is read-and-react on primary sources, the skill files and README. The rest is demo plus opinion.

### Demo

There are three, all on-stream and live, with chat reacting.

1. Unslop A/B (09:23-12:31, ~3 min). He starts a model choice, backs out ("Ah, it's going to take too long. I'm going to stick with Sol"), then asks ChatGPT the same question without skills and reads the "slop" aloud.
2. Grilling on Lakebed (16:01-19:50 and 24:00-25:30, ~5 min total). Setup: "copy-paste the text" instead of installing. He waits about 2 min (cut). He switches Sol from low to high mid-demo ("I just realized I use this on low and slow"). He answers questions on camera and mentions disagreeing with the recommended answers.
3. Wizard install via the fleet repo (21:47-27:50). He fires off the prompt, then returns: "Yep, the wizard skill has now appeared on all of my machines. Yay."

Dead ends stay in: the teach-skill confusion, the docs he should have read, the abandoned Opus run.

### Retention devices

- Open loop at 04:00 ("P stack is going to be the underrated gem"), paid off at 31:16-35:01.
- Running m-dash gag: 08:00, 15:31 ("Matt. Matt."), 26:32, 30:00 ("I almost want to make a d-m-dashed Matt Pocock skills fork"), 30:30 ("Too many m-dashes still").
- Twitch chat as a second voice: "I see my chat realizing that potato was one of the builders of the React compiler" (04:00); "Chat saying that it's a good thing to point out how good the semantic density is here" (08:00).
- Spoiler framing: "I guess here I'll give you the spoiler of how I actually set up all of these things" (21:30).
- Future-video tease: "simplified technical English, which a dedicated video on this bit coming in the near future" (29:02).
- Callback to a past video: "as I mentioned before in my like markdown overhaul video" (05:31).
- Self-deprecation: "Don't call me out like this" (07:31, after reading "agents churning away at 3:00 a.m.").
- Mild exasperation as a pattern break: "This gets deep. I don't want to answer these questions. That's the point, isn't it?" (24:00).

### Ending

At 35:01 he lands on a process lesson rather than a ranking: "This video is supposed to be an overview, but what you're getting instead is my actual process." He admits the format didn't fully work: "God, that this video could be hours long or it could be a 45-second short... It isn't quite what I expected it or wanted it to be" (35:32). Then comes a numbered how-to: have your agent survey pstack and Matt's skills against your history, install unslop first, read the markdown before installing, keep a single skills repo, don't be afraid to edit `.claude` and `.agents`. A personal proof point: "It's a huge part of why I was able to ship so many PR's with so little breakage over the last weekend." The repeated imperative refrain: "Don't blindly install them. Poke around at them. Try them out. Pull the parts you like. Ignore the parts you don't. Play." The CTA: "I'm curious how this affects your workflows. Let me know." Sign-off: "And until next time, peace, nerds."

### Voice

1. "Truly insane. All for markdown files." (00:31)
2. "It's cringe and bad. It means you suck at engineering, period." (03:30)
3. "I see it kind of similar to a YouTube video thumbnail, where the role of the thumbnail isn't to accurately encapsulate everything that the video has in it." (05:31)
4. "It shouldn't be called a description, it should be called a trigger." (06:00)
5. "All of these standards were written in the old Anthropic days before anyone knew what the [bleep] they were doing. We're stuck with it. It is what it is." (06:00)
6. "Anyways, let's take a look at what the skill's actual content is." (06:00), a typical return-from-tangent transition.
7. "So, again, if you're not familiar with how skills work, they have a name and a description." (06:00), a beginner on-ramp.
8. "God. I didn't realize how quickly I adjusted to unslop text. And now when I read the slop text, it hurts me." (11:00)
9. "God, why is he using m-dashes in his skills? Matt. Matt." (15:31)
10. "it will grill the [bleep] out of me momentarily." (17:01)
11. "These are actually good questions. And now I'm curious, do we get similarly good questions if I ask a different model?" (17:31)
12. "Okay, I'm seeing the light. This is useful. I should have tried this before." (19:30)
13. "This little fleet repo saved my ass so many times." (24:00)
14. "God, life post slop is unbelievably cool." (27:01)
15. "This is unreadable. I mean, I'm not surprised, but god damn. Ow." (31:00)
16. "I'm much more philosophically aligned with what potato is cooking over here." (34:01)

Register: casual and spoken, with long run-on sentences broken by short verdicts ("Truly insane.", "Cool.", "Ow."). "God" works as an interjection 11 times. Mild profanity, with heavier words bleeped. Technical explanation comes as quick asides that assume a coding audience but define one concept when it matters (how skills load, what `disable-model-invocation` does).

---

## 2. "It's Here." (XFWpf0wLbh0, 44:12, uploaded 2026-09-04)

### Topic and angle

A launch-day reaction to GPT-6 "Astra" from OpenAI, after weeks of early access. The trigger is a model release plus embargo lift. His stance: the best model ever, a generational leap ("GPT 5.6 felt like the best possible version of a last-gen game whereas Fable 5 felt like a reasonable version of a next-gen game. GPT-6 is the next gen", 01:01). Its special qualities are computer use, 3D, and long-horizon agentic work, not front-end design. Rough edges stay in. He also complains loudly that it is "announced" but not actually available.

Title vs content: "It's Here." names nothing. The description and thumbnail (unseen) presumably carry the name. The video reveals it at 00:30 and pays the title off at once. The wider promise, that the model everyone waited for has arrived, is met by the closing "Is it the best model ever? I think I'm comfortable saying yes" (42:00). It is also undercut: "you can't use it yet, which is stupid" (43:30).

### Hook (00:01-01:35)

> "There's a model we've all been waiting for for quite a while now, and it's finally here. This is where I want to make a joke about how it's Gemini 3.8 Flash, but my new retention guy said I'm not allowed to. He instead said I should just show you guys this, my actual usage with said models. Of course, my terminal is refreshing right when I pick it up... But the point I'm trying to make is I've done about $330,000 of inference over the last few weeks and the vast majority of it has been with the model that we're here to talk about today."

Mechanism:

1. The model name stays withheld through ~25 s.
2. A meta joke about his own retention coaching.
3. An on-screen usage dashboard (inferred) with a shock number as the credential.
4. The reveal, "GPT6 Astra. Yes, it's actually getting the six moniker".
5. Escalating superlatives ("truly is revolutionary", "massive leap", "feel generational").
6. An immediate turn: "but it also still has its rough edges... That is far from the whole story".
7. A spoken roadmap: "availability, cost, security, safety, how it actually works in the day-to-day... all the fun things I've been building with it, as well as the weird restrictions".

The hook promises a balanced verdict and holds back the rough edges.

### Lead-in

- Bridge (01:30): "I can't wait to show you guys what this model can do after a real quick break for today's sponsor."
- CodeRabbit read (~01:35-02:58, ~80 s). It opens with "You've heard me talk about today's sponsor before... But that's not what I want to talk about", the same "that's not the point" ad turn as Depot. It includes a personal anecdote (he reported bugs, and their Slack agent fixed them). It closes on "Ship with more confidence and less bugs at soydev.link/coderabbit."
- Exit (03:00): "I'm going to be so incredibly real with you guys. I could probably go off for five plus hours about this model". Scope-setting follows, plus a structural callback: "I like the way I structured the Fable 5.1 video, so I'll do my best to honor a lot of that here".
- Disclosures spread through the video: early access, OpenAI "politely requested" he not use Astra for open-source code (32:00), OpenAI staff conversations ("I do have confirmation from people at OpenAI", 07:31), Sam Altman asking about his Claude Code/Codex split (40:00), and AI review bot sponsors ("I don't know if any of them are sponsoring this video", 36:31).

### Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01-01:35 | Hook + roadmap | $330k usage reveal, "generational" |
| 01:35-02:58 | Sponsor | CodeRabbit |
| 02:58-03:20 | Framing | Scope, reuses Fable 5.1 structure |
| 03:20-05:30 | Facts: cost | $10/$50 per M, fast mode 2x/2x, token efficiency, cached reads $1 vs Fable's $0.25, >272K context surcharge (2x in, 1.5x out), Codex exception |
| 05:30-08:01 | Facts + rant: availability | Staged rollout "sucks"; ZDR; API + Bedrock, no Azure; Tibo's banked resets; speculation on cause |
| 08:01-11:31 | Benchmark walkthrough | Terminal Bench science (Fable 5.1 medium $15/36% vs Astra low $11/54%), ARC-AGI "malicious" bench now 99.9%, FrontierMath, another bench (caption "Turtle Bench 4", unclear), ARC creator quote, "the model isn't actually learning" clarification |
| 11:31-14:30 | Claim + evidence: computer use | Honeypot 0% vs Sol ~50%; "two or three" generations ahead; OSWorld 2.0 23 min/71.6% vs Sol ~1h15/65.7%; OpenAI Excel demo video (inferred); his medical-records anecdote (15 min, ~150 pages); BenchCAD |
| 14:30-18:00 | Demo: 3D | Slides demo doesn't match his experience; Blender to Unreal house; his 3D fish game, with flawed controls |
| 18:00-21:01 | Release-notes read + experience | Async questions (plugs T3 Code nightly), steering, restraint vs Sol; DeepSWE 74.1%; Gemini 3.8 Flash tangent |
| 21:01-22:58 | Benchmarks | Science, ExploitBench 100% on low, alignment stats; Fable 5.1 "copying Astra code from my machine" |
| 23:00-24:31 | Rebuttal of a bench | Artificial Analysis ties it with Muse Spark/Grok; he calls the bench stale, and its founder agreed with his tweet |
| 24:31-27:31 | Weakness: front end | 2D fish slop with 20+ all-caps subtitles; landing-page compare site in versus mode; "Fable 5 tier"; still prefers Anthropic for UI |
| 27:31-30:20 | Others' demos | Minecraft clone (Flavio), open-world game (Peter), Matthew Berman, Matt Shumer's Manhattan, Max Weinbach's macOS clone |
| 30:20-35:30 | His real builds | Spotify-style player, Plex clone (5 prompts usable, 8 to beat competitors), Lakebed perf (800 ms to <30 ms, P95 -98%) in two prompts; video-editing failure; editor shout-out; subscribe ask |
| 35:30-40:30 | Failure case study | Scroll-bug PR thread: agrees review comments are valid but doesn't act; ignores babysit skill; overengineering; Codex threads linger |
| 40:30-44:12 | Conclusion | Meme, "feels a bit like AGI", Gmail/Notion life triage, "best model ever", "where is your bar?" |

Rough split: release notes and benchmarks ~45%, demos (theirs, his, others') ~30%, his failure story ~11%, cost/availability ~10%, sponsor ~3%.

### Thesis and arguments

Central claim: Astra is the best model ever. It isn't the best coder. It is so far ahead on computer use, 3D, and long agentic work that it "starts to feel a bit like AGI" (40:30).

Order: cost first ("we need to start with the cost and availability", 03:00), then availability, benchmarks, then the novel strengths (computer use, then 3D), interaction quality, science and security, then a dismantled bench, weaknesses (front end), demos, his real usage, the failure case, and the verdict. He builds from objective facts to escalating wonder, inserts weaknesses before the demo high, then puts the most damaging story late but before the verdict.

Counterweights:

- Speed: "this model, I'll be frank, can be slow" (03:30).
- Slides: "skill issue me all you want. I did not think this demo reflected my real world usage" (15:00).
- Controls: "Astra did not even come close" (17:01).
- Front end: "I still much prefer Anthropic for front end" (27:31).
- Editing: "I don't think this model can actually video edit" (35:01).
- Instruction following: the failure story, then "Thankfully, OpenAI agrees and they have since made changes" (39:01).
- Overengineering: "Nowhere near as bad as Soul".

Hedges on speculation: "Could be government, could be something weird with their compute layer... I honestly, I'll be real. kind of thinking it's Microsoft, but we don't know" (07:31). Bias admissions: "I'm admittedly biased. I think mine are cooler" (15:31), and his own products throughout. He defers the comparison verdict to a future video several times.

### Evidence

- The OpenAI release post, read and paraphrased section by section ("The next section of the article calls out...", 18:00; "That's it for OpenAI's coverage", 22:31).
- Benchmarks with exact numbers and costs. Cost per score is his favored framing ("Intelligence per dollar"). He spots anomalies: xhigh/max scoring below high, and "For some reason, high was cheaper than low. I don't know if this is an issue in how they made this table".
- A quoted statement from the ARC-AGI creator.
- A tweet referenced: Tibo's banked resets.
- Third-party bench criticism, backed by a private exchange: "the founder of artificial analysis replied to my tweet... largely agreeing".
- Community demos credited by name with mini-bios ("Flavio is the bouncing ball and hexagon guy").
- Personal builds with metrics (Lakebed latency) and prompt counts.
- His own usage dashboard.

About 45% is source-react. The rest is first-person experience, which is the differentiator he leans on.

### Demo

These are mostly prepared clips and artifacts. Some navigation is live (clicking through the compare site in versus mode, double-clicking in the macOS clone "in Zen, which isn't even a Chromium based browser"). The fish game is played on camera with a live slip left in: "Oh, wait, no. This is the Opus 5 version. This is what it actually created" (16:00). He leaves failures in on purpose: janky controls, cringe shorts cuts, and the four-and-a-half-minute PR thread where the model "said 'Yeah, I should do that.' And then didn't" (38:30). The failure is framed as a duty: "I do feel obligated to show you some of the painful experiences" (35:30).

### Retention devices

- Withheld name in the hook plus a meta retention joke (00:01).
- Teases for later sections: "We'll talk about that in just a second" (00:30); "We'll talk plenty about that in just a bit" (03:30); "I will show you guys some of it in action in a bit, but for now, I just need you to trust me" (11:31); "Don't worry though if you're here for the real world use or more importantly the rough edges... We'll get to all of that right after the demos" (27:31).
- Future-video loops: the Fable 5.1 vs Astra video is promised four times (19:01, 19:30, 40:00, 42:00), plus a swarms video (34:30), a deeper builds video (30:20), the TypeScript-to-Rust port (35:30), Gemini 3.8 Flash (20:30), and the unanswered Sam Altman 90/10 question (40:00).
- Subscribe asks tied to future value (35:30, 42:00).
- Jokes and pattern breaks: "Center div bench coming soon" (30:00); "[groaning]" at Artificial Analysis (23:00); Matt Shumer "had his computer nuked by Soul".
- Comment pre-emption: "I am sorry to anybody who thinks this is acceptable behavior. You're just not shipping hard enough" (39:01).
- Callback: last-gen/next-gen game framing from earlier videos.

### Ending

The wrap starts at 40:30 by reframing "best coder" discourse with a meme he posted. Then comes a cumulative list sentence: "from its genuinely groundbreaking computer use... to its absurd level of 3D... to the way it can use swarms... to the absurd productivity wins". A fresh personal anecdote follows (Gmail and Notion triage while his assistant was out). The verdict: "Is it the best model ever? I think I'm comfortable saying yes there." The analogy: "It almost feels like an iPhone type change". It ends on a rhetorical question to the viewer instead of a recommendation: "My question to you isn't is this model great or not? Especially because you can't use it yet, which is stupid. My question to you is where is your bar? At what point are you going to stop checking the work the model does constantly and let it do its thing?" Sign-off (captioned "these nerds"): "This feels like a taste of something new and I cannot wait for you guys to see it as well. So until next time, peace nerds."

### Voice

1. "This is where I want to make a joke about how it's Gemini 3.8 Flash, but my new retention guy said I'm not allowed to." (00:01)
2. "OpenAI has done it. This model is incredible, but it also still has its rough edges." (01:01)
3. "I'm going to be so incredibly real with you guys." (02:58), his standard transition out of the ad.
4. "As you can guess, it's an OpenAI model, so it's insanely efficient." (04:01)
5. "That sucks. It just It just sucks. I hate this." (06:00)
6. "Yeah, it is what it is." (07:31)
7. "Enough yapping. Let's actually take a look at what this model can do." (08:01)
8. "I'm going to be real with you guys. I thought this bench was malicious." (09:02)
9. "If you care a lot about computer use, there is nothing even close." (11:31)
10. "And it makes anthropic models almost feel like they're in the stone age." (12:01)
11. "But uh yeah, skill issue me all you want." (15:00)
12. "I'm admittedly biased. I think mine are cooler." (15:31)
13. "It's It's unbelievable the quality of the things it rendered here." (16:30)
14. "Let's finish getting through these release notes so we can get to the other fun parts." (21:01)
15. "Okay, you guys get the idea. It's good at 3D. What about everything else?" (29:32)
16. "it's all cringe and bad... no offense, they are not worth trusting when it comes to video editing." (35:01)
17. "I am sorry to anybody who thinks this is acceptable behavior. You're just not shipping hard enough." (39:01)

Register: high-energy superlatives. "Slaughter" appears 7 times, "absurd" 8, "insane" 10. These are paired with precise prices and percentages, so the hype always has a number attached. Profanity is light here. For jargon he gives a one-clause gloss: "Bench CAD, which is using Python to do some CAD work"; "the model isn't actually learning. It's not like the weights are adjusting".

---

## 3. "If you have a Claude sub, watch this" (D8PikZ1KhUo, 66:36, uploaded 2026-10-02)

### Topic and angle

A long tutorial-manifesto on "agent maxing" or "token maxing". It covers how to get many subsidized Claude and Codex subscriptions, route them through one residential-IP proxy (CLI Proxy API, his fork) over Tailscale, and fire off many parallel threads, mostly through his own T3 Code. The trigger is personal practice, a sequel to "my first token maxing video" (12:41). The angle is transgressive and conspiratorial: "This is the video that Anthropic does not want you to watch" (00:30), with the mindset "Burn your tokens" (28:31).

Title vs content: the title targets Claude subscribers and promises useful info. Claude-specific material appears in pieces: ban risk, the Fable 50% cap, "only ever use Claude models through your Claude subs in Claude Code", and Claude's reset semantics. It totals maybe 10 minutes. Codex gets equal space, and ~20 minutes go to T3 Code workflow. A spliced-in correction (19:30) partly undercuts the title's urgency: with Opus 5.5, "you might not need five to 10 Claude subs anymore". The title is a broad audience net. The chapter "Introduction to agent maxing" names the real topic.

### Hook (00:01-01:30)

> "Before we get started with this one, I have a question for you. How many agent threads do you have running right now? I don't mean have you run today, I don't mean are you going to run later, I mean in the exact moment where you clicked this video, did you already have things running in the background? If the answer is less than five, you really, really need to watch this video because you are not taking advantage of the genuinely awesome and unique opportunity we live in today. And if the answer is more than five, you should also probably watch this..."

Mechanism:

1. A direct-address diagnostic question with a threshold (five) that sorts every viewer into "you need this".
2. A pattern break about the format: "this video is not my norm... I don't think we need caffeine for this one. We're going full rodeo. Much better." He apparently swaps coffee for a drink; that is inferred, and 14:31 confirms "I am literally drinking and filming".
3. An enemy and taboo frame: "the video that Anthropic does not want you to watch".
4. Risk reassurance with specifics: "of the 30 plus Claude accounts we're hopping between, I've had one friend get banned twice... reinstated almost immediately".
5. A joke bridge to the ad: "the only thing that can really stop us is a quick break for today's sponsor."

### Lead-in

- Parallel read (chapter 01:30-02:43, ~73 s). It opens with "I have two quick questions", mirroring the hook's question device. It includes a live speed race on screen: "Watch and see just how fast Parallel can get you good results. Going now. All real-time, of course... Open AI still going, still going" (02:01). It closes on "Join now at soydev.link/parallel."
- Roadmap (02:43): "This is a real, real rough order of events that I have planned here." Five sections: get tokens, access them, use well, use poorly ("which I'd argue is more fun and much more important"), and use while asleep. The chapters match the roadmap exactly.
- Intent disclaimer (03:00): "The point here is not to give you the exact formula to copy."
- Pre-emptive comment rebuttal (03:47-05:23): "I can already tell this video is going to cause huge blowback on Twitter. So, I'm going to just list the questions they're all going to bring up to try and dunk on me". Five canned objections each get a one-line comeback ("Wow, OpenAI has paid you off. I have paid OpenAI more money than you're worth. Wow, Anthropic has paid you off. I've paid Anthropic more money than you're worth.").
- Disclosures: a terms-of-service and ban disclaimer is spliced in late ("Dear from the future cuz I forgot an important disclosure", 14:31). T3 Code is his free open-source product ("our open-source that makes no money", 39:02). CI partners Blacksmith and Depot are named as "our awesome partners" (63:00).

### Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01-01:30 | Hook | Thread-count question, taboo frame, ban reassurance |
| 01:30-02:43 | Sponsor | Parallel, live speed race |
| 02:43-05:23 | Roadmap + pre-buttal | Five sections; five anticipated hater comments |
| 05:23-11:00 | Argument (math) | $200 Claude ≈ $8,000 tokens (4k Fable); skip $100 tier; $200 Codex ≈ $12k; Fable price vs Mythos preview's $25/$125; ~95% margin "napkin math"; resets (14 in 30 days) double Codex value; $200 Codex signups paused; "journalist and informant" justification |
| 11:00-12:41 | Instruction + ethics | Turn off training in data controls; use the API only for user-facing traffic, or "you deserve your ban" |
| 12:41-15:23 | Instruction | Callback to the first video; no sign-ins on a VPS; residential IP; spliced ToS disclaimer; Google/Gemini jab |
| 15:23-17:30 | Instruction + tangent | Introduces CLI proxy, then backs up to other subscriptions (Cursor, OpenCode, T3 Chat get worse subsidies); live reaction to a Codex reset announcement |
| 17:30-22:00 | Demo (dashboard) | His fork; prioritize accounts by soonest reset; 5-hour vs 7-day math; "Opus bucket from hell"; spliced "less drunk future Theo" Opus 5.5 note; websockets; session affinity and cache |
| 22:00-25:30 | Demo (setup) | Tailscale URL; his "fleet" repo and "how to set up a box"; "I'm going to tell you to tell your agent to do it" |
| 25:30-29:08 | Caveats + mindset | Separate home dir; never use a Claude sub outside Claude Code; Codex vs Claude reset semantics; banked vs immediate; "Burn your tokens" |
| 29:08-38:35 | Philosophy | De-risk both sides of merge (10-15% of tokens coding, 85-90% verifying); revert in <15 s; Netflix-take rant from chat; bring the agent in when you start thinking; "3 weeks" anecdote; manager analogy; "Don't outsource thinking, scale it" |
| 38:35-50:06 | Product workflow | T3 Code: threads are to-dos, "settle", inbox zero; two live feature prompts; tips (pick machine, Cmd+Enter); load balancing; "Humans are single-threaded"; babysit; merge auto-hides thread; worktrees |
| 50:06-59:05 | "Using tokens poorly" | Malware-fear rant; offloading examples (PR triage, email, medical records); multi-machine sidebar; T3 Connect setup (email-leak blooper); "where did I leave my keys" analogy; side-project revival prompt; live thread triage; real sidebar count |
| 59:05-64:00 | "While sleeping" | Move dev remote to an old Linux box; budget advice; VPS sarcasm (Hetzner $275/mo vs a $700 box); btop shows ~0% CPU; macOS bad for parallel work; CI bottleneck fixes |
| 64:00-66:36 | Emotional close | "This shit's so fun"; new engineering problems; Maria DM; sign-off |

Rough split: instruction and setup ~35%, T3 Code workflow ~25%, philosophy and mindset ~20%, rants and pre-buttals ~10%, hook/sponsor/roadmap ~8%.

### Thesis and arguments

Central claim: subscriptions are subsidized ~40x versus API prices. Unused quota is lost money, so you should stack accounts, route them safely, and restructure your work so many agents run unattended while you only handle decisions.

Order: economics (why), access (how), using tokens well (verification and problem-first prompting), product workflow (managing many threads), using tokens poorly (offload everything, even silly asks), asleep (remote hardware). The logic runs from money to plumbing to mindset to habit to infrastructure, and ends on joy.

Steelmen and limits:

- "You should still use the API for a couple of things though. One is very important. Anything facing users" (11:32).
- "Usually though, if you're not employed as a dev, don't stack subs until you're making money" (35:31).
- "Not going to pretend work trees are perfect, but they are good enough" (48:01).
- He anticipates misquotes ("I am not saying you should stop thinking", 34:00) and answers a named critic: "So again, Dan, I respect you heavily. You were fantastic to work with, but I will push back on this specifically" (36:31). Who Dan is goes unexplained.

Admissions: "I feel a little bad exposing these things to the world" (10:30); "I'm addicted, let's be real" (27:31); "I was like this not long ago" (59:00). The Opus 5.5 insert revises earlier advice.

### Evidence

Almost entirely first-person:

- Subscription arithmetic.
- His own dashboards: account expiries, reset counts ("I have 10 resets across my Codex subs").
- His fleet repo files.
- His T3 Code sidebar ("1 2 3 4 5 6 7 8 9 10 and then a monitor").
- Anecdotes about friends at AWS, Microsoft, and Fortune 500 companies (unnamed, private).
- Rumored margins from "napkin math that [two names, unclear in captions] I know".
- The Mythos preview price as historical evidence.
- A DM from teammate Maria and a post from "Stephen".

Read-and-react is close to 0%. This is the most original-argument video of the five.

### Demo

There are many short live demos with no prepared polish: the CLI proxy dashboard (17:30-22:00), the Tailscale URL explanation, the fleet repo file, two real feature prompts typed into T3 Code (41:01 queue system; 43:00 device-settings UI with a screenshot pasted), settling and archiving threads, load-balancing settings, a mock T3 Connect setup ("I don't have a new box to set it up on... Oh, email leak, great. I should work on that"), and btop on the "Alvin" server ("You can't see because my face is covering it", 61:30). Failures and rough edges stay in: a routing issue ("I have a weird routing issue right now. We'll figure it out", 56:30), the UI he hates in his own app, and the email leak. The whole video plays like an edited stream with chat-driven detours.

### Retention devices

- The roadmap as a five-part promise, with "poorly" teased as "more fun and much more important" (02:43).
- Pre-buttal list (03:47), which turns hate comments into a comedy beat.
- Spliced future-self inserts that break the format: "Dear from the future cuz I forgot an important disclosure... I am literally drinking and filming" (14:31); "Sup nerds, less drunk future Theo here" (19:30), ending "Back to whatever drunk Theo was rambling about."
- Chat rants as pattern breaks: the Netflix take, "Holy [bleep] I think I just saw the actual worst take of all time in my chat" (31:30, ~1 min); malware fear (50:06); VPS replies ("I might have to get into selling VPSs cuz those sound much more lucrative than bridges nowadays", 60:00, then extended sarcasm).
- A named chat question: "a very good question we just got from Strawman Twitch. How do you keep them all straight in your head?" (38:30).
- Imperative attention cues: "I have two tips I'm about to give you that are important, they're going to be rapid fire, so pay attention right now" (41:31). He then forgets the second one: "And I just realized I missed the second tip".
- Viewer inclusion: "the power users like us, yes, I'm including you now viewer, you're joining us on this journey" (16:31).
- Callbacks: "In my first token maxing video" (12:41); "my get out of jail free card" (37:00), referring back to his own anti-misquote line.
- Mild insults as comedy: "get through your thick skulls" (45:01); "you should consider a new Windows install because I know you're also using Windows" (50:32); "If you live in San Francisco... get out" (62:32).

### Ending

It lands emotionally rather than logically: "This shit's so fun. I know a lot of engineers have felt like the thing they loved died..." (64:01). Then: "The fun isn't that I'm checking my phone and sending prompts. The fun is this new type of engineering problem" (65:00). The final asks, in order: spin up more accounts; contribute to T3 Code ("we'll probably ignore them, but we might merge them"); a teammate DM as social proof ("Remote work is the best. This is so fun."); a tease ("Let me know if you want a video about that, too, cuz I have a lot of thoughts about how this goes long-term"). Sign-off: "I'm going to go kick off some more threads and grab another drink. Enjoy the new world of agent maxing and get as many of these tokens out as you can before the subsidization ends, if it ever does... I hope it was helpful. Let me know and until next time. Peace, nerds."

### Voice

1. "We're going full rodeo. Much better." (00:30)
2. "I have paid OpenAI more money than you're worth." (05:00)
3. "Let's do some math here. Who here knows how much money and tokens you get when you put in $200 on the Claude API? Give you a hint. It's $200." (05:00)
4. "OpenAI does numbers very simply. They keep them the same, they lower them 20 to 80% or they double them." (09:31)
5. "my job in my loyalty is as a journalist and informant, not as somebody who's trying to protect and shelter the few hundred people who know how abusable this is." (10:30)
6. "Don't be mad that I'm sharing, be mad that I'm right." (10:30)
7. "If you're using this as an alternative to the API to serve user traffic, you deserve your ban." (12:01)
8. "It's so trivial that I'm not going to tell you how. I'm going to tell you to tell your agent to do it." (24:31)
9. "Burn your tokens. Cool." (28:31)
10. "If undoing a bad change takes more than 15 seconds, you probably shouldn't be vibe coding at all yet." (31:30)
11. "I'm putting this in largely to have a quote that I can grab when people misquote me from this video." (34:00)
12. "You save your tokens and your brain if you give the agent the problem instead of the solution." (34:31)
13. "You ready for the spicy take here? This is similar to how it felt to be a manager." (35:00)
14. "I'm going to be so real with you. If you're not using T3 Code, I do not know how you do it." (38:30)
15. "Threads are not histories that you actively go back to all the time. Threads are tasks. They're to-dos." (39:31)
16. "Agents can be multi-threaded. Humans are single-threaded." (45:01)
17. "If you think your agent is more likely to install malware than you are, then you are dumber than your agent." (50:32)
18. "This is a shitty prompt for a shitty problem." (55:30)

Register: the loosest of the five, since he is drinking. "Be real" or "so real" appears 14 times, "cool" 19, "fun" 19, plus unbleeped "shit" and frequent mock insults. Sentences are long and run-on, with slogan-like aphorisms dropped in. He explains technical terms practically: "What this means is if I have a thread going, ideally the next prompt in that thread goes to the same account because caches are account specific" (21:00). Viewers are assumed to be working developers.

---

## 4. "Your prompts kinda suck" (m-B3jIMMmUE, 31:47, uploaded 2026-10-18)

### Topic and angle

An advice and opinion essay. Engineers under-use agents because they think in features. Much of what they'd build (dashboards, triage flows, visualizers) can just be a prompt. What's left to build are the primitives and data pipes that make prompts more powerful. The trigger is personal: a conversation with a friend who wanted a tool-call timing feature (05:01) and similar conversations with "an engineer that just started a company and went through Y Combinator" (01:01). The stance inverts the title. The problem isn't under-engineered prompts but over-engineering, and "most of us just aren't prompting hard enough" (00:30). The back third turns into a defense of AI-era engineering against "brain rot" critics.

Title vs content: "Your prompts kinda suck" reads like a prompt-craft tips video. The hook rejects that reading within 10 seconds. The payoff is a mindset (ask for outcomes, not features) plus one product case study (T3 triage). The "kinda" softens the insult; the sign-off brings the insult back ("I can't wait for you to be unemployed").

### Hook (00:01-01:40)

> "Remember all the hype around prompt engineering, this idea that we would have to get really, really specific with our prompts in order to set our agents up for success? It would become this whole new fancy field and thing we'd have to study and become good at. Yeah, that's all crap. I'm not going to pretend otherwise. I'm not trying to say with this video that engineers need to do more engineering with their prompts. I'm actually here to say the opposite. I think that engineers suck at prompting, but I don't think it's cuz they're not engineering it enough. I think it's cuz they're over-engineering it..."

Mechanism:

1. A shared-memory callback ("Remember...").
2. A blunt dismissal ("that's all crap").
3. An explicit reversal of what the title implies ("I'm actually here to say the opposite").
4. The thesis stated in under 30 s.
5. Humility plus credential: "I'm still in the early days of this myself... Just last week, I had almost this exact conversation with an engineer that just started a company and went through Y Combinator, and this convo changed how they think about their agents."
6. Mission framing: "I'm realizing I need to take the time to try and explain this to all of you."

It withholds the concrete examples and what "the opposite" looks like in practice.

### Lead-in

- Bridge (01:31): "This is a guide on how to prompt better and to get out of your engineering box in your brain. Because I know engineers really tend to love some things that we talk about, like today's sponsor."
- Macroscope read (chapter 01:47-03:38, ~111 s, the longest of the five). It opens with "I don't know if you have noticed, but we've been shipping a lot lately", then a dashboard walkthrough showing his team's actual work (Rust port, Orchestrator V2, Lakebed, Web MCP). That plants later topics. He self-discloses inflated numbers ("My numbers are a bit bloated here"). There is a mock code reveal: "We're going to actually look at some code in a real codebase... Okay, it is markdown, it's not real code. Sorry if you got baited." The markdown file foreshadows the video's thesis that features are markdown. It closes on "Macroscope has made our team ship better code and has made me a better boss. Figure out why at soydev.link/macroscope."
- Exit (03:31): "Okay, the sponsor break's over. It's time to get out of our engineering box for a bit." There's no roadmap beyond the hook's two-part framing ("What is prompting? What is engineering?"). Mid-video he marks the structure: "I think I have mostly exhausted the first part... But now I want to get into the real meat" (13:30).

### Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01-01:47 | Hook | Prompt engineering is "crap"; over-engineering thesis |
| 01:47-03:38 | Sponsor | Macroscope, custom markdown review agents |
| 03:38-04:58 | Framing analogy | XKCD "Tasks" (national park / bird photo) read and explained; "Now we are too used to this" |
| 04:58-07:31 | Anecdote + demo | Audit found Claude's ripgrep commands failing in zsh; friend wants a tool-call timing feature; "We already have this"; prompts Astra live |
| 07:31-09:01 | Claim + self-correction | "features that aren't actually features. They're information"; his own over-built task dashboard redesigned as a "meta thread" |
| 09:01-10:30 | Demo result | Tool-call report (one home-dir search took 41.7 min); context visualizer prompt; Railway was injecting 70,000 tokens into every request |
| 10:30-11:31 | Extension | Things never worth building are now worth prompting (bug visualizers; Tidal + Last.fm history) |
| 11:31-13:52 | Demo | Sub-agent picker request answered by prompting: two Opus 5.5 delegates, then a Grok 4.7 thread; context visualizer result |
| 13:52-18:31 | Case study | `npx t3 triage`: reveals it just pipes a playbook prompt into Claude Code/Codex; reads the playbook; "thousands of lines" became "five lines of code and then 30 lines of markdown" |
| 18:31-21:57 | Demo + rant | Asks the agent what logging it lacks; terminal rant; asks Codex to describe its computer-use tools, then has Opus clone them; "You can prompt about your prompts" |
| 21:57-24:57 | Life use + rebuttal | MRI records; "brain rot" rebuttal via email analogy; "add your goddamn email to ChatGPT"; Superhuman "slowly rotted"; agent watching an AWS bill |
| 24:57-31:47 | Identity essay + close | "Never felt more like an engineer"; trough of despair (drawn curve, inferred); missing primitives (inline visualizer); Rust, OS, compilers, JS runtime; critics; sign-off |

Rough split: demos ~30%, argument and essay ~40%, anecdotes ~15%, sponsor ~6%, one source read (XKCD plus his own playbook) ~5%.

### Thesis and arguments

Central claim: most "features" engineers want are really information or workflows an agent can produce on request. Ask for outcomes, keep features as prompts or markdown, and spend engineering effort on the primitives and data access that let prompts do more.

Order:

1. The normie and engineer inversion (XKCD).
2. A concrete feature request answered by prompting.
3. His own mistake, an over-built dashboard.
4. Prompting unlocks work that was never worth building.
5. You can prompt your way past missing product options (sub-agent picker).
6. Applied to product engineering (T3 triage).
7. "What's left to build? I don't know. Let's ask" (18:31).
8. Life outside code (email).
9. Identity: this is more engineering, not less.

Concessions:

- "Obviously, using Opus 5.5 on extra high is not going to get you the data or the feature you want immediately" (10:00).
- "I'm not saying that everyone should be adding their own features to T3 Code" (07:31).
- "Am I thinking about the details of every SQL query in my code base anymore? No, absolutely not" (29:31).
- Empathy for critics: "I really do get it. Especially now that I've talked to more people who are in that boat" (28:00).

Admissions of being wrong: the dashboard ("I thought I was really smart and clever for coming up with this idea"), the over-built triage feature, and "I was such a big terminal person. I can't do it anymore." Bias: nearly every example is T3 Code, and he pre-empts it with "This is not a T3 code plug at all. In fact, it's quite the opposite in a lot of ways" (05:01). The paid-off accusation is pre-empted at the end.

### Evidence

- One comic (XKCD), read aloud and explained.
- His own prompt text, read aloud (06:31, 12:00, 19:00).
- His own markdown playbook for T3 triage, read section by section.
- Agent outputs with numbers: 41.7 minutes, 70,000 tokens.
- Anecdotes about a friend, a YC founder, a Windows user's crashes, and his MRI records.
- Product history: Superhuman's decline.
- An analogy: email vs letters, internet friends.

Read-and-react is ~5%. This is the most essay-like structure in the group.

### Demo

There are three live prompts fired early and harvested later. This interleaving is a structural device: the waiting time is filled with argument.

- The tool-call breakdown is fired at 06:31 ("in approximately 3 minutes, hopefully less") and harvested at 09:01 ("We now have the report. I didn't even tell it to make it a page, but it did for me").
- The context visualizer is fired at 09:31 and harvested at 13:01 ("Oh look, the context window breakdown is done").
- The delegates are fired at 12:00 and shown running at 13:01.
- The T3 triage CLI is run live (15:01: "Ready to see what it does? I'll press enter").
- The logging question goes into the triage session (19:00) and is left running. Its result never appears, an unharvested loop.
- The computer-use description and clone is prepared, with a PR mentioned.

There are no outright failures. He admits the triage flow "is going to do a lot of additional steps".

### Retention devices

- Expectation reversal at the start, and again in the triage reveal: "you probably have a lot of ideas for what this is... That's not what I did. Ready to see what it does?" (14:32-15:01).
- Sponsor bait-and-switch joke ("Sorry if you got baited").
- Fire-now, harvest-later demos create small open loops across 3-4 minute spans.
- "flash bang warning" (11:31) before showing a bright image, inferred to be a light-mode XKCD redraw labeled "the new one".
- Rants as pattern breaks: the terminal rant ("Get out of your [bleep] terminals, guys. Get over yourselves. You're just wrong", 19:30); the email rant ("Y'all need to add your goddamn email to ChatGPT", 23:00).
- Platform aside: "Hi y'all watching on YouTube" (29:01), a nod to ad revenue in the middle of describing his job.
- Spoken signposting: "And now I'm going to give an example of one I did wrong" (07:31); "But now I want to get into the real meat" (13:30); "And here is where we get to the silliest example by far" (23:00); "And here is the craziest thing about all of this" (24:30).

### Ending

From 28:00 he speaks to the discouraged ("to the people who don't feel this right now"). He sketches an emotional curve (inferred drawing) and claims the despair is a trough before a harder, deeper kind of engineering: "Now I'm building my own operating system and my own compilers... I'm engineering harder than I've ever engineered". There's a short contrast pair: "Am I building my own tech stacks that you can run with NPX create T3 app right now? No. I'm building my own JavaScript runtime for my own cloud." He returns to the thesis: "the features you want to add are just prompts. They're not features." Then a sting aimed at critics: "Or you can go back to saying I'm paid off by OpenAI and that's the only reason I think this way. Sure, that's a lot easier for y'all and I can't wait for you to be unemployed if you keep thinking that way." Then a warm close: "But for everybody else that genuinely loves building, there has never been more to build and there's never been more reason to build it. Hopefully this inspires y'all. Go build something cool. And until next time, peace, nerds."

### Voice

1. "Yeah, that's all crap. I'm not going to pretend otherwise." (00:01)
2. "I'm still in the early days of this myself" (00:30)
3. "Okay, it is markdown, it's not real code. Sorry if you got baited." (03:02)
4. "We need to lock in for the normie experience for a minute." (03:31)
5. "I'm going to get super literal here with an exact example." (04:30)
6. "If you're a T3 Code user, the next statement I make will either not surprise you at all or surprise you a lot. My reply was, 'We already have this.'" (06:00)
7. "The point I'm trying to make here is a lot of engineers are still thinking about these workflows as features that need to be built into their products." (07:00)
8. "I'm talking about features that aren't actually features. They're information." (07:31)
9. "I thought I was really smart and clever for coming up with this idea for a feature" (08:00)
10. "But that's all fine and dandy." (13:30)
11. "That's not what I did. Ready to see what it does?" (15:01)
12. "This feature when I first started working on it was going to be thousands of lines of complex code. And then I realized it could be five lines of code and then 30 lines of markdown, and now it works way better." (17:30)
13. "So, if half the stuff we should be building should actually just be a markdown file instead, what's left to build? I don't know. Let's ask." (18:31)
14. "Get out of your [bleep] terminals, guys. Get over yourselves. You're just wrong." (19:30)
15. "You can prompt about your prompts and prompt about your programs." (21:31)
16. "Y'all need to add your goddamn email to ChatGPT. I know this sounds insane." (23:00)
17. "Never felt more like an engineer." (24:30)
18. "I'm engineering harder than I've ever engineered and my brain is working harder than it's ever worked." (30:01)

Register: calmer and more essayistic than the release videos ("cool" 6, "fun" 6), with "goddamn" three times and two bleeps. More rhetorical questions and anaphora ("You can prompt about..." x5). He explains technical points through the user's goal and mostly skips the internals.

---

## 5. "NVIDIA Just Lost Their Lead" (VgLwsakPgo4, 25:27, uploaded 2026-08-29)

### Topic and angle

News commentary on hardware threats to Nvidia. The triggers are three items in one week:

1. A SemiAnalysis piece on OpenAI's in-house "Jalapeno" inference chip, reported to beat Blackwell on performance per watt at 700 W.
2. Apple's M5 Max/Ultra Mac Studio.
3. The anonymous "Aux Alpha" model (caption; the real name is unclear) revealed as a GLM model from Z.ai ("ZAI") served entirely on Huawei chips.

His angle is gleeful skepticism of Nvidia: "never been the biggest fan of them. And the opportunity to point out how their monopoly is about to be crushed and crumbled is one I have to take" (01:30). The educational spine explains how Nvidia uses memory capacity for price segmentation.

Title vs content: the title states a completed fact ("Just Lost"). The video argues something weaker. Jalapeno "is still not quite Rubin levels", has been tested only on small models, and Jensen claims rising market share. The close is "Nvidia's weird position in the market might not last as long as they probably think" and "Am I crazy for saying all of this or am I kind of onto something?" The title overclaims and the body hedges. The DGX Spark section ("kills almost all of the reasons you could ever justify buying the DGX Spark, which is a whole category of Nvidia devices killed", 15:30) is the only place a "lost" claim is fully earned.

### Hook (00:02-02:05)

> "Nvidia's a weird company. They originally started making chips for gamers to have fancy 3D graphics in their computer games, and now they are the most valuable company in the world powering the majority of intelligence that we get from all the fancy AI tools we use every single day."

Mechanism: an origin-story irony opener (gamers to the world's most valuable company), not a cold stake. Then the moat is listed ("CUDA... to the crazy deals"), then dependency as vulnerability: "OpenAI could not function if Nvidia decided they wanted to start charging them 10 times more." It escalates to the most motivated adversary, "But there's one particular place that is more motivated than anywhere else to solve this. China.", then "Even OpenAI has started developing their own chips". The giant appears rattled: "All of this has Nvidia acting pretty scared and very very weird. From crashing out on Jim Cramer's show to buying Hugging Face, a little bit absurd." He declares his bias: "I'm a big nerd about chips... never been the biggest fan of them." He withholds the specific numbers and the Cramer clip, which pays off at 20:30.

### Lead-in

- Joke bridge (02:00): "But unlike my friends who invested in Nvidia early, I don't have billions of dollars to spare, so I'm going to have to take a quick break for today's sponsor."
- Browserbase read (~02:05-03:12, ~65 s). It opens with "I got a hot take for you guys", ad copy disguised as an opinion. It closes on a comparison number: "Over 85% of the APIs on the web can't be accessed by simply curling them. If you're okay with only having that 15%, stick to curl... soydev.link/browserbase."
- Exit (03:12): "Before we can talk about how Nvidia loses, it's important to understand how they won." This is the only video of the five that leaves the ad straight into an explainer.
- The disclosure comes late: "I should include a callout here. I am an AMD investor" (23:30), roughly 92% of the way through.

### Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:02-02:05 | Hook | Origin irony, dependency, challengers, Nvidia "scared" |
| 02:05-03:12 | Sponsor | Browserbase |
| 03:12-04:58 | Explainer | Two moats, chips and CUDA ("We'll come back to this one in a bit"); why GPUs (many small cores); chip plus HBM, drawn on screen (inferred: "I'll change this to be GPUs") |
| 04:58-06:32 | Evidence: pricing | RTX 5090 $2,000 retail, now ~$4,500; RTX Pro 6000 $12-16k, same speed or slower; 96 GB vs 32 GB GDDR7 |
| 06:32-08:31 | Chat Q + analogy | "why not just connect them?" Kitchen analogy: fridge a mile away; inter-GPU bandwidth |
| 08:31-10:58 | Rant + evidence | DGX Spark: $4k, "botched install of Ubuntu", ARM Linux "hell", 128 GB LPDDR5, 6,000 vs 24,000+ CUDA cores; "Do you see what they've done here?"; concession on the 200 Gb NIC |
| 10:58-12:31 | News 1 | Aux Alpha revealed as a GLM model on Huawei chips; subscribe ask; "I also got called out"; reads a post on Chinese-chip efficiency |
| 12:31-16:30 | News 2 | Apple M5 Max/Ultra specs read; 10x time-to-first-token vs M1 Ultra; comparison table (inferred); "kills almost all of the reasons... DGX Spark" |
| 16:30-20:01 | News 3, read-and-react | SemiAnalysis on Jalapeno, read line by line: 216 GB HBM, 700 W, 13.4 PF FP4; Doom joke; perf/W; caveats (small models only, power-limited); Jensen quote "throughput per watt is revenue" |
| 20:01-21:47 | Clip reaction | Sarcastic setup, then plays the Jim Cramer clip unseen ("we get to watch it together"); "Definitely not scared at all, are you, bud?" |
| 21:47-22:31 | Steelman | Hugging Face bid is "an actual good faith play"; $12.9B joke |
| 22:31-23:47 | Chat-prompted addition | Terafab (Elon / "SpaceX AI"); size comparisons read |
| 23:47-24:24 | Disclosure + aside | AMD investor; "very behind"; Intel in Terafab |
| 24:24-25:27 | Conclusion | AI speeds catch-up; "fought not on chips, but on electricity"; question CTA |

Rough split: explainer and price analysis ~35%, source read-and-react (Apple, SemiAnalysis, clip, Terafab) ~35%, rants and opinion ~15%, hook/sponsor/close ~15%.

### Thesis and arguments

Central claim: Nvidia's lock on AI compute is cracking. Apple, OpenAI's own silicon, and Chinese chips now hit the memory-plus-efficiency combination Nvidia has used to price-segment, and in a power-limited world, performance per watt decides it.

Order:

1. How Nvidia won (chips and CUDA).
2. How it extracts margin (memory segmentation across 5090, RTX Pro, and Spark).
3. Challenger 1: Huawei-served GLM shows non-Nvidia serving at scale.
4. Challenger 2: Apple M5 Ultra kills the Spark category.
5. Challenger 3: Jalapeno beats Blackwell on perf/W.
6. Nvidia's reaction is weak (Cramer, Hugging Face).
7. Everyone else is trying too (Terafab).
8. AI accelerates catch-up; electricity is the real constraint.

Concessions:

- "I won't say it's cheap, but getting a powerful Nvidia chip is not the hardest or most expensive thing in the world" (04:30).
- "They did do one really nice thing with the Sparks" (10:30).
- On the M5 Ultra GPU: "Not necessarily better than the GPUs in the 5090 and the 6000 Blackwell... I'm guessing almost certainly not" (15:01).
- "It's still not quite Rubin levels" (17:31).
- "This is not large model performance" (19:30).
- The Hugging Face steelman.
- Admission of being wrong: "I also got called out here because people were saying only Frontier Labs have this much compute... I assumed that they were still serving Nvidia" (11:30).

The bias disclosure (AMD stock) is late, and he says it is why he left AMD out. He also admits to an anti-Nvidia stance up front.

### Evidence

- Retail and MSRP prices and memory specs, drawn and compared on screen (inferred).
- An Apple spec page read aloud ("36 cores of CPU, 80 cores of GPU, up to 512 gigs...").
- The SemiAnalysis article, read paragraph by paragraph with short reactions ("spicy deeds. Cool." for "spicy speeds"; "Of course they have it running Doom").
- A quoted Jensen line from Computex.
- The Cramer interview clip, played at length (~70 s).
- A post about the GLM serving, read aloud (attribution unclear).
- Terafab promotional copy ("25 times the size of Apple Park").
- Personal ownership: "The DGX Spark is my least favorite computer in this apartment."

There are no benchmarks of his own and no product of his.

### Demo

None in the build-and-run sense. On-screen drawing and explanation of the chip-plus-memory split (inferred) and a live first watch of the Cramer clip are the closest equivalents.

### Retention devices

- Opened loop: "We'll come back to this one [CUDA] in a bit because this is where things will get complicated" (03:31). It is never paid off as a segment; CUDA returns only in passing (the "CUDA moat" quote at 12:00, the Hugging Face joke, "training is still happening on CUDA"). This is a dropped loop.
- Chat as prompt: "we're already seeing my favorite question in chat, which is why not just connect them?" (06:32); "Somebody in chat mentioned... SpaceX AI" (22:31), which leads to "somehow I entirely forgot about Terafab".
- Sarcasm setup before a clip: "Don't worry though, Jensen's definitely not scared... Not like he's going to say something stupid" (20:01), then the payoff "Definitely not scared at all, are you, bud?" (21:30).
- Subscribe ask tied to a callback: "I already have a video about this... when you're on the way to it, you should hit that subscribe button cuz it costs you nothing and with these videos take a lot of work" (11:01).
- Self-quote callback: "I've been yelling this for a while. Electricity's going to be a big deal" (20:01), repeated in the close ("As I've said many times now").
- Rhetorical teaching questions: "You would assume this chip must be way, way faster... But guess what?" (05:32); "Do you see what they've done here?" (10:01).

### Ending

It's short (~1 min). A synthesis claim: "Their use of AI in their catch-up process has enabled them to do it more effectively than anyone would have anticipated, including Nvidia." The recurring thesis: "the future is going to be fought not on chips, but on electricity." A hedge: "Nvidia's weird position in the market might not last as long as they probably think." The CTA is a comment-bait question: "Am I crazy for saying all of this or am I kind of onto something? Let me know how you guys feel about the future for Nvidia and this whole space in general in the comments." Sign-off: "Until next time, peace nerds."

### Voice

1. "Nvidia's a weird company." (00:02)
2. "But as you guys can probably guess, I have a lot of thoughts on this. I'm a big nerd about chips." (01:30)
3. "I got a hot take for you guys." (02:00, opening the ad)
4. "Before we can talk about how Nvidia loses, it's important to understand how they won." (03:00)
5. "Lots of small brains are a lot more powerful than one giant one in these cases." (04:01)
6. "This might sound crazy. You might be confused. How is the chip that costs six to eight times more slower?" (05:32)
7. "I'm going to use my favorite analogy I always use for chip-related stuff here. A kitchen." (06:32)
8. "Good luck. Have fun. Not [bleep] happening." (07:30)
9. "And having spent far far far too much time fighting arm Linux in my life, I promise you you're not going to use this computer as a computer." (08:31)
10. "Do you see what they've done here?" (10:01)
11. "Obnoxious, dumb, solved." (13:00)
12. "As a video nerd, I love the fact that the new Ultra chip can do 33 streams of 8K ProRes 422... But that's not what we're here for, let's be real." (13:32)
13. "Sorry guys, you're [bleep] around too much. We're going to put an end to that." (16:01, voicing Apple)
14. "The DGX Spark is my least favorite computer in this apartment." (16:30)
15. "Even just this chart should be enough to give Nvidia a heart attack." (17:31)
16. "Yep. I've been yelling this for a while." (20:01)
17. "Definitely not scared at all, are you, bud?" (21:30)
18. "I love them to death. They're very behind." (24:00, on AMD)

Register: the most explanatory and teacher-like of the five, with the most bleeped profanity (about eight bleeps, mostly in the Spark rant). "Crazy" appears 9 times. Technical depth is pitched to a mixed audience: one analogy (the kitchen), simple partitions ("the chip and the high-bandwidth memory"), and numbers given with a reason they matter. He corrects himself mid-explanation ("I'll change this to be GPUs").

---

## Patterns across these 5

### Hooks

Shared:

- Every hook names the subject within 30 s, attaches one shock number or superlative, and states his stance before the ad. The numbers: 200k stars / top 10 on GitHub; $330,000 of inference; "less than five" threads and 30+ accounts; "that's all crap"; most valuable company in the world.
- Every hook ends with the same move: a promise of what's coming, then "after a real quick break for today's sponsor". The ad lands between 1:30 and 2:05 in all five, which is 2-8% of runtime.
- Each hook contains a self-referential credential of effort or access: "I installed... audited the majority"; weeks of early access; "the 30 plus Claude accounts"; "this exact conversation with an engineer that just started a company"; "I'm a big nerd about chips".

Differences by type:

- Release reaction (It's Here): withhold the name, use a meta joke, show a dashboard, reveal, superlatives, then "far from the whole story" plus a spoken roadmap.
- Tutorial (Claude sub): a direct-address diagnostic question and an enemy frame ("the video that Anthropic does not want you to watch").
- Advice/opinion (prompts): a shared memory, a dismissal, and a reversal of the title's implied meaning.
- News commentary (NVIDIA): origin-story irony, then a list of threats escalating to "China", then the giant "acting scared".
- Personal review (Matt's skills): a delayed name reveal with a self-deprecating rank joke, a confession ("I honestly kind of dismissed initially"), and a second subject that hints the verdict will surprise.

### Shared skeleton (as share of runtime)

1. Hook: 0:00 to ~1:30-2:05 (3-8%). Subject, number, stance, and a soft roadmap or tease.
2. Sponsor: 65-111 s (3-6%). The ad ends between 2:40 and 3:40 (4-13% in). The ad topic always touches the video theme: Depot "parallel" in a skills video, CodeRabbit "AI reviewer" in a model video, Parallel "search for agents" in an agent video, Macroscope "markdown review agents" in a features-are-markdown video, Browserbase "agents need the web" in an AI-chips video.
3. Re-entry framing: 20 s to 2.5 min (1-4%). Scope ("I could probably go off for five plus hours"), a disclaimer ("you do not get anything out of blindly copying"), a roadmap ("real, real rough order of events"), pre-butted comments, or "Before we can talk about how X loses...".
4. Body: ~80%. Sections in a logical order, each opened with a spoken signpost. Release and news bodies follow the source's order (release notes, then article). Tutorial and opinion bodies follow an argument ladder (why, then how, then mindset, then habit).
5. A late "honesty" block: ~10%, at 75-90% of runtime. The failure thread in It's Here (35:30-40:30); the critique of Matt's prescriptiveness (28:01-31:16); "using tokens poorly" and the hardware sarcasm; Jalapeno caveats and the AMD disclosure. Weaknesses come late, after the wow, but before the verdict.
6. Close: 1-4 min (4-12%). A verdict in his own words, an emotional or identity lift ("This shit's so fun", "Never felt more like an engineer", "a taste of something new"), a question or "let me know", then the sign-off. The sign-off is "until next time, peace nerds" every time, often preceded by "I think I've said all I have to here/on this one".

### Recurring argument moves

- Thesis by inversion: prompt engineering is crap and the problem is over-engineering; "using tokens poorly... I'd argue is more fun and much more important"; the best skill came from the other repo; "the thing that makes Astra special isn't that it is the best code model ever".
- Pre-buttal of commenters, often as a list with one-line insult comebacks: "my apps are more real than yours"; "I have paid OpenAI more money than you're worth"; "I can't wait for you to be unemployed"; "you are dumber than your agent".
- Quote insurance: he plants a line to point to later ("I'm putting this in largely to have a quote that I can grab when people misquote me"), then calls back to it ("my get out of jail free card").
- His own mistake as the lesson: the over-built dashboard, the over-built triage, 3 weeks of thinking an agent solved instantly, not reading Matt's docs, wrong about who serves GLM.
- Concrete before/after read aloud: unslop vs ChatGPT; Fable 5.1 vs Astra fish game; Sol vs Astra cleanliness; RTX Pro vs 5090.
- Everyday analogies: thumbnail vs skill description; kitchen fridge a mile away; manager handing out problems; email inbox for threads; "Google searching where did I leave my keys"; Netflix; email vs letters; last-gen vs next-gen game; iPhone moment.
- Numbers tied to cost: price per score, prompts needed (5 to usable, 8 to beat competitors), latency before and after, subscription-to-token ratios.
- Self-promotion in the body, not just the ad: T3 Code appears in four of five (not NVIDIA), and Lakebed in three. He pre-empts it ("This is not a T3 code plug at all").
- Deferred verdicts: future videos promised to settle questions (Fable vs Astra, swarms, long-term subsidies, simplified technical English).

### Recurring evidence handling

- Primary documents read aloud with interjected one-liners. He reads in chunks, then reacts in 1-3 short sentences ("Cool.", "Of course they have it running Doom.", "Don't call me out like this.", "This is unreadable.").
- Release and news videos are ~35-45% read-and-react; tutorial and opinion videos are ~0-5%. Everything else is first-person experience, which he treats as the higher-value evidence ("I did not think this demo reflected my real world usage").
- Community figures are credited with one-line bios: Flavio "the bouncing ball and hexagon guy"; Peter "coined the Rottweiler description"; Dillon Mulroy "the effect in functional programming JavaScript guy"; Lauren "one of my old favorite React core team members".
- Insider access is mentioned without detail: "confirmation from people at OpenAI", Sam Altman's question, the Artificial Analysis founder's reply, friends at AWS and Microsoft.
- He flags anomalies in the data instead of hiding them: xhigh scoring below high, "high was cheaper than low", benches "of varying ages".
- Live chat questions become segue triggers in four of five.

### Recurring phrases and transitions

- Into the ad: "after a real quick break for today's sponsor" (3/5 near-verbatim; the other two use "a quick break for today's sponsor" inside a joke).
- Out of the ad: "I'm going to be so incredibly real with you guys", "Couple things I want to say up front", "Okay, the sponsor break's over", "This is a real, real rough order of events".
- Candor markers: "be real / so real / let's be real / I'll be real" (24 uses across the five, 14 in the Claude-sub video alone); "I will say" / "I'll say"; "admittedly" (7); "genuinely" (9); "honestly".
- Signposts: "Let's actually take a look at...", "Enough yapping", "Anyways, let's...", "Back to real world", "And here is where...", "This is where things get really cool", "Okay, you guys get the idea", "Let's finish getting through these...".
- Verdict words: insane (21), crazy (25), absurd (14), cool (48), fun (~60 matches, some of them "funny"), "slaughter" (release only), "slop" (17 in the skills video), "cringe and bad" (2 videos).
- Shrug: "It is what it is", "Take that as you will", "We'll figure it out".
- Audience address: "you guys" (29), "y'all" (10), "nerds", "I need you to...", "I'm including you now viewer".
- Sign-off: "And until next time, peace, nerds."

### Variation by video type

- Release reaction (It's Here): source-ordered (cost, availability, benchmarks, capabilities, demos, real use, failure, verdict). Heaviest superlatives and the most open loops (6+ future videos). No chapters. Disclosures about access and embargo terms.
- Personal review / tutorial-from-experience (Matt's skills): demo-heavy with chat interplay; ends on a numbered how-to and admits the format didn't land as planned.
- Long tutorial (Claude sub): explicit chaptered roadmap; most rants and pre-buttals; spliced pickups; the most product placement for his own app; ends on joy, not a verdict.
- Advice/opinion essay (prompts): demos fired early and harvested later to fill time; two halves marked aloud ("the first part... now the real meat"); ends with an identity pep talk and an insult-then-warmth sign-off.
- News commentary (NVIDIA): explainer-first (how they won, then how they lose); teacher-like analogy; source read-throughs and a clip reaction; shortest close; question CTA; no own-product content.

### Surprises and pattern breaks

- He admits retention coaching on camera ("my new retention guy said I'm not allowed to") and uses the admission as the hook.
- Two videos (It's Here, NVIDIA) have no YouTube chapters. The 66-minute tutorial has the cleanest chapters, matching its spoken roadmap.
- The Claude-sub video splices in two "future Theo" pickups, one adding the ToS disclaimer he forgot and one revising advice after Opus 5.5. It also openly says he is drinking.
- The NVIDIA video opens a CUDA loop ("We'll come back to this one in a bit") and never closes it. Its financial disclosure (AMD stock) comes at 23:30 of 25:27, not up front.
- The title "NVIDIA Just Lost Their Lead" states a fact the body only half-supports. "So I tried Matt's skills..." centers someone else's repo for its first act and admits the verdict favors the other one.
- Ad reads use the same tricks as the content: a "that's not what I promised" pivot, a live speed race, a fake "real code" reveal. They also seed later topics (Macroscope's dashboard previews Orchestrator V2 and Lakebed).
- Tweets read aloud, which I expected to be a staple, barely appear in this group. The sources are release notes, a newsletter article, skill markdown, a spec page, a comic, and a TV clip.
- He leaves his own on-camera mistakes in: a wrong clip ("This is the Opus 5 version"), a forgotten tip, a leaked email, "my face is covering it". They read as authenticity, not polish.
- At 35:01 in Matt's skills he names the format he is actually delivering ("what you're getting instead is my actual process"). That is a useful script move: say out loud when the video turned into something other than what the title promised.
