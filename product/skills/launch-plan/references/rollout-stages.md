# Rollout stages and flags

## Default path

| Stage | Who | Purpose | Typical length |
|---|---|---|---|
| **Internal** | The team, plus a few friendly colleagues | Find the bugs anyone would hit; rehearse the rollback | Until the gate passes, at least a few days of real use |
| **Pilot** | A small invited cohort that matches the target user | Answer the question the PRD asks | Long enough for each person to do the core action several times |
| **Beta** | A wider opt-in group, or a percentage of users | Check it holds up across more people, devices and contexts | Until the watch list is quiet and the metric is readable |
| **GA** | Everyone it's meant for | Reach | Often staged by percentage over days |

Skip stages the tier doesn't need, and say why.

## Choosing a cohort

- Match the people the PRD is for; friends who don't have the problem tell you nothing.
- Count people, not percentages, below about 100. "3 of 20" is honest; "15%" hides how small it is.
- Bring people in in waves. A first wave of a quarter of the cohort lets you catch a bad bug while most people haven't seen it.
- Write down how people leave the cohort, and what happens to their data.

## Length

A stage has to run long enough to see the thing you're worried about. Work it out from how often the core action happens: if it happens once per schedule change, and schedules change every week or two, a one-week stage can't show repeat use.

For a percentage rollout, the canary should be big enough and run long enough to represent everyone, and it should be compared against the people who didn't get the change at the same time, not against last week. (Google SRE workbook, Canarying releases.)

## Distribution for mobile apps

- **Apple TestFlight:** internal testers are members of your developer team; external testers join through a group, and the first build sent to external testers goes through App Review for TestFlight. Check the current limits on Apple's TestFlight page.
- **Google Play testing tracks:** internal testing for a small named list (up to 100 testers per app when last checked), closed testing for larger invited lists, open testing for anyone. Check the current limits in Play Console help.
- Leave time for review before the first external build. Don't put store review on launch day's critical path.

## Flags

Every flag in the plan gets a row:

| Flag | Type | Default | Who can flip it | Removed when |
|---|---|---|---|---|

Types (after the "Feature Toggles" article on martinfowler.com):

- **Release flag**: hides unfinished work. Short-lived; remove once the stage it protects has passed.
- **Experiment flag**: splits a cohort for a test. Must not change mid-test, or the result is spoiled.
- **Ops flag or kill switch**: turns a risky path off in production without a new build. The one your rollback depends on. Test it before launch.
- **Permission flag**: who can see it (internal, pilot, beta). Can live longer, but still needs an owner.

Flags have a carrying cost. Each one gets a removal point, written in the plan.

## Gate format

| Check | Pass when | Source | Read by |
|---|---|---|---|
| Crash-free | Zero crashes in the core flow across all internal testers over 5 days | Crash reports | Engineering lead |

The gate passes when every check passes. If one fails, the named decider chooses: fix and re-run, or go with a written reason.
