# Shiftplate: quiz transcript

> Fictional showcase. Shiftplate, its users and every number here are invented. This is a real, unedited run of the skill (quiz answers written by a made-up founder); only the owner name was replaced with "Founder".

## You
Quiz me on my product. Shiftplate is an app that plans meals for nurses who work rotating 12-hour shifts.

## Agent
Let's do it. Five questions, one at a time: the problem, product–market fit, north star, goals and non-goals, then what to build first. I'll grade each answer and push back where it's thin. At the end you get a scorecard, and I can turn it into a PRD if you want.

---

**Question 1 of 5: What's the problem?**

Fill in this sentence:

> **[Which nurses]** are trying to **[job]**, but **[obstacle]**, so today they **[workaround]**, which costs them **[cost]**.

**Why it matters:** "Nurses on rotating shifts" sounds specific, but it covers a lot of different people. A day-to-night rotator with kids, a single travel nurse and an ICU nurse doing three 12s in a row have different problems. If you can't name the obstacle and what they do about it today, the app turns into a generic meal planner with a shift calendar attached.

**What a strong answer looks like (different product):**
> "Freelance designers with 3+ active clients are trying to invoice on time, but their hours are spread across Toggl, email and Figma comments. So at month-end they rebuild timesheets from memory in a spreadsheet, which takes about 4 hours and they guess they under-bill 10–15%."

That answer names a user you could recruit this week, a workaround people actually use, and a cost with a number on it.

**Things I'll test your answer against:**
- Could you find five of these nurses to interview this week?
- What do they do *today*? Vending machines, takeout after a shift, Sunday meal prep that falls apart when the schedule flips, skipping meals?
- What does it cost them? Money, sleep, weight, energy on shift, feeling guilty?
- Is the problem a real pain and not a feature in disguise? "Nurses need a meal planner that syncs with their schedule" is a solution, not a problem.

Your turn.

## You
Hospital nurses who rotate between day and night 12s are trying to eat properly on shift and on their recovery day, but their schedule flips every week or two, so Sunday meal prep falls apart. Today they buy vending machine food or takeout at 3am. It costs them money and they feel bad.

## Agent
**Verdict: needs work, but close.** Most of this is strong. The cost part is weak.

**What's working**
- **Specific user.** "Hospital nurses who rotate between day and night 12s" is a group you could recruit from one unit's group chat. It also rules out fixed-schedule nurses, which is the right call.
- **Concrete obstacle.** "The schedule flips every week or two, so Sunday meal prep falls apart" names the actual failure. It's not "nurses are busy." It's that a weekly planning habit doesn't survive a schedule that changes every one or two weeks. That's your wedge.
- **Real workaround.** Vending machines and 3am takeout are things people do today, and you can check them.

**What's missing**
- **"It costs them money and they feel bad" won't hold up.** It has no number, and "feel bad" could mean guilt, low energy on shift, weight gain or poor sleep. Each of those points to a different product. If the real cost is money, you're building a budgeting tool. If it's energy at 4am, you're building around meal timing and what to eat on a night shift. If it's the recovery day, you're building for the sleep-wrecked day after the last night shift.

**Follow-up (one question):**
Put a number on it, even a guessed one, and pick the cost that hurts most:

1. **Money:** roughly how much a week goes on vending machines and takeout? (Label it *assumed* if it's a guess.)
2. **Which part of "feel bad" is worst:** crashing on shift, feeling awful on the recovery day, weight or health, or guilt about wasting the food they did prep?

And tell me where that comes from: your own shifts, conversations with nurses, or a hunch. A hunch is fine at this stage, but it decides whether question 2 is about problem fit or solution fit.

## You
Assumed about $60 a week on takeout and vending. The worst part is the crash around 4am on night shifts, and the wasted prep food when the rota flips. This comes from talking to six nurses in my building, nothing more yet.

## Agent
**Verdict: strong. Moving on.**

Here's your problem statement now:

> Hospital nurses who rotate between day and night 12s are trying to eat properly on shift and on their recovery day, but their schedule flips every week or two, so Sunday meal prep falls apart. Today they buy vending machine food or 3am takeout (about $60 a week, *assumed*). The worst costs are the energy crash around 4am on night shifts and the prepped food thrown out when the rota flips.

The two costs fit together well. The wasted prep and the 4am crash come from the same cause: a plan made for a schedule that has since changed. That gives you one problem to solve, not two.

**Logged as open questions** (no need to fix them now):
- The $60 is a guess. Ask the next nurses you talk to to check their banking app for a week of takeout and vending spend.
- Six informal chats with neighbours count as an early signal, not proof. They're probably friendly, and they may all work at the same hospital.

---

**Question 2 of 5: Is there product–market fit, or a path to it?**

Fill in this hypothesis:

> We believe **[narrow segment]** will **[adopt / pay / switch]** because **[value]** is meaningfully better than **[what they do today]**. We'll know when **[signal]** reaches **[threshold]**.

Then tell me which stage you think you're at:

| Stage | What you're proving |
|---|---|
| Problem fit | The problem is real, frequent and painful |
| Solution fit | Your approach fixes it better than what they do today |
| Product–market fit | A segment adopts it and keeps using it |

**Why it matters:** The stage decides what you build next. If you're at problem fit, the next step is a cheap test, not an app. Writing a full spec before you've shown the solution works is the most common way to spend six months building something nobody keeps using.

**What a strong answer looks like (different product):**
> "We believe solo physiotherapists running their own clinic will pay $29 a month because automatic no-show rebooking recovers more revenue than their current method, a receptionist phoning around. We're at solution fit. We'll know when 8 of 15 pilot clinics are still using it unprompted in week 6 and 40%+ say they'd be 'very disappointed' without it."

That example names a narrow segment, an action you can observe, a comparison with what people do today, and a number that passes or fails.

**I'll push on:**
- **Segment:** all rotating nurses, or something narrower? One hospital, one specialty, nurses who already try to meal prep?
- **Action:** what will they do that proves it? Use it every rota change, pay for it, or tell a coworker?
- **Signal and threshold:** a number you'd accept as "this is working", and one that tells you to stop.

## You
We believe nurses who already try to meal prep and work rotating 12s at large hospitals will use Shiftplate every rota change, because it re-plans the week's meals in under a minute when the schedule changes, which beats starting meal prep over from scratch. We're at problem fit. We'll know when 10 of 20 test nurses re-plan through two rota changes in a row without being reminded.

## Agent
**Verdict: needs work, and the gap is an important one.** The segment and the signal are good. The value claim doesn't connect back to the problem you just described.

**What's working**
- **"Already try to meal prep" is the best part of this.** These nurses have shown they want to solve the problem, so you're fixing a habit that breaks rather than trying to create a new one. That's much easier.
- **The signal is behaviour, not opinion.** "Re-plans through two rota changes without being reminded" is hard to fake and is a real measure of repeat use. 10 of 20 is a reasonable bar.

**What's missing**
1. **The stage label doesn't match the test.** You say problem fit, but this test is a solution-fit test because it checks whether *your approach* works. That's fine. Six conversations is decent early evidence that the problem is real, so you're probably between the two. Call it **"early solution fit"** and keep testing the problem with the same 20 nurses: does the $60 hold up, and do they actually throw out prepped food?
2. **There's no stop threshold.** Ten of 20 is your "it's working" bar. What result makes you stop or change direction? Say it now, before you see the data. Otherwise 6 of 20 will start to feel promising.
3. **The value claim doesn't reach the costs.** This is the main gap. In Q1, the costs were *the 4am crash* and *thrown-out prep food*. Your value claim is *re-plans the week in under a minute*. But a fast re-plan doesn't by itself:
   - stop the food you already prepped from going to waste. That needs the new plan to reuse what's already in the fridge.
   - prevent the 4am crash. That needs the plan to cover *what and when* to eat on a night shift, not only which meals go on which days.

   If the re-plan just shuffles meals around the calendar, nurses could re-plan every rota change, pass your signal, and still crash at 4am and throw food out. That would be a false positive.

**Follow-up (one question):**
When the rota flips and Shiftplate re-plans, what does the new plan actually do differently? Specifically, does it (a) use up food that's already prepped, (b) change meal timing and contents for night shifts, or (c) both? Pick the one that matters most for v1, and add your stop threshold.

## You
Fair. For v1 it does (a): the re-plan reuses what's already prepped in the fridge first, then fills the gaps. Night-shift timing comes later. Stop threshold: if fewer than 5 of 20 re-plan twice unprompted, we go back to problem interviews.

## Agent
**Verdict: strong. Moving on.**

Your hypothesis now:

> We believe **nurses who already meal prep and work rotating 12s at large hospitals** will **re-plan in Shiftplate at every rota change**, because it **rebuilds the week around food already prepped in the fridge**, which beats **throwing the prep out and starting over**. Stage: **early solution fit**. **Pass:** 10 of 20 re-plan through two rota changes unprompted. **Stop:** fewer than 5 of 20, and you go back to problem interviews.

Choosing (a) is the right v1 call. Reusing prep is a concrete thing the app can do, and "food thrown out" is easy to measure.

**Logged for later:**
- **You've chosen to fix the smaller pain first.** In Q1 you said the 4am crash was the worst part, and v1 doesn't address it. That's a reasonable trade, but say it openly. It becomes a deferred non-goal in Q4, and some nurses in the test will probably ask for it.
- **This is now your riskiest assumption:** reuse-first only works if the app knows what's in the fridge. Will a tired nurse log their prep? If logging takes 5 minutes, the "under a minute" re-plan isn't true anymore. That's the first thing to test cheaply.
- **The middle zone:** decide now what 5–9 out of 20 means. Probably "iterate and run again," but write it down.

---

**Question 3 of 5: What's the north star, and what feeds it?**

Name **one** metric that only goes up when nurses get real value from Shiftplate *and* the business benefits. Then name 2–3 input metrics that drive it, and one guardrail: something that must not get worse while you push the north star.

```
North star: ___
├── Breadth:   how many nurses reach value
├── Depth:     how much value each nurse gets
├── Frequency: how often
└── Guardrail: what must not get worse
```

**Why it matters:** Whatever you measure is what the team will optimise for. If you pick "weekly active users" or "plans created," you'll end up building nudges and notifications. If you pick a metric tied to the outcome, you'll build things that actually help nurses.

**What a strong answer looks like (different product):**
> A language app: **north star = lessons completed with 80%+ accuracy per week.** Breadth: new learners finishing their first lesson. Depth: lessons per learner. Frequency: days active per week. Guardrail: accuracy mustn't fall. Otherwise you could raise "lessons completed" by making them easier.

**I'll push on:**
- Does it measure *value delivered* (prep eaten instead of thrown out, meals covered) or just *activity* (re-plans, app opens)? Re-plans are your test signal, but that doesn't automatically make them the north star.
- Can you actually measure it? For example, how would you know whether the prep was eaten?
- What's the obvious way to game it, and which guardrail stops that?

## You
North star: weekly shift meals covered by a plan the nurse actually followed (they tick it as eaten). Breadth: nurses who complete a first re-plan. Depth: share of prepped portions eaten rather than binned. Frequency: rota changes re-planned. Guardrail: time to log prep stays under 2 minutes.

## Agent
**Verdict: strong. One measurement gap to close.**

**What's working**
- **The north star measures value, not activity.** "Shift meals covered by a plan the nurse actually followed" only goes up when a nurse eats the planned food instead of buying takeout. Re-plans alone can't raise it.
- **Depth tests your v1 bet directly.** "Share of prepped portions eaten rather than binned" is exactly what the reuse-first re-plan is supposed to improve. That's your **primary metric for v1**.
- **The guardrail targets your riskiest assumption.** Keeping prep logging under 2 minutes stops you from making the plan more accurate by making nurses log more. It also has a number on it, which most guardrails don't.

**What's missing**
1. **Ticking is effort, and it under-counts.** A nurse who eats the planned meal at 4am but doesn't open the app looks the same as one who bought takeout. So the north star will read low, and it will reward ticking more than eating. Note it as a known bias. Consider an end-of-shift check-in ("ate it / binned it / still in fridge") so one tap covers the whole shift.
2. **"Binned" has no data source.** Nobody opens an app to report throwing food away. If you can't measure binned portions, your primary metric is a guess. A practical fix: at the next re-plan, ask what's still in the fridge. Anything prepped, not ticked and no longer there counts as binned.
3. **No baselines or floors.** These are fine as "measure in week 1," but set the floors now, before you see the data.

**Follow-up (one question):**
How will you record "binned"? You can take my suggestion (infer it at the next re-plan) or use your own. And what floor would count as a win for the primary metric? For example, *share of prepped portions eaten goes from ~X% today to at least Y% by week 4.* A guess is fine; label it *assumed*.

## You
Goals: a nurse re-plans after a rota change in under a minute; prepped food waste drops by half for test nurses. Non-goals: no night-shift meal timing in v1; never a calorie counter or diet app; not optimising for families or non-shift workers.

## Agent
You went straight to goals, so I'll treat the Q3 follow-up as unanswered and log it:

- **Open (Q3):** there's no data source for "binned" yet, which affects your primary metric. Partly answered: your "waste drops by half" goal below works as the floor.

---

**Verdict: strong. One fix needed.**

**What's working**
- **"Re-plans in under a minute"** is a goal you can time with a stopwatch in a test session. Nobody can argue about whether it passed.
- **"Prepped food waste drops by half"** connects to your primary metric and gives it the floor that Q3 was missing. You still need the week-1 baseline, and you still need a way to measure "binned" (the open item above).
- **The non-goals cover all three kinds, and each one rules out something people would expect:**
  - *Deferred:* night-shift meal timing. This is the smaller-pain-first trade from Q2, now written down.
  - *Out of scope:* "never a calorie counter or diet app." This is the strongest line in the set. It tells a nurse in a tired, guilty moment that the app won't judge them, and it gives you something to point to when an investor asks for macros.
  - *Not optimising for:* families and non-shift workers. That keeps the meal planning built around the shift.

**What's missing**
1. **Night-shift timing has no trigger.** A deferred item without a trigger tends to either wait forever or sneak back in during week 3. Pick the condition that brings it back. For example: *"once the waste goal is met and 8+ of 20 test nurses ask for night-shift help unprompted."*
2. **Optional: add your PMF test as a goal.** "10 of 20 nurses re-plan through two rota changes unprompted" is already your pass bar. Listing it as goal #3 keeps the team focused on repeat use, not just a fast first re-plan.

**Follow-up (one question):**
What's the trigger that brings night-shift timing into scope? Use mine or write your own.

## You
Use your trigger. And yes, infer binned at the next re-plan. Prioritise these candidate features: fridge prep logging, rota import from the hospital scheduling app, one-tap re-plan, end-of-shift check-in, grocery list, recipe library, night-shift meal timing, sharing plans with a partner.

## Agent
That closes Q3 and Q4. "Binned" is now inferred at the next re-plan, and night-shift timing comes back when **the waste goal is met and 8+ of 20 test nurses ask for night-shift help unprompted.**

---

**Question 5 of 5: What do we build first?**

You asked me to do this one, so it's my recommendation rather than a grade of your answer. Push back wherever you disagree.

I scored the features with **RICE** (reach × impact × confidence ÷ effort). Reach is out of your 20 test nurses, and impact is how much each feature moves your primary metric, *share of prepped portions eaten*. **All numbers are assumed.**

| Feature | Reach | Impact | Conf. | Effort (wks) | Score | Priority |
|---|---|---|---|---|---|---|
| Fridge prep logging | 20 | 3 | 80% | 2 | **24** | **P0** |
| One-tap re-plan | 20 | 3 | 80% | 3 | **16** | **P0** |
| End-of-shift check-in | 20 | 1 | 80% | 1 | **16** | **P0** |
| Grocery list | 20 | 1 | 80% | 1 | **16** | P1 |
| Night-shift meal timing | 20 | 2 | 50% | 4 | 5 | Later |
| Rota import from scheduling app | 20 | 1 | 50% | 6 | 1.7 | Later |
| Recipe library | 20 | 0.5 | 50% | 4 | 1.25 | Later |
| Sharing plans with a partner | 5 | 0.5 | 50% | 2 | 0.6 | Later |

**Your list is missing one P0: manual rota entry.** The re-plan can't run unless it knows the shifts changed. If import is deferred, nurses need a fast way to mark the new pattern, such as tapping days as D, N or off. Count that time inside the "re-plan in under a minute" goal.

**Overrides, and why:**
- **The end-of-shift check-in is P0 even though its impact is only medium.** It adds no value for the user, but it's how you measure the north star. Without it, you can't tell whether the 10-of-20 test passed.
- **The grocery list scores the same as the re-plan but stays P1.** The core loop works without it, and it doesn't test your hypothesis. As a stopgap, show the ingredients for gap-filling meals inside the re-plan screen.
- **Rota import goes to Later even though everyone would use it.** I don't know which scheduling apps your 20 nurses use, or whether any of them export data. That's low confidence and high effort. Trigger to promote it: nurses say rota entry is why they skipped a re-plan.
- **A recipe library goes to Later, but you still need a few meals to fill gaps.** A fixed set of about 20 meals inside the re-plan covers that. Trigger to expand: nurses skip gap meals because they're repetitive.
- **Partner sharing goes to Later.** It goes against your "not optimising for families" non-goal. Trigger: 5+ of 20 ask for it unprompted.
- **Test the riskiest assumption first.** Before you build prep logging, time 5 nurses logging a real fridge on a paper or clickable mock. If anyone takes more than 2 minutes, change the logging design before you build anything else.

---

## Scorecard

| # | Question | Your answer | Verdict | Remaining gap |
|---|---|---|---|---|
| 1 | Problem | Nurses on rotating day/night 12s who prep on Sunday. The rota flips, so prep gets thrown out and they buy 3am takeout (about $60/wk *assumed*). Worst cost: the 4am crash | **Strong** | $60 unverified. Evidence so far is 6 neighbours, probably all at one hospital |
| 2 | PMF | Nurses who already meal prep will re-plan at every rota change, because re-planning reuses food already in the fridge. Pass 10/20, stop <5/20 | **Strong** (after revision) | The 5–9 middle zone has no rule. Willingness to pay not tested |
| 3 | North star | Shift meals followed per week. Primary: share of prepped portions eaten. Guardrail: logging under 2 min | **Strong** | Ticking under-counts meals actually eaten. Baselines arrive in week 1 |
| 4 | Goals / non-goals | Re-plan in under 1 min. Waste halved. Not a diet app. Night-shift timing deferred with a trigger | **Strong** | Optional: add the 10/20 pass bar as goal #3 |
| 5 | Prioritisation | P0: prep logging, re-plan, check-in, manual rota entry | **My recommendation**, not graded | Your effort estimates, and whether rota import is really harder than it looks |

**Overall:** your thinking is in good shape for an early solution-fit test. The weakest point is evidence. Six neighbours count as a signal, not as validation.

**Next:** do you want me to turn this into a **Lite PRD**? Lite fits because you're still testing whether the approach works. I'd follow it with a **prototype prompt** for a coding agent to build the thinnest clickable version: prep logging, rota tap-in and re-plan. That's enough to run the 2-minute logging test with 5 nurses this week.

## You
Yes, write the Lite PRD to PRD.md, then write PROTOTYPE-PROMPT.md.

## Agent
I've written both files: `PRD.md` and `PROTOTYPE-PROMPT.md`.

**The recommendation in short:** build a mobile app for nurses who already meal prep. When their rota changes, it rebuilds the week's meals in under a minute, using up food already prepped in the fridge before suggesting anything new. v1 is a 20-nurse pilot, not a launch. It passes if 10 of 20 nurses re-plan through two rota changes in a row without being reminded, and you stop if fewer than 5 do.

**The three biggest open questions:**
1. **Does the $60 a week hold up?** At the moment it rests on six conversations in your building. Ask the nurses you recruit to check a week of spending in their banking app.
2. **How long is prepped food safe in the fridge?** I set a 4-day default, which is my own guess. Check it against published food-safety guidance before the pilot, because the re-plan relies on it to decide which food is still usable.
3. **Can you recruit 20 qualifying nurses from more than one hospital?** If they all come from one building, the pilot can't tell you whether the pattern holds anywhere else.

**Things I added that we didn't cover in the quiz. Check you agree:**
- **No re-plan reminders during the pilot.** Your pass bar is re-planning "without being reminded", so a nudge would make the result meaningless.
- **A privacy requirement (R8):** the app never collects the employer or hospital name, and deletes data on request within 7 days.
- **"Why now" is marked "Evidence needed".** I couldn't find a real one, so I didn't make one up.
- **Pilot length of 4–6 weeks.** This is a guess based on the rota flipping every one or two weeks.
- **Owner set to "Founder".** Change it if that's wrong.

**The prototype** tests your riskiest assumption: whether a tired nurse will log their fridge in under 2 minutes. It's a phone-sized app that runs locally with one command. It covers logging prep, changing the rota and re-planning, and includes a hidden `/results` page that records how long each step took. It also has an expired-food state and an empty-fridge state you can trigger on demand. Give the file to a coding agent, test with 5 nurses, then bring the numbers back and I'll update the PRD to v0.2.
