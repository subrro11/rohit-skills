# Readiness checklist

Every item gets an owner (a role), a due point relative to launch day, and a status: done, open, or not needed (with a reason). Drop what the tier doesn't need.

| Area | Item | Tier |
|---|---|---|
| **Product** | Every release gate in the PRD before this stage has passed, and the result is recorded | All |
| | Scope frozen: what's in, what's out, what's behind a flag | All |
| | Known issues listed, with the workaround for each | All |
| | Copy reviewed for claims the product can't back (safety, health, money, accuracy) | 2, 1 |
| **Engineering** | The build that ships is the build that was tested | All |
| | Kill switch or rollback path works, rehearsed on a real device or environment | 2, 1 |
| | Crash and error reporting on, and someone can see it | All |
| | Works offline or degrades clearly, if the PRD says it must | As PRD |
| | Capacity checked for the stage's peak | 1 |
| **Support** | A channel users can reach, and hours that cover when they use the product | All |
| | Support has used the build, and has the FAQ, known issues and the pause script | All |
| | Escalation path: what support hands to whom, and how fast | 2, 1 |
| **Legal and privacy** | Data kept matches the PRD's list; nothing extra is collected | All |
| | Consent wording plain, specific and agreed before access | 2, 1 |
| | Deletion on request works end to end, within the promised time | 2, 1 |
| | Whether formal review applies (health, finance, children, research ethics, the place you recruit) is answered by someone qualified | 2, 1 |
| **Data and instrumentation** | Every success metric and watch-list signal is logged, and a test event has been seen | All |
| | Baseline window agreed (what "before" means) | 2, 1 |
| | Experiment split and its flag checked, if an experiment runs | As needed |
| | Known gaps in measurement written down | 2, 1 |
| **Docs** | User help: how to start, how to get help, how to leave | All |
| | Internal runbook: watch list, rollback steps, contacts by role | 2, 1 |
| | Release notes for testers or users | 2, 1 |

A readiness check ends in one of three answers: **go**, **no-go** (with each open item and its owner), or **go with conditions** (each condition is a pass/fail check with a deadline).
