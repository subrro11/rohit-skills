# Test plan: Shiftplate v0.2 prototype

> Fictional showcase. Shiftplate, its users and every number here are invented. Built from the PRD Generator's [Shiftplate PRD](../../../prd-generator/examples/shiftplate/2-PRD.md) and [prototype prompt](../../../prd-generator/examples/shiftplate/3-PROTOTYPE-PROMPT.md). This is the plan, written before any session. There are no results in it.

v0.2 prototype · 2026-11-13 · Plan, not yet run · Owner: Founder

**Riskiest assumption:** a nurse at the end of a long shift will get a week of prepped food into the app in under 2 minutes, and will see that the new plan uses that food first.

It's the riskiest because every other part of Shiftplate depends on the fridge being logged. If logging is a chore, nobody re-plans, and the pilot's PMF signal (10 of 20 re-planning through two rota changes) can't happen. It's also gate G0 in the PRD.

## Research questions

| # | Question | Answered by |
|---|---|---|
| RQ1 | Can a nurse log a typical week of prep in ≤ 2 minutes without help? | T2 |
| RQ2 | After a shift change, can they get a new plan in under a minute, including the rota edit? | T1, T3 |
| RQ3 | Do they understand that the plan uses their prepped food first? | Comprehension check |
| RQ4 | Can they tell the app what happened to their meals after a shift, with little effort? | T4 |
| RQ5 | Do they notice prepped food that can't be used? | T5 |

**Debrief signal, not a gate:** whether re-planning at every rota change fits their real week. What people say they'll do is weak evidence; the pilot measures what they actually do.

**Out of scope:** the 4am energy crash and meal timing (deferred in the PRD), whether nurses would pay, the grocery list, and whether the gap meals appeal. The test doesn't measure waste; the pilot does.

## Participants

**Five nurses, P1 to P5,** from one user group: hospital nurses on rotating 12-hour shifts who already meal prep.

**Why five:** this is a qualitative think-aloud round. Five people from one group usually show the main problems with a flow, and the plan is to fix what they find and test again with new people, not to stop here. Five can't give a completion rate that holds for all nurses, so results are reported as counts ("4 of 5"). G0 is written in the same terms.

**Must have:**
- Works as a nurse in a hospital, on 12-hour shifts that rotate between days and nights.
- Has prepped meals for their shifts at least twice in the last four weeks.
- Can join a video call and open a link on a smartphone at the same time (two devices, or screen sharing from the phone).

**Nice to have:** at least two hospitals across the five; a mix of people whose rota flips weekly and every two weeks.

**Exclude:** the six nurses from the founder's original conversations, anyone in the founder's building, anyone who has seen Shiftplate, and anyone who works in UX, market research or app development.

**Incentive:** $40 gift card (*proposed*), paid whether or not they finish.

### Screener

**Recruiting post:** "Nurses on rotating shifts: 30-minute video call about how you plan food around work. $40 gift card. Fill in a 3-minute form to apply." The post doesn't name the app or mention meal prep.

| # | Question | Options | Rule |
|---|---|---|---|
| 1 | Which best describes your job? | Hospital nurse · Community or clinic nurse · Healthcare assistant · Paramedic · Pharmacist · Other | Must pick hospital nurse |
| 2 | Which best describes your shifts over the last two months? | Days only · Nights only · 12-hour shifts that switch between days and nights · 8-hour shifts that switch · Varies week to week, mostly days | Must pick 12-hour, switching |
| 3 | In the last four weeks, which of these have you done before a run of shifts? Tick all that apply. | Bought snacks to keep at work · Cooked several meals in one go to eat on later days · Ordered a meal kit · Packed leftovers from a family meal · Used a food delivery app on shift · None of these | Must include "cooked several meals in one go". Exclude anyone who ticks every option. |
| 4 | How many times in the last four weeks did you cook several meals in one go? | 0 · 1 · 2–3 · 4 or more | Must pick 2–3 or 4 or more |
| 5 | Describe the last time your shift pattern changed at short notice. What happened with your meals that week? | Free text | Must describe a real, specific week. Read before inviting. |
| 6 | Do you, or does anyone in your household, work in any of these? | UX or design research · Market research · App or software development · Food or meal-planning business · None of these | Exclude any except "None" |
| 7 | Have you taken part in research about meal planning or food apps in the last six months? | Yes · No | Exclude yes |
| 8 | Which devices could you use for a video call? Tick all that apply. | Smartphone · Laptop or desktop · Tablet | Must include smartphone |
| 9 | Roughly where do you work? (Used only so we talk to people from more than one hospital.) | Free text: town or area | Spread across at least two sites |

**Data handling:** screener answers and contact details live in a separate recruitment sheet, used only to choose and book people, and are deleted once all five sessions are done and incentives are paid. Neither goes in the notes. The PRD's privacy rule (R8: no employer or hospital name stored) applies to these notes too, so question 9 asks for an area, not a hospital.

**Scheduling:** don't book anyone straight after a night shift. Offer slots on days off or before a day shift. T4 asks people to imagine the end of a night shift; nobody should have to be in one.

## Setup

- **Format:** remote, moderated, 30 minutes, video call. The participant opens the prototype on their own phone, and shares the phone screen into the call (or joins on a laptop and shares from the phone). The prototype is built for 390 px; if their phone is wider, it still works but note the width in the grid.
- **People:** a moderator (talks) and a note-taker (silent, fills the grid, runs the timer). Up to two observers, cameras and mics off, questions to the moderator by private message.
- **Recording:** screen and audio, only with consent. Kept for 30 days, then deleted (*proposed*).
- **Reset between sessions:** clear localStorage, then open the link with `?today=` set to the test date. Every session uses the same date, so the use-by maths is the same for everyone.

### Needs from the v0.2 build

The [v0.1 prototype prompt](../../../prd-generator/examples/shiftplate/3-PROTOTYPE-PROMPT.md) left the end-of-shift check-in out. This plan tests v0.2, which needs:

1. **A simple check-in screen** (R5): after a shift, mark each planned meal as eaten, binned or still in the fridge, with an "all eaten" shortcut. Reachable from Home when a shift has just ended.
2. **A way to put Home in the "just finished a night shift" state** without changing the date, for example a `&shiftEnded=night` flag. Changing `?today=` mid-session would move every use-by date and change T5.
3. **The `/results` route** extended to log the number of taps on the check-in screen, alongside the existing log-prep and re-plan timings.
4. **A rota strip with no shifts entered** after reset, so T1 starts from empty.

### Task cards

Shared in the chat at the start of the task they belong to.

**Rota card (T1):** your next 14 days.

| | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Week 1 | Day | Day | Off | Day | Off | Night | Night |
| Week 2 | Off | Off | Day | Day | Day | Off | Off |

**Fridge card (T2):** what's in your fridge. The moderator fills the real dates from the fixed test date before the first session.

| Dish | Portions | Prepped |
|---|---|---|
| Chicken and rice | 3 | today |
| Lentil soup | 3 | 1 day ago |
| Veggie chilli | 2 | 2 days ago |
| Pasta bake | 2 | 5 days ago |

10 portions in all. The pasta bake is past the use-by window whether the build uses the PRD's original 4-day default or the 3-day default the [research pass](../../../deep-research/examples/shiftplate/RESEARCH.md) recommended, so T5 has the same answer either way.

**Shift card (T4):** "On the night shift you just finished, you ate your pre-shift meal and your on-shift meal. You didn't eat your post-shift meal; it's still in the fridge."

## Tasks and success criteria

Timed tasks (T1, T2, T3) are done without thinking aloud, because talking slows people down and the times feed a gate. The participant talks it through straight afterwards. T4 and T5 are think-aloud.

The app's button says "Log prep", so the T2 scenario says "get these into the app" instead of "log".

Outcome levels are from the [scoring guide](../../references/note-grid-and-scoring.md): pass, minor issue, major issue (finished only with a hint), fail. "Without help" counts pass only when a time target is part of the criterion.

| Task | Scenario (read word for word) | Starting state | Ends when | Pass | Fail signals | Target | Source |
|---|---|---|---|---|---|---|---|
| **T1** Enter your rota for the next 14 days | "Here's your rota for the next two weeks. Enter it." | Home, empty rota, rota card shared | All 14 days match the card and they say they're done | 14 of 14 days correct, no hint | Wrong day types left uncorrected; asks where to start; over 60 s | **Median ≤ 20 s**, from first tap on a day to the last correct day | R1 |
| **T2** Log the 4 dishes in the scripted fridge (10 portions) | "This card shows what's in your fridge right now. Get these 4 dishes into the app." | Home, rota from T1, fridge empty, fridge card shared | They return to Home with the fridge logged | 4 dishes, 10 portions, prep dates as on the card, in ≤ 2 min, no hint | Asks how to add a second dish; wrong counts or dates left uncorrected; over 2 min | **4 of 5 pass, ≤ 2 min each, without help** (timed by `/results`) | R2, G0 |
| **T3** Change Thursday to a night shift and re-plan | "Thursday has changed from a day shift to a night shift. Update your plan." | Home, rota from T1, fridge from T2 | A saved 7-day plan with week 1 Thursday as Night | Rota edited and plan saved in < 1 min, no hint | Edits the wrong Thursday; doesn't rebuild the plan; looks for an edit option inside the plan; over 1 min | **4 of 5 pass, < 1 min including the rota edit** (timed by `/results`) | R1, R3, G0 |
| **T4** End-of-shift check-in | "You've just finished a night shift. Tell the app what you ate." | Home in the just-finished-night state (`&shiftEnded=night`), shift card shared | Check-in saved | Pre-shift and on-shift marked eaten, post-shift marked still in the fridge, no hint | Marks everything eaten via the shortcut; marks the post-shift meal binned; can't find where to start | **4 of 5 pass** (*proposed*). Taps logged against R5's ≤ 3 taps for a typical shift; this shift is mixed, so taps are recorded, not gated | R5 |
| **T5** Find prep past its use-by | "Find out which of your prepped food can't be used this week." | Wherever T4 left them | They name the dish aloud | Names the pasta bake (2 portions), no hint | Names a dish that's still in date; says everything is fine; looks only at the plan | **4 of 5 pass** (*proposed*) | R7 |

**If stuck** (all tasks): after 10 seconds of silence, "What are you looking for?" After 20 more, "What would you do next if I weren't here?" Any hint beyond that makes the task a major issue at best. Move on at 3 minutes (T2) or 2 minutes (others) and mark it fail.

### Comprehension check

Asked straight after T3, with the new plan on screen: **"Which meals this week use your prep?"**

- **Pass:** points to the meals filled from their logged dishes and none of the new ones, without counting aloud from the fridge card.
- **Target:** 4 of 5 (*proposed*). This is the second half of the prototype's "What we're testing", so it gates G0 alongside T2 and T3.

## Decision rule

Set before testing. It doesn't change after the sessions; if it looks wrong afterwards, that goes in a separate note.

| Result | Means | Next |
|---|---|---|
| **Pass:** T2 and T3 each 4 or 5 of 5, and the comprehension check 4 or 5 of 5 | G0 passes as written in the PRD | Fix any minor problems and move to G1 (recruit the 20-nurse pilot) |
| **Iterate:** T2, T3 or the comprehension check at 3 of 5 | The loop works but a step is weak (*proposed*, mirroring the PRD's pilot bands) | Fix the weakest step, then run this plan again with 5 new nurses |
| **Stop:** T2 at 2 of 5 or fewer | Logging the fridge is too much work for a tired nurse; the riskiest assumption is wrong (*proposed*) | Go back to the PRD and rethink how prep gets into the app before building more |

T1, T4 and T5 don't gate G0. Their results feed the acceptance criteria for R1, R5 and R7 before G1, and any blocker in them must be fixed before the pilot.

## Session script (30 minutes)

| Block | Minutes |
|---|---|
| Intro | 2 |
| Consent | 2 |
| Warm-up | 4 |
| T1 | 3 |
| T2 | 5 |
| T3 + comprehension check | 4 |
| T4 | 3 |
| T5 | 3 |
| Debrief | 4 |
| **Total** | **30** |

### Before each session

- Reset the prototype (clear localStorage, open with the fixed `?today=`). Check the rota strip is empty and the fridge shows nothing.
- Open a new set of rows in the note grid for P*n*.
- Have the three cards ready to paste into the chat.

### Intro (2 min)

"Hi, I'm [first name], and [first name] is here taking notes. Thanks for giving up your time, especially on a day off.

We're trying out an early version of an app, and we want to see where it works and where it doesn't. We're testing the app, not you. If something's confusing, that's the app's problem, and it's exactly what we need to find out.

There are no right or wrong answers, and you won't hurt anyone's feelings. This takes about 30 minutes."

### Consent (2 min)

"With your permission, we'll record your phone screen and our voices. Only the small team working on this will see it. We'll keep it for 30 days and then delete it. Your name won't be in any notes; we'll call you P[n]. Please don't show anything personal on your phone, like messages or notifications. Turning on Do Not Disturb helps.

You can skip anything or stop at any point, and you'll still get the gift card.

Is it OK to record?"

Start recording only after a clear yes, then say: "You've said it's OK to record. Thank you." If they say no, carry on without recording and the note-taker writes fuller notes.

### Warm-up (4 min)

- "Tell me about your shifts at the moment. What does a typical fortnight look like?"
- "Tell me about the last time you prepped food for your shifts. What did you make, and when?"
- "Think back to the last time your rota changed after you'd prepped. What happened to the food?"

### Tasks (18 min)

"I'll give you a few things to try on your phone. Please do them as you normally would. For the first three, just do it without talking, and we'll chat straight after. For the last two, I'll ask you to think out loud as you go."

Read each scenario from the table above, word for word. Paste the card for that task into the chat first.

**After T1, T2 and T3** (silent tasks), ask: "Talk me through what you just did. Was there any moment you weren't sure?" Then use one or two of the probes below if time allows.

**After T3**, with the plan on screen, ask the comprehension check: "Which meals this week use your prep?"

**Before T4 and T5:** "For this one, please say what you're thinking as you go, even if it seems obvious."

**Probes** (after a task, never during):
- "What were you expecting to happen there?"
- "You paused on that screen. What was going through your mind?"
- "How would you normally keep track of this?"
- "Was there anything you looked for and didn't find?"

**Neutral prompts during think-aloud:** "What are you thinking?", "What are you looking for?", "Say more about that."

**Don't say:** any screen or button name before they use it; "good" or "right" after an action; "Did you notice…?"; "Most people…". If they ask "Is this right?", reply "What do you think?"

### Debrief (4 min)

- "Think about the next time your rota changes. Walk me through what you'd do with the food you've prepped."
- "When, if at all, would you open this? What might stop you doing it every time your rota changes?"
- "What would you change about it?"
- "Is there anything else we should know?"

"Thanks so much, that's really helpful. The gift card will arrive by email within two working days. If you've any questions about the recording later, just reply to the booking email."

### After each session (10 min, moderator and note-taker)

- Fill gaps in the grid while it's fresh, and agree each outcome level and severity.
- Note anything the moderator said that may have led the participant.
- Check `/results` recorded the T2, T3 and T4 numbers for P*n*.
- Reset the prototype.

## Note-taking grid

One row per participant per task, plus one for the comprehension check and one for the debrief. Full guidance in the [scoring guide](../../references/note-grid-and-scoring.md).

| P | Task | Outcome | Time / taps | Path taken | Hesitations and wrong turns | What they said | Help given | Problem and severity |
|---|---|---|---|---|---|---|---|---|
| P1 | T1 | | | | | | | |
| P1 | T2 | | | | | | | |
| P1 | T3 | | | | | | | |
| P1 | Comprehension | | n/a | | | | | |
| P1 | T4 | | | | | | | |
| P1 | T5 | | n/a | | | | | |
| P1 | Debrief | n/a | n/a | n/a | n/a | | n/a | |
| P2 … P5 | (same rows) | | | | | | | |

**What to watch for in particular:**

- **T1:** whether they understand that tapping a day cycles it, and how many taps they spend going round past the shift they wanted.
- **T2:** whether they find the recent-dishes list or type everything; how they enter "5 days ago"; whether they log 4 dishes as 4 entries or try to add portions in one go.
- **T3:** whether they edit the rota first or look for an edit inside the plan; whether they notice the "rota changed" prompt.
- **Comprehension:** which tag or label they point to, and whether they count from memory or from the screen.
- **T4:** whether the "all eaten" shortcut pulls them into marking the post-shift meal wrongly.
- **T5:** whether they look on Home, in the plan or in the fridge list, and how long before they find it.

## Scoring

- Each task is scored per participant on the four outcome levels, and reported as counts ("3 of 5 passed, 1 minor issue, 1 fail"). Never averaged.
- T1 time is the median of the five times, with each time listed. T2 and T3 are checked per person against their limit, then counted.
- Problems are logged once each with the participants who hit them, and a severity: blocker, major, minor or cosmetic.
- Each research question gets a one-line answer, with participant IDs.
- The decision rule above is applied as written.

## Unmoderated variant (optional)

Only if moderated sessions can't be booked. Use an unmoderated testing tool that records the phone screen and voice.

- **Scenarios stand alone.** Each task screen shows the card as an image and the scenario word for word, plus: "When you've finished, tap Next."
- **Check completion.** After T2: "How many portions did you log?" After T5: "Which dish can't be used?" The answers, plus `/results`, decide pass or fail.
- **One written question per task** instead of probes: "Was there any moment you weren't sure what to do? What happened?"
- **The comprehension check** becomes: "Which meals this week use food you'd prepped? List them."
- **Same success criteria and decision rule.** Recruit 5 again; don't use more people to make up for weaker data.
- **What's lost:** no follow-up questions, no rescue when someone is stuck (so more fails that teach less), and think-aloud is less reliable without someone prompting. If G0 sits on the line between pass and iterate, run moderated sessions before deciding.

## Next step

After the five sessions, hand the filled-in grid and `/results` export to a `user-interview-synthesis` skill if one is available, or synthesise it against the criteria above. Then apply the decision rule and revise the PRD (version bump, changelog).
