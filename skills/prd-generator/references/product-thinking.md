# Product thinking: answer these before writing requirements

A PRD is only as good as the answers to five questions. Work through them in order: each answer constrains the next. Put the answers in the PRD's own sections (listed under each heading), not in a separate essay.

---

## 1. What is the product problem?

Goes in: **Users and problem**

Frame it as: **<user> is trying to <job>, but <obstacle>, so today they <workaround>, which costs <cost>.**

Tests:
- **Specific user:** could you recruit five of them for interviews this week?
- **Real workaround:** if nobody does anything about it today, it may not hurt enough.
- **Cost:** time, money, risk or missed outcome. Use a number, or "assumed" plus how you'll measure it.
- **Not a solution in disguise:** "users need a dashboard" is a solution; "managers can't tell which projects are slipping until it's too late" is a problem.

If the problem fails these tests, the PRD should recommend discovery work before any build.

---

## 2. Is there product–market fit, or a path to it?

Goes in: **Recommendation**, **Evidence**, **Metrics**, **Release gates**

Treat PMF as a hypothesis with a test, never a claim.

**State the hypothesis:**
> We believe **<segment>** will **<adopt / pay / switch>** because **<value>** is meaningfully better than **<current alternative>**. We'll know when **<signal>** reaches **<threshold>**.

**Pick the stage and the matching signal:**

| Stage | What you're proving | Signals to use |
|---|---|---|
| Problem fit | The problem is real, frequent and painful | Interview patterns, the workaround is in active use, willingness to try something unfinished |
| Solution fit | Your approach solves it better than the alternative | Prototype task success, "would be very disappointed without it" ≥ 40% (Sean Ellis survey), repeat use without nudging |
| Product–market fit | A segment adopts and keeps using it | A retention curve that levels off instead of falling to zero; organic referral; willingness to pay; sales cycle shortening |
| Scale fit | Growth is efficient | CAC payback, expansion revenue, channel saturation |

**Rules:**
- Name the segment narrowly. PMF is found in one segment first, not "SMBs".
- A retention curve that levels off is stronger evidence than total sign-ups or downloads.
- If the stage is problem or solution fit, scope the PRD as an experiment (usually Lite), with a gate on the PMF signal.
- Never write "this has PMF" without a cited signal.

---

## 3. What is the north star, and what feeds it?

Goes in: **Metrics**

**The north star** is the one metric that rises only when users get the core value *and* the business benefits. It measures value delivered to users; counts of logins or page views don't qualify.

| Good north star | Why | Weak version |
|---|---|---|
| Weekly projects shipped on time | Value to the user, and it drives retention | Daily active users |
| Nights booked | Value to both sides of the marketplace | App opens |
| Messages read during working hours | The outcome the feature exists for | Notifications sent |

**Build a small tree:**

```
North star: <value metric>
├── Input 1: breadth   (how many users reach value)
├── Input 2: depth     (how much value per user)
├── Input 3: frequency (how often)
└── Guardrails:        (what must not get worse: quality, cost, trust, latency)
```

**Rules:**
- The feature's **primary metric** must be one of the inputs, or move one directly. If it doesn't connect to the north star, ask why you're building it.
- Every metric needs a baseline (or "measure in week 1") and a floor to beat.
- Add at least one guardrail against the obvious way to game the primary metric.
- For an early product with no north star yet, propose one and label it *proposed*.

---

## 4. What are the goals and non-goals?

Goes in: **Goals, scope and principles**

**Goals** are outcomes, phrased so you could tell at the end whether they were met:
- Good: "A new user completes their first booking in under 3 minutes."
- Bad: "Improve onboarding."

Keep it to 3–5. More means nothing is a priority.

**Non-goals** are things a reasonable person would expect this to do, which it deliberately won't. Write three kinds:

| Kind | Example |
|---|---|
| **Deferred** (with the trigger that brings it in) | "No team accounts until 20% of signups come from shared email domains." |
| **Out of scope** (positioning) | "Not a CRM. We coexist with one." |
| **Not optimising for** (tradeoff) | "Not optimising for power users in v1; defaults over configuration." |

A non-goal nobody would have asked for is filler. Delete it.

---

## 5. What do we build first? (prioritisation)

Goes in: **Requirements** (the priority column) and the **Decision log**

**Default method: score with RICE, then sanity-check against the bet.**

| Factor | Question | Scale |
|---|---|---|
| **R**each | How many users does it affect per quarter? | Count or estimate |
| **I**mpact | How much does it move the primary metric per user? | 3 massive · 2 high · 1 medium · 0.5 low · 0.25 minimal |
| **C**onfidence | How sure are we, given the evidence? | 100% data · 80% some evidence · 50% gut |
| **E**ffort | Person-weeks to ship | Number |

Score = R × I × C ÷ E. Show the table in the PRD for anything contested.

**Then override deliberately, and log why:**
- **Must-haves for the core loop** are P0 even if they score low. Without them nothing works; score them as part of one bundle.
- **Risky assumptions first.** If a cheap item tests the riskiest assumption in the PMF hypothesis, pull it forward.
- **Kano check:** basic expectations (missing = angry) are P0 regardless of delight. Delighters rarely belong in v1.
- **Confidence below 50%** means the item becomes an experiment, not a requirement.

**Map to priorities:**
- **P0:** the core loop doesn't work without it, or it is a basic expectation. Ships in the first release.
- **P1:** it has a high RICE score and the core loop works without it. Ships in the next release if metrics hold.
- **Later:** low score or low confidence. Record the trigger that would promote it.

**Alternatives and when to use them:**
- **MoSCoW:** for a fixed-deadline negotiation with stakeholders.
- **Opportunity scoring** (importance vs satisfaction): when you have survey data from users.
- **Cost of delay:** when timing matters, for example regulation, a seasonal window or a competitor launch.

Pick one method per PRD and say which one. Don't mix scores.
