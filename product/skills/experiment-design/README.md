# Experiment Design

Most experiments I've seen go wrong before they launch. The sample was never big enough to show anything, the metric could be moved by the change itself, or someone decided what "good" looked like after seeing the numbers.

This skill is how I design a test so that doesn't happen. You start from the decision you need to make, pick the cheapest test your sample can actually support, do the maths before launch, and write down what result means ship, iterate or kill while you still don't know the answer.

If your sample is too small for an A/B test, it tells you, shows you why, and gives you something that will work.

## Try it

```
Design an experiment to test whether <change> will <move metric> for <who>. We have about <number> users a week.
```

It also handles smaller questions:

- "How long should this A/B test run?"
- "We only have 20 users. Can we still test this?"
- "Design a fake door test for <feature>"
- "Read out this test: <results>"

In Claude Code: `/product:experiment-design`. In Codex: `$experiment-design`.

## What I care about

- **Start from the decision.** If nothing changes based on the result, don't run the test.
- **Pick the method from the sample.** Twenty people can't power an A/B test. A crossover, a pilot with a holdout or a fake door often can.
- **One metric decides.** Guardrails can veto a win. Everything else just helps explain.
- **Write the rule first.** A threshold picked after the results is a story.
- **Show the maths.** Every sample size comes with its inputs so anyone can rerun it, and every guessed number is marked as a guess.

## What you get

An `EXPERIMENT.md` with the decision, the hypothesis, the method and why, the metrics, the sample size with the working, the decision rule, what could fool you and how you'll catch it, the events to log, and an empty readout to fill in once the data is in.

## Example

[Shiftplate](examples/shiftplate/) is a made-up meal-planning app for nurses on 12-hour shifts. The team wants to know if a one-tap check-in gets more nurses to log their meals, inside a 20-nurse pilot. On paper 240 shifts looks like plenty. Once you account for the same nurses logging every shift, an A/B test could only spot a 36-point jump, so the plan switches to a crossover where every nurse tries both versions. [`sample-size.py`](examples/shiftplate/sample-size.py) reproduces every number.

## Install

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `experiment-design`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install product@rohit-skills`.

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/experiment-design` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keep the name `experiment-design`, and upload it under Customize → Skills.

Works best in an agent that can run code, so the numbers get computed rather than guessed.
