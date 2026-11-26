# User Interview Synthesis

Turn interview transcripts, usability-test notes, survey free text or support tickets into findings you can act on. Every theme says how many participants back it, keeps what they did apart from what they said, and traces back to a participant ID and their own words.

It never invents a quote, and it anonymises people on the way in.

**Who it's for:** PMs, designers and researchers who have just run sessions and need a readout before the next decision, and anyone handed a pile of notes or tickets and asked "so what are people saying?".

## Try it

```
Synthesise these notes from <n> sessions. The question is <what you're deciding>.
```

Other prompts:

- *"Affinity map these interview transcripts"*
- *"What are the themes in these survey answers?"*
- *"Write a usability test readout against these task targets"*
- *"Did the prototype pass the gate in this PRD?"*
- *"Turn these findings into an opportunity solution tree"*
- *"Quick themes from these support tickets"* answers in chat with counts and IDs

You can also call it directly: `/product:user-interview-synthesis` in Claude Code, `$user-interview-synthesis` in Codex.

## How it works

```
Question ─▶ Observation log ─▶ Codes ─▶ Themes ─▶ Insights ─▶ Opportunities ─▶ Readout
```

| Step | What it produces | What makes it trustworthy |
|---|---|---|
| **Question** | The decision, the data, and any targets set before the sessions | Targets are never set or moved after seeing results |
| **Observation log** | One row per thing a participant did, said or asked | Participant ID, task and time, and a verbatim or detail on every row |
| **Themes** | Codes clustered by affinity, named as findings | Counted as x of n distinct participants, with did and said in separate columns, and graded Strong, Moderate or Weak |
| **Insights** | Observation, why it matters, implication | Why it matters names a real goal or metric; the implication is a test or direction, not a decision the data can't carry |
| **Contradictions and outliers** | Evidence that disagrees, and single-person needs | Both sides shown; outliers kept, ruled-out requests recorded and not acted on |
| **Opportunities** | Outcome → needs → candidate solutions → riskiest assumption and a test | Each need cites insights; each top solution is checked for whether it would break the metric it's judged on |
| **Can't tell you** | The gaps in the data | Each gap comes with what would close it |

## What you get

A `SYNTHESIS.md` with:

- **The answer first.** The verdict (for a test, pass, iterate or stop against your own criteria), how sure, and what would change it.
- **Results against criteria**, task by task, when there were targets.
- **A theme table** with counts, did versus said, and a strength grade.
- **Insights**, each with two or three short verbatims and participant IDs.
- **Contradictions and outliers**, nothing dropped.
- **An opportunity map** hung from one outcome metric, with the riskiest assumption to test next.
- **What this data can't tell you.**
- **Feeds next.** Findings mapped to PRD sections and the next experiment.
- **The observation log**, so anyone can check any sentence against the notes.

## See it work

[Shiftplate prototype test](examples/shiftplate/) is a fictional five-nurse usability test of a meal-planning app. The readout passes half a release gate, fails the other half, and picks a top opportunity that's riskier than it looks: the obvious fix would hide the very food waste the product is meant to measure.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `user-interview-synthesis`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install product@rohit-skills` (installs every product skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/user-interview-synthesis` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `user-interview-synthesis`, and upload it under Customize → Skills.

It needs no web access. Paste or attach the notes, transcripts, survey export or tickets.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/coding-and-clustering.md`](references/coding-and-clustering.md) | The observation log, coding, affinity clustering, counting and strength grades |
| [`references/insight-format.md`](references/insight-format.md) | Observation → why it matters → implication, with weak and strong examples |
| [`references/opportunity-mapping.md`](references/opportunity-mapping.md) | Outcome, opportunities, candidate solutions and assumptions to test |
| [`references/readout-template.md`](references/readout-template.md) | The `SYNTHESIS.md` structure |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 26 checks to run before handover |
| [`examples/shiftplate/`](examples/shiftplate/) | Fictional session notes and the readout made from them |

## Further reading

Background the method draws on, written up in this skill in its own words:

- Nielsen Norman Group, [Affinity diagramming for collaboratively sorting UX findings and design ideas](https://www.nngroup.com/articles/affinity-diagram/): clustering observations, keeping small clusters, duplicating a note that fits two places.
- Nielsen Norman Group, [Analyze qualitative data: thematic analysis](https://www.nngroup.com/articles/thematic-analysis/): codes versus themes, and the common ways analysis goes wrong.
- Nielsen Norman Group, [First rule of usability? Don't listen to users](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/): why behaviour outweighs self-report and prediction.
- GOV.UK Service Manual, [Analyse a research session](https://www.gov.uk/service-manual/user-research/analyse-a-research-session): observations, affinity sorting, findings and actions as a team.
- Teresa Torres, Product Talk, [Opportunity solution trees](https://www.producttalk.org/opportunity-solution-trees/): outcome, opportunity, solution and assumption tests, and how to tell an opportunity from a solution.
