# Pre-registration and readout

Two halves. Fill the first before launch and don't edit it afterwards; if something has to change, add a dated amendment underneath saying what and why. Fill the second only when the data is in.

## Before launch: decision rule

```markdown
## Decision rule (written <date>, before launch)

**Primary metric:** <name> = <numerator> / <denominator>, per <unit>, over <window>
**Comparison:** <version B> minus <version A>
**Analysis:** <test or model>, <interval, e.g. 95% confidence interval>, analysed per <unit of randomisation>
**Sample:** <n per group or n units × k events>, ending <date or condition>. No early stopping unless <stopping rule>.
**Missing data and dropouts:** <how they count>

| Outcome | Primary metric | Guardrails | Action |
|---|---|---|---|
| Ship | <threshold> | All hold | <what happens, and which product gate it feeds> |
| Iterate | <threshold> | <any near limit> | <what changes, and the rerun> |
| Kill | <threshold> | <any fails> | <what happens instead> |

**Guardrails:** <metric> must stay <above/below> <threshold> · …
**Segments looked at (named in advance):** <list, or "none">
**Validity checks before reading results:** sample ratio, events firing in both groups, <crossover: carryover and period>
```

## After the data is in: readout

```markdown
# Readout: <experiment name>

**Decision:** <ship / iterate / kill> · **Date:** <date> · **Owner:** <name>

## Answer
<Two to three sentences: what happened to the primary metric, with its interval, what the guardrails did, and what the rule says to do.>

## Validity checks
| Check | Result | Pass? |
|---|---|---|
| Sample ratio (chi-square on counts) | <observed vs expected, p-value> | |
| Sample reached as planned | <planned vs actual> | |
| Stopped early? | <no / yes, why> | |
| Instrumentation complete in both groups | <missing events, if any> | |
| Dropouts by group | <counts> | |
| Novelty or trend by period | <effect per period> | |
| Crossover only: carryover and period | <effect in first vs later periods> | |

## Primary metric
| Group | Units | Events | Metric | |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| Difference | | | | <interval> |

## Guardrails
| Guardrail | Threshold | Result | Holds? |
|---|---|---|---|

## Against the rule
<Quote the pre-registered row the result falls in. If it falls between rows, say so and take the more cautious one.>

## What we learned
<What the result says about the mechanism. What surprised us. Exploratory findings, labelled as exploratory.>

## Next
<The action, who owns it, and the next experiment if any.>
```

## Reading a result honestly

- **Read the rule, not the hope.** If the result lands in "iterate", it's iterate, even if the point estimate looks good.
- **Report the interval, not just the verdict.** "+12 points (95% CI −2 to +26)" says more than "not significant".
- **Not significant is not "no effect".** It means this test couldn't tell. Say what effect sizes the interval still allows.
- **A failed validity check comes first.** If the sample ratio is off or events are missing in one group, the result isn't readable until the cause is found.
- **Segments found after the fact are exploratory.** Name them as hypotheses for the next test.
- **If there was no decision rule written in advance,** call the whole readout exploratory.
