# Coding and clustering

Synthesis has three layers, and each one cites the layer below it:

```
Observation log (N1, N2…)  →  Themes (T-A, T-B…)  →  Insights (I1, I2…)
one thing seen or heard       codes grouped           what it means and what to do
```

A reader should be able to start from any insight, follow its IDs down to the notes, and find the participant and the words.

## 1. Read everything first

Read every session before coding any of them. Skimming for memorable quotes is the most common way synthesis goes wrong: the vivid line from one person ends up outweighing the quiet pattern across five.

## 2. Break the data into observations

One observation per row. An observation is one thing a participant **did** or **said**, at one moment, described without interpretation.

| ID | Participant | Where | Type | Observation | Verbatim or detail |
|---|---|---|---|---|---|
| N1 | P1 | T2, 1:40 | said | Called logging homework | "this is a bit of homework, isn't it" |
| N2 | P2 | T2 | did | Entered 1 portion for a lasagne, changed it to 4 | Asked what "portions" meant |

- **Type is one of: did, said, or asked.** *Did* is behaviour you watched (completed, failed, hesitated, took 2:50, used a shortcut). *Said* is opinion, prediction or explanation. *Asked* is a question the participant raised, which often shows a gap in their mental model.
- **Predictions are *said*, not *did*.** "I'd use this every week" is a statement about the future. Keep it, but never let it outweigh what the same person did.
- **Copy verbatims exactly** from the notes or transcript, short (under 25 words), in quotation marks. If the notes paraphrase, write the paraphrase without quotation marks.
- **Answers to your own questions count, but mark them.** A remark the participant offered unprompted is stronger than an answer to "would you use this?".
- **Note the context that might bend the data**: moderator help, a prototype bug, a task the participant misread, a session cut short.

For large inputs (dozens of interviews, hundreds of tickets), sample first: code 5–8 sources fully, build draft codes, then code the rest against them and add codes as you go. Say how much of the data was coded.

## 3. Code

A code is a short label for what an observation is about: `rota entry speed`, `portions wording`, `check-in effort`, `re-plan delight`. Keep the research questions or task list in view while you code, so codes stay tied to what the work is for.

- **Descriptive codes first** (what it's about), then **interpretive codes** (what it might mean): `logging feels like work after work`.
- **One observation can carry two codes.** If it fits two themes, put it in both.
- **Don't code to a hoped-for answer.** If you came in expecting a theme, look hardest for observations that cut against it.

## 4. Cluster into themes

Group codes by what they're about, then name each group. Name groups last, after the notes have settled, so the label describes the notes and not your first guess.

- **A theme needs more than one participant.** A pattern from one person is an outlier, not a theme. Keep it in the outlier list.
- **Name a theme as a finding, not a topic.** "Check-in" is a topic. "Check-in feels like too much after a shift" is a theme.
- **Split big clusters.** If a theme has observations pulling in two directions, it's two themes.
- **Keep small clusters.** A theme backed by two people can matter more than one backed by five, if it blocks the core loop.
- **Don't force fits.** Notes that belong nowhere go in a "parked" pile, and the readout says how many were parked.

## 5. Count the backing

For each theme, count **distinct participants**, not observations. Five remarks from P1 is still one person.

| Theme | Did | Said | Participants | Against |
|---|---|---|---|---|
| T-A Re-plan is understood and liked | P1, P2, P4, P5 completed in < 1 min; all 5 named their prep meals | P1, P5 praised it | 5 of 5 | P3 missed the button |

Always write the count as *x of n*, with *n* being everyone who had the chance to show it. "Most users" and "several people" are not counts.

## 6. Grade the strength

| Grade | When to use it |
|---|---|
| **Strong** | Observed behaviour from most participants (about 4 of 5 or more), consistent with what they said, and no unexplained counter-evidence |
| **Moderate** | Behaviour from about half, or behaviour plus statements that partly disagree, or strong behaviour with a known distortion (moderator help, prototype bug) |
| **Weak** | Statements or predictions only, or one or two participants, or a single source type (only survey text, only tickets) |

- **A prediction can't be graded Strong** on its own, however many people made it.
- **When did and said disagree, grade on what they did**, and record the disagreement as a contradiction.
- **The sample caps the grade's meaning.** Strong from five people means "this is very likely real for people like these five", not "this is how all users behave".

## 7. Contradictions and outliers

- **Contradiction:** two pieces of evidence that can't both be the whole story. The same person saying they'd use it every time and then failing the task. Two participants wanting opposite things. Behaviour that disagrees with what a survey says. Show both sides with IDs and say which you weight and why.
- **Outlier:** one participant, one need. Keep every outlier in a table with what it would take to act on it (a trigger in the PRD, a pattern in the next round). Never delete one because it's inconvenient, and never promote one to a theme because it's interesting.
- **Out-of-stance requests:** if an outlier asks for something the product has ruled out, record it and point to the decision that rules it out. Don't act on it, and don't hide it.

## Inputs other than test sessions

| Input | What changes |
|---|---|
| Interview transcripts | Mostly *said*. Look for stories of what people actually did last time, which are closer to behaviour than opinions. |
| Usability test notes | Rich in *did*. Use task results and times as the backbone, remarks as colour. |
| Survey free text | All *said*, and self-selected. Count responses, quote sparingly, grade no higher than Moderate. |
| Support tickets | Behaviour that already broke something, but only from people who wrote in. Good for "what goes wrong", bad for "how common". |
