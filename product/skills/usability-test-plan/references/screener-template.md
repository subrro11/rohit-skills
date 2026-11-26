# Screener template

A screener finds people who really have the behaviour you're designing for, without telling them what answer gets them in. If the purpose is obvious, keen people will shape their answers to qualify.

## Rules

- **Describe the study in general terms.** "A 30-minute video call about how you plan meals around work", not the product name or the feature.
- **Ask about behaviour, not opinions.** "In the last two weeks, how many times did you…?" beats "Do you like to…?"
- **Avoid yes/no questions.** They're easy to game. Use multiple choice with plausible distractors, or ask people to describe a recent example.
- **Distractors must be believable.** Absurd options give the game away.
- **Watch for people who tick everything.** If someone selects every option across several questions, exclude them.
- **Ask one open question.** "Describe the last time…" separates real experience from guesses. Read it before inviting anyone.
- **Ask only what you need.** Every question should decide in or out, or balance the group. No date of birth, no full address.
- **Keep it short.** Six to ten questions, under five minutes.

## Template

```markdown
## Screener

**Recruiting post:** <general description of the study>, <length>, <format>, <incentive>. <How to apply.>

| # | Question | Options | Rule |
|---|---|---|---|
| 1 | <role / situation question> | <target>, <distractor>, <distractor>, <distractor>, Other | Must pick <target> |
| 2 | <frequency of the target behaviour, in a recent window> | Never · Once · 2–3 times · Weekly or more | Must pick <threshold> |
| 3 | <multiple choice with the target behaviour among others> | <target>, <distractor>, <distractor>, <distractor>, None of these | Must include <target>; exclude if all ticked |
| 4 | <device and setting needed for the session> | | Must have <device> |
| 5 | <exclusion: works in or near the field being tested> | <industry list with the risky ones> | Exclude <list> |
| 6 | <exclusion: taken part in research on this in the last n months> | | Exclude if yes |
| 7 | Open: "Describe the last time <target behaviour>." | Free text | Must describe a real, specific instance |
| 8 | <balancing question, used only to spread the group> | | Aim for <mix> |

**Must have:** <behaviours>
**Nice to have:** <mix across groups, sites, experience>
**Exclude:** <people who shaped the idea, work on it, are close to the team, or work in UX or market research>
**Data handling:** answers live in a separate recruitment sheet, used only to select and contact people, and deleted <when>. They never go in the test notes.
```
