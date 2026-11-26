# Launch plan: Shiftplate 20-nurse pilot

> Fictional showcase. Shiftplate, its team, its nurses and the hospital are invented. The plan states thresholds and owners; no results exist yet.

v0.1 · Launch day: TBC · Status: Draft, two no-go items open · Decider: Product lead
Dates are relative to launch day. Numbers come from the PRD unless marked.

Inputs: [PRD](../../../prd-generator/examples/shiftplate/2-PRD.md) v0.1, [research](../../../deep-research/examples/shiftplate/RESEARCH.md), copy and UX reviews of the v0.1 prototype, a 5-nurse usability test, and the one-tap check-in experiment design.

## Summary

Shiftplate's v1 is a **4-week pilot with 20 nurses at one hospital**, run to answer one question from the PRD: will nurses who already meal prep re-plan in Shiftplate at every rota change? It is not a launch to the public. Nobody outside the invited cohort can install it.

**Decision rule (copied from the PRD):** **Pass:** 10 of 20 pilot nurses re-plan through two rota changes in a row without being reminded. **Iterate:** 5–9 of 20. **Stop:** fewer than 5 of 20. Nurses who leave the pilot count as not passing; the denominator stays 20.

**What's launching:** manual rota entry, prep logging, one-tap reuse-first re-plan, end-of-shift check-in (two versions, under the experiment), about 20 gap meals, offline use. **Not launching:** the grocery list (P1), night-shift meal timing, rota import, partner sharing, anything to do with calories or diets.

**What the inputs told this plan to protect:**

- **Food safety.** Research changed the use-by default from 4 days to **3 days**, with a per-dish override. A portion planned past its use-by is the one thing that must never happen.
- **The hook.** The usability test found re-plan is what nurses came back for, so re-plan has its own kill switch rather than taking the whole app down.
- **The weak step.** Logging and the end-of-shift check-in were the friction; 3 of 5 test nurses said they wouldn't check in after a real shift. Check-in completion is on the watch list, and the experiment tests a one-tap version. Nobody tunes the check-in mid-pilot.
- **Personal data.** Rota and food logs are personal, health-adjacent data. No employer or hospital name is collected, and deletion on request happens within 7 days (PRD R8).

### Conflicts with the PRD

| PRD says | This plan does | Before go |
|---|---|---|
| G1: nurses recruited "from more than one hospital" | One hospital | Product lead updates G1 and adds a decision-log row: one site is faster to support; the cost is that results may not hold elsewhere |
| Use-by default 4 days (*assumed*) | 3 days, from research | Product lead updates the PRD's use-by line |
| Pilot 4–6 weeks (*assumed*) | 4 weeks | Recorded in the PRD; screening checks each nurse expects at least two rota changes in the window |

## Tier

**Tier 2.** Reach is low (20 invited nurses, no public listing), but risk is high: the app tells tired people what to eat and when, it holds their work rota, and food logs are health-adjacent. The higher score sets the tier. That means written gates, consent comms, a rehearsed kill switch and a dated review, but no public announcement, no press and no capacity planning.

## Rollout stages

| Stage | Who | How they get it | When | Gate to move on |
|---|---|---|---|---|
| **Internal** | The team, on their own phones, with their own (made-up) rotas | TestFlight internal testers; Google Play internal testing track | Day −14 to Day −1 | Gate A |
| **Pilot, wave 1** | 5 of the 20 consented nurses | TestFlight external testing group; Play internal testing track | Launch day to Day +3 | Gate B |
| **Pilot, wave 2** | The other 15 | Same groups | Day +4 to Day +28 | Gate C (the review) |
| **Wider beta** | Only if the pilot passes. Nurses across several hospitals | Gets its own launch plan | Not before the review | n/a |

Wave 1 exists to catch a bad bug while three quarters of the cohort still haven't seen the app. Both waves include nurses from both experiment arms (assignment happens at enrolment, as the experiment design sets out), so wave timing doesn't skew the check-in result.

**Distribution notes.** The first build for external testers goes through App Review for TestFlight, so it is submitted by Day −10 and is never on launch day's critical path. Google Play's internal testing track takes up to 100 named testers, which covers the cohort. Nurses on iPhone and Android get the same build number.

### Flags and config

| Flag | Type | Default | Who can flip it | Removed when |
|---|---|---|---|---|
| `pilot_access` | Permission | On for invited accounts only | Engineering lead | Replaced by the beta plan's access rule |
| `replan_enabled` | Ops kill switch | On | Engineering lead or Product lead | Kept through beta |
| `one_tap_checkin` | Experiment | Set per nurse at enrolment | Nobody during the pilot | At the review, once the experiment is read |
| `use_by_default_days` | Remote config | 3 | Product lead, with Food-safety reviewer sign-off | Moves into the build after the pilot |

The app reads flags at launch and when it returns to the foreground. If it can't reach the server, re-plan still works offline (PRD R7), and the use-by check runs on the device, so the kill switch is never the only thing between a nurse and an expired portion.

## Gates

**Gate A: internal → wave 1** (Day −1; includes the PRD's G1). Decider: Product lead. Every check must pass.

| Check | Pass when | Source | Read by |
|---|---|---|---|
| Requirements | R1–R8 meet their acceptance criteria on the release build | Test log | Engineering lead |
| Use-by default | Default is 3 days in the build and in remote config; per-dish override works | Test log | Food-safety reviewer |
| Use-by guard | Zero portions placed past use-by across the edge-case test set (empty fridge, all expired, mixed prep dates, offline) | Automated check | Engineering lead |
| Kill switch | Turning `replan_enabled` off shows the pause message on one iPhone and one Android test device within 15 minutes, and turning it on restores re-plan | Rehearsal log | Engineering lead |
| Deletion | A test account is deleted end to end, including backups and analytics, and the confirmation message is sent | Rehearsal log | Privacy reviewer |
| Data kept | Export holds only rota, portions and check-ins; no employer or hospital field | Export review | Privacy reviewer |
| Food-safety wording | Every screen that mentions use-by, storage or reheating is signed off | Copy review | Food-safety reviewer |
| Cohort | 20 nurses screened (rotating 12-hour day and night shifts, already meal prep, expect two or more rota changes in the window) and consented; 5 assigned to wave 1 | Recruitment tracker | Design and research lead |
| Support | Channel tested from outside the team; FAQ, known issues and pause script handed over | Walkthrough done | Support lead |
| Instrumentation | Every event behind the watch list and the success metrics has been seen from internal use | Analytics | Engineering lead |
| Internal crash-free | Zero crashes in the logging and re-plan flows across all internal phones over the last 5 days | Crash reports | Engineering lead |

**No-go:** any check fails. The Product lead can't waive the use-by guard, kill switch, deletion or data-kept checks.

**Gate B: wave 1 → wave 2** (Day +3). Decider: Product lead.

| Check | Pass when | Source |
|---|---|---|
| Harm | Zero harm triggers (see Rollback) | Watch list |
| Crashes | No crash in logging or re-plan has hit 2 or more nurses | Crash reports |
| Setup | At least 4 of 5 nurses have entered a rota and logged at least one portion | Analytics |
| Support | Every message answered inside the support target | Support log |

**Stop instead of moving on:** any harm trigger whose cause isn't found and fixed.

**Gate C: end of pilot** is the post-pilot review below. It applies the PRD's G2.

## Owners

Shiftplate is a small team, so people hold several roles. Every role is filled, and the rollback decider is reachable during night shifts in wave 1.

| Role | Holds it in this pilot |
|---|---|
| Product lead (decider) | Founder |
| Engineering lead | Engineer |
| Design and research lead | Designer |
| Support lead | Designer, with the Founder as stand-in for nights |
| Privacy reviewer | Outside advisor, part-time |
| Food-safety reviewer | Outside advisor, part-time |

| Decision or job | Owner | Decides | Told |
|---|---|---|---|
| Gates A, B | Engineering lead | Product lead | Everyone |
| Pause re-plan | Engineering lead | Engineering lead (acts alone), or Product lead | Support lead, Product lead |
| Stop the pilot | Product lead | Product lead | Everyone, nurses |
| Food-safety wording and default | Design and research lead | Food-safety reviewer | Product lead |
| Consent wording, data deletion | Support lead | Privacy reviewer | Product lead |
| Recruitment and screening | Design and research lead | Product lead | Support lead |
| Watch-list readouts | Engineering lead | n/a | Team |
| Post-pilot review | Product lead | Product lead | Everyone, nurses |

## Readiness

| Area | Item | Owner | Due | Status |
|---|---|---|---|---|
| Product | PRD updated for the three conflicts above | Product lead | Day −10 | Open |
| Product | Known issues list with workarounds | Engineering lead | Day −7 | Open |
| Product | Copy says "use within 3 days of prepping" and never calls a portion "safe" | Design and research lead | Day −7 | Open |
| Engineering | Release build = tested build, same number on both platforms | Engineering lead | Day −2 | Open |
| Engineering | Kill switch and use-by guard rehearsed (Gate A) | Engineering lead | Day −3 | Open |
| Engineering | Daily automated check: no saved plan places a portion past its use-by | Engineering lead | Day −3 | Open |
| Engineering | First external build submitted for App Review for TestFlight | Engineering lead | Day −10 | Open |
| Support | One-to-one support channel (email plus a messaging number), no group chat, so nurses never see each other's details | Support lead | Day −7 | Open |
| Support | Hours: replies within 4 hours, 07:00–23:00. Food-safety or data issues answered within 1 hour at any hour in wave 1, then within 4 hours | Support lead | Day −7 | Open |
| Support | FAQ, known issues, pause script, escalation to Engineering lead | Support lead | Day −7 | Open |
| Legal and privacy | Consent wording signed off | Privacy reviewer | Day −12 | Open |
| Legal and privacy | Deletion within 7 days rehearsed end to end | Privacy reviewer | Day −3 | Open |
| Legal and privacy | Whether recruiting staff at the hospital needs its permission, and whether any research-ethics review applies, answered by someone qualified | Privacy reviewer | Day −21 | Open (no-go until answered) |
| Legal and privacy | Free-text dish names checked for anything that identifies a workplace; FAQ asks nurses not to type one | Privacy reviewer | Day −7 | Open |
| Data | Events for re-plan, check-in, portions, binned (R6) and crashes all seen | Engineering lead | Day −3 | Open |
| Data | Baseline: binned share is measured in pilot week 1, per the PRD | Product lead | Launch day | Planned |
| Data | Experiment flag assignment checked against the experiment design | Engineering lead | Day −5 | Open |
| Data | Known gaps written down: "eaten" is self-reported; "binned" is inferred | Product lead | Day −7 | Done (in PRD) |
| Docs | One-page start guide: enter rota, log prep, re-plan, check in, get help, leave | Design and research lead | Day −5 | Open |
| Docs | Internal runbook: watch list, rollback steps, roles and stand-ins | Engineering lead | Day −3 | Open |

## Comms

| When | Audience | Message | Sender | Channel |
|---|---|---|---|---|
| Day −21 | Nurses (recruitment) | What Shiftplate is, who it's for, what taking part involves (4 weeks, check-ins, a 20-minute exit interview), screening questions | Design and research lead | Personal referral between nurses; never through the employer's channels |
| Day −14 | Team, advisors | This plan, roles, rollback triggers | Product lead | Team channel |
| Day −12 to −8 | Each recruited nurse | Participant information and consent (checklist below) | Design and research lead | Email, one to one |
| Day −7 | Support | Build walkthrough, FAQ, known issues, pause script | Product lead | Walkthrough + runbook |
| Day −1 | Wave 1 nurses | How to install, first three steps, how to reach support and when | Support lead | Email + messaging number |
| Launch day | Team | Live; who's watching what tonight | Product lead | Team channel |
| Day +1, +3, +7 | Team | Watch-list readout | Engineering lead | Team channel |
| Day +3 | Wave 2 nurses | Install message (same as Day −1) | Support lead | Email + messaging number |
| Day +14 | All nurses | Halfway note: thanks, how to get help, reminder they can leave. No prompt to re-plan or check in | Product lead | Email |
| As needed | Affected nurses | Pause message (below) | Support lead | In app + direct |
| As needed | One nurse | Deletion confirmation: what was deleted, when | Privacy reviewer | Email |
| Day +28 | All nurses | Pilot over; exit interview invite; what happens to their data next | Product lead | Email |
| Day +31 | Team, advisors, nurses | Decision and why | Product lead | Review doc; short email to nurses |

**Partners.** The hospital is not told or involved: Shiftplate collects no employer name and recruits through nurses, not the employer. That stays true only if the Day −21 privacy question comes back clear. If it doesn't, recruitment stops until written permission is in hand.

**Consent covers:** Shiftplate is a meal-planning app, not medical or dietary advice. It keeps your rota, the food you log and your check-ins. It never asks for your employer or hospital. You can leave at any time without a reason. Ask us to delete your data and it's gone within 7 days, and we'll confirm. Pilot data is kept until the review, then deleted unless you choose to stay on for a later beta (*proposed*; Privacy reviewer to confirm). Support answers within 4 hours between 07:00 and 23:00.

**Pause message (written now):** "Re-planning is paused while we fix a problem. Your rota and logged food are safe. Until we're back, don't eat anything you prepped more than 3 days ago because the app planned it. We'll message you by [time]."

## Success metrics and first-week watch list

**Success metrics** are the PRD's, unchanged: binned share of prepped portions (primary; halve the week-1 rate by week 4), nurses re-planning through two rota changes in a row (PMF signal), re-plan time (median under 1 minute), planned meals ticked eaten per nurse per week (north star), and time to log prep (guardrail; median 2 minutes or less).

**Week-1 watch list.** Counts are in nurses, not percentages.

| Signal | Kind | Expected | Alert when | Source, how often | Acts |
|---|---|---|---|---|---|
| Portion planned past its use-by | Harm | Never | **1** | Daily automated check + support reports | Engineering lead (see Rollback) |
| Employer or hospital name found in stored data | Harm | Never | **1** | Daily scan of free-text fields | Privacy reviewer |
| Crash-free sessions | Health | No crashes in logging or re-plan | Any crash in those flows; or the same crash for 2+ nurses | Crash reports, daily | Engineering lead |
| Check-in completion: shifts with a check-in within 12 hours of the shift ending | Use | Unknown; the test suggests low | Fewer than half of active nurses check in at least once in their first 3 shifts | Analytics, Day +3 and +7 | Product lead notes it. No nudges, and the experiment flag stays as it is |
| Re-plan use: nurses who re-planned after a rota change | Use | Most nurses with a change | A nurse changes their rota and has no re-plan within 48 hours | Analytics, daily | Engineering lead checks for a bug first. No reminder is sent (PRD decision log) |
| Support replies | Health | Inside target | Any message unanswered past target | Support log, twice daily | Support lead |
| Deletion requests | Harm | Rare | Any request open for 5 days | Support log, daily | Privacy reviewer |
| Nurses leaving | Use | Few | 3 or more in week 1 | Support log | Product lead holds wave 2 and asks why |

## Rollback

| Trigger | Threshold | Response | Decides (stand-in) | Time to act | Mechanism | Nurses see |
|---|---|---|---|---|---|---|
| A portion planned past its use-by | 1 | **Pause** re-plan for everyone. **Stop** the pilot if the cause isn't found and fixed within 24 hours | Engineering lead acts alone (Product lead) | 1 hour from detection | `replan_enabled` off; daily check re-run on all saved plans | Pause message, plus a direct message to any nurse whose plan held the portion |
| A nurse reports getting ill from food the app planned | 1 | **Stop** the pilot pending review | Product lead (Engineering lead) | 1 hour | `replan_enabled` off; `pilot_access` closed to new installs | Direct call or message from Product lead; pause message to the rest |
| Employer or hospital name collected by a field we built, or data sent anywhere consent doesn't cover | 1 | **Stop** | Privacy reviewer with Product lead | 4 hours | Remove the field or the data flow; delete what was collected | Direct message to affected nurses saying what happened and what was deleted. Privacy reviewer checks whether any reporting duty applies |
| Crash in logging or re-plan for 2+ nurses within 24 hours | 2 nurses | **Roll back** to the last good build | Engineering lead (Product lead) | 24 hours | Offer the last good build in TestFlight and the Play testing track; pause re-plan meanwhile if the crash is there | "We've sent a fix; please update" |
| Food-safety wording found wrong on a live screen | 1 | **Pause** the affected screen | Food-safety reviewer (Product lead) | 4 hours | Remote config hides the screen or text; fix in next build | Pause message if re-plan is affected |
| Deletion request about to miss 7 days | Day 5 open | Escalate; nothing else ships until it's done | Privacy reviewer | Same day | Manual deletion from the runbook | Deletion confirmation |

Every response is logged with the time it was detected, the time it was acted on and who decided. Resuming after a pause or stop needs Gate A's use-by guard and kill-switch checks to pass again.

## Post-pilot review

**Data cut-off:** Day +28 · **Review:** Day +31 · **Decider:** Product lead · **Template:** `references/post-launch-review.md`

The review:

1. Applies the PRD rule exactly as written: 10 or more of 20 pass, 5–9 iterate, fewer than 5 stop. Leavers count as not passing. If anyone wants to change the rule now, that is said openly and recorded, not done quietly.
2. Reports the primary metric (binned share, week 1 against week 4), the guardrail and the north star, with the PRD's measurement gaps stated next to them.
3. Hands the check-in result to the experiment readout; this review doesn't re-analyse it.
4. Lists every watch-list alert and rollback, with time to act.
5. Confirms commitments kept: every deletion inside 7 days, data handled as consent said, `one_tap_checkin` removed.
6. Records the decision in the PRD's decision log (gate G2).

**If pass:** the wider beta gets its own launch plan, due before any recruitment. It starts at tier 2 again (more nurses, several hospitals, same risk), uses TestFlight external groups and a Play closed testing track, and keeps the use-by guard and kill switch. **If iterate:** fix the weakest step the data points to and re-run with a new cohort. **If stop:** go back to problem interviews, as the PRD says.

## Open items

| Item | Owner | Needed by | No-go if open? |
|---|---|---|---|
| Does recruiting at the hospital need its permission? Does any research-ethics review apply? | Privacy reviewer | Day −21 | Yes |
| PRD updated for one hospital, 3-day default and 4 weeks | Product lead | Day −10 | Yes |
| Data retention after the review (delete by default unless a nurse opts into beta) confirmed | Privacy reviewer | Day −12 | No, but consent wording waits on it |
| Experiment assignment confirmed to mix both arms across both waves | Engineering lead | Day −5 | No |
