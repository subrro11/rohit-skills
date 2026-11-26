# Experiment Design

Turn an assumption into an experiment you can make a decision on. You get a hypothesis, the right method for the sample you actually have, the sample size with the maths shown, and a ship, iterate or kill rule written before any data arrives.

When the sample is too small for an A/B test, it says so, shows why, and designs something that will work instead.

**Who it's for:** PMs, designers, founders and analysts who need to test a change, size a test, or read out one that already ran.

## Try it

```
Design an experiment to test whether <change> will <move metric> for <who>. We have about <number> users a week.
```

Other prompts:

- *"How long should this A/B test run?"* gives a sample-size check in chat
- *"What's the minimum detectable effect with 2,000 users a week?"*
- *"We only have 20 users. Can we still test this?"*
- *"Which guardrail metrics should this test have?"*
- *"Design a fake door test for <feature>"*
- *"Read out this test: <results>"* checks the design first, then reads the result against its rule

You can also call it directly: `/product:experiment-design` in Claude Code, `$experiment-design` in Codex.

## How it works

```
Decision ─▶ Hypothesis ─▶ Method ─▶ Metrics ─▶ Sample size ─▶ Decision rule ─▶ Threats ─▶ Instrumentation ─▶ Launch plan
```

| Step | What it decides | What keeps it honest |
|---|---|---|
| **Decision** | What changes depending on the result, and the riskiest assumption behind it | No decision, no experiment |
| **Hypothesis** | Change, segment, metric, smallest effect worth acting on, time, and why | The null result is written too |
| **Method** | A/B test, crossover, cluster or shift-level randomisation, pilot with holdout, fake door, concierge, Wizard of Oz, before/after | Chosen from the sample size, with one line on why it beats the next-best |
| **Metrics** | One primary metric, two to four guardrails, the unit of randomisation | Baselines labelled *assumed* when guessed; metrics the change could game are caught |
| **Sample size** | Sample, duration and the effect it can detect | Formula and inputs shown, numbers run, clustering corrected |
| **Decision rule** | Ship, iterate and kill thresholds, tied to existing product gates | Written before launch; guardrails can veto |
| **Threats** | Peeking, sample ratio mismatch, novelty, contamination, seasonality, carryover | Each one blocked or detected |
| **Instrumentation** | Every event the readout needs | Denominator and version on every event |

## What you get

An `EXPERIMENT.md` with:

- **Decision, assumption and hypothesis**, including what a null result means.
- **The method and why**, with the maths if an A/B test was ruled out.
- **Metrics and baselines**, each guess labelled.
- **Sample size and duration**, formula, inputs, result and sensitivity to the assumed numbers.
- **A pre-registered decision rule** with ship, iterate and kill rows.
- **Threats to validity**, each with how it's handled.
- **Instrumentation** and a timeline.
- **An empty readout**, ready to fill when the data is in.

## See it work

[Shiftplate experiment](examples/shiftplate/) designs a test inside a 20-person pilot. It proves an A/B test can't work there, swaps in a crossover that can, and guards against a default that would game its own metric.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `experiment-design`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install product@rohit-skills` (installs every product skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/experiment-design` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `experiment-design`, and upload it under Customize → Skills.

It works best in an agent that can run code, so the sample sizes are computed rather than estimated.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/method-chooser.md`](references/method-chooser.md) | Which method fits which question and sample |
| [`references/hypothesis-and-metrics.md`](references/hypothesis-and-metrics.md) | Hypothesis form, primary metric, guardrails, baselines |
| [`references/sample-size-and-power.md`](references/sample-size-and-power.md) | The formula, a plain-words explanation, a lookup table, clustering and crossovers |
| [`references/validity-threats.md`](references/validity-threats.md) | Threats to validity and how to block or detect each |
| [`references/readout-template.md`](references/readout-template.md) | Pre-registered decision rule and readout |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 29 checks to run before handover |
| [`examples/shiftplate/`](examples/shiftplate/) | A full design for a fictional product's pilot, with its maths script |

## Further reading

- Evan Miller, [How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html), on peeking
- Evan Miller, [Sample Size Calculator](https://www.evanmiller.org/ab-testing/sample-size.html)
- Microsoft Experimentation Platform, [Diagnosing Sample Ratio Mismatch in A/B Testing](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/)
- Microsoft Experimentation Platform, [External validity of online experiments](https://www.microsoft.com/en-us/research/articles/external-validity-of-online-experiments-can-we-predict-the-future/)
- Optimizely, [Sample size calculations unpacked](https://www.optimizely.com/field-notes/articles/sample-size-calculations-for-experiments)
- Wikipedia, [Crossover study](https://en.wikipedia.org/wiki/Crossover_study) and [Design effect](https://en.wikipedia.org/wiki/Design_effect)
