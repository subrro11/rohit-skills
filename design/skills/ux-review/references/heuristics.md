# Heuristics

The ten usability heuristics, put in plain words, with what to look for and a typical fix. Then the mobile specifics. Use them as lenses on a task walk, not as a form to fill in. The original list is Jakob Nielsen's (see `sources.md`).

## The ten

| # | Heuristic | In plain words | Look for | Typical fix |
|---|---|---|---|---|
| H1 | Visibility of system status | The user always knows what just happened and what's happening now | Actions with no visible result; data that changes silently; spinners with no end; a count that disagrees with what's shown | Confirm in place, show the new state, show progress, say what changed |
| H2 | Match with the real world | It speaks the user's language and follows the order they think in | Internal terms (inventory, mutation, algorithm); formats people don't use (ISO dates); steps in system order rather than task order | Use the user's words and units; order steps the way the job is done |
| H3 | User control and freedom | Mistakes are cheap: there's always a way back or out | No back or cancel; destructive actions with no undo; flows that trap you; modals with no close | Undo for 5–10 seconds; visible back; cancel that keeps work |
| H4 | Consistency and standards | The same thing looks, sits and is named the same everywhere, and platform conventions hold | One action with three names; the same data in two formats; custom controls that behave unlike the platform | One name, one style, one place per action; use native patterns |
| H5 | Error prevention | The design stops mistakes before they happen | Free text where a choice would do; no defaults; easy-to-hit destructive buttons; invalid states reachable | Constrain inputs (steppers, pickers), sensible defaults, separate or confirm destructive actions |
| H6 | Recognition rather than recall | People choose from what they can see instead of remembering | Codes with no legend; formats to memorise; repeat entries typed again; context lost between screens | Legends, labels, recent items, show the context where the decision is made |
| H7 | Flexibility and efficiency | Fast for people who do it often, without getting in the way of first-timers | No shortcuts for repeated tasks; every entry from scratch; long paths to frequent actions | Recents, presets, bulk actions, remember last values |
| H8 | Aesthetic and minimalist design | Nothing competes with what matters | Explanatory paragraphs; decorative labels; several equal-weight headings; the main action not the most prominent thing | Cut, then make the primary action and key fact the strongest things on screen |
| H9 | Recognise, diagnose, recover from errors | Errors say what's wrong, where, and how to fix it | Generic "invalid input"; errors far from the field; codes; errors that clear your entry | Inline, per field, plain words, keep what was typed, offer the fix |
| H10 | Help and documentation | Ideally none needed; when needed, short, in context and about the task | Help text describing the interface; manuals; nothing where people get stuck | A one-line hint or tooltip at the point of confusion; fix the design first |

## Layout and hierarchy

Not a separate heuristic, but check it on every screen:

- **One primary action per screen**, styled as the strongest element and placed where the task ends.
- **Hierarchy follows importance.** The key fact (what's in the fridge, what's next) should be read first. Squint: what stands out?
- **Grouping.** Related items sit together, with more space between groups than inside them.
- **Even spacing** on a scale (4 or 8 px steps). Uneven gaps read as mistakes.
- **No horizontal scroll or clipped text** at the target width. Long names wrap or truncate with a full view available.

## Mobile specifics

- **Target size.** At least 44 × 44 px for anything important on touch (WCAG 2.5.5 and common platform guidance). 24 × 24 px is the WCAG 2.2 minimum (2.5.8) and only with enough space around it. NN/g's physical guide is about 1 cm square. Measure the hit area, not the visible label.
- **Spacing between targets.** Small, adjacent targets cause mis-taps; a mis-tap on a toggle that cycles states is worse than one on a link.
- **Reach.** On a phone held in one hand, the bottom half and centre are easy to reach; the top corners are hard. Primary and frequent actions belong low; rare or destructive ones can sit high.
- **Gestures.** Every gesture-only action (swipe to delete, long-press) needs a visible alternative. Hidden gestures fail recognition (H6).
- **Keyboards.** Numbers get a numeric keypad (`inputmode="numeric"`), dates a date picker, emails an email keyboard. Typing on a phone is the slowest thing people do; avoid it where a tap would do.
- **Interruptions.** Mobile users get interrupted. Can they leave mid-task and come back to their work intact?
- **Conditions.** Tired, gloved, walking, bright light, one hand. Design for the worst realistic case the brief names.
- **Back.** The system back gesture or button must work and must not lose work. In single-page apps, check that changing the URL actually changes the screen.
