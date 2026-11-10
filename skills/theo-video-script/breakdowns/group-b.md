# Group B: structural reading of 5 Theo (t3.gg) videos

Source: auto-caption transcripts, ~30-second paragraphs. All timestamps are the paragraph start, so a quote can sit up to ~30s after the stamp. Quotes are lightly cleaned of caption errors. Where I correct a misheard name, I say so; where I can't be sure, I mark it "(guess)". Anything about what's on screen is inferred from speech and marked "(inferred)".

Recurring caption mishearings across this group, corrected throughout:

- "Soul"/"sole"/"sold" → **Sol** (OpenAI's GPT-6/6.1 Sol; the description of vu8X3YroB-w spells it "Sol").
- "Aux Alpha" → **Ox Alpha** (the title spells it that way).
- "soyv.link", "swa.link", "slite.link", "cited.link", "siteof.links", "swrve.link" → **soydev.link** (the description URLs).
- "per ams" → params; "Kimmy K3" → Kimi K3; "Deep Sweep"/"DSV4" → Deep SWE / DeepSeek V4; "Whisper flow" → Wispr Flow; "Jeb" → Jev; "RHF" → RLHF; "Daniel Conman" → Daniel Kahneman; "Scien"/"Syon" → Scion; "Chad is pointing out" → "Chat is pointing out".
- `[\h__\h]` is a bleeped swear (11 of them in hiI0Vk4NgeY, none in the others).

---

## 1. "Jev is incredible" (F3YXg7AaKWE, 30:29, uploaded 2026-09-21, 501k views)

### 1. Topic and angle

A new model, Jev, from Typesafe AI: a "System 1" classifier that only returns typed JSON, with near-free output tokens and 70–500ms latency. The trigger is the launch blog post plus a flood of Twitter demos ("It feels like it just poof appeared and took over my entire Twitter feed," 03:02). The stance has two halves: the model really is impressive, and most people are about to misuse it. The second half gets more airtime than the title suggests. Roughly a third of the video is corrective: don't use it as an LLM judge, don't use it for context compaction, "it is roughly as intelligent as a switch statement" (13:30).

The title promises unqualified praise. The video pays it off with speed and cost numbers (40–200x faster, "rounds to zero") and frames the praise from the first minute: "this model isn't going to replace things like Fable or Astra" (00:31). The description says it outright: "it doesn't replace reasoning models like Astra/Fable." So the title is the hype half, and the body is half hype, half correction.

### 2. Hook (0:00–1:00)

> "Oh boy, it's new model time. This one's very different though. This isn't our usual new LLM that's slightly better at code and it's not going to be the type of thing that the model counter guy is going to show up and say, 'Look, best new model.' If anything, this might take the counter guy out of his job because this model is for data processing." (00:01)

Mechanism: he sets up a familiar genre ("new model time") and breaks it in the second sentence. The novelty is the hook: a model whose point "isn't to generate text, write code." He then stacks spectacle: "lightning fast computer use even in like the iOS simulator to the model playing Minecraft at lightning speed to compaction that takes under a second" (00:31). He plants the frame he'll spend the video defending ("If you are using Fable and Astra for the stuff you can do with this, I have a lot of questions for you"). He withholds how it works and what it's bad at. The compaction demo named in the hook as a wow item comes back at 23:01 as the thing he tears apart, a nice reversal.

### 3. Lead-in

- **Sponsor (Depot), 01:00–03:02, ~2:00.** Transition in is a pun on the topic: "I can't wait to show you all the best things you can do with this model. But first, we got to classify something. The next section, which is the sponsor break." Then a filter line aimed at the audience: "If you're not a developer, you can skip this ad. But if you are, you should listen close." The read follows a problem → numbers → product → agent angle shape ("8-minute builds and knocking them down to 20 seconds"; "GitHub actions were poorly assembled for humans over 10 years ago. Depot was crafted carefully for agents today"). Exit is the URL, then a hard cut to "Quick breakdown on how this all happened" (03:02), with no bridge sentence.
- **Context, 03:02–04:31.** Who made it: "Dio who used to work at OpenAI, he apparently helped co-invent chat GPT as well as RLHF" (name probably misheard; guess). The "System 1/System 2" framing from *Thinking, Fast and Slow*, and the Jevons paradox naming, which he uses as the thesis: "It's not unlocking new capabilities... It's making them fast and cheap enough that they're way more viable" (04:00).
- **Roadmap:** only implicit. "We'll go to the official announcement in a sec, but first I just want to show you how insanely fast the model is" (04:31).
- **Disclosures:** none about payment or early access, though he says he built a checkers game on it, so he had access.

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01–01:00 | Hook | Genre break, spectacle list, "won't replace Fable/Astra" frame. |
| 01:00–03:02 | Sponsor | Depot. |
| 03:02–04:31 | Context | Creator backstory, System 1 vs 2, Jevons paradox. |
| 04:31–05:00 | Claim | Use cases: video topics, email triage, moderation. |
| 05:00–06:00 | Own demo | Checkers vs Jev: instant moves, but "it's not very smart." |
| 06:00–07:30 | Read source | Founder letter from the launch post; "frontier intelligence function call." |
| 07:30–09:30 | Comparison / personal tangent | BAML: what it is, his own experience with GPT-OSS-120B breaking JSON. |
| 09:30–11:00 | Explainer for chat | Determinism of shape vs content; 4 cents per million in vs $10 for Fable. |
| 11:00–12:30 | Read source | Speed, calibration, "smart if statement," real-time UI demos (Matt's palette demo). |
| 12:30–14:00 | Rant / pre-emptive correction | "Don't use it to judge LLM outputs"; "I want to beat into your guys' heads"; 32k context. |
| 14:00–17:50 | Benchmarks / charts | Race demo (0.114s vs 9s), log-scale cost chart, benchmark caveats, structured-output error rates, Haiku dunk. |
| 18:00–19:30 | Third-party demos | Doom at <$7/hour, frame-by-frame amnesia explained; wiki racing. |
| 19:30–21:30 | Community uses | JSON Render (Chris at Vercel), Ryan's email-classification video clip (100 emails, 200ms avg). |
| 21:30–22:00 | Speculation | Future image support: find PII in video frames. |
| 22:00–26:00 | Critique / rant | Braintrust tweet (judge scorer) and the compaction demo, with a 5-point technical rebuttal. |
| 26:00–26:17 | Sub CTA | Folded into a Twitter-attention-span joke. |
| 26:17–28:30 | Own demo | His 1,118 T3 Code threads classified for 37 cents; threshold slider app. |
| 28:30–30:29 | Conclusion | 10-second rule, knee reflex analogy, "use this like an if statement." |

Rough runtime shares: sponsor 7%; reading the blog and charts ~35%; demos (own and others') ~20%; explainer/correction/rant ~30%; hook + conclusion ~8%.

### 5. Thesis and arguments

Thesis: Jev makes classification so fast and cheap that it becomes a function you call from code, and it's useless, even harmful, as a replacement for reasoning models.

Arguments, in order:
1. **The category is new** (System 1). Supported by the Kahneman framing and the founder letter.
2. **It's for code, not chat.** "This model isn't even useful if a human triggers it" (06:30), backed by BAML as prior art and the "frontier intelligence function call" line.
3. **Output shape is guaranteed.** Supported by his GPT-OSS-120B story and the 0% structured-output error chart.
4. **Speed and cost change what's viable.** Race demo, 170x cheaper, log-scale chart, Doom at under $7/hour, his 37-cent thread audit.
5. **It's dumb, so don't make it judge.** Checkers loss, Doom spinning left and right, the Braintrust tweet, the compaction rebuttal.

Self-hedging and concessions: benchmark caveats he reads from the post ("they expect this is the higher end of real world gains," 15:30; reference answers come from GPT-6 Astra and Fable, "the data might not be perfect"). He concedes Jev's limits repeatedly, which is the point. He apologizes to smart viewers: "I'm sorry for those who get it because it's going to be tedious" (13:30). He hedges his own enthusiasm: "I am scared to even make this video if I'm being real because if I increase excitement too much around this model, we're going to end up with some really, really dumb things" (22:00). No financial disclosure about Typesafe.

### 6. Evidence

- **Launch blog read aloud:** founder letter, use cases, benchmark methodology, error-rate charts. Mostly paraphrased, with interjections ("Yep, that part I absolutely agree with," 17:01; "Cool," after a methodology sentence).
- **Charts:** described while on screen (inferred), e.g. the log-scale cost chart, which he praises the authors for: "They could have made this linear and it would have looked hilarious" (14:31).
- **Numbers:** 4 cents/M in vs $10/M; 70–500ms vs 3–300s; 0.114s vs 9s; 193.6x faster / 444.6x cheaper; Haiku 45.5% error; 32k context.
- **Tweets and third-party demos:** Matt's palette, Chris's JSON Render, Ryan's video (played with audio, inferred from the first-person narration at 20:30), the Braintrust tweet (as a negative example).
- **Personal experience:** BAML with GPT-OSS-120B.
- **His own builds:** checkers game, T3 Code thread classifier. T3 Code is his product, though he doesn't plug it here.
- **His own prior writing:** "you should just read my longer post if you're curious" (23:30).

Read-and-react is about 55% of the runtime. Original argument (the determinism explainer, the judge rant, the compaction rebuttal, the 10-second rule) is ~30%.

### 7. Demo

Three demos of his own:
1. **Checkers (05:00–06:00, ~1 min).** Sounds live ("I'm clicking now. Yeah, it's practically instant"). He leaves the failure in on purpose and turns it into the lesson: "I was barely paying attention and I'm going to crush it here."
2. **Email-classification clip** (someone else's, played back).
3. **T3 Code thread classifier (26:30–28:30, ~2 min).** Prepared (Astra built it beforehand). Interactive threshold slider ("at 80%... 22%... at 90%, it's down to 6.8"). He includes the dead end: Astra "tried multiple times to revise the prompt... and it still concluded about half of my threads were worth using for content. So, it's not good at this."

### 8. Retention devices

- **Open loop/reversal:** compaction is promised as a highlight at 00:31 and paid off as a takedown at 23:01.
- **Delayed source:** "We'll go to the official announcement in a sec, but first..." (04:31).
- **Pre-empting comments:** "I already see people getting confused" (09:31); "I see more confusion in chat already. So, is it deterministic?" (10:30); "one of the questions I've seen the most by far" (12:30). This suggests it was recorded with a live chat.
- **Audience-insult jokes:** "I know a lot of y'all don't code anymore sadly" (11:30); "It's so fast that it fits in the attention span of the average Twitter user. So, the video is guaranteed to go viral" (25:30), which turns into the sub CTA.
- **Brand dunk as pattern break:** "That model is so bad and it needs to stop being used for anything... Anthropic is treating Haiku as dead. We should do them the favor" (17:30).
- **Escalating rant:** 13:01 → 13:30 → 22:00 → 26:30 ("Don't get me started on the people who think they can compact their history by... shoving it into a small image. Insanity.").
- **Concrete rule of thumb as a closing gift:** the 10-second test (28:32).

### 9. Ending

He lands on a mental model, not a verdict: "How many seconds would it take for you to answer the question once you've perceived all of the information?... If the answer is under 10 seconds, this model's probably good for it" (28:32). He restates the opening frame ("This is the point I'll end on, and it's similar to the one I started on") and adds the knee-reflex analogy. Final takeaway: "You should see this like a new library you install or a function that you call" (29:30). He closes with a chat quote ("Somebody in chat just said the only way this would replace an LLM is if you're using them badly. I mostly agree"; caption says "China", probably "chat").

Sign-off: "Don't use this to replace Fable or judge between complex topics. Use this like an if statement and you'll have a lot of fun with it. Let me know how y'all feel. And until next time, peace nerds."

The sub CTA comes early (26:01), not at the end.

### 10. Voice

1. "Oh boy, it's new model time." (00:01)
2. "But first, we got to classify something. The next section, which is the sponsor break." (01:00) — topical pun as sponsor transition.
3. "If you're not a developer, you can skip this ad. But if you are, you should listen close." (01:00)
4. "Quick breakdown on how this all happened because it's actually been pretty crazy to watch." (03:02) — post-sponsor restart.
5. "So, let's read through the announcement." (03:30) — source intro.
6. "This is one of the biggest important pieces to understand." (06:30)
7. "I already see people getting confused so I want to be really really clear here" (09:31)
8. "That is actually 40 to 200x faster. There's no doubt on that claim. That is real and true and based." (11:00)
9. "I know a lot of y'all don't code anymore sadly. I get it. But if statements were a great way of thinking of logic." (11:30)
10. "I want to beat into your guys' heads how this works. And I'm sorry for those who get it because it's going to be tedious, but I'm increasingly tired of comment sections that fundamentally don't understand what's being talked about." (13:01)
11. "That doesn't mean it's not cool, and it is cool as hell." (13:30)
12. "Respect to them for keeping the cost per workflow in their chart in log." (14:31)
13. "Yep, that part I absolutely agree with." (17:01) — reacting to a sentence just read.
14. "I am scared to even make this video if I'm being real" (22:00)
15. "then I would plead that you never ever ever stray from the defaults in those tools because you just fundamentally don't understand yet. And don't worry, you're not the only one." (23:01) — insult, then softener.
16. "I will do my best to tell TL;DR why this is a bad idea" (23:30)
17. "Don't get me started on the people who think..." (26:30)

Style: short declaratives broken up by long run-on spoken chains. Register is casual-technical with internet slang ("based," "cool as hell"). Profanity is mild ("damn," "hell"). For a mixed audience he uses programmer analogies (if statement, switch statement, function call) and human ones (shirt color, knee reflex), and explains the same point twice in different words, apologizing to experts as he does. Intensifiers repeat: "insane" ×7, "crazy" ×7, "comical(ly)" ×3, "way way faster."

---

## 2. "Ox Alpha is INSANE" (Xdxp3lbQKyQ, 43:14, uploaded 2026-08-27, 358k views)

### 1. Topic and angle

An anonymous model, "Ox Alpha," released free through OpenCode and OpenRouter, turns out to be ZAI's GLM 5.3 Flash. The trigger is the reveal plus a week of his own use. The angle is a framework: models have two axes, "intelligence" and "behavior," and this is the first cheap, dumb model that behaves well enough to be a joy. The money shot: it audited "hundreds" (later "thousand plus") of PRs in his repo for 12 cents.

The title promises "INSANE." He pays it off with the 12-cent audit (21:01–22:32) and the tier-list promotion next to Sol (40:33). He tempers it right away: "the numbers being shared here are misleading, but it doesn't mean the model is bad" (01:31) and "This model is not as smart as those models" (23:01).

### 2. Hook (0:00–2:02)

> "Last week there was a really interesting model drop, and the more I've been using it, the more impressed I've been. The model came out anonymously under the name Ox Alpha... we don't know who made it, but there was one other detail that was even more interesting. We have capacity for 100 trillion tokens per day. That is crazy." (00:01)

Mechanism: a mystery plus a number that doesn't add up. He grounds the number in scale comparisons ("On my absolute heaviest usage days, I'm doing upwards of like 7 billion"; "All of Google's Gemini traffic... 150 trillion," 00:33). He builds suspicion with a friend's benchmark: "Sol got a 52%, Opus 5 got a 65% [caption 'People 5', guess], and whatever the hell Ox was, somehow got an 80%. Something is up" (01:01). Then he reveals the answer inside the hook, unlike a pure mystery video: "I bet you wouldn't have guessed it's a flash model. GLM 5.3 flash" (01:31). The surprise moves from "who made it" to "a small model behaves this well." He holds back one secret for the end, the Chinese chips (teased at 29:01, paid at 37:01).

### 3. Lead-in

- **Credential/relationship:** "You guys might know Ben Davis, he's been in a bunch of my content, he does the podcast with me" (01:01).
- **Sponsor 1 (CodeRabbit), 02:02–03:47, ~1:45.** In: "I can't wait to show you everything that makes this model cool and all the things I've been using it for after a real quick break for today's sponsor." He opens with a topical tie-in: "if you ask models like Fable and Sol to come in and do this audit for you, they're going to throw a bunch of errors because the labs won't let you do security work with them." The read includes a live product walkthrough on his own repo, with blurring ("I'm blurring these because these are real security issues we're going to have to go fix," 03:00) and a face-cam joke ("the little button that my face is currently covering"). Out: "As I mentioned before, this model came out under the name Ox Alpha originally" (03:31). This time there is a callback bridge.
- **Specs:** 1M context, full multimodality (03:31).
- **Disclosure:** he notes his $80/month ZAI plan later (10:00, 23:01). No payment disclosure for the model maker.
- **Roadmap:** "This is a wild model launch and there are so many fun details for us to dive into" (02:02), plus the later "before we dive into benchmarks" (12:00).

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01–02:02 | Hook + reveal | Mystery, 100T tokens/day, Ben's bench, GLM 5.3 Flash. |
| 02:02–03:47 | Sponsor | CodeRabbit security. |
| 03:47–04:30 | Context | Specs, his setup (OpenRouter binding in Codex through a proxy). |
| 04:30–07:00 | Live demo | Prioritize open PRs; steering mid-task; GitHub rate-limit failures. |
| 07:00–10:00 | Recorded demo | Earlier run: 6 subagents, self-recovery from auth failures, merged 8 PRs. |
| 10:00–11:33 | Live data | OpenRouter speeds, provider latency, pricing (7.5¢ in / 25¢ out). |
| 11:33–12:15 | Specs | 320B total / 18B active vs Kimi K3 at 3T. |
| 12:15–18:30 | Framework (original argument) | Intelligence vs behavior; T3 Chat users always pick "extra high"; GPT-4.5 and Gemini 3.1 Pro as smart-but-misbehaving; Skatebench. |
| 18:30–20:30 | Demo payoff | HTML report, his own prompt mistake, a real PR it surfaced. |
| 20:30–22:32 | Demo: cost | Asks the model to compute its own cost: 50¢, then corrected to 12¢ with a screenshot (vision test). |
| 22:32–25:00 | Comparison | vs DeepSeek V4 Flash (no vision, gets lost). Teases fish slop. |
| 25:00–30:00 | Read source / benchmarks | ZAI blog: hybrid attention, flat pricing, Pareto chart, token efficiency, coding bench. |
| 30:00–32:30 | Critique | Token efficiency is its one weakness; live "am I misremembering?" moment. |
| 32:30–34:40 | Third-party bench | Dara's design bench with skills toggled. |
| 34:40–36:00 | Own demo | Fish slop 2D and 3D: logic bugs, good animation. |
| 36:00–37:00 | Third-party demo | ZAI's Blender kitchen scene. |
| 37:00–37:54 | Withheld reveal | Runs on Huawei Ascend chips. |
| 37:54–39:52 | Sponsor 2 | DNSimple. |
| 39:52–42:30 | Verdict device | Tier list: GLM 5.3 Flash moves next to Sol; DeepSeek V4 Flash drops. |
| 42:30–43:14 | Wrap | "Give a model like this a shot"; Gemini dunk; sign-off. |

Shares: sponsors ~9% (two reads); demos ~35%; framework/opinion ~20%; reading blog/benchmarks ~20%; tier list ~6%.

### 5. Thesis and arguments

Thesis: GLM 5.3 Flash isn't smart, but it behaves so well and costs so little that it's one of only three models worth using.

Arguments, in order:
1. **It does real agentic work without derailing.** Shown in demos: steering mid-task, recovering from subagent auth failures ("This is phenomenal... debug its own flows," 07:30), producing PR links unprompted.
2. **Behavior is a separate axis from intelligence.** Six minutes of framework, built from examples (GPT-4.5 = smart, behaves poorly; Gemini 3.1 Pro = knows the most, can't code), then applied to the model.
3. **It's absurdly cheap.** 7.5¢/25¢ pricing, 12-cent audit vs "over a hundred dollars" on Fable.
4. **Benchmarks agree.** Pareto chart, parity with Opus 4.8 at "under a tenth the price."
5. **It beats its nearest competitor on capabilities that matter to him** (vision vs DeepSeek V4 Flash).

Concessions and self-criticism: "This model is not as smart as those models. It will not solve hard problems as well as Fable or Sol will" (23:01); "For what it's worth, I am still coding with Sol and Fable" (25:00); token efficiency is "not quite where I would like" (30:30); fish slop logic bugs. He admits his own error on camera: "Oh, no. I said all the pull requests in the repo for this one. That is my bad" (18:30), and turns it into evidence: "I should have second-guessed what I sent because Ox, aka 5.3 Flash, does what you told it." He corrects himself on numbers live: "4 minutes and 40 seconds for first token now. Correction, 4.4 seconds" (10:31). The same happens with cost (50¢ to 12¢) and with Gemini Flash token counts ("Am I misremembering?... I guess not," 32:00). Bias: he declares the Gemini defense reluctant ("I hate that I'm doing this... I have to defend Gemini a little bit," 14:00).

### 6. Evidence

- **His own usage logs and runs** (the core): PR audits, cost calculation done by the model itself.
- **Friends' numbers:** Ben Davis's Deep SWE subset; testers' reports.
- **His benchmark:** Skatebench (88% best, Gemini 3.1 Pro 95–97%).
- **Official blog read aloud** (25:00–30:00), with skepticism about chart scales: "The cost measure here is logarithmic... this gap is nowhere near as big as it seems due to the log scale" (26:31). He edits charts: "I deleted a bunch to make it easier" (29:01).
- **Live dashboards:** OpenRouter speed and latency pages (inferred, on screen).
- **Third-party benches/demos:** Dara's design bench (name a guess), ZAI's Blender scene, a friend's chip research ("Barrel," guess).
- **Products:** T3 Code (his) is the demo harness; T3 Chat (his) gives him the "users always pick extra high" anecdote.

Read-and-react ~30%; demos and original argument ~60%.

### 7. Demo

The live PR-prioritization demo (04:30–07:00) is clearly live and partly fails: "Also, love the GitHub error connection issues"; "Something is causing the skill file reads to fail. Again, I've been hacking the hell out of my Codex and I'm suffering for it. This demo would have been a lot cooler if GitHub wasn't rate limiting us" (06:31). He keeps the failure and pivots to a prepared run: "I could sit here and wait forever, but I ended up finding a run I did when I first got access to the model 5 days ago" (06:31). The live thread finishes later (10:00: "Oh, it finally got my skill read to work... Hurrah"), and he returns to it at 18:30. Other demos: the model computing its own cost, with a vision check done live on a viewer's question (22:00); fish slop 2D/3D, prepared and played live, bugs narrated. Demo setup is always a pre-stated test ("One of my favorite first tasks when I get access to a new model like this is to ask it to just go over the work I already have going," 04:30) and a named failure mode he's watching for ("This is the type of thing that throws a lot of models off," 05:30).

### 8. Retention devices

- **Withheld secret:** "There's a special word here that we're going to get to in a little bit... the secret that made this model so interesting that I currently have highlighted" (29:01), paid at 37:01 ("And now for the final hook at the end here").
- **Fish slop tease:** "spoiler I have a build of fish slop that I made with this model" (24:33), paid at 34:42.
- **Tier list as the final question,** used to bridge into sponsor 2: "where is this going to fall in my tier list? I do want to tell you about one other thing that ranks really high in my tier list though, our sponsor" (37:31).
- **Audience-insult humor:** T3 Chat users "their IQ level is low, their choice to always pick extra high is dumb" (13:00).
- **Self-deprecation:** "Here I was, big spender out here spending 50 cents" (22:32).
- **Live chat interaction:** "to the chatter asking a very important question... does it have vision? Yes, it does. I'll show you" (22:00).
- **Pre-empting comments:** "And no, V4 Flash does not have vision. Stop saying that" (41:30).
- **Callback joke at the end:** "everybody who is speculating that Ox Alpha was a Gemini model, huh, you really thought a Gemini model would ever behave that well?" (43:01), which calls back the Gemini-behaves-badly framework.
- **Repeated awe line:** "I don't know if you guys understand how crazy this is" (21:01, 22:32).

### 9. Ending

The verdict is a ranking, with reasoning about what the list measures: "This list isn't just how capable or smart is the model... This list is meant to be ranking what unique value does this model bring?" (40:33). He settles it as: "with Fable, Sol, and 5.3 Flash, there is practically zero reason to use anything else in this list" (41:00). The wrap (42:32) is a recommendation: "If you want something absurdly cheap, surprisingly capable, and incredibly thorough and well-behaved, you should give a model like this a shot. I have a feeling that you'll be surprised."

Sign-off: "This is an absolute wild drop, and I've had a great time using GLM 5.3 flash. I bet you will, too. Let me know how you feel in the comments, and until next time, peace out."

### 10. Voice

1. "Last week there was a really interesting model drop, and the more I've been using it, the more impressed I've been." (00:01)
2. "That is so much compute, it's hard to even fathom." (00:01)
3. "Something is up. Well, guess what? We actually know what the model is now" (01:01)
4. "I will also say that the numbers being shared here are misleading, but it doesn't mean the model is bad." (01:31) — early hedge.
5. "If only there was a tool that understood your code base... You know, something like CodeRabbit but for security. Oh, yeah. CodeRabbit made a security product" (02:31) — mock-rhetorical sponsor setup.
6. "So, let's push it a little bit more." (05:01)
7. "This is what happens when your models are RL'd on the specific behaviors of a harness." (05:01) — explaining while demoing.
8. "Small thing, but like these little things you start to notice a lot as you do more and more of this work." (08:31)
9. "I don't know how to explain what I mean here, so I'm just going to use examples." (12:00)
10. "And I hate that I'm doing this because it's going to force me to do something I really don't feel like. I have to defend Gemini a little bit." (14:00)
11. "Or to be a little more blunt, Gemini 3.1 Pro." (15:31)
12. "That is my bad." (18:30)
13. "I I don't think you guys understand just how crazy that is." (21:01)
14. "To everybody who's complaining that AI is getting more expensive, I hope you understand that more intelligence is the thing getting more expensive." (27:00)
15. "Hopefully I've made my point here. This model is absurdly good for the money." (30:00)
16. "Huh. Anyways, as always thank you to Dara for the work he has put in" (32:00) — "Anyways" as segment reset.
17. "Oh god, this style. Everything has a template with this style in it." (32:31)
18. "It almost cooked. It's getting in close." (33:31)
19. "Okay, so time to answer the eternal question." (39:52)

Style: long spoken chains; frequent live self-correction. Mild profanity ("whatever the hell," "god damn"). Heavy intensifiers: "absurd(ly)" ×7, "insane" ×8, "crazy" ×6. He explains technical concepts in passing (MoE active params, log scale, why token efficiency matters even when cheaper: "it affects how long it takes... and how much it blows its own context," 31:30), usually prompted by a chat question.

---

## 3. "OpenAI fights back" (vu8X3YroB-w, 30:58, uploaded 2026-09-29, 322k views)

### 1. Topic and angle

GPT-6.1 Sol, OpenAI's reply to Anthropic's Opus 5.5, which had dropped the week before. Trigger: the release, to which he had early access, filmed at 2–3 a.m. right after his Sonnet 5.5 video. The angle: Sol is "like Astra, but less dumb, and way way cheaper" (description). It's a great reviewer and auditor. Opus stays his daily driver. And the pricing hints at the end of subsidized subscriptions. He adds insider-ish speculation that 6.1 "was not meant to be 6.1."

The title frames this as a competitive drama ("fights back"). The video pays it off on price ("73x cheaper" for the same Deep SWE score) and on review quality. He refuses the knockout, though: "This isn't it, and I'm not planning on canceling any of my Claude subs" (30:00).

### 2. Hook (0:00–1:31)

> "They're back. Okay, let me catch you guys up quick. Last week Anthropic dropped a new model, Opus 5.5, and it was unbelievably good. It was so unbelievably good that OpenAI rushed out two model drops, GPT-6 Sol and GPT-6 Luna. You might have noticed I didn't do a video on those models. There's a reason. They weren't that good." (00:05)

Mechanism: a two-word cold open, then a fast recap framed as a rivalry, then a credibility move: he skipped the last releases, so this one must matter. Then the insider tease: "this model made it very, very hard to film that Sonnet 5.5 video because I knew something was coming. Something surprisingly cheap, surprisingly capable, and most surprisingly better than Astra" (00:31). A rule-of-three "surprisingly" build. He adds urgency and authenticity: "I'm filming this at 2:00 in the morning... you are getting my true honest take and not the distilled version of what everyone else is saying" (01:00). He holds back whether it replaces Opus, and only reveals it in the final minute (with an early spoiler at 22:00).

### 3. Lead-in

- **Disclosure, 01:00–01:31:** "As always, I feel obligated to remind you I do have early access, but I'm not being paid in any way, shape, or form. OpenAI has no influence over what and how I say things, just when. They politely asked me to wait until the model is out to talk about it."
- **Sponsor (Depot), 01:31–03:01, ~1:30.** In, as a wordplay bridge on "wait": "But I have to wait for one other thing first. Today's sponsor." The read ties to agents' CI feedback and includes a personal story ("when Ben moved Pick Thing over to Bun, we immediately had some CI failures"; "Pick Thing" is likely the product name Picthing, guess). Out: the URL, then "Let's talk about this model a bit because it is not quite what I expected and it's probably not what you guys expected either" (03:01).
- **Methodology disclosure:** "the numbers I'm currently showing on my screen are unlikely to be exactly accurate because I am running Terminal Bench for myself... the first two times I ran it, I screwed things up" (03:32).
- **Roadmap:** "Obviously, we'll have all the fun things like fish slop near the end, so stay tuned for that" (09:02); "I promise we'll get some good answers to that in a bit. But first, we need to talk a bit about model behaviors" (09:30).

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:05–01:31 | Hook + disclosure | Rivalry recap, 2 a.m. filming, early-access disclosure. |
| 01:31–03:01 | Sponsor | Depot. |
| 03:01–05:02 | Benchmarks (own, live) | Terminal Bench in progress, Deep SWE log-scale: 21¢ vs $14.65 for the same score. |
| 05:02–08:30 | Speculation / insider read | "Things I probably shouldn't say": smarter, slower tokens, Tibo's tweet on Pro plan usage math, cache-read price cut to 95% off, margins. |
| 08:30–09:57 | Benchmarks | Live refreshes, dropped H100 tasks, per-task cost vs Opus. |
| 09:57–13:00 | Framework + anecdote | Spikiness diagram; Astra "smart and dumb at the same time"; he churned; the invoice-wiring story; testers Julius and Ben. |
| 13:00–19:30 | Evidence: real work | Orchestrator V2 audit, T3 Code improvement bench (87.4), Opus blind-reviewing the model, Opus guessing its price. |
| 19:30–22:00 | Tangent / dunk | Jev Router (OpenRouter) is "an incredibly stupid idea," backed by his bench. |
| 22:00–22:17 | Spoiler | "I'm going to keep using Opus 5.5 for now." |
| 22:17–26:00 | Demo + rant | Fish slop: beautiful graphics, jank movement, 20+ cutesy UI strings, "crashed out in the Slack." |
| 26:00–28:00 | Real-world demo | Sol reviews a real T3 Code PR and catches bugs Fable and Opus missed. |
| 28:00–29:30 | Twist story | TS Rust port: Opus finished it, Sol's audit found 1.3M of 1.8M lines unused. |
| 29:30–30:58 | Verdict + tease | Tandem workflow, Sonnet replaced, "start of the end of the subsidization era," sign-off. |

Shares: sponsor ~5%; benchmarks/pricing/speculation ~30%; real-work evidence and anecdotes ~35%; fish slop ~12%; verdict ~5%.

### 5. Thesis and arguments

Thesis: GPT-6.1 Sol matches frontier models on scoped work like review and audits at a fraction of the price, but Opus 5.5 is still the better collaborator for long builds.

Arguments, in order:
1. **The price/score ratio is unprecedented.** Deep SWE log chart, cache-read cut, $1.38 vs $5.12 per task.
2. **It's not a dot-release.** Three inference points (smarter, slower, Tibo's tweet), offered openly as speculation: "They've kind of just left the details out there for us to reverse-engineer, so take this as you will" (08:31).
3. **It fixed Astra's spikiness, mostly.** He trusted it to prepare money wires.
4. **It's an elite reviewer.** Audits, the blind Opus review, the real PR catch.
5. **It's weak at long unattended builds and at UI.** TS Rust port, fish slop.

Ordering: positives first, then the caveat, saved for after the spoiler. The twist story at 28:00 complicates both sides: Opus "did it," but Opus also left the slop.

Hedges and admissions: "I would say mostly. Not entirely" (11:02); "I will gladly admit that Deep SWE is far from a perfect measure" (04:31); "I'm more skeptical of benchmarks than ever" (04:01); "To be fair, so is Opus" (16:31). He shifts blame for a funny claim: "According to Opus, so don't blame me, blame Opus for saying this" (18:01). He flags himself walking an NDA line: "There are things I'm not supposed to say and I'm definitely walking a thin line here by sharing it, so I hope this proves I'm not paid off by OpenAI" (05:02). Bias: he's an early-access tester, and he says he spent "hundreds of thousands of dollars in tokens" on OpenAI models (16:01).

### 6. Evidence

- **His own benchmarks run live** (Terminal Bench on "random VMs on my network"), with process flaws disclosed.
- **His private evals:** Orchestrator V2 audit, T3 Code improvement bench, his "10-model bench."
- **A tweet from an insider** (Tibo, OpenAI), paraphrased and decoded for implications.
- **Pricing math** worked out loud (margins "rumored to be as high as 95%").
- **Other testers' quotes:** "Julius called the model incredible. Ben called it incredibly boring" (12:01).
- **A model's opinion as evidence:** Opus 5.5's blind review and price guess, read aloud (14:32–18:31). It's a novel and funny device.
- **Personal stories:** invoice wiring; the TS Rust port; the real PR.
- **Demo:** fish slop.

Almost no external article reading. Read-and-react ~15% (the tweet, Opus's output). Original argument and first-hand evidence ~80%. This is the most "own data" video in the group.

### 7. Demo

Fish slop (22:17–26:00, ~4 min) is a prepared build played live, with sound ("Oh god, it's blaring," 22:31). He reads the UI strings aloud one after another as a comedy beat (24:01: "take a breather, paused, your little world can wait, back to the reef..."). He mentions an earlier failure: "the first time I tried demoing this before filming, it just randomly game overed" (25:01). The PR review demo (26:00–28:00) shows a prepared thread on screen (inferred: "Ignore the GPT-6 Sol there, just a placeholder"). The benchmark dashboard is semi-live ("Every time we refresh, the numbers change," 08:31).

### 8. Retention devices

- **"Stay tuned"** for fish slop (09:02) and "we'll get some good answers to that in a bit" (09:30).
- **Forbidden-knowledge tease:** "Here's where I'm going to say some of the things that I probably shouldn't" (05:02).
- **Self-aware spoiler:** "I'm kind of spoiling the ending here, aren't I?" (22:00); "Normally, I would make you guys wait for the Opus versus Sol video... but I'll just spoil the details now" (27:31).
- **Twist:** "And this is the funniest part" (28:01), the 1.3M unused lines.
- **Comedy via quoting a model:** Opus's pricing guess (17:31: "This is the funniest part of the whole thread though").
- **Rant/crash-out:** "This model is unacceptably garbage at UI... go spend your money somewhere else" (24:30).
- **Jokes:** "I make decent money. I don't make H100 money, okay?" (09:02).
- **Tease of a future video:** "this does potentially mark the start of the end of the subsidization era. So, make sure you're subscribed so that you can be here when I cover all of that" (30:00).
- **Exhaustion as authenticity:** 2 a.m. at the start, 3 a.m. at the end.

### 9. Ending

The argument lands as a workflow recommendation, not a winner: "I like using them in tandem because I find Sol to be way better at reviewing and digging into the details, but I find Opus a more pleasant collaborator" (27:31). Concrete next action: "I'll be going and making adjustments inside of my Claude config... so that Opus knows this is the model to have review its work" (29:30). Market takeaway: "I have almost no reason to use Sonnet anymore." Sub CTA tied to the subsidization tease. Then a vulnerable aside: "God, I hope this doesn't get me canceled online. I have no idea how others feel about this... I legitimately don't know if you all are going to love it or hate it" (30:30).

Sign-off: "Uh, this is a tiring one. Hopefully I did a good job. Let me know in the comments. And until next time, peace nerds. God, I'm so dead. Ah."

### 10. Voice

1. "They're back. Okay, let me catch you guys up quick." (00:05)
2. "You might have noticed I didn't do a video on those models. There's a reason. They weren't that good." (00:05)
3. "So, yeah. I got a lot to say about this one." (00:31)
4. "So, you are getting my true honest take and not the distilled version of what everyone else is saying." (01:00)
5. "As always, I feel obligated to remind you I do have early access, but I'm not being paid in any way, shape, or form." (01:00)
6. "But I have to wait for one other thing first. Today's sponsor." (01:31)
7. "Let's talk about this model a bit because it is not quite what I expected" (03:01)
8. "Here's where I'm going to say some of the things that I probably shouldn't." (05:02)
9. "Why in the world would they do this?" (06:01) — rhetorical setup before decoding a tweet.
10. "I make decent money. I don't make H100 money, okay?" (09:02)
11. "I know I cite this diagram a lot, but there's a reason for it." (10:01)
12. "It is smart and dumb at the same time." (10:01)
13. "So, I'm literally trusting this model to wire money for me." (11:30)
14. "Julius called the model incredible. Ben called it incredibly boring. And I think that's the best place you can be for a model drop like this." (12:01)
15. "I've had a lot of fun testing with is..." / "This whole thread was particularly fun because..." (14:00, 14:32)
16. "According to Opus, so don't blame me, blame Opus for saying this." (18:01)
17. "I'm kind of spoiling the ending here, aren't I?" (22:00)
18. "This model sucks at front end. It sucks at design. It has no taste. And you're going to have to bring your taste yourself still." (24:30)
19. "you bet your butt the moment this model comes out, I'll be going and making adjustments" (29:30)
20. "God, I hope this doesn't get me canceled online." (30:30)

Style: tired, run-on, more stumbles than usual (he warns about it). Mid-level profanity ("shitload," "god damn," "you bet your butt"). Technical concepts are explained by consequence, not mechanism: cache reads are explained as "a 90% discount, and now it's a 95% discount... massively reducing the cost for real-world agentic use" (07:32). He names many friends and insiders (Ben, Julius, Tibo) as social proof.

---

## 4. "You're using AI agents wrong" (q1D90-uGvBg, 49:22, uploaded 2026-09-09, 257k views)

### 1. Topic and angle

A screen-share workflow video: how a part-time-coding CEO merges ~50 PRs a week with parallel agents, mostly through his own app, T3 Code. Trigger: his own contribution chart and a stream (it was filmed live, with chatters contributing bugs and PRs). The angle: velocity comes from removing friction and protecting motivation ("burn more tokens" to avoid demotivating failures), from running agents off your laptop on Linux, and from "de-risking the merge button" with safety nets instead of guardrails.

The title accuses the viewer ("you're using... wrong"). The video never names a wrong way. It shows his way, and he softens the accusation himself: "Not all of it will be perfect. Not all of it should be copied" (02:01). The description is the honest version: "the AI workflow that helped me merge 50+ PRs on vacation." He admits the bait in the opening: "Okay, I may have baited you guys a bit" (01:32).

### 2. Hook (0:00–2:22)

> "I have a confession to make. Ever since I started focusing more on running my company and running my YouTube channel, I have been less good of an engineer. Not that like my code is worse or I'm holding the team back. Okay, I am kind of doing that. But more I'm just not able to spend as much time coding." (00:01)

Mechanism: a vulnerable confession that sets up a contradiction. He then shows the chart: "I'm landing as many as 50 PRs a week. Huh" (00:31), and plays it as fake surprise: "Huh. I guess I just wasn't that busy during this window. Oh wait, the week of August 7th I was traveling. I was at Def Con. And somehow between my flights, my Ubers and my awful internet at the hotel at Def Con I managed to get 52 PRs landed" (01:00). Then a challenge to the viewer: "a CEO that is a part-time coder is somehow probably out-shipping you" (01:32). And stakes for the video itself: "if all goes well, I'm going to land some real changes while I'm filming this video. I've never done anything like this, and I'm admittedly kind of scared. I'm going to be showing my ass a bunch here" (01:32–02:01). He withholds the method.

### 3. Lead-in

- **Sponsor (Browserbase), 02:01–03:50, ~1:30.** In, with a sincere-sounding pivot: "And the first really cool thing I want to show you guys is today's sponsor." Opens on a claim: "If your agent doesn't have access to the web, it's probably not a very good agent." Uses one stat ("over 80% of the web cannot simply be curled"), plus social proof ("everyone from Microsoft to DeepMind"). Out: "So, let's dive in to how I get so much work done recently" (03:30).
- **Disclaimer about bias:** "a lot of the changes that we're making to T3 Code have been from my experience working this way" (04:00). The big plug disclaimer comes at the end (48:01).
- **Roadmap:** numbered steps ("Step one, new thread... Step two, paste. Step three," 05:00) and a promise of depth: "we are at the very surface level right now. Where things are going to get really cool as we go is the work I did to T3 Code itself" (06:00). Also "I promise you we'll be touching on this a lot throughout" (11:00).

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01–02:01 | Hook | Confession, PR chart, bait admission, live-stakes promise. |
| 02:01–03:50 | Sponsor | Browserbase. |
| 03:50–05:00 | Live bug intake | A chatter reports a `$`-skill bug. |
| 05:00–06:30 | Tip | Steps 1–3; don't run agents on your laptop; Linux box "BB-1" (name guess). |
| 06:30–10:30 | Tutorial core | Dictates a prompt, then annotates it sentence by sentence (goals, "in my opinion" as room to push back, stating his knowledge gaps, early-exit permission). |
| 10:30–11:00 | Tip | "Ignore the thread until it's done." |
| 11:00–13:30 | Principle + prompt | Protect motivation; burn tokens auditing a PR before testing it. |
| 14:00–15:30 | Tip / opinion | Linux vs macOS for parallel agents (5% CPU with 40+ agents). |
| 15:30–17:30 | Tip | Run the same PR-triage prompt on two models (GLM 5.3 Flash and Luna). |
| 17:30–19:30 | Product walkthrough | T3 Code PR-linked threads, "settle," "snooze." |
| 19:30–21:30 | Results + trick | Skill-bug audit returns; the ELI5 follow-up "so the ADHD doesn't win." |
| 21:30–22:30 | Live bug intake | Notices a "done" status bug and a disconnect; spins a thread. |
| 22:30–29:30 | Results → action | PR audit (429 risk, 60s vs 180s polling) → drafts a contributor comment → corrects it → lets the agent post it; "link to thread." |
| 29:30–31:30 | Tip | The "babysit" skill loop for review-bot comments. |
| 31:30–32:30 | Failure kept in | Luna's triage is wrong; he archives it. |
| 33:00–36:00 | Results + rant + chat poll | Skill stacking doesn't work in the SDK; "Anthropic's docs are full of lies"; lets Fable post on the Claude Code issue. |
| 36:00–37:00 | Tip | Keep the thread list minimal; the Swift app built in one thread. |
| 37:00–39:30 | Live demo | Tailscale `--share-dev` to test a remote PR; uploads and screenshots. |
| 39:30–43:30 | Infra walkthrough | iOS remote builds (a tool caption-heard as "Swim," guess), the `preview:mac` label builds, faster signing. |
| 43:30–44:30 | Principle | Find friction in your flow, fix it, compound. |
| 44:30–47:30 | Principle | Nightly builds every 3 hours; "de-risk the merge button"; "Safety nets, not guardrails." |
| 47:30–49:22 | Recap + disclaimer + sign-off | Recap, plug disclaimer, "do one every 3 months," asks for tips. |

Shares: sponsor ~3%; live screen-share doing real work ~60%; explaining prompts/principles ~25%; recap ~4%. No external sources are read except agent outputs.

### 5. Thesis and arguments

Thesis: shipping fast with agents is less about the model and more about removing every point of friction and fear between an idea and the merge button.

Arguments, built up one at a time by demonstration rather than stated up front:
1. **Get the work off your machine** (Linux box, remote threads).
2. **Prompt with goals, your knowledge gaps, and permission to push back or stop early** (the annotated prompt).
3. **Don't watch threads; protect motivation by spending tokens before you spend effort** ("One of the easiest ways that you can prevent these failures is burning more tokens," 12:30).
4. **Keep your queue small and self-cleaning** (settle, snooze, link-to-thread).
5. **Automate loops** (babysit skill).
6. **Make testing cheap** (share-dev, preview builds).
7. **Accept that bugs ship and build safety nets** (nightlies, rollback).

The "burn more tokens" refrain repeats at 12:30, 16:02 ("If you guessed burning more tokens, you're starting to catch on"), 20:30, and 42:01 ("So, I did what I always do. I burned more tokens"). This is a running gag that also carries the argument.

Concessions: "Not all of it should be copied" (02:01); "I don't think work trees are the best solution" (05:30); "Mistakes do absolutely still happen. Sometimes things merge that shouldn't" (44:00); nightly is "an admittedly not perfect solution" (44:31). Bias disclosure: "I know that a lot of this might have come off as an unintentional plug for T3 Code, but what I really wanted to be was a showcase of how I improve the tools I use" (48:01). He names the "correct" option that he isn't choosing: "Option two, I can go write a real, better comment, which is the correct option, to be clear" (35:00).

### 6. Evidence

- **His own GitHub contribution chart** (00:31).
- **Live agent outputs** read aloud and summarized (audits, plans, drafted comments).
- **Machine stats:** "I'm using 5% or less of my CPU... 40-plus agents" (14:02); "a 16-thread machine that I paid like 600 bucks for."
- **Personal anecdotes:** Def Con, hotel Wi-Fi at 10 Mbps, the motivation loss scenario, his ADHD.
- **External:** a Claude Code GitHub issue where "Boris commented in the thread and confirmed that it is a real bug" (34:30); other projects' implementations (CodexBar).
- **Product data:** T3 Code's "surprisingly big 200,000 plus user base," "a few thousand" nightly users (45:01).

Read-and-react on outside sources is close to 0%. Everything is first-person demonstration and explanation.

### 7. Demo

The whole video is one long demo, mostly live (filmed on stream with chat present). Setups are spoken prompts via Wispr Flow, shown as he dictates. Many threads run in parallel, and he cuts between them as they finish ("This one finished though, so let's take a quick look," 19:31). Failures and dead ends stay in: Luna's bad triage ("This is a bad recommendation. I do not like Luna for this type of work," 32:02); "Oh, did it hit a bug? Whatever. It'll probably figure itself out" (32:32); the remote disconnect he notices mid-prompt (21:30); his ADHD glazing over the fix. The cleanest live success is the Tailscale share-dev test (37:30–39:30): file upload works ("Oh, look at that. It accessed the data correctly"), then he tests the screenshot path because "I do have concerns that it might break screenshots." He doesn't actually merge it ("god damn, I do really wish I could merge this right now"). The promised "land real changes while filming" pays off partly: one squash-merge at 18:01 and a comment left on a contributor's PR.

### 8. Retention devices

- **Fake-surprise chart reveal** with "Huh" (×4 across the video).
- **Bait confession:** "Okay, I may have baited you guys a bit" (01:32).
- **Live-risk stakes:** "I'm admittedly kind of scared."
- **Running gag/refrain:** burning more tokens, with the audience invited to guess (16:02).
- **Numbered steps** at the start, then given up as the video turns into a live stream of threads.
- **Open loops:** "come back to it later to explain why I did it" (18:01); "I promise you we'll be touching on this a lot throughout" (11:00).
- **Chat as co-host:** bug reports, a PR to make it "51 instead of 50" (11:00), a rhetorical poll: "So, now I want your guys' opinion, chat... Am I right? I don't even need to see chat. I know I'm right on this" (35:00–35:31).
- **Rants:** Anthropic's docs "are full of lies"; the closed-source SDK; "I'm going insane" (34:00–34:30); "Cloudflare, please get your [expletive] together" (32:02, word dropped from captions).
- **Self-deprecation:** "showing my ass," "it might be my ADHD."
- **Named slogan:** "Safety nets, not guardrails" (47:00), credited to a chatter ("our boy Igor has caught on").

### 9. Ending

He lands the principle twice: once as a pattern ("If you find where there is friction in your flows... All of these are opportunities to improve your project," 43:30), once as a slogan ("de-risk the merge button," 46:01; "Safety nets, not guardrails," 47:00). The recap lists the pieces (sidebar inbox, verification systems, burning tokens, rollback). He defuses the plug criticism and adds a meta note: "a lot of why I made this is I want to look back to it in 6 months and see how silly some of the things I was doing are" (48:31); "Man, I need to do one of these every 3 months now, don't I?" CTA: comments and tips.

Sign-off: "Maybe you learned some things here. Maybe you hate everything I just showed you. Let me know in the comments. And if you have pro tips that are things that could benefit my workflows that I'm not trying yet, please let me know those as well, cuz I'm always looking for opportunities to improve, streamline, and be more effective in this new era of development. Let me know how y'all feel. Until next time. Peace, nerds."

### 10. Voice

1. "I have a confession to make." (00:01)
2. "Not that like my code is worse or I'm holding the team back. Okay, I am kind of doing that." (00:01) — self-undercut.
3. "Huh. I guess I just wasn't that busy during this window. Oh wait" (01:00)
4. "Huh. Okay, I may have baited you guys a bit." (01:32)
5. "Which means that a CEO that is a part-time coder is somehow probably out-shipping you." (01:32)
6. "I'm going to be showing my ass a bunch here." (02:01)
7. "And the first really cool thing I want to show you guys is today's sponsor." (02:01)
8. "So, let's dive in to how I get so much work done recently." (03:30)
9. "There's a couple pieces of this prompt I just spoke that I want to explain." (07:30)
10. "but Fable is Fable. If you don't say something explicitly, it will do whatever it wants" (10:01)
11. "I'm going to show you guys what's arguably the most important step of landing a lot of code. Ignoring the thread until it's done." (10:30)
12. "And I'm going to be real here, one of the things I optimize for is preventing loss of motivation." (11:31)
13. "If you guessed burning more tokens, you're starting to catch on." (16:02)
14. "I will admit, it might be my ADHD, but after the problem section, my eyes kind of are glazing over the fix." (20:01)
15. "And now I don't have to let the ADHD win." (21:00)
16. "I could do some crazy stuff to intelligently include it, but the lazy option is often the best one." (28:30)
17. "I do love that even Anthropic models know that Anthropic's docs are utter full of lies." (34:00)
18. "Am I right? I don't even need to see chat. I know I'm right on this." (35:31)
19. "I know these things probably seem a bit silly, but I'm trying to emphasize this pattern to you guys." (43:30)
20. "But I need to be real with you guys." (44:00)
21. "Safety nets, not guardrails." (47:00)

Style: most conversational of the five; he narrates his own clicks ("Squash and merge," "settle, settle, settle"). Mid-level profanity ("shitload," "pissed me off," "showing my ass"). Technical explanation comes through meta-commentary on his own prompts rather than through concepts, so beginners get "why I phrased it this way" and experts get the tooling. "You guys" ×7, "chat" ×7, "let me know" ×5, the most audience address in the group.

---

## 5. "Anthropic Rebuilt Git (yes really)" (hiI0Vk4NgeY, 48:04, uploaded 2026-10-16, 246k views)

### 1. Topic and angle

A line-by-line reading of Anthropic's engineering post "Redesigning source control at Anthropic," which describes Scion, an in-house VCS. They went from 2,500 to 30,000+ merges a day and migrated off Git in 5 months with a team of 7. Trigger: the blog post. Angle: validation and generalization. Git and GitHub weren't built for agent-scale work. Agents make bespoke infrastructure cheap now. And Anthropic's lessons echo things Theo has argued for years ("Theo was right again"). He adds one bearish note: they still categorize diffs programmatically instead of with Claude.

The title promises a surprising fact plus disbelief ("yes really"). He pays it off quickly (01:33) and spends the body on how it works. The title's skepticism is the opposite of his stance: he finds the project sensible and inevitable ("It's crazy how something like this would have felt comical a year ago. And now it's almost like, yeah, of course," 47:30).

### 2. Hook (0:00–2:30)

> "For as long as I've been writing code, I've been using Git and GitHub. Funny enough, I actually started using Git before I wrote code cuz I used it to manage plugins for my Minecraft servers way, way back when I was in like early high school. Git is core to the way that I build and work with software, but I have been starting to notice rough edges." (00:01)

Mechanism: personal history establishes authority and attachment, so the critique that follows carries weight. He states the problem as a thesis ("Git is not the right primitive for the way that things are moving right now," 00:31), shows a familiar villain (GitHub's uptime "looks more like a Christmas tree than a green bar," 01:01), then escalates with "But what if I told you GitHub wasn't the only problem here?" (01:01). The payoff number comes from the source: "Back in May they were merging 2,500 changes per day, but now in September they're doing more than 30,000" (01:33). He self-positions as an early thinker ("back in December I explored JJ... It turns out I'm not the only one who's been thinking about this"). He holds back how Scion works.

### 3. Lead-in

- **Sponsor (Infinite Red), 02:24–03:48, ~1:25.** In, a clever bridge built from the topic: "That said, I don't think everything should be ripped out for your own vibe coded alternatives. There's a lot of places where it makes sense to use a vendor product, like for example, today's sponsor" (02:02). The read pitches a consultancy for the AI era: "The role of a consultancy has fundamentally changed as a result of AI... What you bring them in for is the expertise." Personal tie: "I hit up my friend James at Infinite Red." Out: "Man, I'm actually really excited to dive into this article" (03:30).
- **Authenticity disclosure:** "As soon as I saw it drop, I wanted to read it, but I decided to put it off for this filming. So, you're getting my organic take on this" (03:30).
- **Screen apology (inferred visual):** "If you're wondering why the site looks gross, it's because when I leave it on the default light mode... everyone yells at me. So, using the dark reader extension... this is the poop green brown color it chose" (03:30–04:00).
- **No roadmap** beyond the article's own structure.

### 4. Segment outline

| Time | Job | Summary |
|---|---|---|
| 00:01–02:24 | Hook | Git history, GitHub downtime, JJ, the 2,500 → 30,000 stat. |
| 02:24–03:48 | Sponsor | Infinite Red. |
| 03:48–05:00 | Read source | Post intro: coding is no longer the bottleneck. |
| 05:00–07:30 | Tangent / self-proof | "De-risking the merge button" callback; his 3 pages of merges from midnight to 4 a.m. |
| 07:30–10:39 | Context / prior art | Meta's Mercurial fork, Graphite (now part of Cursor), monorepos, OpenAI's `openai/openai` "fun fact." |
| 10:39–17:52 | Read + explain | Why Git breaks at their scale (100 GB history, 25M checkouts/day, 600 PB); the design principles: always online, client-server asymmetry, API-first, horizontal scale, lock-free commits, no refs, sparse working copy. |
| 17:52–22:12 | Read + explain (deep) | Change sets, blob storage, Spanner, derived data; his "dumb this down" re-explanations. |
| 22:12–28:00 | Read + explain (deep) | Content addressing, tiered caches, daemon per node; he translates "Claude-isms to English." |
| 28:00–30:00 | Tangent | His Lust language project (a Rust subset for faster compiles). |
| 30:00–30:30 | Open loop | Asks for his own CI Git-checkout numbers: "We'll come back." |
| 30:30–33:28 | Read + react | Building with AI: Mythos preview rewrite (20x less memory), team of 7; his own ClickHouse migration; his TypeScript compiler. |
| 33:28–34:02 | Loop payoff | ~1,000 hours of T3 Code CI spent on Git checkouts, $350–600. |
| 34:02–37:01 | Read + react | Engineers "tell Claude no"; adversarial-review over-engineering; Gemini dunk. |
| 37:01–37:30 | Benchmarks | The speedup table (status 207x, new worktrees 84x). |
| 37:30–39:56 | Read + react | Security, directory ACLs ("Look who was right about committing your environment variables"), the bearish take on programmatic diff categorization. |
| 39:56–41:00 | Read + react | Operations; "super fans" Claude Slack bots; cringe at "Clauds." |
| 41:00–44:15 | Thesis moment | "Rethinking our priors"; post-merge testing; "Theo was right again"; rant about friction; his merge-queue idea. |
| 44:15–47:30 | Read + speculate | Not a Git replacement, not open-sourced; he imagines the internal sales/comms debate. |
| 47:30–48:04 | Close | "Fight the urge to make my own Git clone"; asks deep dives vs vibe coding. |

Shares: sponsor ~3%; reading and explaining the post ~65%; personal tangents and self-proof ~20%; hook/close ~6%.

### 5. Thesis and arguments

Thesis: agent-scale coding breaks tools built for humans, and since agents also make custom infrastructure cheap, companies (and you) should rethink trusted defaults like Git.

Arguments, following the article's order:
1. **Git's design assumptions (offline, everyone has everything) don't hold for always-online agents.**
2. **Rebuilding is normal** (Meta, Google Piper, Graphite).
3. **The architecture works**: immutability, content addressing, cache tiers, 200x smaller infra, the speedup table.
4. **Small teams with AI can now build this fast**, which he supports with his own Lust, TypeScript compiler, and ClickHouse projects.
5. **Engineering judgment still matters** (telling Claude no).
6. **Low-friction-plus-fast-recovery beats gatekeeping**, presented as Anthropic confirming his long-held view.

Counterpoints and steelmanning: "For the vast majority of repos, that is the right design, and it is a large part why Git became the standard" (11:01, from the post, which he endorses). "Would this work for most Rust projects? [Hell] no, absolutely not" (29:00, about his own project). He respects the Git maintainers: "You shouldn't have to force the industry standard into your workflow if it doesn't fit" (09:00). Criticism of Anthropic: the programmatic categorization is "the thing I'm most bearish on in this whole thing... maybe they are out of compute. Maybe we are screwed" (39:01), and the "Clauds" cringe. Concession of credit: "And you know what? To their [damn] credit, it is. Their uptime is significantly better" (39:01). He also says he's not secretly an OpenAI employee (09:30).

### 6. Evidence

- **One primary source,** the Anthropic engineering post, read nearly in full, paragraph by paragraph. He reads a sentence or two (sometimes repeating one by accident, 18:00), then reacts or re-explains.
- **Charts/tables in the post:** merges chart (blue PRs vs orange change requests, inferred visual), the commit history chart, the speedup table.
- **Personal proof:** his GitHub merge history scrolled live ("three full pages of GitHub merge history that I did in 4 hours," 06:31), his CI numbers, his side projects.
- **Insider knowledge and social context:** an ex-Meta engineer's tweet (name caption-heard as "Jay Gold," guess); "I know Boris was deep in developer tooling at Meta"; OpenAI's monorepo.
- **Background facts:** "External estimates are measuring as much as 7% downtime" for GitHub (00:31).

Read-and-react is ~70% of the runtime, the highest in the group. His original contribution is translation ("dumb this down"), applying the ideas to himself, and "Theo was right" framing.

### 7. Demo

None of a product. Two small live screen actions: scrolling his GitHub merge history (06:00–07:00, live: "We're still going. All the way up") and a background request for CI checkout stats that he kicks off at 30:00 and reports at 33:28 ("Oh, I got my numbers"). The second works as a mini-demo with a planted open loop.

### 8. Retention devices

- **"But what if I told you"** escalation (01:01).
- **Open loop with payoff:** CI numbers at 30:00 → 33:28 ("It's going to be a number that hurts me a lot").
- **Fun facts as pattern breaks:** "Ready for a really silly fun fact?" (09:30) about OpenAI's monorepo, with a twist joke: "So, for those saying I'm secretly employed, here's your proof."
- **Sarcastic asides to the source:** "Unsurprisingly, Anthropic uses Claude to write software far more than almost any other company. You might be surprised, guys" (10:30); "Okay, maybe they are using the same Claude that we are" (34:30).
- **Gloating callbacks to past takes:** env vars (00:31 → 38:01: "Look who was right... The Theo wins never end"), de-risking merge (05:00), "Theo was right again" (42:00).
- **Tangent with explicit permission:** "And like it's a silly thing to pivot to, but hear me out" (28:00).
- **Signposting difficulty:** "Oh boy, we're now in the data structure section. This is where we're going to get into the fun details" (17:32); "we're deep in the weeds, which I love" (21:00).
- **Insult humor aimed at critics:** "Can't wait for another anime profile picture on Twitter to say I'm wrong cuz they don't have a job" (38:01); "I hope that your mom's basement doesn't smell too bad" (43:01).
- **Imagined backstory skit** of Anthropic's internal debate (45:30–46:01).
- **Brand dunk:** Gemini hallucinating SQLite columns (36:31).

### 9. Ending

He lands on the cultural point the article ends on, not the tech: "It's crazy how something like this would have felt comical a year ago. And now it's almost like, yeah, of course" (47:30). Joke takeaway: "I'm going to go fight the urge to make my own Git clone. It's going to be hard, but I'll do my best." He states the genre and his enjoyment: "I love these types of nerdy rants." The CTA is a format question to the audience, unusual and useful for him: "Do you still enjoy these deep dives or do you just want to see me vibe code more?"

Sign-off: "Let me know in the comments and until next time, peace nerds."

### 10. Voice

1. "For as long as I've been writing code, I've been using Git and GitHub." (00:01)
2. "Seriously though, Git is not the right primitive for the way that things are moving right now. I'll be real with y'all." (00:31)
3. "The fact that GitHub's uptime looks more like a Christmas tree than a green bar like it's supposed to should say everything you need to know." (01:01)
4. "But what if I told you GitHub wasn't the only problem here?" (01:01)
5. "That said, I don't think everything should be ripped out for your own vibe coded alternatives... like for example, today's sponsor." (02:02)
6. "Man, I'm actually really excited to dive into this article." (03:30)
7. "I won't lie, the 5 months feels like one of those Claude timeline hallucinations" (04:00)
8. "If I had only heard people saying these things and I hadn't experienced it myself, I'd be calling [bullshit] right now. But this is reality." (07:02)
9. "So, let's dive in a bit here. This is interesting." (07:31) — standard source re-entry.
10. "The point I'm trying to make here is that this isn't as unprecedented as it might seem." (08:30)
11. "Ready for a really silly fun fact?" (09:30)
12. "Back to what Anthropic was saying here" (10:00) — return from tangent.
13. "This is a very interesting and worthwhile callout." (12:30)
14. "Fascinating." (18:00)
15. "To try and dumb this down, cuz we're deep in the weeds, which I love." (21:00)
16. "this is touching my functional programming heart deep at its core." (23:00)
17. "so I will do my best to translate from Claude-isms to English here." (25:01)
18. "I really hate how they use node here." (25:31)
19. "Look who was right about committing your environment variables... The Theo wins never end." (38:01)
20. "Guys, why why do you have to do this, Anthropic? I was defending you and it felt good." (40:00)
21. "Look at that. Theo was right again. I'm sorry to freak out about these things again, but you guys have no idea how long I've been harassed" (42:00)
22. "I don't care who the [hell] you are." (43:01)

Style: teacher mode. He reads a dense sentence, then restates it in plain words, often twice ("What this is trying to say is you just have to append," 19:00). Highest profanity in the group (11 bleeps). Highest use of "crazy" (×10) and "insane" (×9). Many short interjections after read passages ("Fascinating." "Makes sense." "Huge." "Can confirm."). Mixed-skill handling: explicit "dumb this down" flags, and analogies to what Git users already know (pack files, force pushes, worktrees).

---

## Patterns across these 5

### Hooks

What they share:
- **The first sentence names the genre or the trigger in plain words** ("it's new model time"; "Last week there was a really interesting model drop"; "They're back"; "I have a confession to make"; "For as long as I've been writing code, I've been using Git").
- **Within 30 seconds there's a hard number or a concrete surprise:** 100 trillion tokens/day; 50 PRs/week; 2,500 → 30,000 merges/day; "40 to 200x faster."
- **He takes a stance early that he'll defend or complicate:** "won't replace Fable or Astra"; "the numbers being shared here are misleading, but it doesn't mean the model is bad"; "They weren't that good."
- **He places himself in the story:** his usage, his early access, his history with Git, his chart.
- **The hook withholds the full verdict or the method,** not the topic. He never hides what the video is about.

How they differ:
- Ox Alpha is a mystery that resolves inside the hook (reveal at 01:31), with a smaller secret held for later.
- OpenAI fights back is a rivalry recap plus insider authenticity (2 a.m., early access).
- Agents wrong is a confession, then a contradiction, then a viewer challenge ("probably out-shipping you"), then live stakes.
- Git is personal history, then a villain, then "what if I told you," then the source's number.
- Jev breaks a genre ("this one's very different").

Hook length runs 1:00–2:30 (3–5% of runtime) before the sponsor.

### Shared skeleton (share of runtime)

1. **Hook, 3–5%.** Ends with a "can't wait to show you" or similar promise.
2. **Sponsor, 3–7%,** always right after the hook (01:00–02:30). It's bridged by a topical line (pun or argument), framed around agents, and closed with a soydev.link URL. The exit is a hard restart ("Quick breakdown on...", "Let's talk about this model a bit...", "So, let's dive in to...", "Man, I'm actually really excited to dive into this article"). Ox Alpha adds a second sponsor at ~88%, slotted before the tier-list verdict.
3. **Context/disclosure, 3–8%:** who made it, early access, "organic take," methodology caveats.
4. **Body, 70–80%,** which alternates three kinds of block:
   - **Read source and react** (blog post, chart, tweet, agent output).
   - **Show it** (his demo, his numbers, his repo).
   - **Zoom out** (framework, rant, tangent about his own projects).
   Blocks run 1–6 minutes. Release videos put the official blog/benchmarks in the middle third, not the start, and lead with his own usage.
5. **Late "fun" set piece, 8–12%:** fish slop or another visual demo at ~75–85% of runtime (Ox Alpha 34:42/43:14; OpenAI 22:17/30:58). Jev's equivalent is his own classifier app at 87%.
6. **Verdict, 5–8%:** a workflow placement ("use it like an if statement"; "in tandem with Opus"; tier list; "de-risk the merge button"). It's rarely a simple yes/no.
7. **Sign-off, under 1%:** "Let me know [how y'all feel / in the comments]. And until next time, peace nerds." (Ox Alpha: "peace out.")

### Recurring argument moves

- **Reframe the axis.** He introduces his own two-axis model and judges the product on it: System 1 vs 2 (Jev), intelligence vs behavior (Ox), spiky vs reliable (Sol), friction vs safety nets (agents), human-scale vs agent-scale (Git).
- **"It's great, but you'll misuse it."** Praise followed by a pre-emptive correction aimed at the comment section (Jev's judge/compaction, Ox's "always pick extra high").
- **Verdict as placement in his workflow,** not a score: which model he'll call for which job, what moves in the tier list, what he'll change in his Claude config.
- **Price/performance as the headline metric,** always with a concrete per-task dollar figure (37¢, 12¢, 21¢ vs $14.65, $350–600 of CI).
- **Self-proof tangents:** he applies the source's claim to himself (his merges, his compiler, his ClickHouse migration, his CI numbers).
- **"I was right" callbacks** to his past takes (env vars, de-risking merge, safety nets).
- **Balancing hedges:** "To be fair," "I will gladly admit," "for what it's worth, I am still coding with Sol and Fable," "Not entirely, but for the most part."
- **Disclosure as credibility:** early access but unpaid; "you're getting my organic take"; "I hope this proves I'm not paid off."
- **Brand dunks as comic relief:** Haiku, Gemini (in 3 of 5 videos), GitHub uptime (in 3 of 5), Anthropic docs.

### Recurring evidence handling

- **Blog posts are read in chunks of 1–3 sentences,** each followed by a reaction ("Yep, that part I absolutely agree with," "Fascinating," "Makes sense," "Can confirm") or a plain-words restatement ("What this is trying to say is...").
- **Charts get a skepticism pass:** log vs linear scales (Jev 14:31, Ox 26:31, OpenAI 04:31), chart cleanup ("I deleted a bunch"), methodology caveats read aloud.
- **His own benchmarks are named and reused:** Skatebench, fish slop, Deep SWE runs, Orchestrator V2 audit, T3 Code improvement bench. He discloses their flaws.
- **Friends and insiders are named** for social proof (Ben, Julius, Tibo, Boris, Dara, Matt, Chris, Ryan).
- **Live chat is a source:** questions answered on the spot, corrections, a slogan credited to a chatter.
- **The read-and-react share depends on type:** Git 70%, Jev 55%, Ox 30%, OpenAI 15%, Agents ~0%.

### Recurring phrases and transitions

- Sponsor in: "after a real quick break for today's sponsor"; "But first..."; "But I have to wait for one other thing first. Today's sponsor"; "the first really cool thing I want to show you guys is today's sponsor."
- Restart: "So, let's read through the announcement"; "So, let's dive in a bit here"; "Let's talk about this model a bit"; "Let's take a look at..."
- Return from tangent: "Anyways,"; "Back to what Anthropic was saying here."
- Emphasis: "I want to be really really clear here"; "This is one of the biggest important pieces to understand"; "I don't think you guys understand just how crazy that is."
- Candor markers: "I'll be real with y'all"; "if I'm being real"; "I'm going to be so real"; "I need to be real with you guys" (3 per video).
- Spoken self-correction: "Correction,"; "That is my bad"; "Am I misremembering?"; "Huh."
- Intensifiers: insane, crazy, comical(ly), absurd(ly), hilarious, wild, "rounds to zero," "hard to fathom."
- Insult softeners: "And don't worry, you're not the only one"; "I'm sorry for those who get it."
- Sign-off: "Let me know how y'all feel. And until next time, peace nerds."

### Variation by video type

- **Model/product release reaction** (Jev, Ox, OpenAI): own usage first, official benchmarks second; a framework segment; late fish slop or a visual demo; verdict as tier placement or workflow role. Disclosures about early access and pay are common (explicit in OpenAI; implicit elsewhere).
- **Tutorial/advice** (Agents): accusatory title that the video softens; almost all live screen-share; numbered steps that give way to live improvisation; a running gag ("burn more tokens"); principles named as slogans at the end; recap; an explicit plug disclaimer.
- **Blog deep dive / news commentary** (Git): read-along structure that follows the source's headings; heavy translation for a mixed audience; personal tangents as proof; "I was right" callbacks; speculation about the company's internal politics; ends by asking the audience which format they want.
- **Personal story** (none in this group as a pure type, though the Agents video uses confession and personal stakes as its spine).

### Surprises and pattern breaks

- **A model as a witness.** In the OpenAI video, Opus 5.5 blind-reviews the new model and guesses its price, and he reads its output as evidence and as a punchline ("blame Opus for saying this"). Using one AI's opinion of another as evidence is a distinctive move.
- **Failure left in as evidence.** Checkers loss, GitHub rate limits, Luna's bad triage, his own wrong prompt at Ox 18:30 that he turns into proof of good behavior. Failures are rarely cut.
- **The title can contradict the video.** "Jev is incredible" spends a third of its time telling you not to use it. "You're using AI agents wrong" never says what wrong is. "Anthropic Rebuilt Git (yes really)" argues it was obvious.
- **Second sponsor slotted as a cliffhanger** right before the tier-list verdict (Ox 37:31), using the tier-list language as the bridge.
- **Sub CTA placement varies:** mid-video joke (Jev 26:01), tied to a future-video tease (OpenAI 30:00), or absent (Agents, Git, Ox).
- **Exhaustion as content.** The OpenAI video opens and closes with how tired he is ("God, I'm so dead"), which reads as authenticity, not a flaw.
- **Profanity varies a lot:** Git has 11 bleeps while Jev has none. The deep-dive/rant mode is harsher than release reactions.
- **The "I was right" gloat is unusually personal** in the Git video ("The Theo wins never end"), aimed at Twitter critics with insults ("anime profile picture," "mom's basement"). That's sharper than the other four.
- **Chat as a live co-author** is constant in the Agents and Jev videos (recorded on stream) and absent in the OpenAI video (filmed alone at 2 a.m.). Viewer-address density follows from that.
