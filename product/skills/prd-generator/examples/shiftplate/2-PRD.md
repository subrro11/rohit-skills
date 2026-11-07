# Shiftplate: reuse-first re-planning for rotating-shift nurses

> Fictional showcase. Shiftplate, its users and every number here are invented. This is a real, unedited run of the skill (quiz answers written by a made-up founder); only the owner name was replaced with "Founder".

v0.1 · 2026-11-07 · Draft · Owner: Founder
Numbers are proposed or assumed unless a source is cited.

## Recommendation

Build a mobile app that rebuilds a nurse's meal plan in under a minute when their rota changes. It uses up food that's already prepped in the fridge first, then fills the gaps. The wedge is the nurse who already meal preps on Sundays and watches that prep go to waste every time the schedule flips between days and nights. They already want to solve this, so Shiftplate is fixing a habit that breaks, not creating a new one. v1 is a 20-nurse pilot to test whether reuse-first re-planning gets used again and again. It is not a launch.

**Rejected alternative:** night-shift meal timing first, aimed at the 4am crash that nurses called the worst cost. It lost because food waste can be measured from day one and ties directly to the prep habit we're building on, while timing is harder to measure and its value is less certain. It's deferred with a trigger (see Scope).

**Why now:** Evidence needed. Nothing has changed in the market or technology to make this more urgent today than a year ago. The case rests on six conversations, so treat this as an experiment, not a timed bet.

**PMF hypothesis:** We believe nurses who already meal prep and work rotating 12-hour shifts at large hospitals will re-plan in Shiftplate at every rota change, because it rebuilds the week around food already in the fridge, which beats throwing the prep out and starting over. **Pass:** 10 of 20 pilot nurses re-plan through two rota changes in a row without being reminded. **Iterate:** 5–9 of 20, so fix the weakest step and run again. **Stop:** fewer than 5 of 20, so go back to problem interviews. **Stage:** early solution fit.

## Problem

**User:** Hospital nurses who rotate between day and night 12-hour shifts and already try to meal prep.
**Today they:** prep on Sunday for the week, the rota flips every one or two weeks, the plan stops fitting, and they buy vending machine food or 3am takeout.
**It costs them:** about $60 a week on takeout and vending (*assumed*), prepped food thrown out when the rota flips, and an energy crash around 4am on night shifts.
**Evidence:** informal conversations with six nurses in the owner's building. Evidence needed: whether the $60 holds up (ask pilot nurses to check a week of spending in their banking app), whether the pattern holds outside one building or one hospital, and how much prep is actually thrown out (measured in pilot week 1).

## Goals and non-goals

**Goals**
1. A nurse re-plans after a rota change in under a minute, including entering the change.
2. Prepped food thrown out drops by half for pilot nurses, comparing week 1 with week 4.
3. 10 of 20 pilot nurses re-plan through two rota changes in a row without being reminded.

**Not optimising for:** families or non-shift workers. Plans are built around one nurse's shifts, not a household's meals.

## Scope

| In scope (v1 pilot) | Deferred (and what brings it in) | Out of scope |
|---|---|---|
| Manual rota entry (tap days as Day / Night / Off) | **Night-shift meal timing:** once the waste goal is met and 8+ of 20 nurses ask for night-shift help without being prompted | **Calorie counting, macros, diets or weight tracking.** Shiftplate is never a diet app. |
| Logging prepped portions in the fridge | **Rota import from hospital scheduling apps:** when nurses say rota entry is why they skipped a re-plan | Household or family meal planning |
| One-tap reuse-first re-plan | **Recipe library:** when nurses skip gap meals because they're repetitive | |
| End-of-shift check-in (eaten / binned / still in fridge) | **Partner sharing:** when 5+ of 20 ask for it without being prompted | |
| A fixed set of about 20 gap-filling meals | **Grocery list (P1):** next release if pilot metrics hold | |

## Requirements

Definitions: a **portion** is one serving of prepped food logged in the fridge. A **gap meal** is a meal from the fixed set, used when there's no prepped portion for a slot. A **slot** is one planned meal (pre-shift, on-shift or post-shift on a work day; usual meals on a day off).

| ID | Priority | Requirement | Acceptance |
|---|---|---|---|
| R1 | P0 | Enter the rota by tapping each of the next 14 days as Day, Night or Off | Entering 14 days takes ≤ 20 s in test sessions (median). Changing one day takes ≤ 3 taps. |
| R2 | P0 | Log prepped portions: dish name (chosen from recent dishes or typed), number of portions and the date it was prepped | Logging 4 dishes / 10 portions takes ≤ 2 min (median, test users). Portions can be edited and deleted. |
| R3 | P0 | Re-plan the next 7 days in one tap, assigning logged portions first (oldest first), then gap meals | After a rota change, the re-plan, including the R1 edit, takes < 1 min. Every portion still within its use-by window is placed before any gap meal is used. No portion is placed after its use-by window. |
| R4 | P0 | Fill unassigned slots from a fixed set of about 20 gap meals, showing each meal's ingredients | Every slot in the 7-day plan has a meal. Each gap meal shows its ingredient list. |
| R5 | P0 | After each shift, ask the nurse to mark each planned meal as eaten, binned or still in the fridge, with an "all eaten" shortcut | A typical shift can be checked in with ≤ 3 taps. Marks are stored per portion with a timestamp. |
| R6 | P0 | At each re-plan, ask the nurse to confirm which portions are still in the fridge, and record every unconfirmed, unticked portion as binned | Test case: 5 portions logged, 2 ticked eaten, 1 confirmed in the fridge, so 2 are recorded as binned. |
| R7 | P0 | Handle edge states: empty fridge, all portions past use-by, no rota entered, and offline | Empty fridge produces a plan of only gap meals, with a note saying so. Expired portions are listed as "past use-by" and not planned. With no rota, the plan screen asks for rota entry. Every P0 works offline. |
| R8 | P0 | Keep pilot data private: store only rota, portions and check-ins; never collect the employer or hospital name | The data export contains no free-text employer field. Data is deleted on request within 7 days. |
| R9 | P1 | Build a grocery list from the ingredients of the week's gap meals | Shows a combined list of ingredients for all gap meals in the current plan. |

**Use-by window:** the default is 4 days from the prep date (*assumed*). The nurse can change it per dish. Check against published food-safety guidance before the pilot (see Open questions).

**Priority method:** RICE, with reach out of the 20 pilot nurses and impact on the share of prepped portions eaten. Scores (all inputs *assumed*): prep logging 24, re-plan 16, check-in 16, grocery list 16, night-shift timing 5, rota import 1.7, recipe library 1.25, partner sharing 0.6.

**Overrides:**
- **R5 check-in is P0 even though its impact is only medium,** because without it nothing in Success can be measured.
- **R1 manual rota entry is P0 even though it wasn't on the original list,** because the core loop can't run without the rota.
- **The grocery list stays P1 even though it ties with the re-plan at 16,** because the core loop works without it and it doesn't test the hypothesis. R4's ingredient lists cover the gap in the meantime.
- **Rota import is Later even though every nurse would use it,** because confidence is 50% (we don't know which apps pilot nurses use or whether they export data) and effort is high.

## Success

**North star (proposed):** shift meals each week that came from a plan the nurse actually followed, counted as meals ticked eaten. v1 moves the **depth** input: the share of prepped portions eaten rather than binned.

| Metric | Baseline | Floor to beat | When |
|---|---|---|---|
| **Primary:** share of prepped portions binned (R5 + R6) | Measure in pilot week 1 | Half of the week-1 rate | Week 4 |
| PMF signal: nurses who re-plan through 2 rota changes in a row without being reminded | 0 | ≥ 10 of 20 (pass) · 5–9 iterate · < 5 stop | End of pilot (4–6 weeks, *assumed*) |
| Re-plan time, from opening the app to a saved plan | Measure in prototype test | Median < 1 min | Prototype test, then weekly |
| North star: planned shift meals ticked eaten per nurse per week | Measure in pilot week 1 | Higher in week 4 than in week 1 | Weekly |
| **Guardrail:** time to log prep | Measure in prototype test | Median ≤ 2 min; must not get worse | Prototype test, then weekly |

**Instrumentation gaps:**
- "Eaten" is self-reported, so the north star will under-count nurses who eat the meal but skip the tick.
- "Binned" is inferred at the next re-plan, not observed directly.
- Takeout spending isn't tracked in the app, so the $60 stays unverified unless it's asked about in exit interviews.

## Release gates

| Gate | Passes when |
|---|---|
| G0: Prototype test | ≥ 4 of 5 nurses log a 4-dish fridge in ≤ 2 min without help, and ≥ 4 of 5 complete a re-plan in < 1 min |
| G1: Start the pilot | R1–R8 meet their acceptance criteria. 20 nurses are recruited who already meal prep and work rotating shifts, from more than one hospital. The use-by default has been checked. |
| G2: Pilot decision | The PMF signal falls in the pass, iterate or stop band above, and the decision is recorded in this document |

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| Does the $60 a week hold up when nurses check their banking apps? | Founder | G1 (ask at recruitment) |
| What is a safe default use-by window for refrigerated prepped meals, according to published guidance? | Founder | G1 |
| Can 20 qualifying nurses be recruited from outside the owner's building and from more than one hospital? | Founder | G1 |
| Which scheduling apps do pilot nurses use, and can any of them export a rota? | Founder | G2 |
| Will nurses pay, and how much? Not tested in v1. | Founder | After G2 passes |

## Decision log

| Decision | Tradeoff accepted |
|---|---|
| v1 fixes waste (reusing prep), not the 4am crash | Starts with the smaller pain because it can be measured; some pilot nurses will ask for night-shift help |
| Manual rota entry instead of import | Adds about 20 s of work to every re-plan, in exchange for not building a fragile integration before the core loop is proven |
| Binned is inferred at re-plan, not reported | Less accurate, but no nurse has to report throwing food away |
| No reminders to re-plan during the pilot | Lower usage numbers, but the PMF signal stays honest |

## Next step

Build the prototype in `PROTOTYPE-PROMPT.md` and test the riskiest assumption, that a tired nurse will log their fridge in under 2 minutes, with 5 nurses this week (gate G0).
