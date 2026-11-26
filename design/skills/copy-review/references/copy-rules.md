# Copy rules

Rules by element, then the cross-cutting ones: terminology, numbers and dates, tone. Each rule has a quick test. When a product has its own style guide, it wins; note where it differs.

## Everywhere

- **Sentence case.** Capitalise the first word and proper nouns only. "Add to fridge", not "Add To Fridge". No all caps for emphasis or decoration.
- **Plain words.** Write the word the user would say out loud. No internal names, code names, spec terms or algorithm talk. Test: would the user say this word to a friend about this task?
- **No eyebrow text.** No small uppercase or monospace labels above headings, panels or controls ("STEP 2 · INVENTORY", "YOUR SHIFTS"). If a section needs a name, give it a real heading in sentence case. If it doesn't, delete the label.
- **No meta explanations.** Don't describe the interface, what it's made of, or how it works: "Here you can…", "This screen lets you…", "Below is…", "Our algorithm…", "Tap to…", "Drag to…". A control's label is its name. If a control really needs explaining, use a tooltip or a hint next to it.
- **Minimum text.** Every sentence has to earn its place by helping the next action. Cut welcome lines, restated headings, decorative counters ("Your shifts (14 days)" when all 14 are visible) and exclamation marks.
- **True.** The words must match what happens. A button called "Optimise" that only opens a page, or a question with no way to answer it, is a Blocker or Major, whatever the wording.
- **Front-load.** Put the word that matters first. "Stew is past its use-by date", not "Please note that one of your dishes, stew, is past…".
- **"You" for the user.** Avoid "my" in labels ("My plan") unless the product uses it everywhere. Avoid "we" unless the product is genuinely acting on the user's behalf and saying so helps.

## Headings and page titles

- **Nouns or short noun phrases**: "Fridge", "Shifts", "Meal plan".
- **No welcome lines** on screens people return to. Onboarding can say hello once.
- **No "Your" padding** unless it separates the user's thing from someone else's.
- **The page `<title>` matches the heading**, so tabs and history make sense.

## Buttons and links

- **Start with a verb that names the outcome**: "Add to fridge", "See meal plan", "Remove". Avoid Submit, OK, Yes, No, Continue and Go when a specific verb exists.
- **Match the button to the heading or dialog question.** A dialog asking "Remove stew?" has a "Remove" button, not "Confirm".
- **Two to four words.** If it needs more, the screen needs fixing, not the button.
- **Link text says where it goes**, never "click here" or "learn more" on its own.
- **Use "select" or "choose" in instructions, not "click" or "tap"**, so they work on every device. Better still, don't write the instruction.
- **Destructive actions say what's destroyed**: "Delete account", not "Delete".

## Form labels, placeholders and hints

- **Every field has a visible label.** A placeholder isn't a label: it disappears as soon as someone types, and some screen readers skip it.
- **Labels are nouns**: "Dish", "Portions", "Prepped on". No colons, no "Enter your…".
- **Hints say what isn't obvious**: format, defaults, limits. "Leave blank for today." If the field has a default, the hint must say so.
- **No abbreviations in labels** ("Qty", "Desc") unless the user abbreviates the same way.
- **Ask for the date in the format people say it**, or use a picker. Never make users type a database format.

## Errors

- **Say what happened and what to do next**, in that order, and in one or two short sentences. The fix often is the message: "Enter a dish name".
- **One message per problem.** An empty field, a wrong format and an out-of-range number each get their own message.
- **Next to the field**, and, on long forms, repeated in a summary at the top with the same words.
- **Reuse the label's words.** Label "Portions" → error "Enter how many portions".
- **No blame, no drama.** Not "You entered an invalid date". Not "Oops!".
- **Avoid "invalid", "illegal", "error", "failed", error codes and regex.** They describe the system, not the fix.
- **Avoid "please" and "sorry" in validation errors.** They add length and don't help. Save an apology for when the product has genuinely let someone down, such as lost data or an outage.
- **Don't repeat the hint or example** the user can already see.
- **Keep what they typed.** If the form clears on error, that's a UX finding; note it in Out of scope.

## Empty states

- **Say what's empty, then how to fill it**, and offer the action as a button: "Nothing in the fridge yet" + "Add food".
- **Never "No data", "No results", "N/A" or a blank area.** Users can't tell empty from broken or still loading.
- **Different empty states get different messages**: never used, filtered to nothing, cleared by the user, failed to load.
- **No meta explanation** of the feature. One line of why it matters is fine only in a first-run empty state, and only if it's about the user's outcome, not the mechanism.

## Confirmations and dialogs

- **Ask only before actions that are hard to undo.** For everything else, act and offer undo.
- **The title is the question, with the object named**: "Remove stew from the fridge?" Never "Are you sure?".
- **The body says the consequence**, if there is one the title doesn't already make plain.
- **Buttons are the action and the way out**: "Remove" and "Keep". Never Yes/No/OK.

## Toasts and banners

- **Toasts confirm what just happened, with the object**: "Chicken curry added", not "Success!".
- **Past tense, no exclamation mark.** "Added", "Removed", "Saved".
- **Offer undo in the toast** for anything destructive, as a one-word button: "Undo".
- **Banners describe a state that persists** and say what to do, if anything: "Shifts changed. Meal plan updated." A banner that asks a question needs buttons that answer it.
- **Don't state the obvious.** If the screen already shows the change, the toast can go.

## Tooltips and hints

- **Only for what can't be said in the label.** A tooltip that repeats the label is noise.
- **One sentence, no heading**, about the user's outcome, not how the system does it.
- **Never put essential information only in a tooltip.** Touch screens and keyboards can miss it.

## Onboarding

- **Get to the first useful action fast.** Ask for the one thing the product can't work without, then show value.
- **Teach by doing**, through empty states and first-use hints at the point of need, rather than a tour.
- **Say hello once, then never again.**

## Status, tags and counters

- **A tag earns its place if it changes what the user does.** "From fridge" tells a nurse not to shop for that meal. "Portion" doesn't.
- **Counters count something useful.** "7 portions in the fridge" helps. "Logged items (4)" next to a list of four doesn't.
- **Status words match the glossary** and read the same everywhere.

## Numbers, dates and times

- **Numerals for numbers**, including small ones in UI ("3 portions").
- **Units and plurals are right**: "1 portion", "2 portions". Check the code handles singular.
- **Dates the way people say them**: "Fri 20 Nov" in lists, "Friday 20 November" in sentences. No ISO dates (2026-11-20), no ordinals (20th). Use "Today", "Tomorrow" and "Yesterday" where they're shorter and unambiguous.
- **Relative where it helps the decision**: "Use by tomorrow" is more useful than a date for anything about to expire.
- **Times in the user's clock** (12 or 24 hour, by locale), and say which day when a time crosses midnight. Night-shift products especially.
- **Ranges with "to"**: "3 to 4 days".
- **Match the locale** for date order, spelling and currency.

## Terminology and the glossary

- **One concept, one term, everywhere**: headings, buttons, errors, toasts, help, notifications, accessible names.
- **One term, one concept.** Don't let "plan" mean both the week's meals and a subscription tier.
- **The user's word beats the spec's word.** Specs need precise terms like "slot"; screens need the word a nurse would use.
- **Retire words explicitly.** The glossary lists the words to stop using, so a search can find them.
- **Abbreviations**: spell out on first use, unless the user already says the short form.
- **Glossary format**:

| Concept | Use | Don't use | Notes |
|---|---|---|---|
| One serving of food already made | portion | serving, meal, item, qty | "3 portions"; singular "1 portion" |

## Tone ladder

Voice stays the same; tone shifts with the user's state. Pick the rung from step 1 of the skill.

| Moment | What the user needs | Tone | Example |
|---|---|---|---|
| **Error they caused** | The fix, fast | Direct, neutral, no blame, no apology | "Enter how many portions" |
| **Something we broke** | To know it's not them, and what now | Plain, own it, one short apology, the next step | "Couldn't save. Your changes are still here. Try again." |
| **Risk** (safety, money, data) | The fact, without alarm | Calm, specific, no exclamation marks | "Stew is past its use-by date, so it's not in the plan." |
| **Success** | Confirmation, then out of the way | Brief, past tense, no cheerleading | "Chicken curry added" |
| **Empty or first use** | What to do first | Warm, one line, the action | "Nothing in the fridge yet" + "Add food" |
| **Tired, stressed or one-handed** | Fewer words, bigger targets, no decisions | Shortest form that's still clear; no jokes | "See meal plan" |
| **Calm and exploring** | Enough to choose | Room for a little warmth; still plain | A one-line description under a choice |

Rules for every rung:

- **Humour only when nothing is wrong**, and never in an error that will be seen twice.
- **Warm means plain and considerate**, not exclamation marks, emoji or "Yay".
- **Never moralise.** No "Great job eating healthy!" in a product that isn't about health, and not in one that is, either.
