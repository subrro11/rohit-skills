# Research plan

Write the decision and the subject at the top. Then plan the stages in order. For each one, ask: *could an answer here change the decision?* If not, skip it. Seven questions at most across all stages; if you need more, the decision is too broad, so split it.

## Questions by stage

| Stage | Good questions | Weak questions |
|---|---|---|
| **1. Company** | What does it sell, to whom, at what price? How does it make money? How big is it (revenue, customers, headcount), and as of when? What does it say its strategy is? | "What is the company about?" |
| **1. Problem** (idea mode) | Who has the problem, and how often? What do they do today instead? What does that cost them, in time, money or risk? How many people match, by what definition, in what year? | "Do people have this problem?" (always yes) |
| **2. Competitors** | Who does the same job for the same buyer? Who could stretch to do it? What do they charge, and what traction do they show? What's the do-nothing workaround? | "Are there competitors?" (always yes) |
| **3. News** | What has the company, or a rival, launched, priced, raised, bought, cut or been sued over in the last 12 months? | "Any news?" with no window and no subject |
| **4. Trends** | Which shifts in behaviour, technology, regulation or economics will change this market in 2–3 years, and in which direction? | Trends with no link to the decision |
| **Contrarian** (at least one) | Who has tried this and failed, and why? What's the strongest case against it working? | Skipping it because the answer might be unwelcome |
| **5. Frameworks** | Which one to three frameworks answer the decision best, given the evidence? See `frameworks.md`. | Running every framework "to be thorough" |

## Search patterns

Run 3–5 phrasings per question. Mix these:

- **Plain**: the question as a person would type it.
- **Primary source**: name the publisher you expect ("site:gov", "systematic review", "annual report", "10-K", "pricing", "changelog", "app store").
- **Practitioner**: the words users use, plus "forum", "reviews", "how do you", "alternative to".
- **Competitor**: "<company> alternatives", "<company> vs", "<category> tools", "switched from <company>".
- **News**: "<company> launches", "<company> raises", "<company> acquires", "<company> layoffs", "<company> pricing change", each with the current or previous year.
- **Trends**: "<category> market report <year>", "<category> adoption survey", "<regulation> <category>", "state of <category>".
- **Disconfirming**: "<claim> myth", "<competitor> shut down", "<segment> don't use", "<approach> failed", "why <category> startups fail".
- **Own words**: "<company> CEO interview", "<company> earnings call", "<company> careers", "<company> changelog".
- **User voice**: "<product> reviews", "<product> reddit", "<product> vs", "cancelled <product>".

## Source ladder

Prefer the highest rung that answers the question. Climb down only when the rung above has nothing.

1. **Primary and official**: the company's own site, pricing, docs, help centre, dated changelog entries, filings and press releases; structured data such as app store listings and code-repository or package-registry APIs; government agencies and statistics offices; regulators and standards bodies; peer-reviewed papers and systematic reviews.
2. **Reputable secondary**: established news and trade press, university extension services, professional bodies, analyst reports with a stated method.
3. **Practitioner signal**: forums, reviews, community threads, job posts. Strong for what people do and say, and for what a company is hiring for; weak for how many.
4. **Everything else**: content marketing, listicles, AI-written summaries, undated pages. Use only as a lead to a better source.

For **news**, a company's own press release is primary for *what it announced*; independent press is better for *what happened next*. See `verification.md` for sources that look reliable and aren't.

## When a source won't load

Paywalls, bot checks and 403s happen. Don't cite the page from its snippet. Instead:

1. Look for the same claim on an equal or higher rung that does load: the company's help centre or docs subdomain, a filings archive, a structured API, or the PDF saved and opened as a file.
2. If nothing loads, log it under *Found, not read* with what it was expected to show, and add an "Evidence needed:" line.

## Stopping rule

Stop a stage when one of these is true:

- Two independent sources on rung 1–2 agree, and a disconfirming search found nothing that changes the answer.
- Two more searches return nothing new.
- The answer would no longer change the decision.
