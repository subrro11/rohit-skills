# Prototype handoff: from PRD to a coding agent

The PRD's job ends when the riskiest assumption can be tested. The fastest test is usually a prototype built by a coding agent in an afternoon, put in front of five real users. This file is the template for `PROTOTYPE-PROMPT.md`.

## Choose what to prototype

1. Take the PMF hypothesis and find the assumption that would kill the idea if it were wrong.
2. Find the smallest slice of the P0 core loop that lets a user experience that assumption.
3. Everything else gets faked: hard-coded data, no auth, no real backend, one happy path plus the one failure state that matters.

The prompt goes to a coding agent, so keep it clean: no real customer data, API keys, passwords, internal URLs or confidential names. Use invented data that looks realistic.

| Fidelity | Use when | Agent builds |
|---|---|---|
| Clickable | Testing comprehension or desirability | Static pages with fake data and working navigation |
| Working slice | Testing whether the core loop delivers value | A real core interaction with local storage, everything else stubbed |
| Wizard of Oz | Testing value before the hard part (often the AI) exists | A real UI where a human or a fixed script produces the "smart" output |

## Template

```markdown
# Prototype: <name>

## What we're testing
<One sentence: the riskiest assumption, taken from the PRD's PMF hypothesis.>
Success looks like: <the observable signal in a 5-user test, e.g. "4 of 5 complete the task unaided and say they'd use it this week">.

## Build
A <clickable / working slice / Wizard of Oz> prototype of <the core loop in one line>.

Screens or steps:
1. <step>: what the user sees and does
2. ...

Include exactly these states: <happy path>, <the one failure state that matters>, <empty state if it's the first thing a user sees>.

## Fake on purpose
- Data: <invented fixture data; describe it or attach JSON. Never real customer data>
- Auth, payments, settings, admin: not built
- <anything else from the PRD that's P0 but not under test>

## Constraints
- Stack: <whatever runs fastest locally; e.g. a single Vite + React app, or one HTML file>
- Runs with one command, and needs no accounts or API keys unless the test requires them
- Mobile width works if users will test on phones
- Copy taken from the PRD; no lorem ipsum on screens under test

## Don't
- Don't build anything listed under "Fake on purpose"
- Don't add features beyond the steps above, even small ones
- <PRD invariants that still apply, e.g. "never send a message without the user confirming">

## Done when
- [ ] `<command>` starts it locally
- [ ] Every step above can be clicked through end to end
- [ ] The failure state can be triggered on demand (a button or URL flag)
- [ ] A short README says how to run it and what's fake

## Source
PRD: <path>, sections <list>. Requirements in scope: <IDs>.
```

## After the test

- Record results against the success signal as numbers.
- Revise the PRD: update the evidence, re-score priorities, move or kill requirements, bump the version and add changelog lines.
- Decide one of: **build** (move to the Standard PRD and the real first vertical slice), **iterate** (another prototype on the next riskiest assumption), or **stop**.
