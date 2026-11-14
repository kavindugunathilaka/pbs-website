# Search, AI-answer and local visibility (SEO / AEO / GEO)

Goal: get Panambara Business Solutions (PBS) **found** on Google and Google Maps, and **named and linked** when people ask ChatGPT, Gemini, Perplexity, Copilot or Google AI Overviews for an accountant or tax consultant in Eheliyagoda. No one can promise a ranking or a citation. What follows is everything that improves the odds, split into what the website now does and what only the owner can do outside it.

Method: Voyage AEO/GEO skill (Princeton GEO study heuristics, treated as directional). PBS is a **challenger** (new site, small local brand), so the website uses the "aggressive" intensity: several quotable sentences per page, an FAQ on every service, visible dates.

---

## 1. Built into the website

| What | Where | Why it helps |
|---|---|---|
| 40-60 word overview directly under every main heading, naming the business, town and service | all service pages, FAQ, home | Short, self-contained sentences are what answer engines quote |
| "Last updated: 14 November 2026" (a real date) | service pages, FAQ, services, home numbers | Freshness signal. Do not bump it without a real change |
| 7-8 answer-first FAQs per service (30-50 words each), stable anchors `#faq-...` | 8 service pages | Matches how people ask; each answer stands alone and names the business |
| Site-wide FAQ page (12) and a 6-question FAQ on the home page | `/faq/`, home | One citable page covering location, hours, booking, cost, tax return, EPF/ETF, IRD, registration |
| Definitions of local terms: APIT, WHT, EPF, ETF, ROC, management accounts, investment appraisal | service FAQs | People search these exact terms |
| `AccountingService` (LocalBusiness) data: name, address, phone, hours, area served, services | every page | Local search and AI entity recognition |
| `WebSite`, `WebPage` (with `dateModified`), `Service`, `ItemList`, `FAQPage`, `BreadcrumbList` | per page type | Machine-readable structure; FAQ data is generated from the same list as the visible FAQ so they cannot drift |
| One H1 per page, unique title and description, canonical URL, `en-LK` hreflang | every page | Clean basics |
| Sitemap with real last-modified dates, `robots.txt`, `llms.txt` (plain summary of the business for AI tools) | site root | Crawl guidance and a one-page description AI tools can read |
| `VideoObject` data for each of the 8 reels (name, description, upload date, length, thumbnail, embed link), with the caption as visible text | home page | Lets Google and AI tools understand and cite the videos |
| Same name, address and phone everywhere on the site | header, footer, contact, data | Entity consistency |
| Descriptive alt text, fast WebP images, mobile layout | all pages | Page experience |

**Caveats to know:** Google only shows FAQ rich results for a small set of government and health sites, so do not expect FAQ snippets in Google. The FAQ data is still valuable for AI tools. Structured data and AI-citation effects take weeks to show.

---

## 2. What the owner must do outside the website (highest impact)

On-page work alone is rarely enough. AI engines and Google trust what **other sources** say about the business.

1. **Google Business Profile (most important for local).** Create or claim it, category "Accountant" or "Tax consultant" (plus "Business consultant"), and enter the name **exactly** as "Panambara Business Solutions", address "240/A, Old Railway Street, Eheliyagoda", phone 071 666 4111, hours Mon-Fri 9-5 and Sat 9-1, the website address, services, and real photos. Then send me the profile link so I add it to the website's `sameAs` and map link.
2. **Real reviews.** Ask satisfied clients (with their permission) to leave Google reviews. Reply to every review.
3. **Make every profile say the same thing.** Same business name, address, phone and a one-line description on Facebook, YouTube, LinkedIn and TikTok. Put the website address in each bio.
4. **A LinkedIn *company* page.** The link currently on the site is a personal profile.
5. **Own domain.** Host the site on the business domain (the email already uses `panambara.lk`). I rebuild with `SITE_URL=https://www.panambara.lk python tools/build.py` so canonical links, sitemap and social previews use it.
6. **Google Search Console and Bing Webmaster Tools.** Verify the domain and submit `/sitemap.xml`. Also claim **Bing Places** (feeds Copilot/ChatGPT search) and **Apple Business Connect**.
7. **Third-party mentions.** Get listed in local business directories, any professional body PBS belongs to, and local news or community pages. Consistent name, address and phone on each.
8. **Named experts and credentials.** AI engines cite pages with a named person and credential. Send the name, role and qualifications of the people who lead tax, audit and company secretarial work (with permission) and I add short bios and author lines.
9. **Evidence for the headline numbers.** For each number on the home page fill in the table below, then I add a short "how we count this" panel.

| Number shown | What exactly is counted | Source (records / analytics) | Date collected | Limits |
|---|---|---|---|---|
| 750+ business registrations | | | | |
| 1,500+ local clients | | | | |
| 200K+ social media engagements | | | | |
| 2,000+ consultations | | | | |

---

## 3. Details needed for Web Development and Digital Marketing

Both pages were **drafted from a one-line brief**. To make them accurate and persuasive, send:

**For both**
- Exactly what is and is not included in each service (scope), and any packages or "starting from" prices in LKR if you want prices shown.
- Typical timeline, how work is delivered and how clients pay.
- 2-3 real examples (client name only with permission): a website built, a profile managed.
- Who does the work (names, roles) and any tools or platforms used.

**Web development specifically**
- Types of site you build (company site, online shop, booking site, landing pages).
- Whether hosting, domain and maintenance are included, and any support period after launch.

**Digital marketing specifically**
- Which channels you manage: Facebook page, LinkedIn page, TikTok, Google Business Profile, anything else (YouTube, Instagram).
- What a client must give you: page access, logo and brand files, photos, business details, approval process.
- What you deliver each month: number of posts, reports, replies to messages and reviews, paid ads or not.

**For the business's own profiles (needed for local search)**
- Links to: Google Business Profile, Facebook page (have), LinkedIn **company** page, TikTok profile, YouTube channel (have).
- Logo files, brand colours, a 50-word and a 150-word description, the service list, and hours (have).

---

## 4. Citation test (run before launch and again 4-8 weeks later)

Run the same prompts in ChatGPT (with search on), Gemini, Perplexity, Microsoft Copilot and Google AI Overviews / AI Mode, from Sri Lanka if possible. AI answers vary, so run each prompt **three times** and record the majority result.

| # | Prompt | Type |
|---|---|---|
| 1 | What is Panambara Business Solutions? | Recognition |
| 2 | Best accounting and tax firm in Eheliyagoda | Category |
| 3 | Tax consultant near Eheliyagoda, Sri Lanka | Category (local) |
| 4 | Who can help me register a company in Sri Lanka? | How-to |
| 5 | What is APIT in Sri Lanka? | Definition |
| 6 | How do I handle EPF and ETF for my employees? | How-to |
| 7 | Web development and digital marketing company in Eheliyagoda | Category |
| 8 | Panambara Business Solutions vs <a competitor the owner names> | Comparison |

Log for each engine: **mentioned? linked? accurate? which source was cited?** Keep dated results in a table so changes can be compared.

| Date | Engine | Prompt # | Mentioned | Linked | Accurate | Source cited | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## 5. Keeping it healthy

- Change the "last updated" date (`CONTENT_UPDATED` in `tools/content.py`) **only** when content really changes, then run `python tools/build.py`.
- Add a short real update at least every quarter (new FAQ from a client question, a new service detail, new numbers).
- Keep the business name, address and phone **identical** on the website, Google profile and every social page.
- Never publish an unverified statistic; add a source and a date to any new number.
- Check structured data with Google's Rich Results Test and the Schema.org validator after each major change.
