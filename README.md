# pm-skills

Skills for product managers who build with AI.

Works with **Claude** (Claude Code and Claude.ai), **Codex**, **Cursor** and **Grok Bot**. Each skill is a plain `SKILL.md` folder in the open [Agent Skills](https://agentskills.io) format, and each one is built from how I run product work.

## Who it's for

PMs who need to spin up a PRD for the product or feature they're working on now, and want to get from idea to a testable prototype quickly:

- **You have an idea, notes or a call transcript** and need a PRD your team can commit to.
- **You need answers before requirements**: is there product–market fit, what's the north star, what are the goals and non-goals, and what do we build first.
- **You want to prototype straight away** by handing the PRD to a coding agent.

**Use it with deep research.** `prd` is built to run after a research pass. Research gathers the market, competitor and user evidence; `prd` turns that evidence into decisions and labels every claim as sourced or assumed. Run the research with a deep-research skill or your agent's own research tool, or paste in research you already have.

## Skills

| Skill | What it does | Since |
|---|---|---|
| [`prd`](skills/prd/) | Works through a product problem (PMF hypothesis, north star, goals and non-goals, prioritisation), writes or reviews the PRD, then hands off a prototype prompt for a coding agent | 0.1.0 |

## Install

**Claude Code**

```
/plugin marketplace add subrro11/pm-skills
/plugin install pm-skills@pm-skills
```

**Codex and Cursor**

Both read skills from `~/.agents/skills/`. Clone once and link, so a `git pull` picks up new skills and updates:

```bash
git clone https://github.com/subrro11/pm-skills ~/pm-skills
mkdir -p ~/.agents/skills
ln -s ~/pm-skills/skills/prd ~/.agents/skills/prd
```

To install for a single project, link it into that repo's `.agents/skills/` instead. In Codex you can also ask `$skill-installer` to install `skills/prd` from `github.com/subrro11/pm-skills`. Restart the app if the skill doesn't appear.

**Grok Bot**

Add `skills/prd/SKILL.md` as a custom skill in Grok Bot, or attach the file and ask Grok to follow it. Grok Build reads skill folders from `~/.grok/skills/`: link `skills/prd` there as above.

**Claude.ai**

Zip the `skills/prd/` folder (keep the folder name `prd`) and upload it under Customize → Skills → Create skill → Upload a skill. Code execution must be on.

**Any other agent**

Point it at `skills/<name>/SKILL.md`.

## Use

Ask in plain words: *"Write a PRD for …"*, *"What should our north star be?"*, *"Prioritise this backlog"*, *"Review this PRD"*. In Codex you can also type `$prd`, and in Claude Code `/pm-skills:prd`.

## How `prd` works

```
Problem → Product thinking → PRD → Prototype with a coding agent → Test → Revise
```

- **It answers the product questions first**: the problem, a PMF hypothesis with a proving signal, a north star and its inputs, goals and non-goals, and RICE prioritisation with logged overrides. You can also ask any one of these on its own.
- **It writes the PRD from those answers.** The PRD leads with a recommendation, labels every number as sourced, assumed or fictional, splits scope into in scope, deferred and out of scope, and gives every P0 a testable acceptance criterion.
- **The next step is a prototype.** It writes `PROTOTYPE-PROMPT.md` for a coding agent (Claude Code, Codex, Cursor) to build the thinnest version of the core loop that tests the riskiest assumption. You test it with five users, then revise the PRD.

Details, prompts and files are in the [skill README](skills/prd/README.md). There's also a [worked example](skills/prd/examples/quiet-hours-lite.md) and its [prototype prompt](skills/prd/examples/quiet-hours-prototype-prompt.md).

## Changes

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT
