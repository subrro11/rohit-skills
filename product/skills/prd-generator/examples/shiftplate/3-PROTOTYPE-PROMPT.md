# Prototype: Shiftplate fridge logging and reuse-first re-plan

> Fictional showcase. Shiftplate, its users and every number here are invented. This is a real, unedited run of the skill (quiz answers written by a made-up founder); only the owner name was replaced with "Founder".

## What we're testing
A tired nurse will log what's prepped in their fridge in under 2 minutes, and the reuse-first re-plan will clearly use that prep before suggesting anything new.

Success looks like: in a 5-nurse test, **at least 4 of 5** log the scripted fridge (4 dishes / 10 portions) in ≤ 2 min without help, **at least 4 of 5** finish the rota change and re-plan in < 1 min, and when asked "which meals this week use your prep?", they point to the right ones.

## Build
A working-slice prototype of the core loop: log the fridge, change the rota, re-plan, and see a 7-day plan.

Screens or steps:
1. **Home.** Shows the next 14 days as a strip of D / N / Off chips, the fridge count ("10 portions in the fridge") and a large **Re-plan** button.
2. **Log prep.** Add a dish by picking from a "recent dishes" list or typing a name, set the number of portions with − / + buttons (default 2), and set the prep date (default today). The list of logged dishes is shown underneath, and each can be edited or deleted. A **Done** button returns to Home.
3. **Change rota.** Tapping a day chip cycles it D → N → Off. A banner appears: "Rota changed. Re-plan?"
4. **Re-plan.** One tap builds the next 7 days. Each work day has three slots (pre-shift, on-shift, post-shift) and each day off has two (lunch, dinner). Fill slots with logged portions first, oldest prep date first and only within the use-by window, then fill the rest with gap meals.
5. **Plan view.** A 7-day list. Slots filled from prep are tagged **From your fridge**. Gap-meal slots are tagged **New** and show their ingredients when tapped. At the top: "Uses 10 of 10 prepped portions."
6. **Timer log.** A hidden `/results` route lists, for each session, the time from opening Log prep to Done, the time from the first rota tap to a saved plan, and the dish and portion counts. The test moderator uses it to score G0.

Include exactly these states:
- **Happy path:** steps 1–5 with the scripted fridge.
- **Expired prep:** one dish has a prep date more than 4 days ago. It's listed under "Past use-by, not planned" and never placed in the plan.
- **Empty fridge:** the first screen a new user sees. Re-plan produces only gap meals, with the note "Nothing logged in your fridge, so this plan uses new meals only."

## Fake on purpose
- **Data:** a fictional set of about 20 gap meals with ingredient lists (for example, "Chicken & rice bowl", "Lentil soup + bread", "Overnight oats"), and a scripted fridge with 4 fictional dishes and 10 portions, one of them prepped 5 days ago. No real user data.
- **"Now"** is fixed to a date chosen with the `?today=YYYY-MM-DD` URL flag, so the expired state can be triggered whenever the moderator needs it.
- No auth, accounts, sync, notifications, settings or onboarding.
- The end-of-shift check-in (R5) and inferring binned portions (R6) are not built. They aren't under test.
- The use-by window is fixed at 4 days, not editable.

## Constraints
- A single Vite + React app with state in localStorage. `npm run dev` starts it.
- Works at 390 px width with one hand: tap targets at least 44 px, primary buttons in the bottom half of the screen.
- Copy comes from the PRD and this file. No lorem ipsum.
- Plain, warm tone. This is for people who just finished a 12-hour shift.

## Don't
- Don't show calories, macros, nutrition scores or anything about weight. Shiftplate is never a diet app.
- Don't add re-plan reminders or nudges of any kind.
- Never place a portion after its use-by window, and never leave a slot in the plan empty.
- Don't build a grocery list, recipe library, rota import, night-shift timing advice or sharing.

## Done when
- [ ] `npm run dev` starts it locally
- [ ] Steps 1–5 can be clicked through end to end on a 390 px viewport
- [ ] `?today=` triggers the expired-prep state. Clearing localStorage shows the empty-fridge state.
- [ ] `/results` shows both timings for every session
- [ ] A short README says how to run it, how to reset it between participants, and what's fake

## Source
PRD: `PRD.md`, sections Recommendation, Scope, Requirements and Release gates (G0). Requirements in scope: R1, R2, R3, R4, R7 (the empty-fridge and expired-prep parts).
