# Group C: structural reading of 4 Theo videos

Source: auto-caption transcripts. Quotes are verbatim except for light caption fixes, marked where the fix is a guess. "Inferred" means I am reconstructing what was on screen from speech. Recurring caption errors I corrected silently: "Cloud Code" → Claude Code, "codecs/CEX" → Codex, "Grock" → Grok, "cash read/write" → cache read/write, "OTAA" → OTA, "Julia" → Julius, "Babel" → Fable, "soy.../swedev.link/sid.link/slative.link/atvive.link" → soydev.link. The captions also drop or bleep profanity (`[\h__\h]` in the React Native file; gaps like "beat the out of the model" elsewhere), so he swears more than the text shows.

---

## Video 1: "T3 Code broke me" (uLGxb4F3SyI, 41:49, uploaded 2026-10-29)

### 1. Topic and angle

A full feature tour of T3 Code, the open-source multi-harness coding-agent app that Theo co-builds. No news trigger. The trigger is the product's own growth ("about to hit 550,000 users and 140,000 weekly actives", 02:01) and his guilt at never having explained it: "I haven't talked about T3 Code enough" (02:01). The stance is a founder's redemption arc. It used to be "the open source worst alternative" (00:32), and now "it felt like we had something unique" (02:01).

The title promises personal damage, and the description says "T3 Code has broken over 700,000 users". The video pays this off only in the jokey negatives section at 37:30 ("It will ruin your sleep schedule", the therapist and ex-partner bit). The user count in the description (700k) is higher than in the video (550k), which fits the "Theo from the future" pickup at 31:31: the main recording predates the upload by weeks. The title is a curiosity hook pasted onto a tutorial/tour.

### 2. Hook (0:00-1:30)

> "All the way back at the start of 2026, Julius and I got really hyped on the new Codex app by OpenAI. It blew us away... which is why we were really upset when the performance started to get bad, and as much as we would bother the team, we just wanted to access the code and fix it ourselves. The OpenAI guys, as awesome as they were, wouldn't give us access to the source." (00:02)

> "But I'm going to be incredibly honest with you guys. Despite being open source and built by incredibly talented devs like Julius and Maria, and also me, for many, many months, T3 Code was just the open source worst alternative to the Claude Code and Codex desktop apps." (00:32)

> "I'm going to be incredibly real and say I was almost a bit ashamed to push it." (01:01)

The mechanism is an origin story turned confession. He sets up a villain (closed source, bad performance), introduces the hero product, then undercuts it himself. That admission buys credibility for the turn at 01:31 ("But then things started to change") and the growth numbers at 02:01. What he withholds: what actually changed and why it is "unique". The open question is "what made it good?"

### 3. Lead-in

- 02:31-03:01 promise: "Give you a real overview of not just what T3 Code is, but how it's changed, how I build with it, and why over half a million developers are choosing to work with it now." He targets lapsed users: "if you tried out T3 Code back when it was this ugly, gray, sloppy mess, definitely stay tuned."
- Disclosure that doubles as the sponsor bridge (03:01): "T3 Code is open source, requires you to bring your own sub, and we don't make any money off it. In fact, it's quite expensive for us to run, so I hope you can forgive me for a quick break for today's sponsor."
- Sponsor: Apify, 03:01 to about 04:28, roughly 90 seconds. He ties it to the topic: "I added it to Claude Code, so now it works in T3 Code." Exit line: "Make sure your agents have the tools they need today at soydev.link/apify." He goes straight into content with no transition: "It's hard to summarize what T3 Code is and I almost feel like a bad founder for it."
- Roadmap (04:31): "I'm going to do my best to try and summarize like the top-level three and then we'll dive into the details." He shows a prepared list on screen (inferred: "I put together a long list of all the things I love") and addresses a live chat ("Thank you all for hanging out here"), so this was recorded on stream.

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:02-03:01 | Hook / origin story | Codex app inspiration, closed source, confession, turnaround, numbers. |
| 03:01-04:28 | Sponsor | Apify. |
| 04:31-05:00 | Roadmap | "Top-level three", then details. |
| 05:00-09:30 | Pillar 1 + demo | Every harness and sub (Codex, Claude, Cursor, Grok, OpenCode, Antigravity, Pi, ACP registry). Live demo of delegating one review to four models in four harnesses, then cross-thread orchestration. Anecdote of a user running 10,000 threads over iMessage. |
| 09:30-10:00 | Recap + correction | Restates pillar 1 and clears up "T3 Chat vs T3 Code". |
| 10:01-14:30 | Pillar 2 + demo | Remote control: `npx t3 serve`, Tailscale, his machine fleet by name, load balancing, device hub, a jab at the Claude Code and Codex mobile apps, live `npx t3 connect` setup on a Linux box. |
| 14:30-21:31 | Pillar 3 + demo | "Built to get work done": critique of the ChatGPT/Codex sidebar (inferred: screen-sharing that app), then live triage of his own real threads (settle, snooze, scheduled task, steer vs queue, working section, cmd-enter, PR-linked auto-settle). Ends on the idea of "spatial awareness". |
| 21:31-31:50 | Feature rapid-fire | About 30 features in 10 minutes: terminal over T3 Connect, diagnostics, HTML visualizations, PR tab, usage tab, multi-select, web app, drafts/stash, remote 3D iOS simulator, harness switching, OS support (Windows ARM rant), themes, keybindings, git providers, PR monitoring, webhooks (pays off the 14:30 tease), folder icons. |
| 31:31-34:30 | Pickup insert | "Theo from the future here": update-all, open in VS Code over SSH, port a project to another machine, `npx t3 triage`. |
| 34:30-36:30 | Chat favorites | Features chat says it loves: file attachments that give agents the bytes, snapshots, fonts, live activities. |
| 36:30-38:30 | Mock negatives | Bring your own compute, 3-device limit, no built-in computer use, "made by Theo", ruins your sleep, burns tokens. |
| 38:30-40:30 | Positioning + CTA | "Built for code", file issues, stable vs nightly. |
| 40:30-41:49 | Credits + sign-off | Thanks contributors by name, 516 contributors, 27k stars. |

Runtime split: about 7% hook, 3.5% sponsor, 45% pillar demos, 30% rapid-fire list, 5% negatives, 8% CTA and credits. Almost all of it is demo.

Note: the transcript repeats a block word for word (23:31-24:30 restates 23:00-23:31: "Julia's even got this all working in the mobile app... Concerned about where your tokens are going?"). This is either a caption artifact or an editing slip that left a duplicated take in.

### 5. Thesis and arguments

Thesis: T3 Code went from a worse clone to the best place to run all your coding agents, because it is built for engineers doing parallel work across many machines, which the labs' apps are not.

The arguments come in a fixed order, three pillars and then volume:
1. One app for every harness and subscription, shown with the four-model delegation demo.
2. "World-class remote control", backed by an architecture explanation (a WebSocket server instead of terminal or Electron RPC) and his own fleet.
3. "Built to get work done": the sidebar is an inbox and "Every time you open a thread, the goal should be to close it" (16:00). Supported by contrast with the ChatGPT app and a live triage of his own threads.
4. Breadth: the sheer number of features is the argument.

Concessions and hedges: the opening confession; "I didn't think people were going to like this" about the sidebar (15:30); "you'll have some growing pains... and I'm sorry in advance" (15:30); "Since T3 Code integrates with so many different things, there will always be some niche edge cases and bugs" (34:01). The negatives section is self-critique played mostly for laughs, with three real limits in it (own compute, 3 devices, no built-in computer use). Bias disclosure is structural: he builds it, "we don't make any money off it" (03:01). He also pre-empts the token-burn complaint: "I've audited this heavily" (38:30).

### 6. Evidence

Almost entirely his own product and his own usage. Numbers: 550k users / 140k WAU (02:01), "half the events... from Linux users" (28:01), "over 80% of the issues... resolved" by triage (34:01), "a hundredth as much" of the GitHub API rate limit (30:32), 516 contributors and 27,000 stars (41:00). Competitor evidence is a screen-share of the ChatGPT app (inferred, 14:30) and verbal jabs at the Claude Code and Codex mobile apps. One second-hand anecdote (the iMessage user). Chat acts as a live focus group (34:30, 37:30). About 0% read-and-react. This is all original demo and assertion.

### 7. Demo

Most of the video. It sounds live and lightly prepared: he runs real prompts on his real threads ("This one is restore working thread drag references. If I wasn't filming right now, I'd probably go and see if we can finally get these PRs landed", 17:00). Setups are brief ("I'll do a kind of silly demo to show what I mean", 06:00). Rough edges stay in: "Gemini's a little annoying you have to click a sign-in button" (07:00), "I don't think I got that in this build yet" (23:31), "I don't sign into my accounts directly, so I can't show this next feature" (23:31), and a real surprise on camera: "Jesus, I didn't even know this. You can two-finger to look at the full 3D device" (26:01). He blurs a sign-in link (13:31). Nothing outright fails.

### 8. Retention devices

- Planted tease with payoff: "Make sure I mention webhooks later. I promise you want to hear that part" (14:30), paid at 31:00.
- Escalation framing: "make sure you stick around because the layered real fun stuff underneath is where most people find the magic" (09:30); "Would you believe me if I said we were just getting started?" (21:31).
- Withheld item: "It's also much faster, which I want to put in my list of three things, but I won't" (09:00).
- Pattern break: the "Theo from the future" pickup (31:31) and its exit "You can go back to whatever Theo was just yapping about" (34:01).
- Rants: Claude/Codex mobile apps (13:00), "I hate, hate, hate Windows ARM so much" (28:01), GitHub sarcasm ("the loved and not at all frustrating GitHub", 30:00).
- Self-deprecation: "It's made by Theo, which sucks. Probably the biggest issue with T3 Code" (37:30); the ex-partner joke (38:01); a gag about the team being "totally aren't Twitter shitposters" with an on-screen prop he hates (39:31, inferred: "I hate this thing so much. Bring it up back").
- Chat participation: "Ones in chat if T3 Code has affected your ability to go to bed on time" (37:30).
- Direct address to lapsed users (03:01) and to people on multiple subs (05:32).

### 9. Ending

The argument lands as identity positioning, not a verdict: "Everybody else is forcing code into a tab in their other apps. T3 Code is built for code" (39:01) and "T3 Code was built by engineers for engineers, and we are not compromising on that" (39:31). CTA: download, try nightly, file issues or join GitHub discussions, star the repo. Then credits. He names Julius, Maria, Shiv, Wout and Bilal, each with a specific contribution. Sign-off:

> "I just wanted to make sure that the future tools we build with wouldn't be super expensive private closed source things. And I'm thankful that the future for open source is bright... Thank you all for coming on this wild ride with me. I can't wait to see what we do next. And until next time, peace nerds." (41:31)

### 10. Voice

1. "But I'm going to be incredibly honest with you guys." (00:32)
2. "I'm going to be incredibly real and say I was almost a bit ashamed to push it." (01:01)
3. "It's hard to summarize what T3 Code is and I almost feel like a bad founder for it." (04:31)
4. "When I say everything else, I mean it." (05:00)
5. "I'll do a kind of silly demo to show what I mean." (06:00)
6. "If you thought you could, you're misremembering. That was T3 chat, not T3 code." (09:30)
7. "World-class remote control. What do I mean by this?" (10:01)
8. "They just do not work for this. It is hilarious that they pretend they do. They are so far from good. It's insane." (13:00)
9. "And I'll be real, it has not succeeded. I was so hopeful for that feature." (15:30)
10. "If the thing is working, get it out of my face. Don't bother me until it's ready." (20:00)
11. "to not destroy your ADHD if you're like me" (20:00)
12. "Want to make your chat width disgustingly wide? Feel free to. I'll judge you, but you can do it if you really want." (29:01)
13. "This one hurts me a bit, but we support pretty much every Git provider" (30:00)
14. "We've been being too nice to T3 Code. Let me go through the negatives fast. I actually wrote them down." (36:31)

Register: casual, spoken, sales-adjacent but self-mocking. Sentences are short claims chained with "and", "but", "so". Profanity is light here ("crappy", "hell", "shitposters"). Technical explanation stays at the level of user benefit, with one quick architecture aside (WebSocket server, 10:30). Rhetorical question then answer ("What do I mean by this?", "Why do you need the thread anymore if the code is merged?") is his main teaching move. The verbal tics "I'll be real", "incredibly", "genuinely", "super" show up constantly.

---

## Video 2: "Well This Was Unexpected..." (jKCjLzjmiaA, 27:05, uploaded 2026-08-30)

### 1. Topic and angle

Breaking news: OpenAI is ending Cursor's direct model access on November 12th after SpaceX acquired Cursor. Trigger: OpenAI's post plus quote-tweets from OpenAI's Tibo (Thibault Sottiaux, @thsottiaux) and Cursor's Michael (by context Michael Truell, Cursor's CEO; the caption gives only "Michael"). The stance is the friend of both sides who still picks fights. He calls the cut-off understandable (Astra distillation fears), calls distillation bans "bad for the ecosystem", calls both companies' comms childish, and ends with advice to "own your tools". The description's angle, "it's not really about Cursor", is paid off at 12:31 ("There's the important detail... This is because Astra..."). The title "Well This Was Unexpected..." is a pure curiosity gap that names neither company. The video pays it off in the first five seconds.

### 2. Hook (0:00-0:32)

> "Mom and dad are fighting and I'm going to be real with you guys, it's kind of stressing me out. For those who don't know, I've been a big fan of both Cursor and OpenAI for quite a while. For those who aren't reading the screen right now, what it says is the following. We're ending our partnership with Cursor following its acquisition by SpaceX... Yeah, this is real. Your Cursor subs will no longer allow you to use OpenAI models." (00:01)

> "So, instead of spending my weekend relaxing or doing weekend things, I'm stuck here on a Saturday night filming a last second video... I've talked to my friends at both Cursor and OpenAI in order to get as many of the important details as I possibly can." (00:01-00:30)

Mechanism: a family-drama metaphor for corporate conflict, then the news read straight off the screen (inferred: the OpenAI post), then urgency (Saturday night, last-second video) and insider access (talked to friends at both). It promises "what's actually going on" and "what you can do to work around these limitations". It withholds the real reason, which he flags later as "a little bit at the end I feel like almost everyone has been missing" (03:00).

### 3. Lead-in

- Sponsor bridge (00:32): "I have a bad feeling I'm about to piss off both mom and dad. So, let me cover my bases quick with a word from today's sponsor." It calls back to the hook metaphor.
- Sponsor: WorkOS, 00:32 to about 02:31, roughly 2 minutes (7% of runtime, the highest share of the four). It opens with a scenario question to the viewer ("If you were building an app... Do you actually think you could do it?"). Exit: "Set yourself up for every customer at soydev.link/workos."
- Roadmap (02:31) in three explicit parts: "what is changing and how it affects things", "the personal drama... The beef forming between Tibo and Michael", and "most importantly, I want to save some time at the very end to cover how to work around this."
- Open loop (03:00): "there's a little bit at the end I feel like almost everyone has been missing that you should definitely pay attention to."
- Context and disclosure (03:00-04:31): SpaceX bought Cursor (the $10B partnership vs $60B acquisition options). Then: "I was an early investor in Cursor... I might make some money off this deal. I might not." "I have no bottom line tied to how I cover Cursor here." "If anything, I tend to be more harsh on the companies that I have financial ties to." "I also have no tie financially whatsoever to OpenAI. In fact, I spend a lot of money on OpenAI, so take that as you will. Anthropic is still the company I pay the most."

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01-00:32 | Hook | Mom-and-dad metaphor, post read aloud, Saturday-night urgency. |
| 00:32-02:31 | Sponsor | WorkOS. |
| 02:31-03:00 | Roadmap | Three parts plus "the bit at the end everyone missed". |
| 03:00-04:31 | Context + disclosure | SpaceX acquisition, investor disclosure. |
| 04:31-08:01 | Read-and-react | OpenAI post line by line; how lab contracts work; Cursor once drove 70% of Anthropic's non-research inference; Anthropic's head of compute dunks; aside on Claude Code limits dropping 17%, with a subscribe plug; subsidy math (a $200 sub gets about $8k of inference). |
| 08:01-11:30 | Claim + history | "There's the detail that matters": distillation. Precedents: Anthropic cut off Windsurf, then xAI-via-Cursor, then OpenAI's own API access. A live fight with the NYT paywall. His opinion: distillation is fair, bans hurt the ecosystem. |
| 12:01-14:30 | Reveal + anecdote | Astra is the real reason. He explains the "double dipping" data incentive and tells a story about OpenAI engineers using Cursor during GPT-5 early access. |
| 14:30-21:30 | Drama breakdown | Tibo's post ("decent"); an OpenAI contact confirming T3 Code is safe; Michael's post ("egregious wording"); token-share rebuttal with Artificial Analysis and CursorBench numbers; Tibo's reply; "that's my job". |
| 21:30-25:30 | Advice | Subscribe to the labs directly; T3 Chat economics; Grok as a fallback; his own spend; open-source alternatives; a T3 Code plug; "own your tools". |
| 25:30-26:15 | Rant | Google bans subscription use in third-party apps; Antigravity is "sinfully bad". |
| 26:15-27:05 | Recap + sign-off | "This sucks. It is what it is." |

Split: about 9% hook and roadmap, 7% sponsor, 5% disclosure, 50% reading posts and analyzing them, 15% advice, 3% rant, 3% close.

### 5. Thesis and arguments

Thesis: OpenAI is cutting Cursor off because it fears Elon will distill the upcoming Astra model through Cursor's data, and users lose either way, so you should own your tools and buy models directly from the labs.

Argument order:
1. Contracts and margins explain how this is even possible (05:01).
2. Distillation is the stated reason, and it has precedent (08:01-10:01). The precedents are all Anthropic's ("there isn't a precedent for OpenAI doing it, which is really strange").
3. His counter-opinion: distillation is legitimate and bans are hypocritical, because the labs collected their data early (11:01).
4. Astra is the real driver (12:31), then the double-dipping explanation (13:01).
5. Both sides' comms were bad (15:02-21:30). The 5% figure is the centerpiece rebuttal.
6. Practical consequence and what to do (21:30).

Steelmanning and balance: "This does make why OpenAI is doing this more understandable. It doesn't make it better or worse in my opinion" (12:31). He defends Tibo's first post ("No issue with how Tibo framed this", 16:01), then says Tibo's second post was right on substance but unnecessary: "Everything Tibo said here is true and it was entirely unnecessary" (21:00). He grants Cursor sympathy: "to their credit, OpenAI did drop this news pretty harshly on a Friday evening, forcing them to scramble" (20:31). Before criticizing Michael he softens it: "So, know that this is coming from a place of love" (16:30). Bias disclosures come early and in detail (03:30-04:31). A conflict he does not flag: plugging T3 Code (24:00, 25:01), though he half-admits it with "I am tempted to just plug T3 Code here."

### 6. Evidence

- Posts read aloud: the OpenAI post (most of 04:31-14:00), NotTomBrown's post (05:31; by context Anthropic's head of compute), Tibo twice, Michael once. He reads a sentence, then reacts.
- Linked articles: NYT and a distillation article, skimmed and fumbled live.
- Numbers: $10B/$60B, 70% of Anthropic inference, 17% limit cut, $8k of inference per $200 sub, 20-30% vs 80-95% discount, Artificial Analysis tokens per task (17k Soul vs 36k Fable), CursorBench (70.5% vs 67.2% score; 28k vs 103k tokens), "$2 vs $20" per prompt on T3 Chat vs ChatGPT, his own "a grand a month" in subs buying "upwards of a hundred grand a month" of inference.
- Insider talk: "I had a contact at OpenAI hit us up making sure we knew that this will not affect T3 Code" (15:30).
- Personal history: the OpenAI office visit during GPT-5 early access (13:30).
- About 55% is read-and-react. The token-efficiency rebuttal (18:00-20:31) is the main original analysis.

### 7. Demo

None. The nearest thing is fighting the NYT paywall on camera, kept in: "Okay, there we go. Nope. I have to refresh over and over to get it" (10:30).

### 8. Retention devices

- Hook metaphor called back at the sponsor bridge (00:32).
- Open loops: "a little bit at the end... almost everyone has been missing" (03:00), "there is one other thing that they are really scared of that we'll get to at the end of this post" (10:01), paid at 12:31.
- Spoiler aside: "which spoiler, the reason Grok got so much better is because they bought Cursor" (03:30).
- Cross-promo tease: "I have a whole video about this coming tomorrow. So, keep an eye out for that. Make sure you're subscribed" (07:00).
- Joke about his role: "that's my job. Let me do this, man" (21:00).
- Pattern-break rant with an apology: "Speaking of which, hey Google, what the [hell]" (25:30) … "I ah, sorry, I've been holding that one in for a while. I'm pissed at Google... Okay, sorry. Just had to get that out of me" (26:00).
- Direct empathy: "And to those of y'all who I know use 5.6 Soul in Cursor every day, I'm sorry" (26:30).

### 9. Ending

The argument lands as a generalization: "make sure you own your tools and that your relations with the products that you rely on are direct... I have a feeling this is not a one-off thing. If anything, it's the start of the end" (25:01). After the Google rant he gives an emotional recap rather than a lesson:

> "This sucks, especially for somebody who likes both of these companies... Astra's probably going to be great, and I'm excited for the future. But god damn, this moment sucks... You will not get access to Astra in Cursor, and you will lose access to all OpenAI models in November as well. This sucks. It is what it is. I'm sorry. I hope this update was useful and until next time, peace nerds." (26:15-27:01)

The CTA is implicit: try the alternatives (Superset, others) and T3 Code.

### 10. Voice

1. "Mom and dad are fighting and I'm going to be real with you guys, it's kind of stressing me out." (00:01)
2. "For those who aren't reading the screen right now, what it says is the following." (00:01)
3. "I have a bad feeling I'm about to piss off both mom and dad." (00:32)
4. "So, let's start with the official post." (03:00)
5. "If anything, I tend to be more harsh on the companies that I have financial ties to." (04:01)
6. "In fact, I spend a lot of money on OpenAI, so take that as you will." (04:31)
7. "But yeah, anyways, let's read what they said." (04:31)
8. "And there's the detail that matters." (08:01)
9. "you get the idea everyone distills" (11:01)
10. "It is what it is though. I've given Anthropic [shit, inferred] for doing this. I will do the same to OpenAI." (11:30)
11. "There's the important detail." (12:31)
12. "They have enormous respect for the team, the product, yada yada yada. Trying to play nice." (13:30)
13. "So, know that this is coming from a place of love" (16:30)
14. "This is egregious wording in my opinion" (17:01)
15. "I'm going to be real with you guys, you're kind of screwed" (21:30)
16. "The value you get for a $200 Claude Code sub or $200 Codex sub just shits all over what you can get anywhere else." (23:02)
17. "There is no ifs, ands, or buts about it." (26:30)

Register: conversational commentary with a mild moral voice ("egregious", "childish", "bad optics"). Profanity is moderate and peaks in the Google rant. For the mixed audience he explains business mechanics in plain terms (contract margins, why tokens are a bad usage metric) and walks the numbers slowly: "if anthropic models are three times less token efficient, then the 5% should be thought of more like 15%" (20:02). The phrase "It is what it is" shows up three times as a resigned closer.

---

## Video 3: "Fable Vs Astra Debate Is Over" (P7bxbDSnZRM, 76:51, uploaded 2026-09-11)

### 1. Topic and angle

A head-to-head of Anthropic's Fable 5.1 and OpenAI's GPT-6 Astra, the two new frontier models, across about 20 categories, ending in "which sub should you buy?". Trigger: both releases plus weeks of heavy use (130B tokens of free early access). The stance: Astra wins almost everything outside code (3D, computer use, science, orchestration, cost, limits), Fable wins code you can merge and is more consistent, and Astra is "spiky". The title claims a settled debate. The actual verdict is split: "I will be defaulting to Fable for code and I'll be defaulting to Astra for every other thing" (75:02). He does answer the "if I had to pick one" question (Astra, 72:31), so the title is half paid off and half reframed.

### 2. Hook (0:00-1:30)

> "Last week was pretty crazy for new AI models. We got two new heavy hitters that are truly changing the game. Gemini 3.8 Flash and Muse Spark 1.3. How can you ever decide between those two? They're both so incredible. Obviously, I'm joking. We're actually here to talk about Fable 5.1 versus GPT-6 Astra, the two actual models that matter. And I'm sure my attention guy already wants to kill me for doing that joke and confusing people." (00:02)

> "These models are both incredible. If you want to just skip to the end to see which model's better, I guess you could do that, but you'd miss all of the different ways we can compare them... I'm doing nearly a billion tokens a day across both of these models consistently." (00:32-01:01)

Mechanism: a fake-out joke (naming minor models as if they mattered) as a pattern break, then a meta-joke about his retention editor, then credibility (a billion tokens a day), then a checklist of questions he will answer: "what these are good at, what they are bad at, how efficient they are with token usage, how hard the subscription limits will hit you... and of course, the most important question, which sub should you buy today?" (01:01). He openly concedes the skip-to-the-end option and argues against it. The verdict is withheld for 70 minutes.

### 3. Lead-in

- Sponsor bridge (01:30): "I'll do my best to answer all of that after a real quick break for today's sponsor."
- Sponsor: Macroscope, 01:30 to about 03:50 (2:20, 3% of runtime). It is tied to his own repo: "this is a real file in the T3 Code codebase" (02:30), "We're about to break a thousand open PRs" (02:30). Exit: "The best way to stop it is at soydev.link/macroscope."
- Transition into structure (03:50): "So, we have all the different ways we want to compare these models. Let's start with what I'm sure everyone is here for, science, because this is a science channel, right? Okay." The on-screen structure is inferred to be a category board or tier chart he moves an arrow across ("move the arrow over here to gamedev for a sec", 08:31). It has sections: non-code, front end, code, agent stuff, cost.
- No separate credentials block. His credentials are spread through the video (billion tokens a day, 5 Claude and 4 Codex accounts, $30-40k of inference a month).

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:02-01:30 | Hook | Fake-out joke, credibility, question checklist. |
| 01:30-03:50 | Sponsor | Macroscope. |
| 03:50-05:30 | Benchmark comparison | Science: Fable 5.1 doubled to 50%, but low-effort Astra hits 54.3% at a third of the price. "Go get a Codex subscription." |
| 05:30-09:30 | Demo + nuance | 3D: fish-slop game demos side by side, Astra is a "generational gap"; Blender examples from others; but Fable is better at interaction. Workflow tip: prototype with Astra, polish with Fable. |
| 09:30-11:20 | Personal experience | Computer use: Astra "clears"; he bought a Mac Mini to run it 24/7. |
| 11:20-14:00 | Demo + rant | Copywriting: both better, Astra slightly ahead, but it spams all-caps subtitles (21 counted) and "the more I stare at this, the more I hate this model." |
| 14:00-17:45 | Skeptic segment | Audio and video: both disappoint. Ben Davis's Final Cut setup demo is the exception. A 2020 GPT-3 demo throwback as the analogy. |
| 17:45-18:00 | Section recap | Non-code goes to Astra. |
| 18:00-22:30 | Demo comparison | Front end: landing-page one-shots (the word "little" counted 15 times), Fable's one-shot is "actually genuinely compelling", but neither is above 5/10. |
| 22:30-24:30 | Characterization | Full stack: a tie. Fable "has better intuition", Astra is "the smartest model that acts like it's dumb". Plants the "spiky vs steady" theme. |
| 24:30-33:00 | Long-form case study | Giant rewrites: TypeScript-to-Rust port (30% → 82.6% of tests), 40-subagent tease, bias disclosure, T3 Code rebuilt in GPUI, live ping.gg rewrite reveal ("reuse as much UI code as possible"). |
| 33:00-40:00 | Claim + chart | Mergeability: Fable PRs need 2 follow-ups, Astra 6. Hand-drawn "vibe chart" placing Astra near Fable 5. Ben Davis concedes. Podcast plug. |
| 40:00-42:00 | Short verdicts | Scope creep (Fable), gamedev (Fable "feels nice to play"). |
| 42:00-50:00 | Horror story | Understanding intent: the marketing-site autoscroll "revert" fiasco, with the same prompt fixed by Fable in 5 minutes. "The most bad model experiences I have had of any model this year." |
| 50:00-52:30 | Praise | Orchestration "swarms" (callback to the 40 subagents), "the path to something like curing cancer". |
| 52:30-54:30 | Praise | Steering and async questions, with a T3 Code plug ("does this feature better than Codex"). |
| 54:30-57:30 | Quick verdicts | Self-prompting and skill writing (Astra, slightly), skill using (Fable, by a lot; he blames the Codex system prompt), refusals and boundaries (Fable). |
| 57:30-62:30 | Explainer + rant | Cost: cache reads are 3% of his spend and cache writes over 60%; he scolds a chat member; Artificial Analysis cost per task ($3.26 Astra vs $7.60 Fable 5.1). |
| 62:00-63:00 | Data | Token efficiency (27k vs 80k), Flex tier. |
| 63:00-70:30 | Buying advice | Subscription limits: "Opus pot", the 50% Fable cap, $8k vs $12k of inference per plan, 5-hour limits, resets, a defense of Tibo. |
| 70:30-75:30 | Verdict | Hand-drawn quality-over-time lines (orange Fable steady, blue Astra spiky), "blood pressure", "I would pick Astra". |
| 75:30-76:51 | Coda + sign-off | Refusals twist, "they compound each other". |

Split: 2% hook, 3% sponsor, about 18% non-code, 5% front end, 35% code and agents (the rewrite and intent stories alone take about 17 minutes), 17% cost and limits, 8% verdict.

### 5. Thesis and arguments

Thesis: Astra is the more capable and far cheaper model and wins nearly every category, but Fable 5.1 writes more mergeable code and fails less badly, so use Fable for code and Astra for everything else.

He orders the categories from least to most important to his audience, says so ("then we get to what you guys are all actually here for", 14:02), and saves cost and the verdict for last. Each category gets a winner. Astra's wins come with a fast concession ("This does have its flaws", 07:00), and Fable's wins come with a defense of Astra ("Notice how I didn't say that", 34:31).

Counterarguments and bias management:
- Pre-empts accusations of favoritism: "if you think I'm just showing this... because I'm trying to glaze Astra, go watch my video on Kimi K3" (07:00).
- Bias disclosure: "I will also admit to a bias here... when I'm doing early access testing... It does not count towards my usage... I did 130 billion tokens with this model during the early access" (26:31-27:00); "I've never had free unlimited access to Fable before."
- Rejects his own audience's excuses: "And to those saying, 'Oh, it got lost in compaction or something.' No, it didn't. I had it on ultra with one mil token context windows" (31:32).
- Pre-empts the "you're too picky" objection: "You could say that I'm being too picky... or you could just use Fable" (33:00).
- Admits personal context: "I sent these prompts pretty late in the evening drinking with some friends on a weekend" (43:02).
- Corrects how his own past claims get read: "it is perceived by everybody, including my friends at OpenAI, as me saying that Astra is constantly throwing up unmergeable slop. Notice how I didn't say that" (34:31).
- Hedges on video editing: "I should not be the only voice you hear" (14:31).
- Calls on a friendly opponent: Ben Davis, "OpenAI's number one defender", "has admitted that he thinks Fable is way better than he expected" (36:30-37:00).

### 6. Evidence

- Lab launch notes and benchmarks (science bench, Artificial Analysis cost per task and tokens per task), read quickly for the number, not line by line.
- His own artifacts on screen: fish-slop 3D and 2D games, landing pages (from "Dra" and others; caption names uncertain), the ping.gg rewrite, the T3 Code GPUI build, the Rust port thread with 40 subagents, the marketing-site PR history and commits.
- Counting as evidence: "there were 21 unnecessary subtitles" (13:02), "The word little appears on this page 15 times" (19:32).
- His own metrics: 2 vs 6 follow-ups per PR (33:31), 150 PRs YOLO-merged with 2 regressions (both Astra, 42:31), 30% → 82.6% test pass rate, 60% of his Fable spend on cache writes, $30-40k a month in inference.
- Hand-drawn charts, openly called non-scientific: "This is the most vibe based chart you're going to see in a while. I promise" (34:31).
- Other people's demos: Ben Davis's Final Cut setup, Blender scenes, a chat member's 50/50 poll, "Binary Shokan" in chat, "Raphael" on 8 resets in 30 days.
- Under 10% read-and-react. This is his most original-argument video of the four.

### 7. Demo

Many, mostly prepared beforehand and replayed: games, landing pages, PR diffs. One live wait is left in: "Since I hit yet another obnoxious case with Codex where since I was in work mode... I can't actually open the terminal. I have to wait for this... So while I wait for that, I'm going to show you what ping normally looks like" (28:31). He fills the gap with a tour of the original app, his camera feed included ("Hi. You might recognize him", 28:31). He checks live usage mid-video ("how much am I [burning]... Not too bad", 25:32; "it's at 82%... down one more percent", 65:30) and steers a running agent on camera ("You have my permission to do whatever you need to do... Keep going", 25:32). Failures are the centerpiece, not something left in by accident: the ping.gg UI destruction and the revert story are told with commit-by-commit screens.

### 8. Retention devices

- Fake-out opening and the "attention guy" meta-joke (00:02).
- Planted callbacks: "Remember those 40 sub agents, though, because we'll be talking about that in the agent section" (26:31), paid at 51:30; the "spiky" theme planted at 24:30 ("We'll come back to that theme in a bit"), paid at 70:30; "we'll talk more about understanding intent later. Don't you worry" (32:00); "I have an important thought that I need to pencil till later" (50:01).
- Quiz-style reveals: "But do you know what the worst part is?" (30:30); "There's one particular word I used in this prompt... You know what word it was? I'll give you a hint" (44:00).
- Escalation inside a story: wrong dev server, then blocked host, then a commit of his private Tailscale host, then a killed server, then "it merged the PR... after I told it you didn't make the changes" (46:00-47:31).
- Pacing cues: "Let's blast through the rest of these" (50:01), "I'll wrap up code super quick" (41:01).
- Rants: subtitle spam (13:30), cache writes ("I am paying Anthropic more money to manage RAM for me", 58:30), and scolding a named chat member ("Bill, you're better than this", 59:31).
- Throwback pattern break: the 2020 GPT-3 React demo (16:01).
- Self-deprecation and personal life: "I'm currently down a hand" (11:01) recurs three times; "I would pick Astra and have it write DMs to Julius so that he could send off the prompts using Fable for me" (72:31).
- Coda twist: "Remember everybody being really upset about Fable's security refusals? Astra refuses more often. Just wanted to put that one out there" (75:31).

### 9. Ending

The verdict lands on the drawn chart: "When I send a prompt to Astra, it's equal chances it drops my jaw because I'm so blown away... or it drops my jaw because I cannot fathom that I just spent a thousand dollars for it to run in a loop and not ship anything and then break my website" (71:31-72:01). Advice is split by viewer type: easily stressed people should pay for Fable; people who use a computer professionally and earn over $100k should get the $200 Codex plan; budget users should wait for cheaper models. The summary line: "its smart spikes are not quite as smart, but its stupid spikes are way less stupid" (75:02). Close:

> "They don't replace each other, they compound each other. These models are great and you shouldn't feel bad using one or the other... And pretty much everyone who can have the Codex sub probably should because it's such an insane deal. Have fun burning tokens and using all these models. I think they're awesome and I bet you will too. Until next time, peace nerds." (76:00-76:51)

### 10. Voice

1. "Obviously, I'm joking." (00:02)
2. "And I'm sure my attention guy already wants to kill me for doing that joke and confusing people. So, sorry. Well, let me have some fun." (00:02)
3. "Let's start with what I'm sure everyone is here for, science, because this is a science channel, right? Okay. Seriously though" (03:50)
4. "I'd say this looks slightly better, just a little. It's a generational gap here." (06:30)
5. "It really does feel like a sledgehammer." (09:31)
6. "The more I stare at this, the more I hate this model." (13:30)
7. "I do want to make a few things clear before I go on the utter brutal roast session I'm about to do." (18:00)
8. "good designs still require you sit there with a hammer and beat the [shit] out of the model" (22:01)
9. "Astra is the smartest model that acts like it's dumb." (24:30)
10. "I will also admit to a bias here" (26:31)
11. "This is layers upon layers of sins." (30:02)
12. "It is what it is." (37:00)
13. "Notice how I didn't say that." (34:31)
14. "I'll be real. If 5.6 Soul screwed this up, I would have been insulted." (49:01)
15. "It's like saying that macOS is a 100 times faster than Windows because it gets through the splash screen at boot 30 milliseconds faster." (60:00)
16. "I would love to meet the person who convinced you Claude was a better deal so I can hire them... they sold you a bridge, man." (63:30)
17. "Its smart spikes are not quite as smart, but its stupid spikes are way less stupid." (75:02)

Register: high-energy review voice. He coins compact verdict phrases ("Astra mogs", "Opus pot", "groundhog day feeling", "sledgehammer"). Profanity is heavier than the T3 Code video (god damn, pissed, "shitty", "ugly ass", "dick around"). Technical explanation runs through analogies (the splash screen for cache costs, "getting the room ready" for editor setup, the GPT-3 demo for AI video editing) and through walking one number at a time ("Four times cheaper for 3% of your cost is a less than 1% deal", 60:00). Each category ends on a short winner sentence ("So yeah, skill writing. Astra has a slight lead. Skill using. Fable has a huge lead", 56:31).

---

## Video 4: "Did AI Kill React Native?" (oPZLPUtmROo, 62:53, uploaded 2026-09-14)

### 1. Topic and angle

Shopify announced it is moving from React Native back to native Swift and Kotlin, because coding agents made building twice cheap. Trigger: Shopify's engineering blog post "Native is now the future of mobile at Shopify" plus reaction tweets from Jamon Holmgren (Infinite Red), Tobi Lütke (Shopify CEO; the caption says "Toby") and Jay Meistrich (Legend List). Stance: Theo, a long-time React Native defender, argues Shopify undersold React Native's real strengths (OTA updates, Expo, Meta's native talent), skipped the obvious fixes (new architecture, Expo), and over-engineered its migration. Then he concedes the uncomfortable part. AI does erase React Native's hidden edge, the gap between your native devs and Meta's, and Meta is disbanding the team. The question title gets a nuanced "partly yes" at 55:31-56:30 and in the summary at 59:30.

### 2. Hook (0:00-1:59)

> "This video is going to be quite a throwback. I almost feel like I should bust out the blonde hair and the mustache again for it because we're really going back here because we're talking about React Native... And as I'm sure many of y'all know, I am quite a defender. One of my first big like impactful so to speak videos was when I covered the old Airbnb article about why they moved off of React Native." (00:01)

> "There was one thing that helped a lot though. Shopify. They made the move to React Native and showed some crazy wins... It ended up being a huge moment for React Native... which is why this sucks. For those who are listening instead of watching, Shopify has just announced their plans to move off of React Native and go back to native code." (00:31-01:00)

Mechanism: personal history first (his old look, his breakout Airbnb video, the Twitch fight), which turns the news into a personal loss. The reversal ("which is why this sucks") lands only after he has built Shopify up as React Native's hero. He then claims unique standing: "I've been building more React Native than ever recently. And more so, I've been building native, too" (01:30). Promise: "a lot of layers for this one, and I can't wait to unravel all of them with you." He withholds his verdict and the "changes going on at Meta right now" (01:30).

### 3. Lead-in

- Sponsor bridge (01:30): "But since my Shopify store isn't doing particularly well, we're going to have to make some money with a quick sponsor break." It is a joke tied to the topic.
- Sponsor 1: Greptile (T-Rex sandboxed review), 01:59 to about 03:31, roughly 1:30. Exit: "get that today at soydev.link/greptile. Let's dive in where it matters."
- Roadmap 1 (03:31): "We'll start with what they said, then I will go into some conspiracy theories about where the market is moving, what I've been doing, and then try to wrap it all into a nice package of how software dev is changing. I've done such a good job not mentioning AI yet and I will do my best to not until I have to."
- Roadmap 2 (15:31), after the reading: "we'll start with the real benefits of React Native that I feel like were missed. Then we'll go to the weirdness of Shopify... Then we'll go to what moving off of React Native actually looks like as someone who has been doing it and the state of the React Native team." Four sections, all delivered in order.
- Sponsor 2 (mid-roll): Convex, 46:30 to 48:00. In: "We're going to have to do another quick sponsor break so I can pay for my therapy and then we'll get to the real important detail here, which is what's about to happen to React Native itself." Out: "Figure out why at soydev.link/convex. Okay, I did promise we'd go to what's happening to the React Native team, but I want to finish up my story about these ports." Combined sponsor time is about 3 minutes (5%).

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01-01:59 | Hook | Throwback, Airbnb video, Shopify as hero, reversal. |
| 01:59-03:31 | Sponsor 1 | Greptile. |
| 03:31-03:50 | Roadmap 1 | |
| 03:50-15:30 | Read-and-react | Shopify's article paragraph by paragraph, with Jamon's tweets cut in; library fates (Skia to William Candillon, FlashList, Restyle archived); greenfield rewrite in 12 weeks; Helix checkpoints; headless CLI. Rising contempt ("criminally overengineered"). |
| 15:30-16:00 | Roadmap 2 | Four sections. |
| 16:00-25:30 | Explainer (section 1a) | What Shopify missed: OTA updates (iPhone mini scenario, Twitch stats, a live check of his phone showing 54 pending updates, a long chef-and-kitchen analogy), Expo and the dev-client loop, signing pain in his native T3 Code fork. |
| 25:30-31:30 | Steelman (section 1b) | Real negatives: library bloat (but the app-size myth is busted: native saved only 1 MB), footguns ("the average React Native dev is worse than the average native dev"), a moving target, dependence on Meta. "Notice what isn't in this list": performance. |
| 31:30-38:00 | Critique (section 2) | Shopify's weirdness: skipped the new architecture, didn't use Expo, T3 Code's app loads faster than Shop. Then Tobi: repeats the "decided over a weekend" allegation, reads Tobi's reply, flips on air ("this one flipped me"). |
| 38:00-46:30 | Personal story (section 3) | His own ports: Soul built a Swift/AppKit app in 2 hours; the AppKit/UIKit/SwiftUI mix-up; SwiftUI lists are hell; the swipe-back gesture saga with Julius and the Defcon Android user; the twist that iOS Settings doesn't use the native stack. |
| 46:30-48:00 | Sponsor 2 | Convex. |
| 48:00-51:30 | Evidence + jab | Port story continued: shows his one-line prompt and the hour-long autonomous port, a public TestFlight with about a thousand users, "I've not read a line of the code". "I don't know what went wrong at Shopify." |
| 51:30-59:30 | Claim (section 4) | The React Native team: Jay Meistrich's claim that React Native beats native; a quiz on headcount (React core under 30 vs React Native over 300); "the best native devs I have ever met... were on the React Native team"; Codex is now that native dev; Meta disbanding the teams (Lauren Tan, "poteto"); a subscribe bargain over an Electron video. |
| 59:30-61:30 | Synthesis | Bold bets, "learn once, understand everywhere", make someone daily-drive Android. |
| 61:30-62:53 | Engagement plea + sign-off | |

Split: 3% hook, 5% sponsors, 19% article reading, 25% explainers and steelman, 10% Shopify critique, 19% personal port story, 13% React Native team argument, 6% synthesis and plea.

### 5. Thesis and arguments

Thesis: AI didn't kill React Native on technical merit, since Shopify's reasons are weak, but it did erase React Native's real moat, borrowing Meta's elite native engineers, just as Meta stopped investing in the team.

Argument order:
1. Rebut the framing: the article over-weights write-once multiplatform, "I don't think that is the biggest strength of React Native" (05:00).
2. The missing strengths, OTA updates and Expo (16:00-25:30), argued through a hypothetical scenario, real Twitch data and a live phone check.
3. Steelman with real negatives (25:30-30:30), then point to what's absent: "Notice what isn't in this list though... I didn't put performance in here" (30:30).
4. Shopify was a weird case (31:30-38:00): no new architecture, no Expo, a top-down CEO.
5. Counter-evidence from his own port (38:00-51:30): agents port well, so Shopify's elaborate Helix process is unnecessary.
6. The real cause (51:30-59:30): React Native's edge was Meta's native talent; "do you know who else is really good at native code? ... It's Codex" (55:31). Add Meta disbanding the team, and the moat is gone.

Concessions and reversals:
- Admits being wrong live: Tobi's reply "flipped me" (36:30, 38:01). "I hope this isn't him putting off blame... But if this is actually the case, which I do trust him there, I'm on his team" (37:01).
- Admits being wrong in his story: "I did a thing I almost never do. I concluded that Julius was wrong. And as always, I regret that" (44:00).
- "The average React Native dev is worse than the average native dev. This is a fact" (28:00), then the defense: "most bad devs picking a technology does not mean the technology is bad."
- "I'm not going to pretend my app is as complex as Shop" (51:01).
- Hedges on his port: "there's a lot of things the React Native app is faster with than this, especially the list" (49:02).
- Disclaims Meta-bashing: "I'm not saying Meta, evil, bad, terrible" (30:01), and on the team, "I'm not saying like React Native team's horrible now. It's actually the opposite" (59:31).
- A self-correction left in: "I know Skia is actually technically from Android and Chrome, but in this case it is largely associated with Flutter. Whatever. We don't need to go that deep in the weeds, guys" (08:30).
- Bias: a self-described defender (00:01). His own products are in play (the T3 Code React Native and Swift apps), and the Convex sponsor is framed as his own preference.

### 6. Evidence

- The Shopify article, read paragraph by paragraph with interjections (03:50-15:30). It is the longest single read in the four videos.
- Tweets: Jamon ×2, folded in as agreement ("Thank you, Jamon... called it the same thing I did", 04:32); Tobi's reply read in full "out of courtesy" (34:30); Jay's benchmark claim (52:00).
- Shopify's own numbers turned against it: "They shaved a whopping 1 megabyte by moving to native. Wait, what? It's bigger?" (26:30).
- Personal data: at Twitch "half or more of the users were on a version of the app that was at least two versions old" (17:01); his phone's 54 pending updates (17:32); ports in under 3 hours.
- Insider claims: Tobi's weekend decisions "allegedly" (34:30), the React/React Native headcounts as "my understanding" (53:00), people leaving Meta.
- Analogy as evidence: the chef in a kitchen (19:00-21:01), the window/DOM thought experiment (53:32).
- Own product as proof: his T3 Code SwiftUI app and the prompts he gave it (49:31).
- About 25% read-and-react (article plus Tobi plus tweets); the rest is original argument and story.

### 7. Demo

Small live checks rather than a built demo:
- Phone app-update check, live, with a surprise left in: "It says none right now, but now that I scrolled, 54" (17:32).
- An on-screen diagram of swipe zones (inferred: "let's say this is your mobile app... I have a section here", 42:30).
- Live iOS Settings check: "If I swipe from the left, it works fine. But ready for this? If you swipe from the middle, it does too" (45:31).
- A walk through his real port thread and prompt (49:31-50:31).

All sound live. The port itself was done offline and is narrated as a story.

### 8. Retention devices

- Two explicit roadmaps (03:31, 15:31) and frequent "we'll get to that" markers: "We'll talk about what that is and why it matters in a little bit" (04:32), "This will be one of the most important parts of this video when we get there" (15:00), "which we'll talk about plenty, don't worry" (23:00), "which we'll get to, don't worry" (49:02).
- Withheld topic as a running gag: "I've done such a good job not mentioning AI yet" (03:31).
- Escalating disgust while reading: "Oh god, I'm going to have so many things to say" (07:00), then "I don't love this approach" (12:31), then "My [fucking] god, they'll overengineer anything" (13:31), then "These are CRUD apps" (14:06), then "I'm going insane" (14:31), then "Oh man, this is criminally overengineered" (14:31).
- Writing a statement down on screen: "I'll just write it down because I want you guys to know I mean it" (28:00).
- Quizzes to the viewer: "how many engineers do you think Meta had on both? Do you think they had 50 on both, 500 on both?" (53:00), "I'll give you a hint. It's Codex" (55:31).
- Story twist: "this is my favorite part the the twist you didn't expect" (44:30), then an invitation to the viewer: "If you're on an iPhone right now, I would like for you to open it and go to settings" (45:02).
- Mid-roll sponsor used as an act break with a promise (46:30).
- Rant plus apology: "Sorry, I've been waiting for an opportunity to crash out of this one for a while" (46:30).
- Future-video bargain: "If I see a huge spike in subs from this video, I'll know you actually want me to talk about tech again. And then I'll do an Electron video" (56:30).
- Android jokes as comic closer (61:30).

### 9. Ending

Synthesis first: Shopify's move is a bold bet like React Native once was, and "It was never write once, run everywhere. It was learn once understand everywhere" (61:00). Practical takeaway: test on both platforms, "make someone daily drive Android on your team" (61:30). Then the most explicit engagement plea of the four:

> "I don't think this video is going to perform well, so please prove me wrong. If you liked it, subscribe, give it a like, leave a comment, and send it to a friend... But if this video bombs, then you're going to get what you ask for. So, for once, I'm asking you engage. I hate doing this... Otherwise, I'm going to have to do what people actually care about. Not because I am following the money, but because I want the things we talk about to have impact... Thank you as always and until next time, peace nerds." (61:30-62:53)

### 10. Voice

1. "I almost feel like I should bust out the blonde hair and the mustache again for it" (00:01)
2. "which is why this sucks. For those who are listening instead of watching" (01:00)
3. "It's going to be a lot of layers for this one, and I can't wait to unravel all of them with you." (01:30)
4. "Let's dive in where it matters." (03:31)
5. "But back to the reading." (05:00)
6. "Whatever. We don't need to go that deep in the weeds, guys. Come on. Let me make this easy for the people who aren't as familiar." (08:30)
7. "You think your codebase is harder to work in just cuz it's huge? Come on." (11:00)
8. "My [fucking] god, they'll overengineer anything." (13:31)
9. "Cool. Where do I start? [sighs]" (15:00)
10. "Imagine there's an incredibly skilled chef in a kitchen." (19:00)
11. "So yeah, app size is not what we're talking about here." (27:01)
12. "And this is going to be one of the most horrible things I say in this video. I'll just write it down because I want you guys to know I mean it." (28:00)
13. "Notice what isn't in this list though." (30:30)
14. "I feel like people miss the word native in React Native a lot." (31:01)
15. "Okay, this one flipped me." (38:01)
16. "So tell me again about how Apple's developer experience makes better feeling apps than the people who are fixing all the [shit] themselves." (46:00)
17. "To anybody who says vibe coding makes everything easy, the only thing it made easy was the implementation after two weeks of crashing out." (46:30)
18. "It was never write once, run everywhere. It was learn once understand everywhere." (61:00)

Register: veteran insider, protective of his tech, the most profane of the four (bleeped in captions). The video teaches more than the others: he defines OTA from scratch, explains Expo as "the Next.js/Vercel of the React Native world" (22:30), and drops detail for beginners on purpose. Sentences run long when he tells stories and turn punchy when he judges ("These are CRUD apps."). "Notice how I never said..." appears three times in the synthesis (60:31) as a rhetorical recap.

---

## Patterns across these 4

### Hooks

What they share:
- The first sentence is about Theo, not the topic: "Julius and I got really hyped", "Mom and dad are fighting... it's kind of stressing me out", "I almost feel like I should bust out the blonde hair", and even the Fable fake-out is his own joke. The news arrives second, framed by how he feels about it.
- An emotional stake gets named early: ashamed, stressed, "this sucks", "blown away".
- Credentials arrive within 60 seconds and are specific: half a million users, insider friends at both companies, "a billion tokens a day", "one of my first big impactful videos".
- The hook ends on an explicit promise of what you'll learn, then goes straight to the sponsor.
- He narrates the screen for listeners: "For those who aren't reading the screen right now" (Cursor), "For those who are listening instead of watching" (React Native).

How they differ: the T3 Code hook is a confession arc (humility, then pride). Cursor's is a metaphor plus the raw news read aloud. Fable's is a fake-out joke that breaks the fourth wall ("my attention guy"). React Native's is nostalgia leading to a reversal. News videos get to the news in 10-60 seconds. The product and review videos spend 1-3 minutes on framing.

### Shared skeleton (share of runtime)

1. Hook with personal stake and credentials: 1-7% (0:30 to 3:00).
2. A one-line joke bridge into the sponsor, tied to the topic: "piss off both mom and dad", "my Shopify store isn't doing particularly well", "it's quite expensive for us to run", "a real quick break". The sponsor reads are 1:30-2:20 each and land between 0:32 and 3:01. All four sponsors are dev tools, and three of four are tied to his own repo or workflow (Apify in Claude Code/T3 Code, Macroscope on T3 Code PRs, Convex as his stack). Sponsor share is 3-7%.
3. Exit from the sponsor straight into a roadmap or the first source with no pause: "Let's dive in where it matters", "So, let's start with the official post", "So, we have all the different ways we want to compare these models."
4. An explicit roadmap of 3-4 parts, or a visible category board. The hour-plus video repeats the roadmap after the first block.
5. Body: 75-85%. Read-and-react blocks alternate with original argument, personal anecdotes and rants.
6. Concessions or negatives section near the end (T3 Code's "negatives fast", Fable's cost caveats, React Native's real negatives in the middle).
7. Verdict and takeaway, usually a single rule for the viewer ("own your tools", "Fable for code, Astra for everything else", "make someone daily-drive Android").
8. Sign-off with "until next time, peace nerds" in all four, often right after "I think I've said all I have to" (T3 Code 38:30 and 41:00, Cursor 26:15, React Native 61:30).

### Recurring argument moves

- **Disclose, then claim independence.** Investor in Cursor, but "I tend to be more harsh on the companies that I have financial ties to"; free Astra tokens, so "I will also admit to a bias"; T3 Code is his, "we don't make any money off it".
- **Concede first, then hit harder.** "GPT-6 Astra has made massive improvements... I do want to make a few things clear before I go on the utter brutal roast session" (Fable 18:00); "React native apps can be fast... but" (React Native).
- **Correct how people will read him.** "Notice how I didn't say that" (Fable 34:31); "Notice what isn't in this list" (React Native 30:30); "I'm not saying Meta, evil, bad".
- **Pre-empt the comments.** "And to those saying, 'Oh, it got lost in compaction'... No, it didn't"; "If you thought you could, you're misremembering"; "if you think I'm just... trying to glaze Astra, go watch my video on Kimi K3".
- **Name the hidden variable.** The 5% traffic share is measured in tokens (Cursor); cache reads are 3% of spend (Fable); OTA is the real React Native benefit; Meta's native talent is the real moat. Each video has one "the number you're looking at isn't the number that matters" moment.
- **Change his mind on camera.** Tobi "flipped me"; "I concluded that Julius was wrong... as always, I regret that"; "I didn't think people were going to like this. Turns out they did."
- **Call a friendly opponent as witness.** Ben Davis, "OpenAI's number one defender", concedes Fable; Jamon "called it the same thing I did".
- **Use his own product as proof.** T3 Code shows up in all four: the subject in one, the "this won't affect T3 Code" reassurance in Cursor, "T3 Code actually does this feature better than Codex" in Fable, and "the T3 Code mobile app... loads way faster than the Shop app" in React Native.

### Recurring evidence handling

- Reads a source one sentence at a time, then reacts, then says "back to the reading" or "Anyways, back to the details". Interjections get sharper as the read goes on.
- Numbers get walked through as arithmetic, out loud: "If anthropic models are three times less token efficient, then the 5% should be thought of more like 15%"; "Four times cheaper for 3% of your cost is a less than 1% deal."
- Counting is used as ridicule: 21 subtitles, the word "little" 15 times, 54 app updates, a 1 MB size win.
- Hand-drawn charts, labeled honestly as vibes ("the most vibe based chart you're going to see in a while").
- Insider claims hedged with "my understanding", "allegedly", "I have been told".
- Live chat as a second source and a foil ("Thank you, chat", "Binary Shokan said", "Bill, you're better than this"). Three of four were filmed in front of a live stream audience; the Cursor emergency video was not.

### Recurring phrases and transitions

- Sincerity markers: "I'm going to be real with you guys", "I'll be real", "I'm going to be incredibly honest", "to be very clear here", "to be frank", "Seriously though".
- Resignation: "It is what it is" (in Cursor, Fable, React Native).
- Dismissal: "yada yada yada" (Cursor, React Native).
- Reveal: "And there's the detail that matters", "There's the important detail", "But do you know what the worst part is?", "I'll give you a hint", "the twist you didn't expect".
- Pacing: "Let me blast through", "Let's blast through the rest of these", "I'll wrap up code super quick".
- Loops: "we'll get to that", "don't worry", "Remember those 40 sub agents", "Make sure I mention webhooks later".
- Rant exit: "Sorry, I've been holding that one in for a while", "Okay, sorry. Just had to get that out of me", "Sorry, I've been waiting for an opportunity to crash out of this one."
- Vocabulary: "slop", "crash out", "mogs/clears", "egregious", "insane", "hilarious", "genuinely", "unbelievable", "chaos/chaotic", "nerds".
- Recurring cast: Julius, Ben Davis, Tibo, chat. Plus his injury ("down a hand").

### Variation by video type

- **Product tour (T3 Code):** no sources, demo-heavy, pillar structure then a rapid-fire list, mock-negatives section, credits roll at the end. Retention runs on teases and "we're just getting started". Lowest profanity.
- **News and drama (Cursor):** shortest, recorded fast ("Saturday night"), highest sponsor share, about half the video reading posts aloud, careful disclosures, a both-sides drama segment, practical "what do you do now" advice, emotional close with no firm verdict.
- **Model comparison (Fable vs Astra):** a category scoreboard with a winner per category, prepared demos, his own usage stats, a long horror-story case study as the emotional peak, cost and subscription buying advice saved for last, and a drawn verdict chart.
- **Tech-ecosystem commentary (React Native):** read-and-react on one long article, then explainers for beginners (analogies, acronyms defined), a steelman, a personal story with a twist, a quiz-driven structural argument, and a reflective synthesis. Two sponsors.

### Surprises and pattern breaks

- The T3 Code title and description ("broke me", "broken over 700,000 users") barely relate to the content, and the user count in the description is higher than the one in the video. An edited pickup ("Theo from the future here") admits the video was filmed earlier and patched.
- A duplicated block in the T3 Code transcript (23:00-24:30) points to a missed edit.
- The Fable title says the debate "Is Over", yet the verdict is split, and his single-model pick (Astra) contradicts his code default (Fable).
- React Native ends with an open bargain for engagement ("if this video bombs, then you're going to get what you ask for"). No other video asks this directly, though Cursor has a mid-video "make sure you're subscribed" for a next-day video.
- He reverses on Tobi on air instead of cutting the earlier criticism. He leaves in content he then retracts.
- The Cursor video opens on the source itself (reading the post at 00:01), while the others delay the topic.
- He talks openly about his production team ("my attention guy already wants to kill me") and tags the editor in every description ("S/O @Ph4seon3").

### What the hour-plus videos do to hold attention

The two long videos (Fable 77 min, React Native 63 min) and, to a lesser degree, the 42-minute T3 Code video use these tactics:
- **Visible structure.** A category board with an arrow (Fable), two spoken roadmaps (React Native), "top-level three" (T3 Code). Viewers always know where they are and how much is left. He announces pace changes ("let's blast through the rest").
- **Planted payoffs 20-45 minutes apart.** 40 subagents (26:31 → 51:30), the spiky theme (24:30 → 70:30), webhooks (14:30 → 31:00), "the React Native team... when we get there" (15:00 → 51:30).
- **One long story per video with escalation and a twist,** placed in the second or third quarter: the autoscroll "revert" fiasco (8 min), the swipe-gesture saga (8 min), the ping.gg UI destruction (5 min). These are the emotional peaks, and each ends on a punchline ("It merged the PR... after I told it you didn't make the changes"; "They're not using the native stack on iOS").
- **Mid-roll sponsor as an act break** with a promise of what comes after (React Native 46:30).
- **Rants spaced out as pattern breaks,** each followed by an apology that resets the tone: Windows ARM, Google and Antigravity, cache writes, SwiftUI lists, Electron.
- **Audience participation:** quizzes ("how many engineers do you think...?"), instructions ("open it and go to settings on your iPhone"), and live chat reactions and polls.
- **Live, unscripted moments left in:** waiting on a Codex terminal, the phone's update count changing on scroll, discovering a 3D simulator feature, checking usage percentages mid-take.
- **Short verdict lines** closing each sub-segment ("So yeah, skill writing. Astra has a slight lead"), so a viewer who drifts in mid-video still gets a takeaway every few minutes.
