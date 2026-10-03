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
| English only | English plus the firm's own Sinhala lines | "ඔබගේ විශ්වසනීය ගිණුම්කරණ සහකරුවා", "ඔබගේ බදු ගැටලුවට හොඳම විසඳුම අපෙන්" and "ප්‍රමාද නොවී Tax Return file කරමුද?" all come from their artwork. |
| Contact form opened only the email app | Sends via WhatsApp or email, with a pre-written message | Most Sri Lankan visitors do not have a desktop mail client set up; WhatsApp is how this firm already takes enquiries. |
| Dead social icons pointing to `#` | Hidden until a URL is set in `js/script.js` | Dead links look unfinished. |
| "Never a call centre" | "An office you can walk into, not just a phone number" | Says the same thing without the dig at others. |
| Static hours text only | Live "Open now / Closed, opens Mon 9:00 am" (Sri Lanka time) | Useful for a walk-in practice. |

Also added: Schema.org `AccountingService` data (address, phone, hours, services) for Google and AI answer engines, Open Graph tags, and descriptive alt text.

## Needs the owner to confirm

1. **Sinhala text.** Copied from the ad artwork. Have a Sinhala reader check spelling before launch.
2. **"IRD notices & penalties" under Tax Services.** Inferred from the ad "IRD එකෙන් රතු නිවේදන ඇවිත්ද? දඩ ගෙවන්න වෙලාද?". Remove if it is not a service they offer.
3. **"Explained in plain language, in Sinhala or English".** Based on their bilingual ads. Add Tamil if they serve Tamil-speaking clients.
4. **"Bookkeeping, Financial statements"** chips and the Business/Financial Consulting descriptions. The ads name these services but do not describe them. Wording is conservative; adjust to what is really delivered.
5. **Office hours** (Mon–Fri 9–5, Sat 9–1) came from the owner during this project. Confirm they apply year-round.
6. **Phone lines.** 071 666 4111 is treated as the WhatsApp number. Confirm that, and that 070 167 9811 / 074 244 8951 / 036 226 0888 are all staffed.
7. **Social links.** Need the real Facebook, LinkedIn, TikTok and YouTube URLs (set in `SOCIAL` at the top of `js/script.js`).
8. **Domain.** Add the live URL to the `og:image` and Schema.org `url` once known.

## Deliberately left out

- **Client testimonials and client-count statistics.** None were supplied; inventing them would be false. Add real ones (with permission) when available.
- **Specific tax deadlines, rates or thresholds.** They change; a wrong figure on a tax firm's site is worse than none.
- **Team names and bios.** Not supplied. The team photo is used unnamed in the hero.

## Photo note

The hero photo is a candid and charming shot of the real team, which suits a small local firm. The ceiling damage and open boxes are visible only faintly under the overlay. A re-shoot is optional, not necessary.
