# Content review: PBS website

Every line on the site was checked against what the business has actually published (the logo files and the Facebook-style ads in the `PBS` folder). Below: what changed, and what still needs the owner's confirmation.

## Changed

| Was | Now | Why |
|---|---|---|
| "Free consultation" (header button, process step 1) | "Book a consultation" | No source says it is free. The ads say "Contact us today for a consultation". A free-of-charge promise should only go live if the owner confirms it. |
| "Deadlines tracked, so you never face late filing penalties" | "Filing deadlines tracked on your behalf" | "Never" is a guarantee the firm cannot make. |
| "10+ years in practice" (several places) | "Est. 2015" / "Since 2015" | A year does not go stale and is easy to verify. |
| "For over a decade we've helped..." | "Established in 2015" | Same reason; avoids a claim that needs updating. |
| Generic one-line service blurbs | Real sub-services from the ads | The ads list exact scopes (Personal/Corporate Income Tax, Partnership & SME Tax, VAT, Tax Planning & Advisory; Company Registration, Statutory Records, Annual Returns, Board & Shareholder Documentation, Corporate Compliance Support). |
| Contact form opened only the email app | Sends via WhatsApp or email, with a pre-written message | Most Sri Lankan visitors do not have a desktop mail client set up; WhatsApp is how this firm already takes enquiries. |
| Dead social icons pointing to `#` | Hidden until a URL is set in `js/script.js` | Dead links look unfinished. |
| "Never a call centre" | "An office you can walk into, not just a phone number" | Says the same thing without the dig at others. |
| Static hours text only | Live "Open now / Closed, opens Mon 9:00 am" (Sri Lanka time) | Useful for a walk-in practice. |

Also added: Schema.org `AccountingService` data (address, phone, hours, services) for Google and AI answer engines, Open Graph tags, and descriptive alt text.

## Needs the owner to confirm

2. **"IRD notices & penalties" under Tax Services.** Inferred from one of the PBS ads about IRD notices and penalties. Remove if it is not a service they offer.
3. **"Explained in plain language, in Sinhala or English".** Based on their bilingual ads. Add Tamil if they serve Tamil-speaking clients.
5. **Office hours** (Mon–Fri 9–5, Sat 9–1) came from the owner during this project. Confirm they apply year-round.
6. **Phone lines.** 071 666 4111 is treated as the WhatsApp number. Confirm that, and that 070 167 9811 / 074 244 8951 / 036 226 0888 are all staffed.
7. **Social links (added).** Facebook (`/PBSolutionsSL`), YouTube channel and LinkedIn are live in `SOCIAL` at the top of `js/script.js`.
   - The LinkedIn link is a **personal profile** (Deepani Panambara), not a company page. If PBS has a LinkedIn company page, swap it in.
   - No TikTok URL was supplied, so its icon stays hidden until one is added.
7a. **Video reels (added).** Eight YouTube Shorts play inside the site (list in `REELS`, same file). Confirm each one is public, still wanted on the site, and has captions or a clear message. Reels are labelled "Reel 1" to "Reel 8" because I did not invent titles.
8. **Domain.** Rebuild with the real address (`SITE_URL=https://... python tools/build.py`) so canonical links, the sitemap, social previews and Schema.org `url` use it. Until then they point at the GitHub Pages address.

## Multi-page restructure (follows businessadvisor.lk)

New pages: Services overview, one page for each of the six services, About Us, Contact Us, Terms & Conditions, Privacy Policy. Home order: slider hero, stats strip, why us, services grid, tax band, reels, process, call-to-action. A top bar (phone, email, live open status, socials, WhatsApp), a Services dropdown, FAQs with Schema.org data and a sitemap were added.

Please check these before launch:

10. **Terms & Conditions and Privacy Policy.** I wrote them to describe what this site actually does (no accounts, contact form stores nothing, Google Fonts/Maps/YouTube embeds). They are sensible general text, **not legal advice**. Have the owner read them, ideally a lawyer, and add the legal company name once known.
13. **Slider headlines.** Slides 2 and 3 reuse the wording of the "Simplifying Tax & Business Compliance" and "Company Secretarial" ads. Slides 4 and 5 ("One team for your tax, payroll and filings", "Books and payroll, kept in order") are my wording; confirm or change them in `HERO` in `tools/build.py`.
15. **Dropped from the reference site because PBS has no equivalent:** Client Portal, external consultation booking site, event link, Request Details pop-up, the Spotify link.

## November 2026: services, numbers and search/AI visibility

21. **Services restructured to the owner's list.** The five categories the owner pasted (Taxation & Tax Consultancy; Financial Management & Accounting; Audit & Assurance; Business Advisory & Consultancy; Corporate Compliance & Regulatory Affairs) are now the main services, plus Payroll Management (from the ads), Web Development and Digital Marketing. "Accounting & Bookkeeping" and "Financial Consulting" merged into Financial Management & Accounting; "Business Consulting" became Business Advisory & Consultancy; "Company Secretarial" became part of Corporate Compliance. Page addresses changed accordingly.
22. **Audit & Assurance.** Taken from the owner's list. Confirm PBS is allowed to offer each item (for example, statutory audits in Sri Lanka must be signed by a qualified, registered auditor). The page claims only internal audits, financial statement reviews, help with audit queries and risk assessments, and does not claim statutory audits.
23. **Web Development and Digital Marketing are drafted from a one-line brief.** The owner asked for "web development" and "digital marketing (Facebook / LinkedIn / TikTok / Google profile)". The scope lists and FAQs were written by me. Confirm exactly what is offered, what is not, and whether prices or packages should be shown.
24. **Headline numbers** are shown exactly as supplied: 750+ business registrations, 1,500+ local clients, 200K+ social media engagements, 2,000+ consultations. Please confirm: (a) where each number comes from (records, social media analytics, etc.), (b) the "+" on "200K" (the owner wrote it without), (c) what "engagements" counts and over what period (the reference site said "monthly"; this site does not), and (d) a date. The note under the numbers reads "Figures supplied by Panambara Business Solutions, as of November 2026." and should be updated whenever the figures change.
25. **Definitions in the FAQs** (APIT = Advance Personal Income Tax, WHT = withholding tax, EPF/ETF, ROC = Registrar of Companies, internal audit, management accounts, investment appraisal) are general, plain-language definitions. They avoid rates, thresholds and deadlines. A tax professional at PBS should read them once.
26. **FAQs.** Every service page has seven to eight questions, and there is a site-wide `/faq/` page and a short FAQ on the home page. Answers are 30-50 words, answer first, and name the business. The structured data for each FAQ is generated from the same list as the visible text so they cannot disagree. Prices are never stated; the cost answer says fees are confirmed directly.
27. **"Last updated" dates** (14 November 2026) are real, set in `tools/content.py`. Change the date only when content genuinely changes. Do not bump it without a real edit.

28. **Reel captions.** Each reel now shows a topic label, an English title and the video's own Sinhala title (exactly as on YouTube). The English titles are my translations, so a Sinhala reader should confirm them: "Two dates every taxpayer must remember", "Why keep business and personal expenses separate?", "Do you know about withholding tax?", "How to make a simple financial plan for a business", "What happens if you miss the VAT deadline?", "Introduction to individual income tax", "Introduction to APIT", "Sole proprietorship or company?". The YouTube descriptions were mostly the brand line, a phone number and hashtags (two videos have none), so the titles are shown instead. The "+94 71 66 64111" number in some YouTube descriptions is written differently from the site's 071 666 4111; worth tidying on YouTube. Sinhala text is back on the site for these captions only (Noto Sans Sinhala).
29. **Video data for search engines.** Each reel has `VideoObject` data (title, upload date, length, thumbnail, link) so Google and AI tools can understand the videos. Dates come from YouTube.

## Photos (real team photos, added)

17. **Staff consent.** The photos show nine staff members. Confirm everyone shown is happy to appear on a public website.
18. **The sign photo** is cropped to the sign only, which leaves the framed certificates beside it out of the picture. The certificates show the company's registered name and a registration number, so check what the owner is comfortable publishing before ever using a wider crop.
19. **Legal company name.** The certificate beside the sign appears to read "Panambara Business Solutions (Pvt) Ltd". If that is right, add "(Pvt) Ltd" to the footer copyright and to the Terms and Privacy pages. I did not change the legal text without confirmation.
20. **Alt text** describes what the photos show without naming anyone. Add names only with each person's permission.

## Deliberately left out

- **Client testimonials and client-count statistics.** None were supplied; inventing them would be false. Add real ones (with permission) when available.
- **Specific tax deadlines, rates or thresholds.** They change; a wrong figure on a tax firm's site is worse than none.
- **Team names and bios.** Not supplied. The team photo is used unnamed in the hero, About and Why sections.
- **"Success Stories" testimonials section** from the reference site. There are no client quotes yet; add real ones with permission and a section can be built in minutes.

## Photo note

The hero photo is a candid and charming shot of the real team, which suits a small local firm. The ceiling damage and open boxes are visible only faintly under the overlay. A re-shoot is optional, not necessary.

## Sinhala

The site is English only, by the owner's decision, with one exception: the original Sinhala video titles shown under the reels (see item 28). All Sinhala marketing text and the Tharu lettering were removed. The other Sinhala wording left is the claim "Explained in plain language, in Sinhala or English" (about service language), which the owner should confirm or delete. Sinhala captions inside the YouTube reels belong to those videos.
