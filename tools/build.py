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

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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

# ---------------------------------------------------------------------------
# Services (all wording comes from PBS's own published ads; items marked
# "confirm" are listed in CONTENT_REVIEW.md for the owner to verify)
# ---------------------------------------------------------------------------
STEPS = [
    ("Talk to us", "Call or message us on WhatsApp and tell us what you need."),
    ("We review", "We look at your records and requirements, then explain what is needed and what it involves."),
    ("We prepare & file", "{deliver}"),
    ("We stay on", "{stay}"),
]

SERVICES = [
    dict(
        slug="accounting-bookkeeping", title="Accounting & Bookkeeping", nav="Accounting & Bookkeeping", icon="s-accounting",
        short="Accurate books and financial statements, always up to date.",
        meta="Accounting and bookkeeping in Eheliyagoda: day-to-day bookkeeping and financial statements for startups, SMEs and companies.",
        lead="Day-to-day bookkeeping and financial statements, kept accurate and up to date, so you always know where the business stands.",
        audience=["Startups", "SMEs", "Partnerships", "Companies"],
        chips=["Bookkeeping", "Financial statements"],
        handle=[
            ("Day-to-day bookkeeping", "Your transactions recorded accurately and kept up to date."),
            ("Financial statements", "Prepared from your books so you can see where the business stands."),
            ("Records ready for filing", "Kept in order for tax and compliance work, so nothing has to be chased at deadline time."),
        ],
        deliver="Books are kept and financial statements prepared by our team.",
        stay="Bookkeeping carries on month after month as your business grows.",
        faqs=[
            ("What does bookkeeping include?", "Recording your day-to-day transactions and preparing financial statements from them. When you call, we confirm exactly what is covered for your business."),
            ("Can you also file my taxes from the books you keep?", "Yes. Accounting, tax and company secretarial work all sit with one team, so your records and your filings stay consistent."),
            ("How do I get started?", "Call 071 666 4111 or message us on WhatsApp. We ask a few questions and explain what we need from you."),
        ],
    ),
    dict(
        slug="payroll-management", title="Payroll Management (EPF / ETF)", nav="Payroll (EPF / ETF)", icon="s-payroll",
        short="Payroll on schedule, with EPF and ETF handled.",
        meta="Payroll management in Eheliyagoda, Sri Lanka, including EPF and ETF, for startups, SMEs and companies.",
        lead="Payroll prepared on schedule, with EPF and ETF handled as part of the same process rather than as an afterthought.",
        audience=["Startups", "SMEs", "Companies with employees"],
        chips=["Payroll processing", "EPF", "ETF"],
        handle=[
            ("Payroll processing", "Salaries calculated and prepared on schedule."),
            ("EPF", "Employees' Provident Fund handled as part of the same payroll run."),
            ("ETF", "Employees' Trust Fund handled alongside EPF, not as a separate chore."),
        ],
        deliver="Payroll is prepared by our team, with EPF and ETF taken care of.",
        stay="Payroll continues each period, with changes in your team reflected as they happen.",
        faqs=[
            ("Do you handle EPF and ETF?", "Yes. Payroll management, including EPF and ETF, is one of our core services."),
            ("Is payroll only for large companies?", "No. We support businesses of different sizes, including startups and SMEs. Tell us how many people you employ and we take it from there."),
            ("How do I get started?", "Call 071 666 4111 or message us on WhatsApp. We ask a few questions and explain what we need from you."),
        ],
    ),
    dict(
        slug="tax-services", title="Tax Services", nav="Tax Services", icon="s-tax",
        short="Returns, VAT and tax planning for individuals and businesses.",
        meta="Tax services in Eheliyagoda, Sri Lanka: personal and corporate income tax, partnership and SME tax, VAT, tax planning and help with IRD notices.",
        lead="Tax returns and tax planning for individuals, partnerships, SMEs and companies, including help when an IRD notice or penalty arrives.",
        audience=["Individuals", "Partnerships", "SMEs", "Companies"],
        chips=["Personal income tax", "Corporate tax filing", "VAT"],
        handle=[
            ("Personal income tax", "Returns and tax calculation for individuals."),
            ("Corporate tax filing", "Income tax filing for companies."),
            ("Partnership & SME tax", "Tax work for partnerships and for small and medium businesses."),
            ("VAT services", "Support with VAT for businesses that need it."),
            ("Tax planning & advisory", "Looking ahead so tax is not a surprise."),
            ("IRD notices & penalties", "Help understanding and responding when a notice or penalty arrives."),
        ],
        deliver="Returns and tax documents are prepared and submitted by our team.",
        stay="Filing reminders and tax planning carry on as your income or business changes.",
        faqs=[
            ("Who can use your tax services?", "Individuals, partnerships, SMEs and companies."),
            ("I have received a notice from the IRD. Can you help?", "Yes. Contact us with the notice and we look at it with you and explain the next steps."),
            ("Is it too late to file my tax return?", "Call us and we check your position and tell you what can be done. The sooner you call, the more options there usually are."),
        ],
    ),
    dict(
        slug="company-secretarial", title="Company Secretarial Services", nav="Company Secretarial", icon="s-secretarial",
        short="Registration through annual compliance, kept in order.",
        meta="Company secretarial services in Eheliyagoda: company registration, statutory records, annual returns and corporate compliance support.",
        lead="From registering a company to keeping it compliant year after year, with the paperwork in order.",
        audience=["Startups", "SMEs", "Companies"],
        chips=["Company registration", "Annual returns", "Statutory records"],
        quote="Stay compliant. Stay organized.",
        handle=[
            ("Company registration", "Setting up a new company."),
            ("Maintaining statutory records", "The official records a company must keep, maintained for you."),
            ("Annual returns filing", "Annual returns prepared and filed."),
            ("Board & shareholder documentation", "Documents for your board and shareholders."),
            ("Corporate compliance support", "Help staying on the right side of company requirements."),
        ],
        deliver="Registrations, records and filings are prepared and submitted by our team.",
        stay="Annual returns, records and compliance support continue year after year.",
        faqs=[
            ("Can you register a new company for me?", "Yes. Company registration is part of our company secretarial service."),
            ("What are statutory records?", "The official records a company is legally required to keep up to date. We maintain them for you."),
            ("Do you help after the company is registered?", "Yes. That includes annual returns, board and shareholder documentation and ongoing compliance support."),
        ],
    ),
    dict(
        slug="business-consulting", title="Business Consulting", nav="Business Consulting", icon="s-consulting",
        short="Practical guidance for startups and SMEs.",
        meta="Business consulting in Eheliyagoda, Sri Lanka: practical guidance for startups and SMEs on setting up, structuring and growing.",
        lead="Practical guidance for startups and SMEs on setting up, structuring and growing the business.",
        audience=["Startups", "SMEs"],
        chips=["Startups", "SMEs"],
        handle=[
            ("Starting out", "Thinking through how to set the business up."),
            ("Structuring", "Arranging the business in a way that suits how you work."),
            ("Growing", "Practical next steps as the business develops."),
        ],
        deliver="Advice is given in plain language, with clear next steps.",
        stay="We stay available as the business grows and new questions come up.",
        faqs=[
            ("Who is business consulting for?", "Startups and SMEs."),
            ("How is consulting different from accounting?", "Accounting records what has happened; consulting helps you decide what to do next. We can do both."),
            ("How do I get started?", "Call 071 666 4111 or message us on WhatsApp and tell us what you are working on."),
        ],
    ),
    dict(
        slug="financial-consulting", title="Financial Consulting", nav="Financial Consulting", icon="s-financial",
        short="Clear financial insight for better decisions.",
        meta="Financial consulting in Eheliyagoda, Sri Lanka: clear financial insight to support better business decisions.",
        lead="Clear financial insight to support better business decisions.",
        audience=["Startups", "SMEs", "Companies"],
        chips=[],
        handle=[
            ("Understanding your numbers", "Making sense of where the business stands."),
            ("Supporting decisions", "Financial insight you can act on."),
            ("Planning ahead", "Looking at what the figures mean for the months to come."),
        ],
        deliver="Insights are presented clearly, in plain language.",
        stay="We keep supporting your decisions as the figures change.",
        faqs=[
            ("What does financial consulting cover?", "Clear financial insight to support better business decisions. When you call, we talk through your situation and agree what is useful."),
            ("Can it be combined with bookkeeping and tax work?", "Yes. All of our services sit with one team."),
            ("How do I get started?", "Call 071 666 4111 or message us on WhatsApp."),
        ],
    ),
]
SLUGS = {s["slug"]: s for s in SERVICES}
PRIMARY = ["accounting-bookkeeping", "tax-services", "company-secretarial", "payroll-management"]
OTHER = ["business-consulting", "financial-consulting"]

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
</defs></svg>"""


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def business_ld():
    return {
        "@context": "https://schema.org", "@type": "AccountingService", "@id": SITE_URL + "/#business",
        "name": NAME, "alternateName": "PBS", "slogan": "Your Trusted Tax & Finance Partner",
        "foundingDate": "2015", "url": SITE_URL + "/", "image": SITE_URL + "/assets/images/hero-1536.webp",
        "telephone": PHONE_TEL, "email": EMAIL,
        "sameAs": [FACEBOOK, YOUTUBE],
        "address": {"@type": "PostalAddress", "streetAddress": "240/A, Old Railway Street", "addressLocality": "Eheliyagoda", "addressCountry": "LK"},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "13:00"},
        ],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["title"], "url": f"{SITE_URL}/services/{s['slug']}/"}} for s in SERVICES]},
    }


def breadcrumb_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE_URL}/{p}"} for i, (n, p) in enumerate(trail)]}


def head(r, title, desc, path, extra=(), home=False):
    canon = f"{SITE_URL}/{path}"
    preload = f'<link rel="preload" as="image" href="{r}assets/images/hero-1536.webp" media="(min-width: 761px)">\n' if home else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js');</script>
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#06231a">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}/assets/images/hero-1536.webp">
<link rel="icon" type="image/png" href="{r}assets/images/logo-badge-512.png">
<link rel="apple-touch-icon" href="{r}assets/images/logo-badge-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Instrument+Sans:wght@400..700&display=swap" rel="stylesheet">
{preload}<link rel="stylesheet" href="{r}css/style.css">
{chr(10).join(ld(x) for x in extra)}
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
      <p class="footer-blurb">Accounting, payroll, tax and company secretarial services in Eheliyagoda, Sri&nbsp;Lanka.</p>
      <ul class="socials" data-socials aria-label="Social media"></ul>
    </div>

    <nav class="footer-col" aria-label="Company">
      <h4>Panambara</h4>
      <a href="{home}">Home</a>
      <a href="{r}about-us/">About Us</a>
      <a href="{r}contact-us/">Contact Us</a>
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

<script src="{r}js/script.js"></script>
</body>
</html>
"""


def page_hero(r, trail, h1, lead, actions=True, extra=""):
    home = r or "./"
    crumbs = [("Home", home)] + trail[:-1]
    bc = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in crumbs) + f'<li aria-current="page">{trail[-1][0]}</li>'
    act = (f'<div class="page-hero-actions"><a href="{r}contact-us/#form" class="btn btn-gold btn-lg">Book a consultation</a>'
           f'<a href="tel:{PHONE_TEL}" class="btn btn-ghost btn-lg"><svg class="i"><use href="#i-phone"/></svg>{PHONE}</a></div>') if actions else ""
    return f"""<section class="page-hero">
  <svg class="watermark watermark--dark" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container page-hero-in">
    <nav class="crumbs" aria-label="Breadcrumb"><ol>{bc}</ol></nav>
    <h1>{h1}</h1>
    <p class="page-lead">{lead}</p>
    {extra}
    {act}
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


def build_home():
    r = ""
    ld_extra = [business_ld()]
    h = head(r, f"{NAME} | Tax, Accounting & Company Secretarial, Eheliyagoda",
             "Panambara Business Solutions (PBS) is an accounting and tax practice in Eheliyagoda, Sri Lanka, established 2015. Bookkeeping, payroll (EPF/ETF), income tax, VAT, company secretarial work and business consulting.",
             "", ld_extra, home=True)
    other = "".join(
        f'<a class="other-item" href="services/{slug}/"><span class="other-ico"><svg class="i"><use href="#{SLUGS[slug]["icon"]}"/></svg></span><span><strong>{e(SLUGS[slug]["title"])}</strong><small>{e(SLUGS[slug]["short"])}</small></span><svg class="i other-arrow"><use href="#i-arrow"/></svg></a>'
        for slug in OTHER)
    cards = "".join(card(r, slug, i + 1) for i, slug in enumerate(PRIMARY))
    body = f"""{nav(r, "home")}
<main id="main">

<!-- HERO SLIDER -->
<section class="hero" id="home" aria-roledescription="carousel" aria-label="Featured services">
  <div class="hero-slides" id="slides" aria-live="off">

    <article class="slide slide--photo is-active" role="group" aria-roledescription="slide" aria-label="1 of 3: Welcome">
      <div class="slide-media">
        <picture>
          <source media="(max-width: 760px)" srcset="assets/images/hero-900.webp">
          <img src="assets/images/hero-1536.webp" width="1536" height="2048" alt="The Panambara Business Solutions team, in green PBS polo shirts, in front of the illuminated PBS sign at their Eheliyagoda office" fetchpriority="high">
        </picture>
        <div class="slide-shade"></div>
      </div>
      <div class="container slide-body">
        <p class="hero-eyebrow"><span>Panambara Business Solutions</span><i></i><span>Est. 2015</span></p>
        <h1 class="hero-title">
          <span class="line"><span>Your trusted</span></span>
          <span class="line"><em>Tax &amp; Finance Partner.</em></span>
        </h1>
      </div>
    </article>

    <article class="slide slide--text" role="group" aria-roledescription="slide" aria-label="2 of 3: Tax services">
      <svg class="slide-bars" aria-hidden="true"><use href="#bars"/></svg>
      <div class="container slide-body">
        <p class="hero-eyebrow"><span>Tax services</span></p>
        <h2 class="hero-title">
          <span class="line"><span>Simplifying</span></span>
          <span class="line"><em>Tax &amp; Business Compliance.</em></span>
        </h2>
        <p class="slide-sub">Professional support for individuals, startups and companies, for accurate tax calculation and reporting.</p>
        <ul class="hero-badges"><li>Personal income tax</li><li>Corporate tax filing</li><li>Partnership &amp; SME tax</li><li>VAT services</li></ul>
        <a href="services/tax-services/" class="btn btn-gold btn-lg slide-cta">Explore tax services <svg class="i"><use href="#i-arrow"/></svg></a>
      </div>
    </article>

    <article class="slide slide--text" role="group" aria-roledescription="slide" aria-label="3 of 3: Company secretarial">
      <svg class="slide-bars" aria-hidden="true"><use href="#bars"/></svg>
      <div class="container slide-body">
        <p class="hero-eyebrow"><span>Company secretarial</span></p>
        <h2 class="hero-title">
          <span class="line"><span>Professional</span></span>
          <span class="line"><em>Company Secretarial Services.</em></span>
        </h2>
        <p class="slide-sub">From registration to annual returns. Stay compliant. Stay organized.</p>
        <ul class="hero-badges"><li>Company registration</li><li>Statutory records</li><li>Annual returns</li><li>Board documentation</li></ul>
        <a href="services/company-secretarial/" class="btn btn-gold btn-lg slide-cta">Explore company secretarial <svg class="i"><use href="#i-arrow"/></svg></a>
      </div>
    </article>
  </div>

  <div class="pager" id="pager">
    <button type="button" class="pg is-active" aria-label="Go to slide 1: Welcome" aria-current="true"><span class="tnum">01</span><i></i></button>
    <button type="button" class="pg" aria-label="Go to slide 2: Tax services"><span class="tnum">02</span><i></i></button>
    <button type="button" class="pg" aria-label="Go to slide 3: Company secretarial"><span class="tnum">03</span><i></i></button>
    <button type="button" class="pg-toggle" id="pgToggle" aria-label="Pause slideshow"><svg class="i"><use href="#i-pause"/></svg></button>
  </div>

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
<section class="stats" aria-label="PBS at a glance">
  <div class="container">
    <p class="stats-intro reveal"><span class="eyebrow">Trusted since 2015</span>An accounting and tax practice you can walk into, on Old Railway Street in Eheliyagoda.</p>
    <dl class="stats-grid">
      <div class="reveal"><dt>Years in practice</dt><dd class="stat-num tnum" data-since="2015">{TODAY.year - 2015}</dd></div>
      <div class="reveal"><dt>Services under one roof</dt><dd class="stat-num tnum" data-count="6">6</dd></div>
      <div class="reveal"><dt>Phone lines, plus WhatsApp</dt><dd class="stat-num tnum" data-count="4">4</dd></div>
      <div class="reveal"><dt>Office open, walk-ins welcome</dt><dd class="stat-num stat-num--text">Mon&ndash;Sat</dd></div>
    </dl>
  </div>
</section>

<!-- WHY PBS -->
<section class="section why" id="why">
  <div class="container why-grid">
    <figure class="why-media reveal">
      <img src="assets/images/hero-1536.webp" width="1536" height="2048" alt="Members of the PBS team smiling in the Eheliyagoda office" loading="lazy">
    </figure>
    <div class="why-copy reveal">
      <p class="eyebrow">Why Panambara</p>
      <h2>Straightforward advice.<br><em>Careful work.</em></h2>
      <p class="lead">We look after the numbers and the filings, so owners can look after the business.</p>
      <ul class="why-list">
        <li><span class="why-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>One team for everything</strong><p>Tax, payroll, accounts and company secretarial work all sit with one team.</p></div></li>
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
      <p class="lead">Individuals, startups, SMEs and companies. Pick a service to see what it covers.</p>
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
    <ul class="rail" id="rail" aria-label="PBS video reels"></ul>
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
    cards = "".join(card(r, s["slug"], i + 1) for i, s in enumerate(SERVICES))
    h = head(r, f"Services | {NAME}", "Accounting and bookkeeping, payroll (EPF/ETF), tax, company secretarial, business consulting and financial consulting from Panambara Business Solutions in Eheliyagoda.",
             "services/", [business_ld(), breadcrumb_ld([("Home", ""), ("Services", "services/")])])
    body = f"""{nav(r, "services")}
<main id="main">
{page_hero(r, trail, "Our <em>services</em>", "Six services, one accountable team. Pick a service to see what it covers and how we work.")}
<section class="section services">
  <svg class="watermark watermark--paper" aria-hidden="true"><use href="#bars"/></svg>
  <div class="container"><div class="svc-grid svc-grid--3">{cards}</div></div>
</section>
{cta_band(r)}
</main>
"""
    write("services/index.html", h + body + footer(r))


def build_service(s):
    r = "../../"
    trail = [("Services", r + "services/"), (s["title"], "")]
    handle = "".join(
        f'<li><span class="handle-ico"><svg class="i"><use href="#i-check"/></svg></span><div><strong>{e(t)}</strong><p>{e(d)}</p></div></li>' for t, d in s["handle"])
    aud = "".join(f"<li>{e(a)}</li>" for a in s["audience"])
    steps = "".join(
        f'<li><span class="vstep-no tnum">{i + 1:02d}</span><div><h3>{e(t)}</h3><p>{e(d.format(deliver=s["deliver"], stay=s["stay"]))}</p></div></li>'
        for i, (t, d) in enumerate(STEPS))
    faqs = "".join(
        f'<details class="faq"><summary><span>{e(q)}</span><span class="svc-icon" aria-hidden="true"></span></summary><div><p>{e(a)}</p></div></details>' for q, a in s["faqs"])
    others = "".join(
        f'<li><a href="{r}services/{o["slug"]}/"><svg class="i"><use href="#{o["icon"]}"/></svg>{e(o["nav"])}<svg class="i go"><use href="#i-arrow"/></svg></a></li>'
        for o in SERVICES if o["slug"] != s["slug"])
    extra = ""
    quote = f'<p class="pull">{e(s["quote"])}</p>' if s.get("quote") else ""
    url = f"{SITE_URL}/services/{s['slug']}/"
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "description": s["lead"], "url": url,
              "provider": {"@id": SITE_URL + "/#business"}, "areaServed": {"@type": "Country", "name": "Sri Lanka"}}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]}
    h = head(r, f"{s['title']} in Eheliyagoda | {NAME}", s["meta"], f"services/{s['slug']}/",
             [business_ld(), svc_ld, faq_ld, breadcrumb_ld([("Home", ""), ("Services", "services/"), (s["title"], f"services/{s['slug']}/")])])
    body = f"""{nav(r, "svc:" + s["slug"])}
<main id="main">
{page_hero(r, trail, e(s["title"]), e(s["lead"]), extra=extra)}
<section class="section svc-page">
  <div class="container svc-layout">
    <div class="svc-main">
      <section class="block reveal">
        <h2>Who it&rsquo;s for</h2>
        <ul class="chips chips--lg">{aud}</ul>
        {quote}
      </section>

      <section class="block reveal">
        <h2>What we <em>handle</em></h2>
        <ul class="handle">{handle}</ul>
      </section>

      <section class="block reveal">
        <h2>How it <em>works</em></h2>
        <ol class="vsteps">{steps}</ol>
      </section>

      <section class="block reveal">
        <h2>Common <em>questions</em></h2>
        <div class="faqs">{faqs}</div>
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
    write(f"services/{s['slug']}/index.html", h + body + footer(r))


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
{page_hero(r, trail, "About <em>Panambara</em>", "An accounting and tax practice on Old Railway Street in Eheliyagoda, established in 2015.")}

<section class="section about-intro">
  <div class="container about-grid">
    <figure class="about-photo reveal">
      <img src="{r}assets/images/hero-1536.webp" width="1536" height="2048" alt="The Panambara Business Solutions team in green PBS polo shirts, in front of the illuminated PBS sign" loading="lazy">
      <figcaption>The PBS team at our office on Old Railway Street, Eheliyagoda.</figcaption>
    </figure>
    <div class="about-copy reveal">
      <p class="eyebrow">Who we are</p>
      <h2>Straightforward advice. <em>Careful work.</em></h2>
      <p class="lead">Panambara Business Solutions is an accounting and tax practice in Eheliyagoda, established in 2015. We look after the numbers and the filings, so owners can look after the business.</p>
      <p>Accounting, payroll, tax and company secretarial work are handled by one team that you can actually reach, by phone, on WhatsApp or in person at our office. We work with individuals, startups, SMEs and companies.</p>
      <ul class="ticks">
        <li>One team for tax, payroll, accounts and company secretarial work</li>
        <li>Filing deadlines tracked on your behalf</li>
        <li>Explained in plain language, in Sinhala or English</li>
        <li>An office you can walk into, not just a phone number</li>
      </ul>
    </div>
  </div>
</section>

<section class="section about-svc">
  <div class="container">
    <header class="section-head reveal"><p class="eyebrow">What we do</p><h2>Six services, <em>one team.</em></h2></header>
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
{page_hero(r, trail, "Let&rsquo;s talk about <em>your numbers.</em>", "Call, message us on WhatsApp or send the form below. We&rsquo;ll get back to you.", actions=False)}

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
    h = head(r, f"{title} | {NAME}", desc, f"{slug}/", [business_ld(), breadcrumb_ld([("Home", ""), (title, f"{slug}/")])])
    body = f"""{nav(r, "legal")}
<main id="main">
{page_hero(r, trail, e(title), e(intro), actions=False)}
<section class="section legal">
  <div class="container legal-in">
    <p class="legal-date">Last updated: {TODAY.strftime("%d %B %Y").lstrip("0")}</p>
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
        "Terms for using the Panambara Business Solutions website.",
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
    h = head(r, f"Page not found | {NAME}", "That page could not be found.", "404.html")
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


def build_seo_files():
    pages = [""] + ["services/"] + [f"services/{s['slug']}/" for s in SERVICES] + ["about-us/", "contact-us/", "terms-and-conditions/", "privacy-policy/"]
    urls = "".join(f"  <url><loc>{SITE_URL}/{p}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>\n" for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    build_services_index()
    for svc in SERVICES:
        build_service(svc)
    build_about()
    build_contact()
    build_legal()
    build_404()
    build_seo_files()
    print(f"built 12 pages + 404 + sitemap + robots for {SITE_URL}")
