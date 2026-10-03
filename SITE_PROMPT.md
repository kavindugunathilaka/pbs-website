# Website build prompt: Panambara Business Solutions (PBS)

Build a premium single-page site for a small Sri Lankan accounting and tax practice. It should feel bespoke and editorial, not like a template. Plain HTML, CSS and vanilla JS; no frameworks.

## Business
- **Name:** Panambara Business Solutions (PBS), established 2015
- **Tagline:** Your Trusted Tax & Finance Partner. Sinhala: ඔබගේ විශ්වසනීය ගිණුම්කරණ සහකරුවා
- **Address:** 240/A, Old Railway Street, Eheliyagoda, Sri Lanka
- **Phones:** 071 666 4111 (call + WhatsApp), 070 167 9811, 074 244 8951, 036 226 0888
- **Email:** info@panambara.lk
- **Hours:** Mon–Fri 9:00 am–5:00 pm, Sat 9:00 am–1:00 pm, Sun closed
- **Audience:** individuals, startups, SMEs, companies

## Brand
- Logo: gold-to-green rising-bars mark and a "PBS" serif wordmark; circular badge on deep green for use over photos.
- Colour: forest green `#06231a` / `#0a3225`, gold `#c8a24a` (gradient `#b88f33 → #f0d98f → #a98225`), paper `#f6f2e7`, ink `#10201a`.
- Type: Bodoni Moda (display, echoes the wordmark's high-contrast lettering), Instrument Sans (body/UI), Noto Sans Sinhala (no letter-spacing, line-height ~1.85).
- Typography rules: curly quotes, en dashes for ranges, non-breaking spaces in phone numbers, tabular numerals, balanced headings, ≤ 60ch measure.

## Structure and copy
1. **Floating glass pill nav:** badge + "Panambara / Business Solutions"; links Services, About, Process, Contact; phone; "Book a consultation". Mobile: circular-reveal full-screen menu with large serif links.
2. **Hero (full-bleed team photo, dark green scrim):** eyebrow "Panambara Business Solutions • Est. 2015"; headline "Your trusted / *Tax & Finance Partner.*" (light roman line, gold italic line); Sinhala tagline; glass dock with Call or WhatsApp number, address, live open/closed status, buttons "Book a consultation" and "WhatsApp". Text sits above the faces, dock below. Mobile: photo on top, copy on solid green beneath.
3. **Services (sticky intro + accordion list, one open at a time):** "Six services. *One accountable team.*"
   - 01 Accounting & Bookkeeping: bookkeeping, financial statements
   - 02 Payroll Management (EPF / ETF)
   - 03 Tax Services: personal income tax, corporate tax filing, partnership & SME tax, VAT services, tax planning & advisory, IRD notices & penalties
   - 04 Company Secretarial: company registration, statutory records, annual returns filing, board & shareholder documentation, corporate compliance support
   - 05 Business Consulting (startups, SMEs)
   - 06 Financial Consulting
4. **Tax band (dark):** "Tax return still pending? *Don't leave it to the last minute.*" with Sinhala line ප්‍රමාද නොවී Tax Return file කරමුද? and a card listing individual income tax, corporate income tax, partnership & SME tax, VAT, the main number and ඔබගේ බදු ගැටලුවට හොඳම විසඳුම අපෙන්.
5. **About:** rotating-text emblem around the circular badge; "Straightforward advice. *Careful work.*"; four ticks (one team for everything, deadlines tracked, plain language in Sinhala or English, a walk-in office); facts: Established 2015, 6 service lines, open Mon–Sat.
6. **Process:** "From first call *to filed.*" Talk to us, We review, We prepare & file, We stay on.
7. **Contact (dark):** "Let's talk about *your numbers.*"; very large gold phone number; Call / WhatsApp / Email buttons; address, other lines, email, hours with live open status; form (name, phone, service, message) that sends via WhatsApp or email with a pre-written message; greyscale Google map; social icons only if URLs are set.
8. **Footer:** badge lockup, Sinhala tagline, explore / services / reach-us columns, copyright with auto year. Floating WhatsApp button.

## Behaviour and quality
- Staggered headline reveal, scroll reveals, subtle hero parallax; all disabled under `prefers-reduced-motion`.
- Accessible: skip link, focus-visible rings, ARIA on accordion and menu, form errors announced.
- SEO/AEO: Schema.org `AccountingService` JSON-LD, Open Graph tags, WebP images with a mobile hero variant.
- No fabricated testimonials, client counts, tax rates or deadlines.
