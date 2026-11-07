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
4. **"Bookkeeping, Financial statements"** chips and the Business/Financial Consulting descriptions. The ads name these services but do not describe them. Wording is conservative; adjust to what is really delivered.
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
11. **Service page wording.** Every service page uses only what the ads say, plus careful plain-language filler. These are my inference, so confirm or edit them: *"Records ready for filing"* (Accounting), *"Starting out / Structuring / Growing"* (Business Consulting), *"Understanding your numbers / Supporting decisions / Planning ahead"* (Financial Consulting). Consulting pages are thin on purpose until the owner supplies real detail.
12. **FAQ answers** (three per service) are deliberately safe and procedural. Check the answers about the IRD notice and about filing late; they promise help, not outcomes.
13. **Slider slides 2 and 3** reuse the wording of the "Simplifying Tax & Business Compliance" and "Company Secretarial" ads, including "Stay compliant. Stay organized."
14. **Stats strip** shows only checkable facts: years since 2015 (calculated each year), 6 services, 4 phone lines, Mon–Sat office. "Walk-ins welcome" is an assumption; remove it if appointments are required.
15. **Dropped from the reference site because PBS has no equivalent:** Client Portal, external consultation booking site, event link, Request Details pop-up, the Spotify link.

## Deliberately left out

- **Client testimonials and client-count statistics.** None were supplied; inventing them would be false. Add real ones (with permission) when available.
- **Specific tax deadlines, rates or thresholds.** They change; a wrong figure on a tax firm's site is worse than none.
- **Team names and bios.** Not supplied. The team photo is used unnamed in the hero, About and Why sections.
- **"Success Stories" testimonials section** from the reference site. There are no client quotes yet; add real ones with permission and a section can be built in minutes.

## Photo note

The hero photo is a candid and charming shot of the real team, which suits a small local firm. The ceiling damage and open boxes are visible only faintly under the overlay. A re-shoot is optional, not necessary.

## Sinhala

The site is English only, by the owner's decision. All Sinhala text and the Tharu lettering were removed. The only Sinhala wording left is the claim "Explained in plain language, in Sinhala or English" (about service language), which the owner should confirm or delete. Sinhala captions inside the YouTube reels belong to those videos.
