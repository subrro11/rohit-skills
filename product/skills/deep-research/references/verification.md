# Verification

Run this pass after the stages and before writing the answer. Its job is to refute, not to add. Research errors are rarely invented from nothing. They're real material bent slightly out of shape, so they survive a casual read.

## The pass

1. **List the load-bearing claims**: the numbers, dates, names, quotes and absence claims the answer depends on, plus anything a reader would repeat out loud in a meeting.
2. **Order them by stakes, then by doubt.** The claim the decision rests on goes first, then the ones you're least sure of. Errors cluster in the first few items, so this order finds them fastest.
3. **Re-open the source for each one** and check it says exactly that. Fix the claim, downgrade it, or cut it.
4. **Upgrade as well as cut.** Weak claims are often one search away from a primary source. If you find it, raise the grade.
5. **Log what changed** in one line at the top of the evidence ledger: how many claims were checked, corrected, downgraded and upgraded.

Ideally a second agent runs this pass, briefed only with the report and the list. If one agent does both, re-open every source rather than relying on what you remember.

## Quotes

- **Quotation marks only for text you read this session and can reproduce exactly.** Anything else is reported speech, with no marks, attributed to the outlet that reported it.
- **Never change a character inside quotation marks**, even to fix house style. If the quote doesn't fit, end it early or paraphrase it.
- **Check the quote against its context.** Read the sentences around it. A verbatim quote used to make a point its paragraph doesn't make is still wrong, and it's harder to catch because the words check out.
- **Check the speaker.** Reporters' narration around an interview isn't the interviewee's claim, and a line from a news article isn't a line from the company's blog.
- **Check the first word.** Summarising tools swap pronouns for names, so a quote that opens with a name may not be verbatim.

## Numbers

- **Check what the number measures.** When a company has two related products, a headline figure often belongs to the other one.
- **Use the stated number over a derived one.** If a filing gives the figure, don't back-calculate it from a rounded percentage.
- **Keep the period.** Year-end figures quoted in the present tense, or two numbers from different quarters set side by side, quietly change the claim.
- **Recount lists.** "12 agents" on the page and "11" in the report is a common, avoidable error.

## Absence

- **Silence isn't exclusion.** A source that doesn't mention X has said nothing about X.
- **An absence claim names its search.** "Doesn't offer X" is usable only if the report says which pages were checked. Check the vendor's own changelog, docs and help centre before saying something doesn't exist.
- **"First" is an absence claim** about every competitor, so it needs the same check.
- **A broken guessed URL isn't absence.** Find the real page.

## Status and dates

- **Separate shipped, announced, in beta, claimed in marketing, and inferred.** Mark which one each competitor capability is.
- **Event date isn't publication date.** A recap published a month after a launch doesn't date the launch, and a page's "last updated" date isn't when it was published.
- **Check the first launch.** A product relaunched this year may have existed for years.
- **Don't log future-dated items as fact.**

## Sources that mislead

| Source | Treat it as |
|---|---|
| Search snippets and AI search summaries | A lead for the next query. They invent events, merge years and attach numbers to the wrong item. A number that appears only there gets cut |
| Reprints and syndication | One source, not two. Check the byline and timestamp before counting outlets as independent |
| Aggregator company profiles and pricing trackers | Unconfirmed until the company's own page says the same thing |
| Paid wire releases and company blogs | What the company said, not what happened |
| Competitor content marketing ("why people are leaving X") | Interested testimony. Flag the publisher's interest |
| AI-generated event transcripts | A lead for substance, never the source of a quote |
| Share prices, analyst targets, and press on why a stock moved | Investor sentiment, not evidence about the product or users |
| Law-firm class action notices | Advertising for allegations, not findings |
| Content farms and listicles | A lead at most. A product name that appears only there is probably out of date |

## Sources that tend to work

- The company's own pricing page, help centre and docs. Billing rules and limits often live in the help centre, not on marketing pages.
- Dated release notes and changelog entries. Open the dated entry, not the index.
- Official filings and investor letters, and earnings-call transcripts from established publishers.
- Structured endpoints that return data instead of prose: code-hosting and package-registry APIs for release dates, app store listings for versions and in-app purchases, forum and community APIs for exact timestamps, and public job-board APIs for postings.
- PDFs saved and opened as files, rather than summarised by a web tool.
- Court records read as the filed documents, not as press summaries.
