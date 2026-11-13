# Research: meal re-planning for nurses on rotating shifts

> Real run, fictional product. Shiftplate is the made-up product from the [PRD Generator showcase](../../../prd-generator/examples/shiftplate/). The sources below are real, and every one in the ledger was opened and read during the run. Pages that wouldn't load are listed under *Found, not read* and aren't cited.

**Decision:** Should Shiftplate's 20-nurse pilot go ahead as scoped, and what should its use-by default be?
**Subject:** idea: a meal-planning app that rebuilds a nurse's week around food already prepped when their rota changes.
2026-11-13 · Every claim cites a ledger ID, or is marked *inference* or *user-supplied*.

## Answer

Go ahead with the pilot, but change two things. First, set the use-by default to **3 days**, not 4: guidance restating USDA advice says to use refrigerated leftovers within 3–4 days (E5), so 4 is the upper limit, not a safe default. Second, keep night-shift meal timing out of v1 on purpose, because that's where the new shift-worker apps lead (E9, E10, E11). Reuse-first re-planning is the open position on the map, but that rests on store listings, not hands-on testing. The segment is real but the size is dated: nearly a quarter of US RNs rotated shifts in 2006 (E1).

**What would change this:** a competitor that already plans around food already prepped, or a current figure showing rotating shifts are now rare among RNs.

## Problem

**Confidence:** Medium for segment size and food safety; Low for eating patterns

- **Who and how many:** nearly a quarter of a 2,273-RN US sample rotated shifts in 2006 (E1), and more than a quarter worked 12+ hour days (E2). One study, 20 years old.
- **What they eat, and when:** a 2019 review reports more snacking, a later last meal, eating at night and irregular meals among night-shift nurses (E3), but says the evidence is limited by how few studies exist (E4). This supports the "4am crash" from the founder's interviews (*user-supplied*) as a theme, not as a measured cost.
- **What waste costs:** the average US household wastes 31.9% of the food it acquires (E8). USDA ERS estimated 31% of the US food supply was lost at retail and consumer level in 2010 (E7). Neither source covers shift workers.
- **Constraint (food safety):** use refrigerated leftovers within 3–4 days, frozen within 3–4 months, and reheat to 165°F (E5, E6). The primary USDA and FoodSafety.gov pages returned 403 and weren't read. *Inference:* a 3-day default with a per-dish override stays inside the window for everything the source covers.

## Competitors

**Confidence:** Low. All three are new with few ratings, and this is based on their store pages only. General meal planners came up in search but weren't opened.

| Name | What it does | Who it's for | Price | Traction signal | Source |
|---|---|---|---|---|---|
| Shift Fuel | Meal timing for rotating shift work; Pro adds planning and reminders | Rotating shift workers | Free; Pro $2.99/mo or $14.99/yr | Not enough ratings to show | E9 |
| NightFast | Stops late-night snacking | Shift workers | Free; Pro $4.99/mo, $29.99/yr or $59.99 lifetime | 4.3 from 6 ratings | E10 |
| ShiftWell | Health and lifestyle tracking for variable hours | Shift workers, including nurses | 14-day trial, then £7.99/mo or £59.99/yr | Listed and reviewed by a health directory, July 2026 | E11 |
| Do nothing | Sunday prep; when the rota flips, the prep gets binned and nurses buy vending or takeout | Founder's six interviewees | ~$60/wk (*assumed* in the PRD) | n/a | *user-supplied* |

## News

**Window:** last 12 months · **Confidence:** Low

No dated news about these competitors was read in this run. Store listings show recent version updates, but without the year, so they aren't reported as news. See Evidence needed.

## Trends

**Confidence:** Low

| Trend | Direction | Evidence | What it means for the decision |
|---|---|---|---|
| Apps built for shift workers' eating are appearing, and they lead with timing, snacking or tracking | New entrants | E9, E10, E11 (signal: store and directory listings, not market data) | Timing is becoming crowded. Reuse is still an open angle, but the window may be short |
| Night-shift nutrition is an open research question | Slow | E3, E4 (one review) | Don't promise health outcomes in v1; measure behaviour instead |

## Frameworks

### Positioning map

Axes: **what the app leads with** (meal timing ↔ using food already prepped) and **who it's built for** (anyone ↔ shift workers).

| | Built for anyone | Built for shift workers |
|---|---|---|
| **Leads with timing or habits** | | Shift Fuel (E9), NightFast (E10), ShiftWell (E11) |
| **Leads with food already prepped** | General meal planners: not read, Evidence needed | **Empty: Shiftplate's proposed position** (*inference*) |

The empty cell could be open because nobody has tried it, or because nobody wants it. The pilot's PMF signal is the test. The buyer evidence for the "leads with" axis is the founder's six interviews (*user-supplied*), so it needs checking in the pilot too.

### Jobs to be done

"When my rota flips between days and nights, I want my prepped food to still fit my week, so I can stop binning it and buying vending food at 3am." (*user-supplied*, from the founder's interviews, consistent with the irregular meals reported in E3)
Hired today: doing nothing (*user-supplied*), timing apps (E9, E10). None of the listings describe this job.

## What the research contradicts

- The PRD's 4-day use-by default is safe → the guidance gives 3–4 days, so 4 is the limit and 3 is the safer default (E5).
- There's no "why now" → new shift-worker eating apps (E9, E10, E11) give a weak one: timing is getting crowded, and reuse isn't taken yet.
- The 4am crash is the worst cost (*user-supplied*) → the published evidence on night-shift eating is too thin to confirm or rank it (E4).

## Evidence needed

- **Current share of RNs on rotating shifts**: get a recent national figure (for example, a BLS or national nursing workforce survey) to replace the 2006 number.
- **Primary food-safety chart**: read the FoodSafety.gov cold storage chart directly and confirm the window for each food type Shiftplate allows.
- **Whether general meal planners handle leftovers**: open the leading meal-planning apps and test whether any plan around food already prepped. This fills the empty cell on the positioning map.
- **Hands-on competitor check**: install Shift Fuel and test whether its weekly planner reuses logged food.
- **Competitor news**: search each competitor's site and the press for launches, funding and pricing changes in the last 12 months.
- **Night-shift eating cost**: the review (E4) says studies are few. Measure it in the pilot rather than citing it.
- **Contrarian pass, not run**: search for shift-worker or nurse meal-planning products that launched and shut down, and why. This run didn't ask, so the case against is untested.
- **Pressure test on the empty cell, not run**: search for why no one leads with food already prepped for shift workers, and whether any meal planner tried it.

## Feeds the PRD

| PRD section | Use this | IDs |
|---|---|---|
| Problem | Irregular meals, night eating and snacking are reported among night-shift nurses, but the evidence is thin | E3, E4 |
| Why now | New shift-worker eating apps are appearing, all leading with timing. Still weak as a "why now" | E9, E10, E11 |
| PMF hypothesis | Segment size: nearly a quarter of RNs rotated shifts (2006) | E1 |
| Metrics (baselines) | The 31.9% household waste figure gives context for the waste goal; measure the pilot's own week 1 | E7, E8 |
| Scope and defaults | Use-by default of 3 days (inside 3–4 days); 165°F reheat guidance in gap-meal instructions | E5, E6 |
| Risks | Timing apps could add reuse to their weekly planners; night-shift timing is crowded, so keep it deferred | E9, E10, E11 |

## Evidence ledger

**Verification:** 11 claims checked against their pages · 0 corrected · 1 lead dropped because its ID matched a different paper · 4 leads moved to *Found, not read*

| ID | Stage | Claim | Source | Quote | Confidence |
|---|---|---|---|---|---|
| E1 | Problem | Nearly a quarter of a 2,273-RN US sample rotated shifts (2006) | Trinkoff et al., "How long and how much are nurses now working?", *American Journal of Nursing* 106(4), April 2006, via the Europe PMC abstract ([record](https://europepmc.org/article/MED/16575241)). Read 2026-11-13 | "Nearly a quarter rotated shifts." | Medium: peer-reviewed, but one study and 20 years old |
| E2 | Problem | More than a quarter of the same sample typically worked 12+ hours a day | Same as E1 | "More than a quarter of the sample reported that they typically worked 12 or more hours per day" | Medium: same as E1 |
| E3 | Problem | Some studies report more snacking, a later last meal, night eating and irregular meals among night-shift nurses | Pepłońska, Nowak and Trafalska, "The association between night shift work and nutrition patterns among nurses: a literature review", *Medycyna Pracy* 70(3), May 2019 ([link](https://medpr.imp.lodz.pl/Association-between-night-shift-work-and-nutrition-pattern-among-nurses-literature,99931,0,2.html)). Read 2026-11-13 | "more frequent snacks consumption, later time of the last meal, eating at night, meals irregularity" | Low: the review says few studies found this |
| E4 | Problem | The evidence base on night-shift nurses' nutrition is small | Same as E3 | "the topic warrants further attention, owing to the relatively small number of the studies performed so far" | High: the source's own judgement of its evidence |
| E5 | Problem | Use refrigerated leftovers within 3–4 days, or within 3–4 months if frozen | Illinois Extension, "Leftovers", University of Illinois, undated ([link](https://extension.illinois.edu/food-safety/leftovers)). Read 2026-11-13 | "Use refrigerated leftover food within 3-4 days, or within 3 to 4 months if they were frozen." | Medium: reputable secondary, undated, primary USDA page not read |
| E6 | Problem | Reheat leftovers to at least 165°F | Same as E5 | "reheat to a minimum of 165 F, the safe temperature needed to kill harmful bacteria" | Medium: same as E5 |
| E7 | Problem | 31% (133 billion lb) of the 430 billion lb US food supply was lost at retail and consumer level in 2010 | Buzby, Wells and Bentley, "ERS's Food Loss Data Help Inform the Food Waste Discussion", USDA ERS *Amber Waves*, June 2013 ([link](https://www.ers.usda.gov/amber-waves/2013/june/ers-food-loss-data-help-inform-the-food-waste-discussion)). Read 2026-11-13 | "at the retail and consumer levels, an estimated 133 billion pounds, or 31 percent" | Medium: primary agency estimate, but 2010 data, and retail and consumer are combined |
| E8 | Problem | The average US household wastes 31.9% of the food it acquires | Penn State news, "Study suggests U.S. households waste nearly a third of the food they acquire", January 2020, reporting a study in the *American Journal of Agricultural Economics* ([link](https://www.psu.edu/news/research/story/study-suggests-us-households-waste-nearly-third-food-they-acquire)). Read 2026-11-13 | "the average American household wastes 31.9% of the food it acquires" | Medium: university press release; the paper itself wasn't read |
| E9 | Competitors | Shift Fuel is a meal-timing app for rotating shift workers, with paid Pro tiers and too few ratings to display | Apple App Store listing, Monarch Labs Collective ([link](https://apps.apple.com/app/id6772874868)). Read 2026-11-13 | "Shift Fuel is the meal-timing app built for rotating shift workers." | High for what it claims to do; Low for traction |
| E10 | Competitors | NightFast targets late-night snacking, rated 4.3 from 6 ratings | Apple App Store listing, NightFast ([link](https://apps.apple.com/us/app/nightfast/id6757072489)). Read 2026-11-13 | "NightFast helps you stop late-night snacking, without willpower speeches." | High for what it claims to do; Low for traction |
| E11 | Competitors | ShiftWell is a health and lifestyle tracking app for people on variable hours or shifts | Healthify app directory, updated 15 July 2026 ([link](https://healthify.nz/apps/s/shiftwell-app)). Read 2026-11-13 | "designed specifically for people working variable hours or shifts" | Medium: an independent directory description, not hands-on |

### Found, not read

| Source | Expected to show | Why not read |
|---|---|---|
| FoodSafety.gov, Cold Food Storage Charts | Fridge times per food type | 403 |
| USDA FSIS, "Leftovers and Food Safety" | 3–4 days; 165°F | 403 |
| Mayo Clinic, leftovers FAQ | 3–4 days, and which source it cites | 403 |
| Phoi and Keogh (2019), *Nutrients*, dietary interventions for night shift workers | Whether meal-timing changes have been tested | Bot check on PubMed Central |
| General meal-planning apps (from search results) | Whether they plan around leftovers | Out of time; listed as Evidence needed |
