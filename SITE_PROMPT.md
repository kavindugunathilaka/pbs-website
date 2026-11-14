# Website build prompt: Panambara Business Solutions (PBS)

Build a premium multi-page site for a small Sri Lankan accounting and tax practice, structured like businessadvisor.lk but with its own identity. Plain HTML, CSS and vanilla JS; pages generated from one script so header and footer stay consistent.

## Business
- **Name:** Panambara Business Solutions (PBS), established 2015
- **Tagline:** Your Trusted Tax & Finance Partner
- **Address:** 240/A, Old Railway Street, Eheliyagoda, Sri Lanka
- **Phones:** 071 666 4111 (call + WhatsApp), 070 167 9811, 074 244 8951, 036 226 0888
- **Email:** info@panambara.lk
- **Hours:** Mon–Fri 9:00 am–5:00 pm, Sat 9:00 am–1:00 pm, Sun closed
- **Audience:** individuals, startups, SMEs, companies
- **Social:** Facebook (PBSolutionsSL), YouTube channel, LinkedIn; TikTok hidden until a URL exists

## Brand
- Logo: gold-to-green rising-bars mark and a "PBS" serif wordmark; circular badge on deep green over photos.
- Colour: forest green `#06231a` / `#0a3225`, gold `#c8a24a`, paper `#f6f2e7`, ink `#10201a`.
- Type: Plus Jakarta Sans (headings 700-800, body 400-500); clean and professional, no decorative serif. English only; no Sinhala text.
- Rules: curly quotes, en dashes, non-breaking spaces in phone numbers, tabular numerals, balanced headings, ≤ 60ch measure.

## Pages
`/` home · `/services/` · `/services/{accounting-bookkeeping, payroll-management, tax-services, company-secretarial, business-consulting, financial-consulting}/` · `/about-us/` · `/contact-us/` · `/terms-and-conditions/` · `/privacy-policy/` · `404.html` · `sitemap.xml` · `robots.txt`

## Global chrome
- **Top bar:** phone, email, live open/closed status, social icons, WhatsApp.
- **Glass pill header:** badge + name; Home · **Services ▾** (dropdown listing all six with a one-line description and "View all services") · Videos · About Us · Contact Us; phone; "Book a consultation". Mobile: circular-reveal menu with a Services accordion.
- **Footer (reference-style columns):** Panambara (Home, About Us, Contact Us, Terms & Conditions, Privacy Policy), Our services (six links), Visit & contact (address, phone, email, hours), socials, copyright.
- Floating WhatsApp button.

## Home, in order
1. **Hero slider (5 photo slides, 7s, pause button, swipe, reduced-motion safe):** every slide is a real team photo that fades into the green at the top, with a short two-line headline above the people and the glass dock under all slides. (1) "Your trusted / *Tax & Finance Partner.*" (2) "Simplifying / *Tax & Business Compliance.*" (3) "Professional / *Company Secretarial Services.*" (4) "One team for your / *tax, payroll and filings.*" (5) "Books and payroll, / *kept in order.*" Slides 2-5 end with a text link to the matching page. Desktop uses 16:9 photos; phones get a 3:2 crop with the copy below the photo.
2. **Stats strip:** "Trusted since 2015": years in practice (calculated), 6 services, 4 phone lines, Mon–Sat. Facts only.
3. **Why Panambara:** arch-framed team photo + four points (one team for everything, deadlines tracked, plain language, a real local office).
4. **"How can we help you?":** four service cards (Accounting & Bookkeeping, Tax, Company Secretarial, Payroll) with numbers, chips and "More details"; "Other services" row (Business Consulting, Financial Consulting).
5. **Tax band (dark):** "Tax return still pending? Don't leave it to the last minute." and a card (tax types, phone).
6. **PBS on video:** rail of 8 YouTube Shorts, tap to play in place, arrows and counter, Subscribe/Follow buttons.
7. **From first call to filed:** four steps.
8. **Call-to-action band.**
No testimonials until real quotes exist.

## Service pages
Dark page hero with breadcrumbs, lead, "Book a consultation" and call buttons. Then: who it's for (chips), what we handle (checked list), how it works (four steps), common questions (native `<details>`), sticky "Talk to us" card with other services, CTA band. Company Secretarial shows "Stay compliant. Stay organized." Each page has Service, FAQPage and BreadcrumbList JSON-LD.

## About / Contact / Legal
- **About:** team photo with caption, who we are, ticks, six-service grid, visit block.
- **Contact:** huge phone number, Call/WhatsApp/Email, address, other lines, hours with live status, socials, form that sends via WhatsApp or email (stores nothing), greyscale map.
- **Terms & Privacy:** plain-language text that matches what the site actually does; flagged for owner/legal review.

## Quality bar
- No invented testimonials, client counts, tax rates or deadlines.
- Accessible: skip link, focus rings, keyboard dropdown, ARIA on carousel/menu, form errors announced, reduced motion respected.
- SEO/AEO: unique titles and descriptions, canonical URLs, Open Graph, sitemap, robots, `AccountingService` + `Service` + `FAQPage` + `BreadcrumbList` JSON-LD.
