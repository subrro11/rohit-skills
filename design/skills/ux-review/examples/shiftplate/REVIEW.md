# UX review: Shiftplate prototype v0.1

> Real run, fictional product. Shiftplate is the made-up product from the [PRD Generator showcase](../../../../../product/skills/prd-generator/examples/shiftplate/). The prototype is a first pass built from its [prototype prompt](../../../../../product/skills/prd-generator/examples/shiftplate/3-PROTOTYPE-PROMPT.md). Every measurement below was taken in a browser during the review; findings read from the code rather than seen on screen say so.

**Reviewed:** `prototype/index.html` (v0.1), opened in headless Chrome at 390 × 844 px, touch emulation on, audio muted. "Today" is the prototype's default fixed date. Storage cleared before each run so the scripted fridge loaded.
**User:** a hospital nurse on rotating 12-hour day and night shifts, exhausted, often one-handed, often on a short break (*from the brief*).
**Top tasks** (*from the brief*, with its success bars):

1. **Log the fridge**: 4 dishes, 10 portions, in 2 minutes or less, without help.
2. **Change the rota and re-plan**: in under 1 minute.
3. **Know which meals use prep**: point to the right meals when asked "which meals this week use your prep?"

Every finding names a task, a heuristic and evidence on screen.

## Verdict

v0.1 isn't ready for the 5-user test. Two problems would sink it on their own: there's no way back from Log prep (the browser back changes the address but not the screen), and the dish past its use-by is silently left out, so the fridge says 10 while the plan uses 8 and nothing says why. Task 2 will be slow because the day chips are small, unlabelled and far from the button, and task 3 depends on faint 11 px tags with no summary. Logging is typing-heavy (free-text quantity and dates, no recent dishes), which puts the 2-minute bar at risk. Fix the ten items under *Fix before testing* and the prototype will test the idea rather than its bugs.

## Task walks

### Task 1: log the fridge

| Step | What the user does | What happens | Finding |
|---|---|---|---|
| 1 | Looks for where to log food on Home | "Manage Inventory", a small green text link inside the fridge card | F20 |
| 2 | Taps it | Log Prep opens. No back control anywhere on the screen | F1 |
| 3 | Types a dish name | Free text. No recent dishes to pick from | F9 |
| 4 | Taps Qty and types 3 | Full text keyboard opens. No default, no − / + | F7 |
| 5 | Taps the date field | Asked to type YYYY-MM-DD. Leaving it blank silently means today, but nothing says so | F8 |
| 6 | Taps Submit with a field wrong | One red line covers every field: screens/4-log-error.png | F11 |
| 7 | Taps Submit with valid entries | "Success!" toast at the top for 1.5 s; fields clear; the dish joins the list below | F12 |
| 8 | Repeats steps 3–7 three more times | About 5 taps and 15–25 characters per dish (*estimate*) | F7, F8, F9 |
| 9 | Wants to go back to Home | No Back or Done. Browser back changes the address to `#plan` but the screen stays on Log Prep (observed) | F1 |

Four dishes cost about 20 taps and 60–100 typed characters on a phone keyboard (*estimate*). For a tired nurse that's likely near or over 2 minutes, before the dead end at step 9.

### Task 2: change the rota and re-plan

| Step | What the user does | What happens | Finding |
|---|---|---|---|
| 1 | Finds the day that changed | 14 chips marked D / N / Off, with no dates, weekdays, today marker or legend: screens/1-home.png | F5 |
| 2 | Taps the chip | It cycles to the next state. A 48 × 28 px target with 4 px gaps | F5 |
| 3 | Reads the banner | A yellow banner appears below the chips. It isn't tappable: screens/2-rota-changed.png | F6 |
| 4 | Notices "Upcoming meals" | Already changed: the plan rebuilt itself on the tap, before any re-plan | F4 |
| 5 | Reaches up for "Optimise" | Top of the screen (y 136–182 of 844), above the chips | F6 |
| 6 | Lands on the plan | No message about what changed. The page opens scrolled, with the heading partly cut off: screens/3-plan.png | F4, F17 |

Two taps if the user finds the right chip first time and knows that Optimise means re-plan. The risk is in steps 1 and 5, not the tap count.

### Task 3: know which meals use prep

| Step | What the user does | What happens | Finding |
|---|---|---|---|
| 1 | Looks at the top of the plan for a summary | None. No "Uses 8 of 10" | F3 |
| 2 | Scans the cards | Each meal has a tag on the right, "portion" or "gap meal", in 11 px grey at 2.2:1 contrast | F3, F14 |
| 3 | Looks for the stew they logged | It isn't in the plan, and nothing says why | F2 |
| 4 | Taps a new meal to see what's in it | Nothing happens | F18 |

## Findings

### F1 · Blocker · Log the fridge

**Heuristic:** H3 User control and freedom; mobile back
**Evidence:** Log Prep has two kinds of button, Submit and Delete. No Back, Done or Home. The browser back gesture changes the address from `#log` to `#plan`, but the screen stays on Log Prep, because the app never listens for address changes (observed, then confirmed in the code).
**Why it matters:** Every participant gets stuck at the end of task 1. Most will reload the page, and the moderator will have to step in.
**Fix:** Add a **Done** button fixed to the bottom of Log Prep that returns to Home (the brief asks for this). Make the app respond to the browser back gesture so it changes the screen too.
**Size:** S

### F2 · Blocker · Know which meals use prep

**Heuristic:** H1 Visibility of system status; edge-data state
**Evidence:** Stew × 2 was prepped 5 days before "today". Log Prep lists it like any other dish, and Home counts it in "10 servings stored", but the plan places only 8 portions and doesn't mention the stew. The brief requires a "Past use-by, not planned" list.
**Why it matters:** The user believes the stew is planned, or eats it after its use-by, or stops trusting the counts. This is the state the test is set up to trigger.
**Fix:** In Log Prep, move expired dishes to a separate group headed "Past use-by, not planned", greyed, with the prep date. Count only usable portions on Home ("8 portions ready · 2 past use-by"). On the plan, add a line under the summary naming what was left out.
**Size:** S

### F3 · Major · Know which meals use prep

**Heuristic:** H1 Visibility of system status; H8 Aesthetic and minimalist design
**Evidence:** There's no "Uses 8 of 8 usable portions" summary at the top of the plan (the brief asks for "Uses 10 of 10"). The only signal on each meal is an 11 px grey tag on the far right. Fridge and new meals look the same at a glance: screens/3-plan.png.
**Why it matters:** Task 3 is the test's main comprehension check. Users have to read eighteen small labels to answer it.
**Fix:** Add a one-line summary at the top of the plan. Mark fridge meals visibly: a filled green tag before the meal name, or a fridge icon plus a tinted row. Keep new meals plain. Use the brief's labels for the wording (handed to copy review).
**Size:** S

### F4 · Major · Change the rota and re-plan

**Heuristic:** H1 Visibility of system status; H4 Consistency
**Evidence:** Tapping a chip rebuilds the plan straight away ("Upcoming meals" changes from Day 1 (D) to Day 1 (N) on that tap), while the banner asks whether to regenerate the plan. Optimise only opens the plan screen. Nothing says what changed.
**Why it matters:** The banner asks for a decision that's already been made, and users can't tell whether the plan they see is old or new. The test's timer for task 2 also needs a clear "saved" moment.
**Fix:** Choose one model. Either keep the plan unchanged until the user re-plans (the brief's model) or re-plan automatically and drop the question. Then confirm after re-plan with what changed ("2 days changed · 8 fridge portions placed"), shown at the top of the plan.
**Size:** M

### F5 · Major · Change the rota and re-plan

**Heuristic:** H6 Recognition rather than recall; mobile target size and spacing
**Evidence:** The day chips measure 48 × 28 px with 4 px gaps. They're labelled D, N or Off only, with no weekday, date or today marker, and there's no legend. Tapping cycles D → N → Off with no hint that it does.
**Why it matters:** To change Thursday, users have to work out which chip is Thursday. A mis-tap on a cycling toggle changes the wrong day, and fixing it takes up to three more taps. Small targets are hardest for tired, one-handed users.
**Fix:** Make chips at least 44 px tall with 8 px gaps. Show the weekday and date on each (Thu 21), mark today, and add a legend under the strip (Day · Night · Off). Consider showing 7 days, with the second week behind a "Next week" toggle, so each chip can be wider.
**Size:** S

### F6 · Major · Change the rota and re-plan

**Heuristic:** Mobile reach; H8 hierarchy
**Evidence:** The only re-plan action, Optimise, sits at y 136–182 of 844 px, above the chips, in the hardest area to reach one-handed. The banner that prompts the re-plan appears below the chips and can't be tapped. The brief asks for primary buttons in the bottom half.
**Why it matters:** After tapping a chip, the user's thumb is at the chips and their eyes are on the banner. The action they need is above both.
**Fix:** Put a full-width **Re-plan** button in a bar fixed to the bottom of Home. Make the banner itself tappable, or put the re-plan button inside it.
**Size:** S

### F7 · Major · Log the fridge

**Heuristic:** H5 Error prevention; mobile keyboards
**Evidence:** Qty is a plain text field with no default and no numeric keyboard (`type=text`, no `inputmode`). It accepts 2.5. The brief asks for − / + buttons with a default of 2.
**Why it matters:** That's a keyboard switch and two taps per dish, and it invites invalid entries that then trigger the generic error (F11).
**Fix:** Replace it with a stepper: − [2] +, buttons at least 44 px, range 1–12.
**Size:** S

### F8 · Major · Log the fridge

**Heuristic:** H5 Error prevention; H2 Match with the real world
**Evidence:** The prep date has to be typed as YYYY-MM-DD. Leaving it blank silently uses today, but the placeholder suggests it's required. Dates in the future are accepted.
**Why it matters:** Most dishes are prepped today or yesterday. Typing ten characters in a format people don't use is the slowest part of the task.
**Fix:** Default to today and show it. Offer three quick choices (Today · Yesterday · Pick a date), with "Pick a date" opening the native date picker. Block future dates.
**Size:** S

### F9 · Major · Log the fridge

**Heuristic:** H7 Flexibility and efficiency; H6 Recognition rather than recall
**Evidence:** Every dish name is typed from scratch. The brief asks for a list of recent dishes to pick from.
**Why it matters:** Nurses batch-cook the same few dishes. Retyping them every week is the main cost of logging, and logging is the habit the product depends on.
**Fix:** Show up to six recent dishes as large buttons above the name field. One tap fills the name; the stepper and date keep their defaults; one more tap adds it.
**Size:** M

### F10 · Major · Log the fridge

**Heuristic:** H3 User control and freedom; H5 Error prevention; target size
**Evidence:** Delete removes a dish instantly, with no confirmation or undo. It's a 56 × 30 px text button at the right edge of each row.
**Why it matters:** It's easy to hit by accident one-handed, and losing a dish means retyping it, or worse, not noticing it's gone from the plan.
**Fix:** Keep delete instant, but show an "Undo" snackbar near the bottom for 8 seconds. Make the button at least 44 px tall. Add an edit action next to it (the brief asks for edit as well as delete).
**Size:** S

### F11 · Minor · Log the fridge

**Heuristic:** H9 Recognise, diagnose, recover from errors
**Evidence:** Any invalid input shows the same message covering every field, in 12 px red under the date field. It doesn't say which field is wrong: screens/4-log-error.png.
**Why it matters:** Users have to check every field. Once F7 and F8 are fixed, only an empty name can go wrong.
**Fix:** Validate per field, inline, and keep Submit disabled until a name is entered. The wording is handed to copy review.
**Size:** S

### F12 · Minor · Log the fridge

**Heuristic:** H1 Visibility of system status
**Evidence:** After adding a dish, a dark toast appears at the very top for 1.5 seconds. The new dish goes to the bottom of the list, which may be off-screen.
**Why it matters:** The confirmation is out of the user's sight, and they can't see the dish they just added.
**Fix:** Add new dishes to the top of the list and highlight them briefly. Drop the toast, or move it near the bottom.
**Size:** S

### F13 · Major · All tasks

**Heuristic:** Accessibility: focus visible (WCAG 2.4.7); labels
**Evidence:** `button:focus { outline:none; }` removes the focus ring from every button, with nothing to replace it. All three inputs rely on placeholder text alone and have no labels.
**Why it matters:** Keyboard and switch users can't tell where they are. Placeholders disappear as soon as someone starts typing, so users lose track of which field is which.
**Fix:** Restore a visible focus style (`:focus-visible` with a 2 px brand-colour ring and offset). Add a visible label above each field.
**Size:** S

### F14 · Major · All tasks

**Heuristic:** Accessibility: contrast (WCAG 1.4.3)
**Evidence:** The muted grey `#aaaaaa` on the `#fafaf7` background is **2.22:1**, and **2.32:1** on white cards, against a minimum of 4.5:1. It's used for the intro text, every small label above a section, the prep dates and the meal tags (11–13 px).
**Why it matters:** The prep dates and tags carry the information tasks 1 and 3 depend on, and the user is often reading in a dim break room or under bright ward lights.
**Fix:** Darken the muted colour to at least 4.5:1 on both backgrounds (for example `#6e6e73`, re-check the ratio) and use 13 px as the minimum for anything that carries information.
**Size:** S

### F15 · Minor · Change the rota and re-plan; Know which meals use prep

**Heuristic:** H4 Consistency and standards
**Evidence:** One action has three names: Optimise (button), Regenerate (banner) and Re-plan (brief). One unit has three: servings (Home), meals (Log Prep) and portion (plan). Home labels days "Day 1 (N)" while the plan uses "2026-11-20 · N".
**Why it matters:** Users can't be sure they're looking at the same thing. Task 3 asks them to match fridge portions to plan meals.
**Fix:** One name for each, used everywhere. Use the same date format on both screens: weekday plus day (Fri 20). Which words to choose is handed to copy review.
**Size:** S

### F16 · Major · Know which meals use prep

**Heuristic:** Edge-data state (use-by); the brief's "never place a portion after its use-by window"
**Evidence:** Read from the code, not seen on screen: the use-by check compares the prep date with today, not with the day the portion is placed. Portions are placed in order from today onwards. A fridge with more usable portions than about four days of slots would place some after their use-by. The scripted fridge doesn't trigger this.
**Why it matters:** It's a food-safety rule in the brief, and the user would have no way to spot the mistake.
**Fix:** Check each portion's use-by against the date of its slot, and skip it when that date is past the use-by. Add a test fridge with 14 portions to the moderator's set.
**Size:** S

### F17 · Minor · Change the rota and re-plan

**Heuristic:** H3 User control; mobile reach
**Evidence:** The plan's only way out is a small green text link, "Back", below all seven day cards, so it's off-screen on arrival. The plan also opened partly scrolled in the headless run, with its heading cut off (screens/3-plan.png). That may be a side effect of the address change, so it should be checked on a real phone.
**Why it matters:** It's a minor slowdown. Users will use the browser back, which is broken (F1) on the other screens.
**Fix:** Put Back in a top bar, open the plan scrolled to the top, and make the browser back gesture work (F1).
**Size:** S

### F18 · Minor · Know which meals use prep

**Heuristic:** H6 Recognition rather than recall
**Evidence:** New meals don't respond to a tap. The brief says they should show their ingredients.
**Why it matters:** Not on a timed task, but users who can't see what a new meal needs can't judge it.
**Fix:** Tapping a new meal expands its row to list the ingredients. The row needs to be at least 44 px tall.
**Size:** S

### F19 · Major · Log the fridge (first run)

**Heuristic:** Empty and first-run states
**Evidence:** With an empty fridge, Home shows "No data." in the fridge card and a plan made only of new meals, with no note. Log Prep's list also says "No data." The brief asks for the note "Nothing logged in your fridge, so this plan uses new meals only."
**Why it matters:** This is the first screen every participant sees if the moderator resets between sessions. Nothing points them to logging.
**Fix:** In the empty fridge card, put a full-width "Log prep" button. Above an all-new plan, add the brief's note. Wording is handed to copy review.
**Size:** S

### F20 · Minor · Log the fridge

**Heuristic:** Mobile target size; H8 hierarchy
**Evidence:** The way into logging, "Manage Inventory", is a 134 × 30 px text link at the right edge of the fridge card, styled less strongly than the Optimise button.
**Why it matters:** Task 1 starts here. It's findable, but it's small and secondary.
**Fix:** Make the whole fridge card tappable, at least 56 px tall, with a clear chevron.
**Size:** S

### F21 · Minor · Know which meals use prep

**Heuristic:** Product question for the test (*inference*)
**Evidence:** The plan puts the same dish in every slot of a day (chicken curry three times on day one, veg chilli three times on day two), because portions are placed in order.
**Why it matters:** It follows the rule (oldest first), but users may read it as broken, or reject a day of one dish. Only testing will tell.
**Fix:** Don't change it before the test. Ask participants about it, and if it bothers them, interleave dishes across days within the use-by window.
**Size:** M

## States

| State | Triggered | What the user sees | Finding |
|---|---|---|---|
| First run / empty fridge | Yes (storage set to an empty fridge) | "No data." and a plan of new meals with no note | F19 |
| Expired prep | Yes (scripted fridge, default date) | Expired dish listed as normal and counted, then left out of the plan in silence | F2 |
| Over use-by in the future | No: read from the code only | Portions could be placed after their use-by | F16 |
| User error | Yes (empty Submit) | One generic message for all fields | F11 |
| Success (log) | Yes | 1.5 s toast at the top | F12 |
| Success (re-plan) | Yes | No confirmation | F4 |
| Destructive (delete) | Yes | Instant, no undo | F10 |
| Interrupted / back | Yes (browser back on Log Prep) | Address changes, screen doesn't | F1 |
| Loading, offline, permission | Not applicable | Everything is local and instant | — |

## Accessibility basics

| Check | Result | Finding |
|---|---|---|
| Text contrast | Muted grey at 2.22:1 fails. Body text, white on the green button (4.99:1) and green links (4.78:1) pass | F14 |
| Target sizes | Day chips 48 × 28, Delete 56 × 30, Manage Inventory 134 × 30: under 44 px tall. Optimise 93 × 46, Submit 80 × 46 and the inputs at 44 tall pass | F5, F10, F20 |
| Focus | Removed on every button | F13 |
| Labels | Placeholder-only inputs | F13 |

Screen reader order and announcements weren't tested. Run a full accessibility audit after v0.2.

## Copy, handed off

To copy review, one line each:

- "Rota mutation detected. Regenerate plan?": system language for the banner.
- "Welcome to Shiftplate!" and the paragraphs under each heading describe the interface instead of helping the user.
- Small uppercase step labels ("Step 1 · Rota") above each heading suggest a sequence the app doesn't have.
- "Error: invalid input (…)" and "Success!": generic.
- "No data.": the empty state copy.
- "portion" and "gap meal" tags, "Manage Inventory", "Optimise": internal terms.

## What works

- **The core loop is short.** A chip tap and one button gets to a full 7-day plan, with no setup.
- **The plan never leaves a slot empty**, and fills fridge portions oldest first, as the brief asks.
- **The day/night/off colours** (yellow, blue, grey) are easy to tell apart at a glance. Keep them when the chips get labels.
- **Inputs and the main buttons** are already 44–46 px tall. Keep that height for the new controls.

## For the usability test to confirm

- Whether participants find the right day chip without dates (F5), and how many mis-taps it causes.
- Whether they understand that the stew was left out once it's shown (F2).
- Whether a day of the same dish bothers them (F21).
- Real times for task 1 after F7–F9. The estimates above are not measurements.

## Prioritised fix list for v0.2

**Fix before testing**

1. F1: Done button on Log Prep, and make browser back change the screen. S
2. F2: "Past use-by, not planned" group, and count only usable portions. S
3. F16: check use-by against each slot's date. S
4. F3: "Uses X of Y" summary and a strong fridge marker on each meal. S
5. F4: one re-plan model, plus confirmation of what changed. M
6. F5: chips at least 44 px with weekday, date, today marker and legend. S
7. F6: re-plan button fixed to the bottom; banner tappable. S
8. F7, F8, F9: stepper with default 2, Today / Yesterday / Pick, and recent dishes. M
9. F19: empty fridge card with a Log prep button, and the note above an all-new plan. S
10. F14: darken muted text to at least 4.5:1, since task 3 depends on reading it. S

**Fix next**

11. F13: restore focus rings, add input labels. Major, but a touch-only test won't hit it. S
12. F10: undo after delete, bigger target, add edit. Major, but no test task needs a delete. S
13. F15: one name and one date format per thing (with copy review). S

**Later**

14. F11, F12: per-field errors; new dish at the top of the list. S
15. F17, F18, F20: Back at the top of the plan, ingredients on tap, a tappable fridge card. S
16. F21: decide on dish variety after the test. M

Then run copy review on v0.2, and test it with five users against the three tasks above.
