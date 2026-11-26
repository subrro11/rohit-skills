# Synthesis: Shiftplate v0.2 prototype test

> Fictional showcase. Shiftplate, the five nurses and every number are invented. The input is [NOTES.md](NOTES.md); this file is the skill's output from it, in test readout mode.

**Question:** does the v0.2 prototype pass gate G0 in the [PRD](../../../prd-generator/examples/shiftplate/2-PRD.md), and if not, which step should be fixed before the 20-nurse pilot?
**Data:** 5 nurses on rotating 12-hour shifts who already meal prep (P1–P5), 30-minute remote think-aloud sessions on their own phones, one round. All notes coded; 0 observations parked.
2026-11-13 · Every claim cites participant IDs and note IDs (N…). Quotes are verbatim from the moderator notes; nothing is invented.

## Answer

**Iterate.** The re-plan is the hook: 4 of 5 re-planned in under a minute and all 5 could say which meals used their prep (Strong, T-A). The friction sits either side of it. Logging the fridge misses G0 (3 of 5 within 2 minutes, where the gate needs 4) and 3 of 5 called it homework (Strong, T-D). Check-in is the weakest link: everyone completed it, but 3 of 5 said they wouldn't after a real 12-hour shift (Moderate, T-C). That matters most, because the PRD's primary metric, share of prepped portions binned, is measured through check-ins. If nurses skip it in the pilot, the waste goal can't be measured at all.

The top opportunity is a one-tap check-in that assumes "all eaten" unless the nurse marks something binned. That is an assumption to test next, not a decision: it removes friction by guessing, and the guess could hide exactly the binned food the pilot is meant to count. Fix the "portions" wording and the missed re-plan button, then re-run G0.

**What would change this:** nurses checking in after real shifts at the same rate they did in a session would downgrade T-C; a second round where logging still fails after the wording fix would make logging, not check-in, the first thing to fix.

## Results against criteria

Targets are from the PRD, set before the sessions.

| Task or criterion | Target | Result | Met? | Notes |
|---|---|---|---|---|
| T1 rota entry (R1) | ≤ 20 s median | 5 of 5 done, median 25 s (range 19–31 s) | No | Think-aloud slows times a little. 2 of 5 expected to photo their rota (N3, N6) |
| T2 log 4 dishes, 10 portions (R2) | ≤ 2 min median | Median 1:52; 3 of 5 within 2 min | Median yes, G0 no | P2 2:50, P4 3:10, both after misreading "portions" (N10, N14) |
| G0 logging half | ≥ 4 of 5 within 2 min, unaided | 3 of 5 | **No** | |
| T3 re-plan after a rota change (R3) | < 1 min | 4 of 5 under 1 min | Yes | P3 failed: missed the Re-plan button after the rota edit (N20) |
| G0 re-plan half | ≥ 4 of 5 under 1 min | 4 of 5 | **Yes** | |
| T4 check-in (R5) | Typical shift in ≤ 3 taps | 5 of 5 done; 4 of 5 took 4–6 taps; only P2 found "All eaten" (1 tap) | No, as built | The shortcut sat below the list (N24, N26) |
| T5 find prep past use-by | none set | 4 of 5 found it in 10–25 s | n/a | P2 searched the plan, not the fridge screen (N33) |
| Would use at every rota change | none set | 4 of 5 yes, 1 maybe (P4) | n/a | Prediction, not behaviour |

**G0 is not passed.** Under the PRD's own logic (pass, iterate, stop), this is iterate: fix the weakest step and run again.

## Themes

| ID | Theme | Did | Said | Participants | Strength |
|---|---|---|---|---|---|
| T-A | Re-plan is understood and valued; it's the hook | 4 of 5 re-planned in < 1 min (N18, N19, N21, N22). All 5 named which meals used their prep from the "From your fridge" tags (N23) | P1 "The re-plan bit is the bit I'd pay for" (N34). P5 "Oh that's clever" (N22). P3 would use it "if it does the re-plan by itself" (N36) | 5 of 5 | **Strong** |
| T-B | The re-plan doesn't follow a rota edit, so it can be missed | P3 edited the rota, never re-planned, and thought the plan had updated (N20). P4 paused before finding Re-plan (N21) | P3 "if it does the re-plan by itself" (N36) | 2 of 5 (P3, P4) | **Moderate**: behaviour, but one failure |
| T-C | Check-in is too much after a real shift | 5 of 5 completed it in the session (N24, N26, N27, N29, N30). 4 of 5 marked meals one by one, 4–6 taps; only P2 used "All eaten" (N26) | P1, P3, P5 said they wouldn't do it after a 12-hour shift (N25, N28, N31). P5: would if it was one tap and assumed eaten (N31) | 3 of 5 said; 4 of 5 over the tap target | **Moderate**: the key evidence is prediction, and sessions weren't after a shift. Strong for "the tap target is missed" |
| T-D | Logging prep feels like homework, and "portions" is misread | 2 of 5 over 2 min (N10, N14), both after changing their portion count. 3 of 5 within 2 min, 2 of them using recent dishes (N12, N17) | P1, P3, P4 called it homework (N9, N13, N16). P4 would only use Shiftplate "if putting the food in was quicker" (N37) | 4 of 5 (P1–P4) | **Strong**: behaviour and statements agree |
| T-E | Rota entry is close but slow, and some expect a photo | Median 25 s against 20 s (N1, N2, N4, N5, N7) | P2 and P4 wanted to photograph the rota (N3, N6) | 5 of 5 timed; 2 of 5 photo | **Strong** for the miss; **Weak** for photo (2 people, said only) |
| T-F | Past use-by food is findable, from the fridge screen | 4 of 5 found it in 10–25 s (N32). P2 searched the plan instead (N33) | P2 "I can't see where it says" (N33) | 4 of 5 found; 1 of 5 lost | **Strong**, low stakes |

## Insights

### I1. Re-planning around the fridge is the reason to come back

**Observation:** 4 of 5 re-planned in under a minute, and all 5 could point at the "From your fridge" tags and say which meals used their prep (N18–N23). Two praised it unprompted (N22, N34). 4 of 5 said they'd use it at every rota change, and the one maybe was about logging, not the re-plan (N37).
**Why it matters:** this is the step the PMF hypothesis rests on ("re-plan at every rota change"), and it meets its G0 bar.
**Implication:** keep the re-plan as it is. Spend the next round on the steps around it.
**Strength:** Strong.
**Evidence:** P1 "oh, the chilli moved to Friday" · P5 "Oh that's clever, it's moved the pasta bake."

### I2. Check-in is the weakest link, and it carries the waste metric

**Observation:** all 5 completed check-in in the session, but 3 of 5 said they wouldn't after a real 12-hour shift (N25, N28, N31). 4 of 5 took 4–6 taps against a 3-tap target because "All eaten" sat below the list; the one person who used it (P2) called it fine (N26).
**Why it matters:** the PRD's primary metric, share of prepped portions binned, comes from check-ins (R5) and the re-plan confirmation (R6). Skipped check-ins mean the waste goal can't be measured, so the pilot could pass on re-plans and still say nothing about waste.
**Implication:** test a one-tap check-in that assumes "all eaten" unless something is marked binned, and test whether that default under-counts binned food (see Opportunities).
**Strength:** Moderate. Three consistent predictions, one participant's idea of a fix, and a context (straight after a shift) the sessions didn't recreate. The stakes are high, which is why it ranks first anyway.
**Evidence:** P3 "I wouldn't do this after twelve hours. I'd forget, or I'd lie." · P5 "If it was one tap, maybe. Like, it assumes I ate it unless I say."

### I3. Logging fails G0, partly on one word

**Observation:** 3 of 5 logged the fridge within 2 minutes (N8, N12, N17). P2 and P4 took 2:50 and 3:10 after reading "portions" as tubs rather than meals the dish makes (N10, N11, N14, N15). 3 of 5 called logging homework (N9, N13, N16).
**Why it matters:** misses the G0 logging bar (4 of 5 needed), sits on the PRD's guardrail metric, and P4's only hesitation about using Shiftplate was logging speed (N37).
**Implication:** reword "portions" as meals the dish makes, put recent dishes first (P5, who used them for 3 of 4 dishes, was fastest; N17), and re-time T2 in the next round.
**Strength:** Strong.
**Evidence:** P2 "is that how many tubs, or how many meals it makes?" · P4 "it's homework, this bit."

### I4. The re-plan needs to follow the rota edit

**Observation:** P3 changed Thursday, returned to the plan and believed it had updated; it hadn't (N20). P4 paused before finding Re-plan (N21).
**Why it matters:** a missed re-plan is a missed rota change, which is exactly what the PMF signal counts. In the pilot it would look like a nurse who didn't care, when the button was simply missed.
**Implication:** after a rota edit, offer the re-plan in place (or run it), and re-test T3 with someone who hasn't seen the app.
**Strength:** Moderate: one failure and one pause.
**Evidence:** P3 "Yes, if it does the re-plan by itself."

## Contradictions

| What | Side A | Side B | Which we weight, and why |
|---|---|---|---|
| Check-in: done, but "wouldn't do it" | 5 of 5 completed check-in (did; N24–N30) | 3 of 5 said they wouldn't after a real shift (said; N25, N28, N31) | The statements, unusually. Behaviour normally wins, but the sessions ran on days off or before shifts, so the behaviour was in the wrong context. The pilot will show the real behaviour |
| P3 would use it, but failed the core task | P3 said yes to every rota change (N36) | P3 missed the re-plan entirely (N20) | Neither cancels the other: P3 believed the plan had updated. The failure is about the entry point (I4), not about wanting the feature |

## Outliers

| Participant | What | Why it's not a theme | What would make it one |
|---|---|---|---|
| P2 | Wanted their partner, who does half the cooking, to see the plan (N39) | 1 of 5; unprompted | The PRD's deferral trigger: 5+ of 20 pilot nurses ask unprompted. Count this as 1 towards it |
| P4 | Asked whether it shows calories, to lose weight (N40) | 1 of 5, and against the product's stance | Nothing in this round. The PRD rules out calories and diets ("Shiftplate is never a diet app"). Recorded, not acted on |
| P1 | Offered, unasked, that the re-plan is what they'd pay for (N34) | 1 of 5; price wasn't tested | A pricing question in the pilot exit interview |

## Opportunities

**Outcome:** share of prepped portions binned halves from pilot week 1 to week 4 (the PRD's primary metric), measured honestly.

| Opportunity | Backed by | Candidate solutions | Riskiest assumption | Test |
|---|---|---|---|---|
| **1. "After a 12-hour shift I'm too tired to tell the app what I ate"** | I2 (Moderate), T-C | a. One tap: assume "all eaten" unless something is marked binned (*new*, from P5) · b. Move "All eaten" to the top of today's check-in (*R5 as specced*) · c. Skip the after-shift check-in and ask only at the next re-plan (*extends R6*) | **Measurable:** with "all eaten" as the default, nurses still mark what they binned, so binned food isn't under-counted. Also **desirable:** they'll do even one tap after a real shift | For one week, 5 nurses check in after real shifts with solution a; at each re-plan, compare portions marked binned against what's actually left in the fridge. Fails if check-ins are mostly skipped, or most binned portions were recorded as eaten (*proposed*; hand to experiment design) |
| **2. "Putting the food in feels like homework"** | I3 (Strong), T-D | a. Reword "portions" as meals the dish makes (*fix*) · b. Recent dishes first (*R2 has them*) · c. "Same as last week" with edits (*new*) | **Usable:** the wording fix alone gets 4 of 5 under 2 min | Re-run T2 with 5 new nurses after the fix. Fails if fewer than 4 of 5 finish within 2 min |
| **3. "I changed my rota, so my plan has changed, right?"** | I4 (Moderate), T-B | a. Offer Re-plan right after a rota edit (*fix*) · b. Re-plan automatically on rota change (*new*) | **Usable:** an in-place prompt is enough; no need to auto-run | Re-run T3 with 5 new nurses. Fails if anyone edits the rota and leaves without re-planning |
| 4. "Copying my rota in takes a while" | T-E (Strong for time, Weak for photo) | a. Fewer taps per week (*fix*) · b. Photo import (*deferred in the PRD*) | Rota time matters to re-planning at all | The PRD's trigger for import is "nurses say rota entry is why they skipped a re-plan". Nobody said that here, so it stays deferred |

**Why 1 ranks first though 2 is stronger:** 2 and 3 are fixes with clear tests. 1 is an open question, and if it goes wrong the pilot can't measure the outcome it exists to move.

**Parked:** partner sharing (P2) against the PRD's 5-of-20 trigger; calories (P4), out of scope by the PRD.

## What this data can't tell you

- **Whether nurses check in after a real shift.** Every session was on a day off or before a shift. → The one-week check-in test above, then the pilot.
- **Whether they'll re-plan at real rota changes.** "Would use it" is a prediction from 4 of 5. → The pilot's PMF signal (re-plans through two rota changes without reminders).
- **How much prep actually gets binned.** No fridge data was collected. → Pilot week 1 baseline.
- **Whether this holds beyond these five.** One round, five nurses, recruited the same way; nothing on other hospitals or nurses who don't already prep. → G1's recruitment rule (more than one hospital).
- **Whether rota photo import is worth building.** Two people expected it; nobody said they'd skip because of it. → Ask at pilot exit.
- **Times without think-aloud.** Talking slows tasks, so T1 and T2 times may be a little high. → Time the pilot's real entries.
- **Willingness to pay.** Not asked. One unprompted remark (N34).

## Feeds next

| Where | Use this | IDs |
|---|---|---|
| PRD: Release gates | G0 not passed: logging half failed (3 of 5), re-plan half passed (4 of 5). Iterate | Results table |
| PRD: R2 | Reword "portions"; keep recent dishes first | I3, N10, N11, N14, N15 |
| PRD: R3 | Offer the re-plan straight after a rota edit | I4, N20, N21 |
| PRD: R5 | Tap target missed as built; one-tap check-in is a candidate to test, not a spec | I2, N24–N31 |
| PRD: Success, instrumentation gaps | Add: a default of "all eaten" would under-count binned food unless nurses mark exceptions | I2, Opportunity 1 |
| PRD: Scope | Partner sharing: 1 unprompted ask towards the trigger. Calories: out of scope, asked once | N39, N40 |
| Experiment design | The one-tap check-in test (Opportunity 1), with its fail conditions | I2 |

## Observation log

Coded: 5 of 5 sessions. Parked: 0.

| ID | Participant | Where | Type | Observation | Verbatim or detail | Codes |
|---|---|---|---|---|---|---|
| N1 | P1 | T1, 0:22 | did | Entered 14 days; one self-corrected tap | | rota time |
| N2 | P2 | T1, 0:31 | did | Entered 14 days after a pause | | rota time |
| N3 | P2 | T1, start | asked | Expected to photo the rota | "can I not just take a photo of the rota?" | rota photo |
| N4 | P3 | T1, 0:25 | did | Entered 14 days | | rota time |
| N5 | P4 | T1, 0:28 | did | Entered 14 days | | rota time |
| N6 | P4 | T1 | said | Expected to photo the rota | "I'd want to just photograph this off the board at work." | rota photo |
| N7 | P5 | T1, 0:19 | did | Entered 14 days | | rota time |
| N8 | P1 | T2, 1:40 | did | Logged within 2 min; typed every dish, no recent dishes | | logging time |
| N9 | P1 | T2 | said | Called logging homework | "this is a bit of homework, isn't it" | logging effort |
| N10 | P2 | T2, 2:50 | did | Over 2 min; entered 1 portion for a lasagne, changed to 4 | Moderator didn't confirm | logging time, portions wording |
| N11 | P2 | T2 | asked | Unsure what a portion is | "is that how many tubs, or how many meals it makes?" | portions wording |
| N12 | P3 | T2, 1:52 | did | Logged within 2 min; recent dishes for 2 of 4 | | logging time |
| N13 | P3 | T2 | said | Called logging homework (about logging in general) | "honestly this is homework after work." | logging effort |
| N14 | P4 | T2, 3:10 | did | Over 2 min; changed a stew's portion count twice | | logging time, portions wording |
| N15 | P4 | T2 | asked | Unsure what a portion is | "wait, portions of what? Servings?" | portions wording |
| N16 | P4 | T2 | said | Called logging homework | "it's homework, this bit." | logging effort |
| N17 | P5 | T2, 1:35 | did | Logged within 2 min; recent dishes for 3 of 4 | | logging time |
| N18 | P1 | T3, 0:41 | did | Re-planned at once, read the tags | "oh, the chilli moved to Friday" | re-plan |
| N19 | P2 | T3, 0:48 | did | Re-planned without hesitating | | re-plan |
| N20 | P3 | T3, fail | did | Edited the rota, missed Re-plan, believed the plan had updated; moderator moved on at 1:20 | | re-plan entry |
| N21 | P4 | T3, 0:55 | did | Re-planned after a pause to find the button | | re-plan, re-plan entry |
| N22 | P5 | T3, 0:38 | did | Re-planned and read the change | "Oh that's clever, it's moved the pasta bake." | re-plan |
| N23 | P1–P5 | After T3 | did | All 5 named which meals used their prep from the tags (P3 after the moderator re-planned) | | prep visibility |
| N24 | P1 | T4 | did | Marked 3 meals one by one, 5 taps; didn't see "All eaten" | | check-in taps |
| N25 | P1 | T4 | said | Wouldn't check in after a real night | "after a real night I'd just go to bed. I wouldn't do this." | check-in context |
| N26 | P2 | T4 | did | Scrolled to "All eaten", 1 tap; called it fine | | check-in taps |
| N27 | P3 | T4 | did | Marked meals one by one, 4 taps | | check-in taps |
| N28 | P3 | T4 | said | Wouldn't check in after a 12-hour shift | "I wouldn't do this after twelve hours. I'd forget, or I'd lie." | check-in context |
| N29 | P4 | T4 | did | Marked meals one by one, 4 taps; no comment | | check-in taps |
| N30 | P5 | T4 | did | Marked meals one by one, 6 taps, corrected one | | check-in taps |
| N31 | P5 | T4 | said | Wouldn't after a shift; would if one tap assumed eaten | "If it was one tap, maybe. Like, it assumes I ate it unless I say." | check-in context, one tap |
| N32 | P1, P3, P4, P5 | T5 | did | Found the past use-by section in 10–25 s | | use-by |
| N33 | P2 | T5, 1:30 | did | Searched the plan, not the fridge screen; didn't find it | "I can't see where it says." | use-by |
| N34 | P1 | Every rota change? | said | Yes; offered that the re-plan is worth paying for | "The re-plan bit is the bit I'd pay for." | intent, re-plan |
| N35 | P2 | Every rota change? | said | Yes | | intent |
| N36 | P3 | Every rota change? | said | Yes, if the re-plan happens by itself | "Yes, if it does the re-plan by itself." | intent, re-plan entry |
| N37 | P4 | Every rota change? | said | Maybe, only if logging were quicker | "Maybe. Only if putting the food in was quicker." | intent, logging effort |
| N38 | P5 | Every rota change? | said | Yes | "Yes, definitely." | intent |
| N39 | P2 | Every rota change?, unprompted | asked | Wanted the partner to see the plan | "Could my partner see this? He does half the cooking" | outlier: sharing |
| N40 | P4 | End, unprompted | asked | Asked for calories, to lose weight | "Does it tell you calories? I'm trying to lose a bit." | outlier: calories |
