"""Build the static PBS website (multi-page) into the site root.

Run from anywhere:   python tools/build.py
Override the public address when the real domain is known:
    SITE_URL=https://www.example.lk python tools/build.py

Pages are generated so the header, footer and service pages stay consistent.
The generated .html files are committed; the deploy workflow only copies files.
"""
import datetime
import html
import json
import os
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (CONTENT_UPDATED, CONTENT_UPDATED_ISO, FAQ_GENERAL, HOME_FAQ_PICK, HOME_OVERVIEW, LEGAL_UPDATED,  # noqa: E402
                     OTHER, PRIMARY, REELS, SERVICE_PHOTO, SERVICES, STATS, STATS_SOURCE, STEPS, common_faqs)
PHOTO_ALT = {
    "card-1": "Four PBS team members in green PBS polo shirts reviewing documents together at a laptop",
    "card-3": "The full PBS team of nine in green PBS polo shirts gathered around a laptop",
    "card-4": "Three PBS team members working together at a laptop, one pointing at the screen",
    "card-5": "Three PBS team members seated at a laptop with a colleague standing beside them",
    "card-6": "Four PBS team members in green polo shirts looking through documents at a laptop",
    "team-full": "The full PBS team of nine in green PBS polo shirts gathered around a laptop",
    "why-arch": "Three PBS team members working at a laptop, one pointing at the screen",
    "sign": "The illuminated PBS sign reading Panambara Business Solutions",
}
SITE_URL = os.environ.get("SITE_URL", "https://kavindugunathilaka.github.io/pbs-website").rstrip("/")
TODAY = datetime.date.today()
NAME = "Panambara Business Solutions"
PHONE, PHONE_TEL = "071 666 4111", "+94716664111"
WA = "https://wa.me/94716664111"
EMAIL = "info@panambara.lk"
ADDRESS = "240/A, Old Railway Street, Eheliyagoda"
FACEBOOK = "https://www.facebook.com/PBSolutionsSL/"
YOUTUBE = "https://www.youtube.com/channel/UCYsc7NPU5trLjidRzrCPwHA"
OTHER_LINES = [("070 167 9811", "+94701679811"), ("074 244 8951", "+94742448951"), ("036 226 0888", "+94362260888")]

SLUGS = {sv["slug"]: sv for sv in SERVICES}
NUM = {6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}


def asset_v(rel):
    """Short content hash of a CSS/JS file, used as ?v=... so browsers always fetch the latest version."""
    import hashlib
    with open(os.path.join(ROOT, rel), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:8]

REELS_NOTE = "Short reels from our channel. Tap any reel to play it right here."

# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------
e = html.escape


def sprite():
    return """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<linearGradient id="barsGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c46a"/><stop offset=".55" stop-color="#4f9a64"/><stop offset="1" stop-color="#0f4533"/></linearGradient>
<symbol id="bars" viewBox="0 0 112 160"><path d="M0 160V104q0-9 10-12l18-5v73z" fill="url(#barsGrad)"/><path d="M40 160V84q0-9 10-12l18-5v93z" fill="url(#barsGrad)"/><path d="M80 160V72q2-24 18-38 10-10 14-34v160z" fill="url(#barsGrad)"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.5 21 3 13.5 3 4c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1L6.6 10.8Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></symbol>
<symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2Zm0 1.8a8.2 8.2 0 0 1 6.9 12.6l-.2.4.7 2.6-2.7-.7-.4.2A8.2 8.2 0 1 1 12 3.8Zm-3.4 4a1 1 0 0 0-.7.3c-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 5 4.3 2.4.9 2.9.7 3.4.7.5-.1 1.7-.7 2-1.4.2-.6.2-1.2.1-1.3-.1-.1-.3-.2-.6-.4l-2-1c-.3-.1-.5-.2-.7.2l-.6.9c-.1.2-.3.2-.5.1-.3-.1-1.2-.5-2.2-1.4-.8-.7-1.4-1.6-1.6-1.9-.1-.3 0-.4.2-.6l.5-.6c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.5-.4-.5-.6-.5h-.5Z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s7-6.1 7-11.5A7 7 0 0 0 5 9.5C5 14.9 12 21 12 21Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="12" cy="9.5" r="2.4" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-pause" viewBox="0 0 24 24"><path fill="currentColor" d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path fill="currentColor" d="M8 5.5v13l11-6.5z"/></symbol>
<symbol id="i-facebook" viewBox="0 0 24 24"><path fill="currentColor" d="M13.5 21v-7.6h2.6l.4-3h-3V8.4c0-.9.2-1.5 1.5-1.5h1.6V4.2C16.3 4.1 15.2 4 14 4c-2.5 0-4.2 1.5-4.2 4.3v2.1H7.2v3h2.6V21h3.7Z"/></symbol>
<symbol id="i-linkedin" viewBox="0 0 24 24"><path fill="currentColor" d="M6.9 8.6H3.7V20h3.2V8.6ZM5.3 3.6a1.9 1.9 0 1 0 0 3.7 1.9 1.9 0 0 0 0-3.7ZM20.3 20h-3.2v-5.9c0-1.4-.5-2.3-1.7-2.3-1 0-1.5.6-1.8 1.3-.1.2-.1.5-.1.8V20h-3.2s.1-9.6 0-10.6h3.2v1.5c.4-.6 1.2-1.5 2.9-1.5 2.1 0 3.9 1.4 3.9 4.4V20Z"/></symbol>
<symbol id="i-tiktok" viewBox="0 0 24 24"><path fill="currentColor" d="M14.5 3h2.7c.2 1.6 1.3 3 3.3 3.3v2.7c-1.2 0-2.4-.4-3.3-1v6.6a5 5 0 1 1-5-5c.2 0 .4 0 .6.1v2.8a2.3 2.3 0 1 0 1.7 2.2V3Z"/></symbol>
<symbol id="i-youtube" viewBox="0 0 24 24"><path fill="currentColor" d="M21.6 8.2s-.2-1.5-.8-2.1c-.8-.8-1.7-.8-2.1-.9C15.9 5 12 5 12 5s-3.9 0-6.7.2c-.4 0-1.3.1-2.1.9-.6.6-.8 2.1-.8 2.1S2.2 10 2.2 11.8v1.4C2.2 15 2.4 16.8 2.4 16.8s.2 1.5.8 2.1c.8.8 1.9.8 2.3.9 1.7.2 7.1.2 7.1.2s3.9 0 6.7-.2c.4-.1 1.3-.1 2.1-.9.6-.6.8-2.1.8-2.1s.2-1.8.2-3.6v-1.4c0-1.8-.2-3.6-.2-3.6ZM10 14.6V8.9l5.2 2.9-5.2 2.8Z"/></symbol>
<symbol id="s-accounting" viewBox="0 0 24 24"><path d="M4 19V5a1 1 0 0 1 1-1h9l6 6v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M14 4v5a1 1 0 0 0 1 1h5M8 13h8M8 16.5h5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="s-payroll" viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.4" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M4.5 20c1-3.6 4-5.6 7.5-5.6s6.5 2 7.5 5.6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></symbol>
<symbol id="s-tax" viewBox="0 0 24 24"><path d="M12 3v2M12 19v2M4.2 6.2l1.4 1.4M18.4 16.4l1.4 1.4M3 12h2M19 12h2M4.2 17.8l1.4-1.4M18.4 7.6l1.4-1.4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
<symbol id="s-secretarial" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 9h8M8 12.5h8M8 16h5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></symbol>
<symbol id="s-consulting" viewBox="0 0 24 24"><path d="M4 20V11l8-6 8 6v9M9 20v-6h6v6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></symbol>
<symbol id="s-financial" viewBox="0 0 24 24"><path d="M4 18V9M10 18V5M16 18v-7M20 18H4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="s-audit" viewBox="0 0 24 24"><circle cx="10.5" cy="10.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m15 15 5 5M8.2 10.6l1.7 1.7 3-3.2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="s-web" viewBox="0 0 24 24"><rect x="3" y="4.5" width="18" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M3 9h18M6.5 6.8h.01M9 6.8h.01" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></symbol>
<symbol id="s-marketing" viewBox="0 0 24 24"><path d="M4 10v4a1 1 0 0 0 1 1h2l6 4V5L7 9H5a1 1 0 0 0-1 1Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M16.5 9.5a3.5 3.5 0 0 1 0 5M18.8 7.2a7 7 0 0 1 0 9.6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></symbol>
</defs></svg>"""


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:70]


def business_ld():
    return {
        "@context": "https://schema.org", "@type": "AccountingService", "@id": SITE_URL + "/#business",
        "name": NAME, "alternateName": "PBS", "slogan": "Your Trusted Tax & Finance Partner",
        "description": HOME_OVERVIEW, "foundingDate": "2015", "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/images/logo-badge-512.png", "image": SITE_URL + "/assets/images/team/og-share.jpg",
        "telephone": PHONE_TEL, "email": EMAIL,
        "sameAs": [FACEBOOK, YOUTUBE],
        "address": {"@type": "PostalAddress", "streetAddress": "240/A, Old Railway Street", "addressLocality": "Eheliyagoda", "addressCountry": "LK"},
        "areaServed": [{"@type": "City", "name": "Eheliyagoda"}, {"@type": "Country", "name": "Sri Lanka"}],
        "knowsAbout": [sv["title"] for sv in SERVICES],
        "contactPoint": [{"@type": "ContactPoint", "telephone": t, "contactType": "customer service", "areaServed": "LK"}
                         for t in [PHONE_TEL] + [tel for _, tel in OTHER_LINES]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "13:00"},
        ],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": sv["title"], "url": f"{SITE_URL}/services/{sv['slug']}/"}} for sv in SERVICES]},
    }


def website_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/",
            "name": NAME, "inLanguage": "en-LK", "publisher": {"@id": SITE_URL + "/#business"}}


def webpage_ld(url, name, desc, modified=None):
    return {"@context": "https://schema.org", "@type": "WebPage", "@id": url + "#webpage", "url": url, "name": name, "description": desc,
            "inLanguage": "en-LK", "dateModified": modified or CONTENT_UPDATED_ISO,
            "isPartOf": {"@id": SITE_URL + "/#website"}, "about": {"@id": SITE_URL + "/#business"}}


def faq_ld(items):
    """FAQPage data generated from the same list that is shown on the page, so the two cannot drift apart."""
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def faq_html(items):
    return "".join(
        f'<details class="faq" id="faq-{slugify(q)}"><summary><span>{e(q)}</span><span class="svc-icon" aria-hidden="true"></span></summary>'
        f'<div><p>{e(a)}</p></div></details>' for q, a in items)


def video_ld(rl):
    mins, secs = divmod(rl["seconds"], 60)
    return {"@context": "https://schema.org", "@type": "VideoObject", "@id": f"{SITE_URL}/#video-{rl['id']}",
            "name": rl["en"], "alternateName": rl["si"],
            "description": f"{rl['en']}. A short video by {NAME} on {rl['topic'].lower()}. Call {PHONE} for more details.",
            "thumbnailUrl": f"https://i.ytimg.com/vi/{rl['id']}/maxresdefault.jpg", "uploadDate": rl["upload"],
            "duration": f"PT{mins}M{secs}S", "inLanguage": "si",
            "embedUrl": f"https://www.youtube.com/embed/{rl['id']}", "contentUrl": f"https://www.youtube.com/shorts/{rl['id']}",
            "publisher": {"@id": SITE_URL + "/#business"}}


def services_list_ld():
    return {"@context": "https://schema.org", "@type": "ItemList", "name": "Services of " + NAME, "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": sv["title"], "url": f"{SITE_URL}/services/{sv['slug']}/"} for i, sv in enumerate(SERVICES)]}


def breadcrumb_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE_URL}/{p}"} for i, (n, p) in enumerate(trail)]}


def head(r, title, desc, path, extra=(), home=False, noindex=False, modified=None):
    canon = f"{SITE_URL}/{path}"
    preload = f'<link rel="preload" as="image" href="{r}assets/images/team/hero-6.webp" media="(min-width: 761px)">\n' if home else ""
    ld_all = list(extra) + [webpage_ld(canon, title, desc, modified)] + ([website_ld()] if home else [])
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    alt = "" if noindex else f'''<link rel="alternate" hreflang="en-LK" href="{canon}">
<link rel="alternate" hreflang="x-default" href="{canon}">
'''
    return f"""<!DOCTYPE html>
<html lang="en-LK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js');</script>
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#06231a">
<link rel="canonical" href="{canon}">
{alt}<meta property="og:type" content="website">
<meta property="og:locale" content="en_LK">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}/assets/images/team/og-share.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:updated_time" content="{modified or CONTENT_UPDATED_ISO}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{r}assets/images/logo-badge-512.png">
<link rel="apple-touch-icon" href="{r}assets/images/logo-badge-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+Sinhala:wght@400;500;600&display=swap" rel="stylesheet">
{preload}<link rel="stylesheet" href="{r}css/style.css?v={asset_v("css/style.css")}">
{chr(10).join(ld(x) for x in ld_all)}
</head>
<body>
{sprite()}
<a class="skip-link" href="#main">Skip to content</a>
"""


def topbar(r):
    return f"""<div class="topbar">
  <div class="topbar-in">
    <div class="topbar-l">
      <a href="tel:{PHONE_TEL}"><svg class="i"><use href="#i-phone"/></svg><span class="tnum">{PHONE}</span></a>
      <a href="mailto:{EMAIL}" class="topbar-mail"><svg class="i"><use href="#i-mail"/></svg>{EMAIL}</a>
      <span class="topbar-status" data-open-status><i class="pulse-dot"></i><span>Mon&ndash;Sat</span></span>
    </div>
    <div class="topbar-r">
      <ul class="socials socials--sm" data-socials aria-label="Social media"></ul>
      <a href="{WA}" target="_blank" rel="noopener" class="topbar-wa"><svg class="i"><use href="#i-wa"/></svg>WhatsApp</a>
    </div>
  </div>
</div>
"""


def nav(r, current):
    home = r or "./"

    def cur(key):
        return ' aria-current="page"' if current == key else ""

    items = "".join(
        f'<li><a href="{r}services/{s["slug"]}/"{cur("svc:" + s["slug"])}><span class="mega-ico"><svg class="i"><use href="#{s["icon"]}"/></svg></span>'
        f'<span class="mega-t"><strong>{e(s["nav"])}</strong><small>{e(s["short"])}</small></span></a></li>'
        for s in SERVICES)
    sheet_items = "".join(f'<li><a href="{r}services/{s["slug"]}/">{e(s["nav"])}</a></li>' for s in SERVICES)
    svc_cur = ' aria-current="true"' if current.startswith("svc") or current == "services" else ""
    return f"""{topbar(r)}<header class="nav" id="nav">
  <div class="nav-pill">
    <a href="{home}" class="brand" aria-label="{NAME}, home">
      <img src="{r}assets/images/logo-badge-256.webp" alt="" width="40" height="40" class="brand-mark">
      <span class="brand-text"><strong>Panambara</strong><em>Business Solutions</em></span>
    </a>

    <nav class="nav-links" aria-label="Primary">
      <a href="{home}"{cur("home")}>Home</a>
      <div class="has-menu">
        <button type="button" class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="svcMenu"{svc_cur}>Services<svg class="i chev"><use href="#i-chev"/></svg></button>
        <div class="mega" id="svcMenu">
          <ul class="mega-grid">{items}</ul>
          <a href="{r}services/" class="mega-all">View all services <svg class="i"><use href="#i-arrow"/></svg></a>
        </div>
      </div>
      <a href="{home}#videos">Videos</a>
      <a href="{r}about-us/"{cur("about")}>About Us</a>
      <a href="{r}contact-us/"{cur("contact")}>Contact Us</a>
    </nav>

    <div class="nav-actions">
      <a href="tel:{PHONE_TEL}" class="nav-phone"><svg class="i"><use href="#i-phone"/></svg><span class="tnum">{PHONE}</span></a>
      <a href="{r}contact-us/#form" class="btn btn-gold btn-sm nav-cta">Book a consultation</a>
      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="sheet"><span></span><span></span></button>
    </div>
  </div>
</header>

<div class="sheet" id="sheet" aria-hidden="true">
  <nav class="sheet-links" aria-label="Mobile">
    <a href="{home}"><span>01</span>Home</a>
    <div class="sheet-group">
      <button type="button" class="sheet-sub-btn" aria-expanded="false" aria-controls="sheetSub"><span>02</span>Services<svg class="i chev"><use href="#i-chev"/></svg></button>
      <ul class="sheet-sub" id="sheetSub">{sheet_items}<li><a href="{r}services/">All services</a></li></ul>
    </div>
    <a href="{home}#videos"><span>03</span>Videos</a>
    <a href="{r}about-us/"><span>04</span>About Us</a>
    <a href="{r}contact-us/"><span>05</span>Contact Us</a>
  </nav>
  <div class="sheet-foot">
    <a href="tel:{PHONE_TEL}" class="btn btn-gold btn-block">Call {PHONE}</a>
    <a href="{WA}" class="btn btn-ghost btn-block" target="_blank" rel="noopener"><svg class="i"><use href="#i-wa"/></svg>WhatsApp</a>
  </div>
</div>
"""


def cta_band(r, title="Ready to simplify your tax &amp; compliance?", text="Speak with our team today for clear next steps on your tax, payroll, accounts or company filings."):
    return f"""<section class="cta">
  <div class="container cta-in reveal">
    <div>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
    <div class="cta-actions">
      <a href="tel:{PHONE_TEL}" class="btn btn-dark btn-lg"><svg class="i"><use href="#i-phone"/></svg>Call {PHONE}</a>
      <a href="{WA}" class="btn btn-outline btn-lg" target="_blank" rel="noopener"><svg class="i"><use href="#i-wa"/></svg>WhatsApp</a>
    </div>
  </div>
</section>
"""


def footer(r):
    home = r or "./"
    svc = "".join(f'<a href="{r}services/{s["slug"]}/">{e(s["nav"])}</a>' for s in SERVICES)
    return f"""<footer class="footer">
  <div class="container footer-top">
    <div class="footer-brand">
      <a href="{home}" class="brand" aria-label="{NAME}, home">
        <img src="{r}assets/images/logo-badge-256.webp" alt="" width="48" height="48" class="brand-mark" loading="lazy">
        <span class="brand-text"><strong>Panambara</strong><em>Business Solutions</em></span>
      </a>
      <p class="footer-blurb">Tax, accounting, audit, advisory, compliance, payroll, web development and digital marketing in Eheliyagoda, Sri&nbsp;Lanka.</p>
      <ul class="socials" data-socials aria-label="Social media"></ul>
    </div>

    <nav class="footer-col" aria-label="Company">
      <h4>Panambara</h4>
      <a href="{home}">Home</a>
      <a href="{r}about-us/">About Us</a>
      <a href="{r}contact-us/">Contact Us</a>
      <a href="{r}faq/">FAQ</a>
      <a href="{r}terms-and-conditions/">Terms &amp; Conditions</a>
      <a href="{r}privacy-policy/">Privacy Policy</a>
    </nav>

    <nav class="footer-col" aria-label="Our services">
      <h4>Our services</h4>
      {svc}
    </nav>

    <div class="footer-col">
      <h4>Visit &amp; contact</h4>
      <span>{ADDRESS}</span>
      <a href="tel:{PHONE_TEL}" class="tnum">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <span class="footer-hours">Mon&ndash;Fri 9:00&nbsp;am&ndash;5:00&nbsp;pm<br>Sat 9:00&nbsp;am&ndash;1:00&nbsp;pm</span>
    </div>
  </div>

  <div class="container footer-bottom">
    <p>&copy; <span id="year">{TODAY.year}</span> {NAME}. All rights reserved.</p>
    <a href="#main" class="to-top">Back to top <svg class="i"><use href="#i-arrow"/></svg></a>
  </div>
</footer>

<a href="{WA}" class="fab" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp"><svg><use href="#i-wa"/></svg></a>

<script src="{r}js/script.js?v={asset_v("js/script.js")}"></script>
</body>
</html>
"""


def page_hero(r, trail, h1, lead, actions=True, extra="", photo=None):
    home = r or "./"
    crumbs = [("Home", home)] + trail[:-1]
    bc = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in crumbs) + f'<li aria-current="page">{trail[-1][0]}</li>'
    act = (f'<div class="page-hero-actions"><a href="{r}contact-us/#form" class="btn btn-gold btn-lg">Book a consultation</a>'
           f'<a href="tel:{PHONE_TEL}" class="btn btn-ghost btn-lg"><svg class="i"><use href="#i-phone"/></svg>{PHONE}</a></div>') if actions else ""
    fig = (f'<figure class="page-hero-photo"><img src="{r}assets/images/team/{photo}.webp" width="1200" height="750" alt="{PHOTO_ALT[photo]}"></figure>') if photo else ""
    return f"""<section class="page-hero{' has-photo' if photo else ''}">
  <svg class="watermark watermark--dark" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container page-hero-in">
    <div class="page-hero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><ol>{bc}</ol></nav>
    <h1>{h1}</h1>
    <p class="page-lead">{lead}</p>
    {extra}
    {act}
    </div>
    {fig}
  </div>
</section>
"""


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
def card(r, slug, n):
    s = SLUGS[slug]
    chips = "".join(f"<li>{e(c)}</li>" for c in s["chips"])
    return f"""<a class="svc-card reveal" href="{r}services/{slug}/">
        <span class="svc-card-top"><span class="svc-card-no tnum">{n:02d}</span><span class="svc-card-ico"><svg class="i"><use href="#{s['icon']}"/></svg></span></span>
        <h3>{e(s['title'])}</h3>
        <p>{e(s['short'])}</p>
        <ul class="chips">{chips}</ul>
        <span class="svc-card-more">More details <svg class="i"><use href="#i-arrow"/></svg></span>
      </a>"""


HERO = [
    dict(n=6, label="Welcome", ih="66%", pos="0%"),
    dict(n=4, label="Tax services", eyebrow="Tax services", l1="Simplifying", l2="Tax &amp; Business Compliance.",
         link=("services/taxation-tax-consultancy/", "Explore tax services"), ih="66%", pos="0%"),
    dict(n=5, label="Corporate compliance", eyebrow="Corporate compliance", l1="Professional", l2="Company Secretarial Services.",
         link=("services/corporate-compliance/", "Explore corporate compliance"), ih="66%", pos="0%"),
    dict(n=3, label="Our team", eyebrow="Our team", l1="One team for your", l2="tax, payroll and filings.",
         link=("about-us/", "Meet the team"), ih="60%", pos="0%"),
    dict(n=1, label="Accounting &amp; payroll", eyebrow="Accounting &amp; payroll", l1="Books and payroll,", l2="kept in order.",
         link=("services/financial-management-accounting/", "Our accounting services"), ih="66%", pos="0%"),
]


def hero_html():
    """The home hero slider: every slide is a real team photo with a short headline."""
    total = len(HERO)
    slides, pgs = [], []
    for i, sl in enumerate(HERO):
        n, first = sl["n"], i == 0
        alt = PHOTO_ALT[f"card-{n}"]
        attrs = 'fetchpriority="high"' if first else 'loading="lazy" decoding="async"'
        pic = (f'<picture><source media="(max-width: 760px)" srcset="assets/images/team/hero-m-{n}.webp">'
               f'<img src="assets/images/team/hero-{n}.webp" width="1920" height="1080" alt="{alt}" {attrs}></picture>')
        if first:
            text = """<p class="hero-eyebrow"><span>Panambara Business Solutions</span><i></i><span>Est. 2015</span></p>
        <h1 class="hero-title">
          <span class="line"><span>Your trusted</span></span>
          <span class="line"><em>Tax &amp; Finance Partner.</em></span>
        </h1>"""
        else:
            href, label = sl["link"]
            text = f"""<p class="hero-eyebrow"><span>{sl['eyebrow']}</span></p>
        <h2 class="hero-title">
          <span class="line"><span>{sl['l1']}</span></span>
          <span class="line"><em>{sl['l2']}</em></span>
        </h2>
        <a href="{href}" class="slide-link">{label} <svg class="i"><use href="#i-arrow"/></svg></a>"""
        slides.append(f"""    <article class="slide slide--photo{'' if first else ' slide--compact'}{' is-active' if first else ''}" style="--ih:{sl['ih']};--ipos:{sl['pos']}" role="group" aria-roledescription="slide" aria-label="{i + 1} of {total}: {sl['label']}">
      <div class="slide-media">
        {pic}
        <div class="slide-shade"></div>
      </div>
      <div class="container slide-body">
        {text}
      </div>
    </article>""")
        cur = ' aria-current="true"' if first else ""
        pgs.append(f'<button type="button" class="pg{" is-active" if first else ""}" aria-label="Go to slide {i + 1}: {sl["label"]}"{cur}><span class="tnum">{i + 1:02d}</span><i></i></button>')
    slides_html = '  <div class="hero-slides" id="slides" aria-live="off">\n\n' + "\n\n".join(slides) + "\n  </div>"
    pager_html = ('  <div class="pager" id="pager">\n    ' + "\n    ".join(pgs) +
                  '\n    <button type="button" class="pg-toggle" id="pgToggle" aria-label="Pause slideshow"><svg class="i"><use href="#i-pause"/></svg></button>\n  </div>')
    return slides_html, pager_html


def build_home():
    r = ""
    home_faqs = [FAQ_GENERAL[i] for i in HOME_FAQ_PICK]
    ld_extra = [business_ld(), faq_ld(home_faqs), services_list_ld()] + [video_ld(rl) for rl in REELS]
    h = head(r, f"{NAME} | Tax, Accounting & Business Services, Eheliyagoda",
             "Tax, accounting, audit, advisory, compliance, payroll, web development and digital marketing in Eheliyagoda, Sri Lanka. Panambara Business Solutions, since 2015.",
             "", ld_extra, home=True)
    reels_html = "".join(
        f'''<li class="reel" data-id="{rl['id']}" data-index="{i}">
        <div class="reel-frame"></div>
        <div class="reel-cap"><span class="reel-topic">{e(rl['topic'])}</span><h3>{e(rl['en'])}</h3><p lang="si">{e(rl['si'])}</p></div>
      </li>''' for i, rl in enumerate(REELS))
    stat_cards = "".join(
        f'<div class="reveal"><dt>{lab}</dt><dd class="stat-num tnum" data-count="{n}" data-suffix="{suf}">{txt}</dd></div>'
        for lab, n, suf, txt in STATS)
    hero_slides, hero_pager = hero_html()
    other = "".join(
        f'<a class="other-item" href="services/{slug}/"><span class="other-ico"><svg class="i"><use href="#{SLUGS[slug]["icon"]}"/></svg></span><span><strong>{e(SLUGS[slug]["title"])}</strong><small>{e(SLUGS[slug]["short"])}</small></span><svg class="i other-arrow"><use href="#i-arrow"/></svg></a>'
        for slug in OTHER)
    cards = "".join(card(r, slug, i + 1) for i, slug in enumerate(PRIMARY))
    body = f"""{nav(r, "home")}
<main id="main">

<!-- HERO SLIDER -->
<section class="hero" id="home" aria-roledescription="carousel" aria-label="Featured services">
{hero_slides}

{hero_pager}

  <div class="container hero-dock-wrap">
    <div class="dock">
      <div class="dock-cell">
        <span class="dock-label">Call or WhatsApp</span>
        <a class="dock-value tnum" href="tel:{PHONE_TEL}">{PHONE}</a>
      </div>
      <div class="dock-cell">
        <span class="dock-label">Visit us</span>
        <span class="dock-value">{ADDRESS}</span>
      </div>
      <div class="dock-cell">
        <span class="dock-label">Office</span>
        <span class="dock-value" data-open-status><i class="pulse-dot"></i><span>Mon&ndash;Sat</span></span>
      </div>
      <div class="dock-actions">
        <a href="contact-us/#form" class="btn btn-gold">Book a consultation</a>
        <a href="{WA}" class="btn btn-ghost" target="_blank" rel="noopener"><svg class="i"><use href="#i-wa"/></svg>WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<!-- STATS -->
<section class="stats" aria-label="Panambara Business Solutions in numbers">
  <div class="container">
    <p class="stats-intro reveal"><span class="eyebrow">Trusted since 2015</span>Numbers behind the work we do for clients.</p>
    <p class="stats-overview reveal">{HOME_OVERVIEW}</p>
    <dl class="stats-grid">{stat_cards}</dl>
    <p class="stats-note">{STATS_SOURCE} <span>Last updated: {CONTENT_UPDATED}</span></p>
  </div>
</section>

<!-- WHY PBS -->
<section class="section why" id="why">
  <div class="container why-grid">
    <figure class="why-media reveal">
      <img src="assets/images/team/why-arch.webp" width="800" height="1000" alt="{PHOTO_ALT['why-arch']}" loading="lazy">
    </figure>
    <div class="why-copy reveal">
      <p class="eyebrow">Why Panambara</p>
      <h2>Straightforward advice.<br><em>Careful work.</em></h2>
      <p class="lead">We look after the numbers and the filings, so owners can look after the business.</p>
      <ul class="why-list">
        <li><span class="why-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>One team for everything</strong><p>Tax, accounts, audit support, compliance, payroll and digital services all sit with one team.</p></div></li>
        <li><span class="why-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>Deadlines tracked for you</strong><p>We keep an eye on filing dates so you don&rsquo;t have to.</p></div></li>
        <li><span class="why-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>Plain language</strong><p>Explained clearly, in Sinhala or English.</p></div></li>
        <li><span class="why-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>A real local office</strong><p>Find us on Old Railway Street, Eheliyagoda, or reach us by phone and WhatsApp.</p></div></li>
      </ul>
      <a href="about-us/" class="btn btn-dark">About us <svg class="i"><use href="#i-arrow"/></svg></a>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="section services" id="services">
  <svg class="watermark watermark--paper" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container">
    <header class="section-head reveal">
      <p class="eyebrow">Our services</p>
      <h2>How can we <em>help you?</em></h2>
      <p class="lead">Individuals, startups, SMEs, partnerships and companies. Pick a service to see what it covers.</p>
    </header>
    <div class="svc-grid">{cards}</div>
    <div class="other reveal">
      <h3>Other services</h3>
      <div class="other-grid">{other}</div>
    </div>
  </div>
</section>

<!-- TAX BAND -->
<section class="band" id="tax">
  <svg class="watermark watermark--dark" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container band-grid">
    <div class="reveal">
      <p class="eyebrow eyebrow--light">Tax returns</p>
      <h2>Tax return still pending?<br><em>Don&rsquo;t leave it to the last minute.</em></h2>
    </div>
    <div class="band-card reveal">
      <p class="band-card-label">Talk to us about</p>
      <ul>
        <li>Individual income tax</li>
        <li>Corporate income tax</li>
        <li>Partnership &amp; SME tax</li>
        <li>VAT</li>
      </ul>
      <a href="tel:{PHONE_TEL}" class="band-phone tnum">{PHONE}</a>
    </div>
  </div>
</section>

<!-- VIDEOS -->
<section class="section videos" id="videos">
  <div class="container videos-head reveal">
    <div>
      <p class="eyebrow eyebrow--light">Watch</p>
      <h2>PBS <em>on video.</em></h2>
      <p class="lead">{REELS_NOTE}</p>
    </div>
    <div class="videos-actions">
      <a href="#" class="btn btn-gold" data-social="youtube" target="_blank" rel="noopener"><svg class="i"><use href="#i-youtube"/></svg>Subscribe on YouTube</a>
      <a href="#" class="btn btn-ghost" data-social="facebook" target="_blank" rel="noopener"><svg class="i"><use href="#i-facebook"/></svg>Follow on Facebook</a>
    </div>
  </div>

  <div class="rail-wrap reveal">
    <ul class="rail" id="rail" aria-label="PBS video reels">{reels_html}</ul>
    <noscript><p class="container rail-fallback"><a href="{YOUTUBE}" target="_blank" rel="noopener">Watch our reels on YouTube</a></p></noscript>
  </div>

  <div class="container rail-controls">
    <p class="rail-count tnum" id="railCount" aria-live="polite"></p>
    <div class="rail-buttons">
      <button type="button" class="rail-btn" id="railPrev" aria-label="Previous reels"><svg class="i"><use href="#i-arrow"/></svg></button>
      <button type="button" class="rail-btn" id="railNext" aria-label="Next reels"><svg class="i"><use href="#i-arrow"/></svg></button>
    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="section process" id="process">
  <div class="container">
    <header class="process-head reveal">
      <p class="eyebrow">How we work</p>
      <h2>From first call <em>to filed.</em></h2>
    </header>
    <ol class="steps">
      <li class="reveal"><span class="step-no tnum">01</span><h3>Talk to us</h3><p>Call or message us on WhatsApp and tell us what you need: tax, payroll, accounts or company filings.</p></li>
      <li class="reveal"><span class="step-no tnum">02</span><h3>We review</h3><p>We look at your records and requirements, then tell you what is needed and what it involves.</p></li>
      <li class="reveal"><span class="step-no tnum">03</span><h3>We prepare &amp; file</h3><p>Accounts, returns and documents are prepared and submitted by our team.</p></li>
      <li class="reveal"><span class="step-no tnum">04</span><h3>We stay on</h3><p>Bookkeeping, payroll and filing reminders carry on as your business grows.</p></li>
    </ol>
  </div>
</section>

<!-- FAQ -->
<section class="section faq-home" id="faq">
  <div class="container faq-layout">
    <header class="reveal">
      <p class="eyebrow">Questions</p>
      <h2>Common <em>questions</em></h2>
      <p class="lead">Quick answers about Panambara Business Solutions. <a href="faq/">See all questions</a></p>
    </header>
    <div class="faqs reveal">{faq_html(home_faqs)}</div>
  </div>
</section>

{cta_band(r)}
</main>
"""
    write("index.html", h + body + footer(r))


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
def build_services_index():
    r = "../"
    trail = [("Services", "")]
    cards = "".join(card(r, sv["slug"], i + 1) for i, sv in enumerate(SERVICES))
    lead = (f"{NUM[len(SERVICES)]} services, one accountable team in Eheliyagoda, Sri Lanka. Pick a service to see what it covers, "
            "the questions we are asked most and how we work.")
    h = head(r, f"Services | {NAME}",
             "Taxation, accounting, audit, business advisory, corporate compliance, payroll, web development and digital marketing in Eheliyagoda, Sri Lanka.",
             "services/", [business_ld(), services_list_ld(), breadcrumb_ld([("Home", ""), ("Services", "services/")])])
    body = f"""{nav(r, "services")}
<main id="main">
{page_hero(r, trail, "Our <em>services</em>", lead, photo="card-3", extra=f'<p class="updated">Last updated: {CONTENT_UPDATED}</p>')}
<section class="section services">
  <svg class="watermark watermark--paper" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container"><div class="svc-grid svc-grid--3">{cards}</div></div>
</section>
{cta_band(r)}
</main>
"""
    write("services/index.html", h + body + footer(r))


def build_service(sv):
    r = "../../"
    trail = [("Services", r + "services/"), (sv["title"], "")]
    faq_items = sv["faqs"] + common_faqs(sv)
    handle = "".join(
        f'<li><span class="handle-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>{e(t)}</strong><p>{e(d)}</p></div></li>' for t, d in sv["handle"])
    aud = "".join(f"<li>{e(a)}</li>" for a in sv["audience"])
    steps = "".join(
        f'<li><span class="vstep-no tnum">{i + 1:02d}</span><div><h3>{e(t)}</h3><p>{e(d.format(deliver=sv["deliver"], stay=sv["stay"]))}</p></div></li>'
        for i, (t, d) in enumerate(STEPS))
    others = "".join(
        f'<li><a href="{r}services/{o["slug"]}/"><svg class="i"><use href="#{o["icon"]}"/></svg>{e(o["nav"])}<svg class="i go"><use href="#i-arrow"/></svg></a></li>'
        for o in SERVICES if o["slug"] != sv["slug"])
    quote = f'<p class="pull">{e(sv["quote"])}</p>' if sv.get("quote") else ""
    url = f"{SITE_URL}/services/{sv['slug']}/"
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": sv["title"], "serviceType": sv["title"],
              "description": sv["overview"], "url": url, "provider": {"@id": SITE_URL + "/#business"},
              "areaServed": [{"@type": "City", "name": "Eheliyagoda"}, {"@type": "Country", "name": "Sri Lanka"}],
              "audience": {"@type": "Audience", "audienceType": ", ".join(sv["audience"])},
              "hasOfferCatalog": {"@type": "OfferCatalog", "name": sv["title"], "itemListElement": [
                  {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "description": d}} for t, d in sv["handle"]]}}
    h = head(r, f"{sv['title']} in Eheliyagoda | {NAME}", sv["meta"], f"services/{sv['slug']}/",
             [business_ld(), svc_ld, faq_ld(faq_items), breadcrumb_ld([("Home", ""), ("Services", "services/"), (sv["title"], f"services/{sv['slug']}/")])])
    updated = f'<p class="updated">Last updated: {CONTENT_UPDATED}</p>'
    body = f"""{nav(r, "svc:" + sv["slug"])}
<main id="main">
{page_hero(r, trail, e(sv["title"]), e(sv["overview"]), extra=updated, photo=SERVICE_PHOTO[sv["slug"]])}
<section class="section svc-page">
  <div class="container svc-layout">
    <div class="svc-main">
      <section class="block reveal" id="who-its-for">
        <h2>Who it&rsquo;s for</h2>
        <ul class="chips chips--lg">{aud}</ul>
        {quote}
      </section>

      <section class="block reveal" id="what-we-handle">
        <h2>What we <em>handle</em></h2>
        <ul class="handle">{handle}</ul>
      </section>

      <section class="block reveal" id="how-it-works">
        <h2>How it <em>works</em></h2>
        <ol class="vsteps">{steps}</ol>
      </section>

      <section class="block reveal" id="faqs">
        <h2>Common <em>questions</em></h2>
        <div class="faqs">{faq_html(faq_items)}</div>
      </section>
    </div>

    <aside class="svc-aside">
      <div class="aside-card reveal">
        <p class="aside-label">Talk to us</p>
        <a href="tel:{PHONE_TEL}" class="aside-phone tnum">{PHONE}</a>
        <a href="{WA}" class="btn btn-wa btn-block" target="_blank" rel="noopener"><svg class="i"><use href="#i-wa"/></svg>WhatsApp us</a>
        <a href="{r}contact-us/#form" class="btn btn-outline btn-block">Book a consultation</a>
        <p class="aside-note"><span data-open-status><i class="pulse-dot"></i><span>Mon&ndash;Sat</span></span></p>
      </div>
      <div class="aside-card aside-card--list reveal">
        <p class="aside-label">Other services</p>
        <ul class="aside-list">{others}</ul>
      </div>
    </aside>
  </div>
</section>
{cta_band(r)}
</main>
"""
    write(f"services/{sv['slug']}/index.html", h + body + footer(r))


# ---------------------------------------------------------------------------
# About, Contact, Legal
# ---------------------------------------------------------------------------
def build_about():
    r = "../"
    trail = [("About Us", "")]
    mini = "".join(
        f'<li><a href="{r}services/{s["slug"]}/"><svg class="i"><use href="#{s["icon"]}"/></svg><span>{e(s["nav"])}</span><svg class="i go"><use href="#i-arrow"/></svg></a></li>' for s in SERVICES)
    h = head(r, f"About Us | {NAME}", "About Panambara Business Solutions, an accounting and tax practice on Old Railway Street in Eheliyagoda, Sri Lanka, established in 2015.",
             "about-us/", [business_ld(), breadcrumb_ld([("Home", ""), ("About Us", "about-us/")])])
    body = f"""{nav(r, "about")}
<main id="main">
{page_hero(r, trail, "About <em>Panambara</em>", "An accounting and tax practice on Old Railway Street in Eheliyagoda, established in 2015.", photo="card-5")}

<section class="section about-intro">
  <div class="container">
    <figure class="about-banner reveal">
      <img src="{r}assets/images/team/team-full.webp" width="1600" height="900" alt="{PHOTO_ALT['team-full']}" loading="lazy">
      <figcaption>The PBS team.</figcaption>
    </figure>
    <div class="about-grid">
      <div class="about-copy reveal">
        <p class="eyebrow">Who we are</p>
        <h2>Straightforward advice. <em>Careful work.</em></h2>
        <p class="lead">Panambara Business Solutions is an accounting and tax practice in Eheliyagoda, established in 2015. We look after the numbers and the filings, so owners can look after the business.</p>
        <p>Tax, accounting, audit support, compliance, payroll, web development and digital marketing are handled by one team that you can actually reach, by phone, on WhatsApp or in person at our office. We work with individuals, startups, SMEs, partnerships and companies.</p>
      </div>
      <ul class="ticks reveal">
        <li>One team for tax, accounts, compliance, payroll and digital services</li>
        <li>Filing deadlines tracked on your behalf</li>
        <li>Explained in plain language, in Sinhala or English</li>
        <li>An office you can walk into, not just a phone number</li>
      </ul>
    </div>
  </div>
</section>

<section class="section about-svc">
  <div class="container">
    <header class="section-head reveal"><p class="eyebrow">What we do</p><h2>{NUM[len(SERVICES)]} services, <em>one team.</em></h2></header>
    <ul class="mini-grid reveal">{mini}</ul>
  </div>
</section>

<section class="section visit">
  <div class="container visit-grid">
    <div class="reveal">
      <p class="eyebrow eyebrow--light">Visit us</p>
      <h2>Come and <em>see us.</em></h2>
      <p class="lead">{ADDRESS}, Sri&nbsp;Lanka<br>Mon&ndash;Fri 9:00&nbsp;am&ndash;5:00&nbsp;pm &middot; Saturday 9:00&nbsp;am&ndash;1:00&nbsp;pm</p>
      <div class="visit-actions">
        <a href="{r}contact-us/" class="btn btn-gold">Contact us</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost"><svg class="i"><use href="#i-phone"/></svg>{PHONE}</a>
      </div>
    </div>
    <figure class="visit-photo reveal"><img src="{r}assets/images/team/sign.webp" width="1400" height="723" alt="{PHOTO_ALT['sign']}" loading="lazy"></figure>
  </div>
</section>
{cta_band(r)}
</main>
"""
    write("about-us/index.html", h + body + footer(r))


def build_contact():
    r = "../"
    trail = [("Contact Us", "")]
    others = "".join(f'<a href="{t}" class="tnum">{p}</a>' for p, t in [(a, "tel:" + b) for a, b in OTHER_LINES])
    h = head(r, f"Contact Us | {NAME}", "Contact Panambara Business Solutions in Eheliyagoda: phone 071 666 4111, WhatsApp, email and office hours. Book a consultation.",
             "contact-us/", [business_ld(), breadcrumb_ld([("Home", ""), ("Contact Us", "contact-us/")])])
    body = f"""{nav(r, "contact")}
<main id="main">
{page_hero(r, trail, "Let&rsquo;s talk about <em>your numbers.</em>", "Call, message us on WhatsApp or send the form below. We&rsquo;ll get back to you.", actions=False, photo="card-6")}

<section class="section contact">
  <div class="contact-glow" aria-hidden="true"></div>
  <div class="container">
    <div class="contact-grid">
      <div class="contact-main reveal">
        <a href="tel:{PHONE_TEL}" class="mega-phone tnum">{PHONE}</a>
        <div class="quick">
          <a href="tel:{PHONE_TEL}" class="btn btn-gold"><svg class="i"><use href="#i-phone"/></svg>Call</a>
          <a href="{WA}" class="btn btn-ghost" target="_blank" rel="noopener"><svg class="i"><use href="#i-wa"/></svg>WhatsApp</a>
          <a href="mailto:{EMAIL}" class="btn btn-ghost"><svg class="i"><use href="#i-mail"/></svg>Email</a>
        </div>
        <dl class="details">
          <div><dt>Address</dt><dd>240/A, Old Railway Street,<br>Eheliyagoda, Sri&nbsp;Lanka</dd></div>
          <div><dt>Other lines</dt><dd class="lines">{others}</dd></div>
          <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div><dt>Office hours</dt><dd>Mon&ndash;Fri&ensp;9:00&nbsp;am&ndash;5:00&nbsp;pm<br>Saturday&ensp;9:00&nbsp;am&ndash;1:00&nbsp;pm<br>Sunday&ensp;Closed</dd>
            <p class="open-line" data-open-status><i class="pulse-dot"></i><span></span></p></div>
        </dl>
        <ul class="socials" data-socials aria-label="Social media"></ul>
      </div>

      <form class="form reveal" id="form" novalidate>
        <h2 class="form-title">Send us a message</h2>
        <p class="form-sub">Tell us briefly what you need and we&rsquo;ll get back to you.</p>
        <div class="field-row">
          <label class="field"><span>Your name</span><input type="text" name="name" autocomplete="name" required></label>
          <label class="field"><span>Phone</span><input type="tel" name="phone" autocomplete="tel" inputmode="tel" required></label>
        </div>
        <label class="field"><span>I need help with</span>
          <select name="service">
            {"".join(f"<option>{e(s['title'])}</option>" for s in SERVICES)}
            <option>Something else</option>
          </select>
        </label>
        <label class="field"><span>Message <em>(optional)</em></span><textarea name="message" rows="4"></textarea></label>
        <p class="form-error" id="formError" role="alert" hidden>Please add your name and phone number.</p>
        <div class="form-actions">
          <button type="submit" class="btn btn-wa" data-channel="whatsapp"><svg class="i"><use href="#i-wa"/></svg>Send on WhatsApp</button>
          <button type="submit" class="btn btn-outline" data-channel="email"><svg class="i"><use href="#i-mail"/></svg>Send by email</button>
        </div>
        <p class="form-note">This opens WhatsApp or your email app with your message ready to send. Nothing is stored on this website.</p>
      </form>
    </div>

    <div class="map reveal">
      <iframe title="Map showing the Panambara Business Solutions office on Old Railway Street, Eheliyagoda"
        src="https://www.google.com/maps?q=240%2FA%20Old%20Railway%20Street%2C%20Eheliyagoda%2C%20Sri%20Lanka&amp;output=embed"
        loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>
</main>
"""
    write("contact-us/index.html", h + body + footer(r))


def legal_page(slug, title, desc, intro, sections):
    r = "../"
    trail = [(title, "")]
    secs = "".join(f"<h2>{e(t)}</h2>{b}" for t, b in sections)
    h = head(r, f"{title} | {NAME}", desc, f"{slug}/", [business_ld(), breadcrumb_ld([("Home", ""), (title, f"{slug}/")])], modified="2026-11-06")
    body = f"""{nav(r, "legal")}
<main id="main">
{page_hero(r, trail, e(title), e(intro), actions=False)}
<section class="section legal">
  <div class="container legal-in">
    <p class="legal-date">Last updated: {LEGAL_UPDATED}</p>
    <div class="prose">{secs}</div>
  </div>
</section>
</main>
"""
    write(f"{slug}/index.html", h + body + footer(r))


def build_legal():
    c = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    legal_page(
        "terms-and-conditions", "Terms & Conditions",
        "Terms for using the Panambara Business Solutions website in Eheliyagoda, Sri Lanka, covering general information, services and liability.",
        "The terms for using this website.",
        [
            ("About these terms", f"<p>This website is run by {NAME} (&ldquo;PBS&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) from {ADDRESS}, Sri&nbsp;Lanka. By using the site you agree to these terms. If you do not agree, please do not use it.</p>"),
            ("General information only", "<p>The content on this site is general information about our services. It is not tax, legal or financial advice for your situation. Laws, rates and filing requirements change, so please speak to us before acting on anything you read here.</p>"),
            ("Our services", "<p>Our services are provided under an engagement agreed with you separately. Scope, fees and timing are confirmed with you directly and are not set by this website. We take care in our work, but outcomes also depend on the information you give us and on decisions made by the relevant authorities.</p>"),
            ("Your responsibilities", "<p>If you send us information or documents, please make sure they are accurate and complete to the best of your knowledge.</p>"),
            ("Contacting us through the site", "<p>The contact form does not send your message through our servers. It opens WhatsApp or your email app with your message ready to send, and the message is then handled by those services and by us. Please do not send passwords or card details this way.</p>"),
            ("Third-party content and links", "<p>This site shows content from other services, such as Google Maps and YouTube, and may link to other websites, including our social media pages. We do not control those services and are not responsible for their content or practices.</p>"),
            ("Intellectual property", "<p>The PBS name, logo, text, images and design on this site belong to us or are used with permission. Please do not copy or reuse them without asking first.</p>"),
            ("Limits of liability", "<p>To the extent the law allows, we are not responsible for loss that results from relying on the general information on this website.</p>"),
            ("Governing law", "<p>These terms are governed by the laws of Sri&nbsp;Lanka.</p>"),
            ("Changes and questions", f"<p>We may update these terms from time to time; the date above shows when they last changed. Questions? Write to {c} or call {PHONE}.</p>"),
        ])
    legal_page(
        "privacy-policy", "Privacy Policy",
        "How the Panambara Business Solutions website handles your information.",
        "What this website does, and does not do, with your information.",
        [
            ("Who we are", f"<p>This website is run by {NAME}, {ADDRESS}, Sri&nbsp;Lanka. You can reach us at {c} or on {PHONE}.</p>"),
            ("What this website collects", "<p>This website has no user accounts and does not set advertising or tracking cookies of its own. Our contact form does not store anything: it opens WhatsApp or your email app with your message ready to send. What you send is then handled by that service and by us.</p>"),
            ("Content from other services", "<p>To work, this site loads some things from other providers, which may receive technical details such as your IP address and browser type under their own privacy policies:</p><ul><li><strong>Google Fonts</strong> for the typefaces on every page.</li><li><strong>Google Maps</strong> on the contact page.</li><li><strong>YouTube</strong>: video thumbnails load on the home page, and the video player loads only after you tap a reel.</li></ul>"),
            ("How we use what you send us", "<p>When you contact us we use your details to reply, to discuss and provide the services you ask for, and to keep the records the work requires.</p>"),
            ("Sharing", "<p>We do not sell your information. We share it only where needed to carry out work you ask us to do, for example when we make a filing with a government authority on your behalf, or where the law requires it.</p>"),
            ("How long we keep it", "<p>We keep client records for as long as we need them to do the work and to meet our legal and professional obligations.</p>"),
            ("Your choices", f"<p>You can ask us what information we hold about you, ask us to correct it, or ask us to delete it, subject to what we are required by law to keep. Write to {c}.</p>"),
            ("Changes", "<p>We may update this policy; the date above shows when it last changed.</p>"),
        ])


def build_404():
    r = ""
    h = head(r, f"Page not found | {NAME}", "That page could not be found.", "404.html", noindex=True)
    body = f"""{nav(r, "")}
<main id="main">
<section class="page-hero"><svg class="watermark watermark--dark" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container page-hero-in"><h1>Page <em>not found.</em></h1>
  <p class="page-lead">That page isn&rsquo;t here. Try the links below or call us on {PHONE}.</p>
  <div class="page-hero-actions"><a href="./" class="btn btn-gold btn-lg">Back to home</a><a href="services/" class="btn btn-ghost btn-lg">Our services</a></div></div>
</section>
</main>
"""
    write("404.html", h + body + footer(r))


def build_faq():
    r = "../"
    trail = [("FAQ", "")]
    overview = ("These are the questions people ask Panambara Business Solutions most often about its services in Eheliyagoda, Sri Lanka: "
                "what it offers, where the office is, how to book a consultation, and how it helps with tax returns, EPF and ETF, "
                "company registration and IRD notices.")
    h = head(r, f"Frequently Asked Questions | {NAME}",
             "Answers about Panambara Business Solutions in Eheliyagoda: services, office hours, booking, tax returns, EPF and ETF, company registration, IRD notices and costs.",
             "faq/", [business_ld(), faq_ld(FAQ_GENERAL), breadcrumb_ld([("Home", ""), ("FAQ", "faq/")])])
    body = f"""{nav(r, "faq")}
<main id="main">
{page_hero(r, trail, "Frequently asked <em>questions</em>", overview, photo="card-1", extra=f'<p class="updated">Last updated: {CONTENT_UPDATED}</p>')}
<section class="section faq-page">
  <div class="container">
    <div class="faqs">{faq_html(FAQ_GENERAL)}</div>
  </div>
</section>
{cta_band(r)}
</main>
"""
    write("faq/index.html", h + body + footer(r))


def build_seo_files():
    pages = ([("", CONTENT_UPDATED_ISO), ("services/", CONTENT_UPDATED_ISO)] + [(f"services/{sv['slug']}/", CONTENT_UPDATED_ISO) for sv in SERVICES] +
             [("about-us/", CONTENT_UPDATED_ISO), ("contact-us/", CONTENT_UPDATED_ISO), ("faq/", CONTENT_UPDATED_ISO),
              ("terms-and-conditions/", "2026-11-06"), ("privacy-policy/", "2026-11-06")])
    urls = "".join(f"  <url><loc>{SITE_URL}/{pth}</loc><lastmod>{d}</lastmod></url>\n" for pth, d in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    svc_lines = "\n".join(f"- [{sv['title']}]({SITE_URL}/services/{sv['slug']}/): {sv['short']}" for sv in SERVICES)
    write("llms.txt", f"""# {NAME} (PBS)

> {HOME_OVERVIEW}

## Key facts
- Name: {NAME}
- Established: 2015
- Address: {ADDRESS}, Sri Lanka
- Phone and WhatsApp: {PHONE}
- Other phone lines: {", ".join(t for t, _ in OTHER_LINES)}
- Email: {EMAIL}
- Office hours: Monday to Friday 9:00 am to 5:00 pm, Saturday 9:00 am to 1:00 pm, closed Sunday
- Facebook: {FACEBOOK}
- YouTube: {YOUTUBE}

## Services
{svc_lines}

## Pages
- [About us]({SITE_URL}/about-us/)
- [Contact us]({SITE_URL}/contact-us/)
- [Frequently asked questions]({SITE_URL}/faq/)

Last updated: {CONTENT_UPDATED}
""")


if __name__ == "__main__":
    # remove service pages that no longer exist, so old URLs do not linger in the deployed site
    svc_root = os.path.join(ROOT, "services")
    valid = {sv["slug"] for sv in SERVICES}
    for name in os.listdir(svc_root) if os.path.isdir(svc_root) else []:
        if os.path.isdir(os.path.join(svc_root, name)) and name not in valid:
            shutil.rmtree(os.path.join(svc_root, name))
    build_home()
    build_services_index()
    for svc in SERVICES:
        build_service(svc)
    build_about()
    build_contact()
    build_faq()
    build_legal()
    build_404()
    build_seo_files()
    print(f"built {len(SERVICES) + 7} pages + 404 + sitemap + robots + llms.txt for {SITE_URL}")
