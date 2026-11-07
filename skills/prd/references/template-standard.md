# <Product or feature name>: product requirements

v0.1 · <date> · Draft · Owner: <name> · Reviewers: <names>
Numbers are proposed or assumed unless a source is cited.

<!-- On revisions, add:
## Changelog
- v0.2 (<date>): <what changed> because <why>. (FB1)
-->

## 1 Recommendation

<What to build, for whom, the wedge, why now. 3–5 sentences. Name the runner-up option you rejected and why, in one sentence.>

**PMF hypothesis:** We believe <segment> will <adopt/pay/switch> because <value> beats <alternative>. Proven when <signal> reaches <threshold>.
**Stage:** <problem / solution / product–market / scale fit>. **Riskiest assumption:** <the one that kills the idea if wrong>.

## 2 Users and problem

**Primary user:** <who, in one line>
**Secondary users:** <optional>
**Current workaround:** <what they do today>
**Cost of the workaround:** <quantified or labelled assumed>

### Jobs to be done
- When <situation>, I want to <motivation>, so I can <outcome>.

### Evidence
| Evidence | Source | What it implies |
|---|---|---|
| … | … | … |

Evidence needed: <gaps and what would settle them>

## 3 Alternatives and positioning

| Alternative | What it does well | Where it falls short for this user |
|---|---|---|
| Doing nothing / the workaround | … | … |
| <competitor or substitute> | … | … |

**Positioning:** <one sentence: for <user> who <need>, <product> is the <category> that <key benefit>, unlike <alternative>.>

## 4 Goals, scope and principles

**Goals** (3–5 outcomes you could check at the end)
- …

**Non-goals**
- Not optimising for: <tradeoff>
- (Deferred and out-of-scope items go in the scope table below.)

**Scope**

| In scope | Deferred (with trigger) | Out of scope |
|---|---|---|
| … | … | … |

**Principles** (tie-breakers when requirements conflict)
1. …

## 5 Experience

<Primary journey as numbered steps from first contact to the moment of value. Then one short paragraph per key screen or surface. Link wireframes if they exist; don't describe pixels.>

## 6 Requirements and acceptance criteria

**Prioritisation:** <method, RICE by default>. For contested items:

| Candidate | Reach | Impact | Confidence | Effort | Score | Priority | Override reason |
|---|---|---|---|---|---|---|---|
| … | … | … | … | … | … | … | … |

| ID | Priority | Requirement | Acceptance |
|---|---|---|---|
| F01 | P0 | … | … |
| F02 | P1 | … | … |
| F03 | Later | … | n/a |

**Non-functional:** performance, accessibility (WCAG 2.2 AA unless stated), privacy, security, reliability. Each as a requirement with a threshold.

## 7 Data, dependencies and constraints

<Data the feature reads or writes, third-party APIs and their terms, platform limits, legal or compliance constraints, cost per user if material.>

## 8 Metrics

```
North star: <value metric>
├── Input: breadth   <metric>
├── Input: depth     <metric>
├── Input: frequency <metric>
└── Guardrails:      <quality, cost, trust>
```
This feature moves: <which input, and how>.

| Type | Metric | Baseline | Floor | Read at |
|---|---|---|---|---|
| Primary | … | … | … | … |
| Supporting | … | … | … | … |
| Guardrail | … | … | must not fall below … | … |

**How it's measured:** <events or sources; note anything not yet instrumented.>

## 9 Delivery and release gates

| Phase | Contents | Gate to ship (pass/fail check) |
|---|---|---|
| Alpha | … | … |
| Beta | … | … |
| GA | … | … |

## 10 Risks, open questions and decisions

**Risks**
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| … | … | … | … |

**Open questions**
| # | Question | Owner | Needed by |
|---|---|---|---|
| Q1 | … | … | … |

**Decision log**
| # | Decision | Tradeoff accepted |
|---|---|---|
| D1 | … | … |

## 11 Prototype and agent handoff

**Prototype next:** <the riskiest assumption, the fidelity (clickable / working slice / Wizard of Oz), and the test signal>. Full prompt in `PROTOTYPE-PROMPT.md`.

**Build first:** <the thinnest vertical slice that proves the core loop end to end>
**Invariants:** <things that must stay true: data never lost, human approves every send, etc.>
**Don't assume:** <tempting shortcuts that are wrong here>
**Read:** <which sections each phase needs>

---

### Optional sections for a Full PRD
Add only the ones that carry real content:
- Research programme before full build (what to learn, how, by when)
- Business model and pricing hypothesis
- Technical architecture and data model
- Content, moderation or AI-evaluation design (for AI features: eval set, graders, failure taxonomy, human-review threshold)
- Go-to-market and launch plan
- Glossary
- Source bibliography
