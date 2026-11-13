# Deep Research

Research a company or a product idea and get a cited report you can make a decision on. It covers the company, its competitors, recent news and market trends, then applies the right strategy frameworks to the evidence.

Every claim traces back to a source the agent actually read, with a quote and a confidence grade. Anything it couldn't settle becomes an "Evidence needed:" line instead of a guess.

**Who it's for:** PMs, founders and strategists who need evidence before they commit to a PRD, a pitch, a positioning call or a meeting with a company, or who just need to check one claim quickly.

## Try it

```
Research the market for <product>, <what it does> for <who>. The decision is <what you're deciding>.
```

Other prompts:

- *"Research <company> before my meeting with them"*
- *"Who already does <job>? Build a competitor table"*
- *"What's changed for <company> in the last year?"*
- *"Run five forces on <market>"*, or *"Draw a positioning map for <category>"*
- *"Is it true that <claim>?"* gives a quick check, answered in chat with sources
- *"Fill the Evidence needed lines in this PRD"* researches only the gaps

You can also call it directly: `/product:deep-research` in Claude Code, `$deep-research` in Codex.

## How it works

```
Decision ─▶ Company ─▶ Competitors ─▶ News ─▶ Trends ─▶ Frameworks ─▶ Verify ─▶ Report ─▶ PRD
```

| Stage | What it finds | What makes it trustworthy |
|---|---|---|
| **Decision** | What you'll do differently depending on the answer | Sets the stopping rule, so research ends when the decision is settled |
| **Company** (or **Problem** for an idea) | What it sells, to whom, how it makes money, how big it is | The company's own pages and filings first |
| **Competitors** | Direct rivals, adjacent tools and the do-nothing workaround, with price and traction | Each rival is marked sourced or *inference* |
| **News** | Launches, pricing, funding, acquisitions, layoffs and lawsuits in a stated window | Every item is dated and was read, not taken from a headline |
| **Trends** | Shifts in behaviour, technology, regulation and economics, with their direction | Two independent sources, or it's labelled a signal |
| **Frameworks** | Jobs to be done, positioning map, five forces, PESTLE, business model, moats, competitor gap table, then a pressure test on the biggest gap | Every cell cites evidence; empty cells become Evidence needed |
| **Verify** | An adversarial pass on the claims the answer depends on | Quotes checked against their context, numbers against what they measure, absence claims against the pages searched |

At every stage it searches wide, opens the best few sources, and asks at least one contrarian question: who tried this and failed, and what's the case against it.

## What you get

A `RESEARCH.md` with:

- **The answer first.** What the evidence means for your decision, what it would do, and what would change its mind.
- **One section per stage**, each with a confidence grade.
- **What the research contradicts.** Each assumption in the brief that the evidence doesn't support, and what it found instead.
- **Evidence needed.** Every open question, with what would settle it.
- **Feeds the PRD.** Each finding mapped to a PRD section, ready for the [PRD Generator](../prd-generator/).
- **An evidence ledger.** Every claim with its source, date, a verbatim quote and a grade, plus a *Found, not read* list for pages that wouldn't load. Those are never cited.

## See it work

[Shiftplate research](examples/shiftplate/) is a real run on a fictional product's real market. It changes a default in the product's PRD, comes back empty on news and says so, and finds an empty cell on the positioning map.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `deep-research`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install product@rohit-skills` (installs every product skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/deep-research` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `deep-research`, and upload it under Customize → Skills.

It needs an agent with web search and page reading. Without them, it can still structure research you paste in and grade it.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/research-plan.md`](references/research-plan.md) | Questions per stage, search patterns, the source ladder, stopping rules |
| [`references/frameworks.md`](references/frameworks.md) | Which framework fits which decision, and how to fill each one with evidence |
| [`references/verification.md`](references/verification.md) | The verify pass, quote and number traps, and sources that look reliable and aren't |
| [`references/evidence-ledger.md`](references/evidence-ledger.md) | Ledger format and confidence grades |
| [`references/report-template.md`](references/report-template.md) | The report structure |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 26 checks to run before handover |
| [`examples/shiftplate/`](examples/shiftplate/) | A real research run on a fictional product's market |
