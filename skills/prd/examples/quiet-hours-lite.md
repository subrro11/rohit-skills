# Quiet Hours

v0.2 · 2026-11-06 · Proposed · Owner: Product lead, Messaging
Fictional example. The company, users and every number below are invented to show the format.

## Changelog
- v0.2: Added the out-of-scope list, and swapped the primary metric from "DAU" to after-hours messages read before 9am. (FB1, FB2)

## Recommendation

Let workspace members set quiet hours that hold notifications and show senders a "delivers at 9:00" preview before they hit send. Start with senders, not receivers: the sender preview is the wedge, because it changes behaviour at the source instead of hiding the problem. Now is the moment because the team is distributed across three time zones and after-hours pings are the top theme in support tickets this quarter (*assumed*: 18% of tagged tickets).

**PMF hypothesis:** distributed teams of 20–200 people will keep quiet hours switched on, because senders defer non-urgent messages when they can see the recipient's local time. Proven when at least 30% of previewed messages are deferred in the prototype, and at least 50% of beta users still have quiet hours on after four weeks. Stage: solution fit.

The runner-up was a receiver-only "do not disturb" toggle; it lost because it already exists at the OS level and doesn't reduce the pings.

## Problem

**User:** Individual contributors on distributed teams who get messages outside their working hours.
**Today they:** Mute the app at night, then miss urgent messages, or leave it on and get interrupted.
**It costs them:** About 25 minutes of evening interruptions a day (*assumed*: to be measured in a week-one diary study with 8 users).
**Evidence:** Support ticket tags (internal, Q3). Evidence needed: whether senders would delay a message when shown the preview; a two-week prototype test would settle it.

## Goals and non-goals

**Goals:** After-hours messages wait until morning without urgent ones getting lost. Senders decide in one tap.
**Not optimising for:** fine-grained control. One schedule per person in v1; defaults over settings.

## Scope

| In scope | Deferred (and what brings it in) | Out of scope |
|---|---|---|
| Personal quiet hours (one schedule, local time) | Per-channel schedules, if more than 20% of users ask for them | Read receipts that reveal when someone is offline |
| Sender preview: "Priya is in quiet hours · delivers 9:00" | Admin-enforced team quiet hours, once enterprise pilots ask for it | Guilt-trip copy such as "Are you sure you want to bother them?" |
| "Send now anyway" for urgent messages | Calendar-synced schedules, after the calendar integration ships | Silently dropping messages |

## Requirements

| ID | Priority | Requirement | Acceptance |
|---|---|---|---|
| R1 | P0 | Set one daily quiet-hours window in local time | Window persists across devices within 5 s; DST changes don't shift it |
| R2 | P0 | Hold push and email notifications during the window | No push sent in window in a 7-day soak test with 50 accounts |
| R3 | P0 | Show the sender a delivery preview before sending | Preview appears in under 200 ms for DMs and @mentions to a person in quiet hours |
| R4 | P0 | Let the sender override with "Send now anyway" | Override delivers immediately and marks the message as urgent to the recipient |
| R5 | P1 | Deliver held notifications as one digest when the window ends | One digest per recipient, grouped by conversation |
| R6 | Later | Per-channel schedules | n/a |

Priority method: RICE. Override: R4 (urgent override) scored low on reach but is P0, because without it the feature risks hiding real emergencies, a basic expectation.

## Success

**North star (company):** weekly active teams that resolve threads within a working day · this feature moves *depth* (healthier threads per team) and must not hurt *frequency*.

| Metric | Baseline | Floor to beat | When |
|---|---|---|---|
| Share of after-hours messages first read during working hours | 41% (*assumed*) | 60% | 4 weeks after beta |
| Urgent overrides per sender per week (guardrail: overuse means the preview is ignored) | n/a | ≤ 1.5 | Weekly |
| Median response time on urgent-marked messages (guardrail) | 12 min (*assumed*) | must not rise above 15 min | Weekly |

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| Should quiet hours be on by default for new users? | Design lead | Beta gate |
| Do admins need to see team quiet-hours coverage? | PM | Before GA scoping |
| Is the override copy neutral enough? Test three variants | UX writer | Prototype test |

## Next step

Prototype R3 and R4 with a coding agent (see `quiet-hours-prototype-prompt.md`) and test it with two internal teams for two weeks. Go to build if senders delay at least 30% of previewed messages.
