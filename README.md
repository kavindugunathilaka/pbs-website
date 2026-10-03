# Panambara Business Solutions: website

Static single-page site (HTML, CSS, vanilla JS). No build step.

```
index.html          page + structured data
css/style.css       all styles
js/script.js        nav, accordion, reveal, form, open/closed status
assets/images/      hero and logo images
assets/sinhala/     Sinhala tagline lettering (SVG outlines)
tools/sinhala_art.py  regenerates those SVGs from the Tharu font (font not stored here)
CONTENT_REVIEW.md   what changed in the copy and what the owner must confirm
SITE_PROMPT.md      full brief (brand, structure, copy) for reuse
```

## Run locally

```bash
python -m http.server 5500
```

Then open http://localhost:5500.

## Before going live

- Add a TikTok URL in `js/script.js` (`SOCIAL`) if there is one; Facebook, YouTube and LinkedIn are set.
- To change the video reels, edit the `REELS` list (YouTube Shorts IDs) in `js/script.js`.
- Work through the checklist in `CONTENT_REVIEW.md`.
- Set the live domain in the Open Graph and Schema.org tags in `index.html`.

## Design notes

- Type: Bodoni Moda (echoes the PBS wordmark) with Instrument Sans; Noto Sans Sinhala for Sinhala lines.
- Palette: forest green `#06231a`, gold `#c8a24a`, paper `#f6f2e7`.
- Respects `prefers-reduced-motion`; keyboard-accessible accordion and menu.

## Sinhala lettering

The Sinhala taglines use the legacy font *Tharu Digital Mahee*, which is not Unicode. They are drawn as SVG outlines (`assets/sinhala/`) and shown as a CSS mask, with the real Unicode text kept in the page (visually hidden) for screen readers, search and copy-paste. To regenerate: `python tools/sinhala_art.py <path-to-font.ttf>`. The font file itself is git-ignored. The Sinhala headline in the tax band stays in Noto Sans Sinhala because it mixes English words the legacy font cannot draw.
