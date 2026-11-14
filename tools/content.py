"""Page content for the PBS website: services, FAQs and headline numbers.

Wording rules (from the AEO/GEO method): the business name is used instead of pronouns, answers
open with the answer, FAQ answers are 30-50 words, and nothing is stated that the owner has not
supplied. Items marked [draft] were written from the owner's short brief and are listed in
CONTENT_REVIEW.md for confirmation.
"""

CONTENT_UPDATED = "14 November 2026"      # change only when the content really changes
CONTENT_UPDATED_ISO = "2026-11-14"
LEGAL_UPDATED = "6 November 2026"

# Headline numbers supplied by the owner (shown exactly as given).
STATS = [
    # label, count, suffix, text shown without JavaScript
    ("Business registrations", 750, "+", "750+"),
    ("Local clients", 1500, "+", "1,500+"),
    ("Social media engagements", 200, "K+", "200K+"),
    ("Consultations", 2000, "+", "2,000+"),
]
STATS_SOURCE = "Figures supplied by Panambara Business Solutions, as of November 2026."

HOME_OVERVIEW = ("Panambara Business Solutions is an accounting, tax and business services practice in Eheliyagoda, Sri Lanka, "
                 "established in 2015. It supports individuals, startups, SMEs, partnerships and companies with taxation, accounting, "
                 "audit, business advisory, corporate compliance, payroll, web development and digital marketing.")

STEPS = [
    ("Talk to us", "Call or message us on WhatsApp and tell us what you need."),
    ("We review", "We look at your records and requirements, then explain what is needed and what it involves."),
    ("We prepare & file", "{deliver}"),
    ("We stay on", "{stay}"),
]

SERVICES = [
    dict(
        slug="taxation-tax-consultancy", title="Taxation & Tax Consultancy", nav="Taxation & Tax Consultancy", icon="s-tax",
        short="Corporate tax, personal income tax, VAT, APIT, WHT and compliance.",
        meta="Taxation and tax consultancy in Eheliyagoda: corporate tax, personal income tax, VAT, APIT, WHT, tax compliance and IRD notice support.",
        overview=("Panambara Business Solutions provides taxation and tax consultancy in Eheliyagoda, Sri Lanka. It prepares corporate tax and "
                  "personal income tax returns, supports VAT, APIT and withholding tax (WHT) obligations, and handles tax compliance for individuals, "
                  "partnerships, SMEs and companies. It also advises on tax planning and helps when an IRD notice arrives."),
        audience=["Individuals", "Partnerships", "SMEs", "Companies"],
        chips=["Corporate tax", "Personal income tax", "VAT"],
        handle=[
            ("Corporate tax", "Income tax returns and tax work for companies."),
            ("Personal income tax", "Returns and tax calculation for individuals."),
            ("VAT", "Support with Value Added Tax for businesses that need it."),
            ("APIT", "Advance Personal Income Tax for employers who deduct tax from employees' pay."),
            ("WHT", "Withholding tax obligations on payments your business makes."),
            ("Tax compliance", "Keeping your returns and filings in order."),
            ("Partnership & SME tax", "Tax work for partnerships and for small and medium businesses."),
            ("Tax planning & advisory", "Looking ahead so tax is not a surprise."),
            ("IRD notices & penalties", "Help understanding and responding when a notice or penalty arrives."),
        ],
        deliver="Returns and tax documents are prepared and submitted by our team.",
        stay="Filing reminders and tax planning carry on as your income or business changes.",
        faqs=[
            ("What does APIT mean in Sri Lanka?",
             "APIT stands for Advance Personal Income Tax. Employers deduct it from employees' pay and pay it to the Inland Revenue Department. Panambara Business Solutions can support APIT obligations alongside payroll. Call 071 666 4111 to discuss your situation."),
            ("What is withholding tax, or WHT?",
             "Withholding tax (WHT) is tax deducted at source from certain payments and paid to the Inland Revenue Department. Which payments it applies to depends on current law. Panambara Business Solutions can review your payments and explain what applies."),
            ("Who can use Panambara's tax services?",
             "Individuals, partnerships, SMEs and companies can use our tax services. We prepare personal income tax and corporate tax returns, support VAT, APIT and WHT, and help with tax planning. Contact us with your situation and we confirm what you need."),
            ("Can you help if I received an IRD notice?",
             "Yes. Contact Panambara Business Solutions with the notice and we look at it with you and explain the next steps. Call 071 666 4111 or message us on WhatsApp so we can see the notice as soon as possible."),
            ("Is it too late to file my tax return?",
             "Call us and we check your position and explain what can be done. Panambara Business Solutions cannot promise a particular outcome, but the sooner you contact us, the more options there usually are."),
        ],
    ),
    dict(
        slug="financial-management-accounting", title="Financial Management & Accounting", nav="Financial Management & Accounting", icon="s-financial",
        short="Financial reporting, management accounts, budgeting and cash flow.",
        meta="Financial management and accounting in Eheliyagoda: financial reporting, management accounts, budgeting, forecasting, cash flow and bookkeeping.",
        overview=("Panambara Business Solutions provides financial management and accounting in Eheliyagoda, Sri Lanka. It keeps day-to-day books, prepares "
                  "financial reporting and management accounts, and supports budgeting, forecasting and cash flow management for startups, SMEs, "
                  "partnerships and companies, so owners can see exactly where the business stands."),
        audience=["Startups", "SMEs", "Partnerships", "Companies"],
        chips=["Financial reporting", "Budgeting", "Cash flow"],
        handle=[
            ("Financial reporting", "Financial statements prepared from your records."),
            ("Management accounts", "Regular figures that show how the business is performing."),
            ("Budgeting", "Plans for income and spending."),
            ("Forecasting", "A view of where the numbers are heading."),
            ("Cash flow management", "Keeping track of money coming in and going out."),
            ("Day-to-day bookkeeping", "Transactions recorded accurately and kept up to date."),
        ],
        deliver="Books are kept and reports prepared by our team.",
        stay="Bookkeeping and reporting carry on month after month as your business grows.",
        faqs=[
            ("What are management accounts?",
             "Management accounts are internal financial reports that show how a business is performing, usually more often than annual statements. They help owners make decisions. Panambara Business Solutions can prepare them from your records. Contact us to agree what you need."),
            ("What does financial reporting include?",
             "Financial reporting means preparing financial statements from your accounting records. They show what a business owns, owes and earns. Panambara Business Solutions prepares them for startups, SMEs, partnerships and companies. Call us to confirm the format you need."),
            ("Do you provide bookkeeping as well?",
             "Yes. Day-to-day bookkeeping is part of our financial management and accounting service. We record your transactions and keep your books up to date, so your reports and tax filings come from consistent records."),
            ("Can you help with budgeting and cash flow?",
             "Yes. We support budgeting, forecasting and cash flow management, so owners can plan income and spending and see how much money is coming in and going out. Contact Panambara Business Solutions to discuss your business."),
        ],
    ),
    dict(
        slug="audit-assurance", title="Audit & Assurance", nav="Audit & Assurance", icon="s-audit",
        short="Internal audits, financial statement reviews and risk assessments.",
        meta="Audit and assurance support in Eheliyagoda: internal audits, financial statement reviews, audit queries and risk assessments for SMEs and companies.",
        overview=("Panambara Business Solutions offers audit and assurance support in Eheliyagoda, Sri Lanka. Services include internal audits, financial "
                  "statement reviews, help with audit queries and risk assessments for SMEs, partnerships and companies, giving owners and stakeholders "
                  "more confidence in their numbers and controls."),
        audience=["SMEs", "Partnerships", "Companies"],
        chips=["Internal audits", "Statement reviews", "Risk assessments"],
        handle=[
            ("Internal audits", "Checks on your processes and controls."),
            ("Financial statement reviews", "A review of your financial statements."),
            ("Audit queries", "Help responding to questions raised during an audit."),
            ("Risk assessments", "Identifying where the business is exposed."),
        ],
        deliver="Reviews and findings are prepared and explained by our team.",
        stay="Follow-up support carries on as your business and its risks change.",
        faqs=[
            ("What is an internal audit?",
             "An internal audit is a review of a business's processes, records and controls to check they work as intended and to find risks or weaknesses. Panambara Business Solutions carries out internal audits for SMEs and companies. Contact us to discuss scope."),
            ("What is a financial statement review?",
             "A financial statement review examines a company's financial statements for accuracy and reasonableness, giving owners and stakeholders more confidence in the figures. Panambara Business Solutions offers these reviews. Contact us to confirm what your situation requires."),
            ("Can you help with audit queries?",
             "Yes. If an auditor or authority raises questions about your accounts, Panambara Business Solutions can help you understand them and prepare responses from your records. Call 071 666 4111 or message us on WhatsApp with the details."),
            ("Is audit and assurance only for large companies?",
             "No. Panambara Business Solutions supports SMEs and partnerships as well as companies. The right scope depends on your business, so contact us with your situation and we explain which review or audit support fits."),
        ],
    ),
    dict(
        slug="business-advisory-consultancy", title="Business Advisory & Consultancy", nav="Business Advisory & Consultancy", icon="s-consulting",
        short="Business registration, financial planning, business plans and investment appraisals.",
        meta="Business advisory and consultancy in Eheliyagoda: business registration, financial planning, business plans and investment appraisals for startups and SMEs.",
        overview=("Panambara Business Solutions provides business advisory and consultancy in Eheliyagoda, Sri Lanka. It helps startups and SMEs with business "
                  "registration, financial planning, business plans and investment appraisals, giving owners clear, practical guidance on setting up, "
                  "structuring and growing a business."),
        audience=["Startups", "SMEs", "Companies"],
        chips=["Business registration", "Business plans"],
        handle=[
            ("Business registration", "Registering a new business."),
            ("Financial planning", "Planning the money side of the business."),
            ("Business plans", "A written plan for your business."),
            ("Investment appraisals", "Assessing whether an investment makes financial sense."),
        ],
        deliver="Advice and documents are prepared in plain language, with clear next steps.",
        stay="We stay available as the business grows and new questions come up.",
        faqs=[
            ("Can you help register a new business?",
             "Yes. Business registration is part of our advisory service, and company registration is also covered under corporate compliance. Contact Panambara Business Solutions with your plans and we explain the steps and what you need to provide."),
            ("What is an investment appraisal?",
             "An investment appraisal assesses whether a planned investment is likely to make financial sense by comparing expected costs and returns. Panambara Business Solutions prepares investment appraisals for businesses weighing a new project or purchase. Contact us to discuss yours."),
            ("Do you help write business plans?",
             "Yes. Panambara Business Solutions helps startups and SMEs prepare business plans, including the financial side. Share your idea with us and we confirm what the plan needs to cover before we start."),
            ("How is consultancy different from accounting?",
             "Accounting records what has already happened, while consultancy helps you decide what to do next. Panambara Business Solutions offers both, so advice is based on your real figures. Contact us to discuss which you need."),
        ],
    ),
    dict(
        slug="corporate-compliance", title="Corporate Compliance & Regulatory Affairs", nav="Corporate Compliance", icon="s-secretarial",
        short="ROC compliance, company secretarial matters and statutory reporting.",
        meta="Corporate compliance and company secretarial services in Eheliyagoda: ROC compliance, company registration, annual returns and statutory reporting.",
        overview=("Panambara Business Solutions provides corporate compliance and company secretarial services in Eheliyagoda, Sri Lanka. It handles company "
                  "registration, Registrar of Companies (ROC) compliance, statutory records, annual returns, board and shareholder documentation and "
                  "statutory reporting, helping companies stay compliant and organized year after year."),
        audience=["Startups", "SMEs", "Companies"],
        chips=["ROC compliance", "Annual returns", "Statutory records"],
        quote="Stay compliant. Stay organized.",
        handle=[
            ("ROC compliance", "Meeting Registrar of Companies requirements."),
            ("Company secretarial matters", "Day-to-day company secretarial work."),
            ("Statutory reporting", "Reports a company is required to prepare."),
            ("Company registration", "Setting up a new company."),
            ("Maintaining statutory records", "The official records a company must keep, maintained for you."),
            ("Annual returns filing", "Annual returns prepared and filed."),
            ("Board & shareholder documentation", "Documents for your board and shareholders."),
            ("Corporate compliance support", "Help staying on the right side of company requirements."),
        ],
        deliver="Registrations, records and filings are prepared and submitted by our team.",
        stay="Annual returns, records and compliance support continue year after year.",
        faqs=[
            ("What is ROC compliance?",
             "ROC compliance means meeting the requirements of the Registrar of Companies in Sri Lanka, such as keeping company details current and filing required documents like annual returns. Panambara Business Solutions helps companies manage these obligations. Contact us about your situation."),
            ("Can you register a new company for me?",
             "Yes. Company registration is part of our corporate compliance and company secretarial service. Contact Panambara Business Solutions with your plans and we explain the steps and the documents you need to provide."),
            ("What are statutory records?",
             "Statutory records are the official records a company is legally required to keep up to date. Panambara Business Solutions maintains them for you as part of our company secretarial service, so they stay accurate and ready when needed."),
            ("Do you help after the company is registered?",
             "Yes. After registration, Panambara Business Solutions helps with annual returns, board and shareholder documentation, statutory reporting and ongoing compliance support, so the company stays compliant and organized. Contact us to discuss what your company needs."),
        ],
    ),
    dict(
        slug="payroll-management", title="Payroll Management (EPF / ETF)", nav="Payroll (EPF / ETF)", icon="s-payroll",
        short="Payroll on schedule, with EPF and ETF handled.",
        meta="Payroll management in Eheliyagoda, Sri Lanka, including EPF and ETF, for startups, SMEs and companies.",
        overview=("Panambara Business Solutions provides payroll management in Eheliyagoda, Sri Lanka, including EPF and ETF. It prepares payroll on schedule for "
                  "startups, SMEs and companies, so salaries and statutory contributions are handled together by one team rather than as separate, "
                  "last-minute tasks."),
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
            ("What are EPF and ETF in Sri Lanka?",
             "EPF is the Employees' Provident Fund and ETF is the Employees' Trust Fund. Employers in Sri Lanka contribute to both for eligible employees. Panambara Business Solutions handles EPF and ETF as part of payroll management. Contact us for your business."),
            ("Do you handle EPF and ETF?",
             "Yes. Payroll management, including EPF and ETF, is one of our core services. Panambara Business Solutions prepares payroll and handles both contributions together, so your statutory obligations are covered in one process."),
            ("Is payroll only for large companies?",
             "No. Panambara Business Solutions supports businesses of different sizes, including startups and SMEs. Tell us how many people you employ and we take it from there. Contact us to discuss how payroll would work for your team."),
            ("Can payroll include APIT?",
             "Payroll often involves APIT, the tax deducted from employees' pay. Panambara Business Solutions offers APIT support under its tax service, so payroll and tax can be handled together. Ask us how that works for your team."),
        ],
    ),
    dict(
        slug="web-development", title="Web Development", nav="Web Development", icon="s-web",
        short="Business websites that are mobile-friendly and easy to find.",
        meta="Web development in Eheliyagoda, Sri Lanka: mobile-friendly business websites with clear service pages, WhatsApp and call buttons and a search-friendly structure.",
        overview=("Panambara Business Solutions builds business websites in Eheliyagoda, Sri Lanka. Its web development service creates mobile-friendly sites with "
                  "clear service pages, call and WhatsApp enquiry buttons and a search-friendly structure, so customers can find a business and contact "
                  "it easily."),
        audience=["Startups", "SMEs", "Companies", "Professionals"],
        chips=["Business websites", "Mobile-friendly"],
        handle=[
            ("Business websites", "A site that presents your business and services clearly."),
            ("Mobile-friendly design", "Pages that work well on phones, where many customers browse."),
            ("Enquiry buttons", "Call, WhatsApp and contact options on every page."),
            ("Search-friendly structure", "Page structure that helps people and search engines find your services."),
            ("Location and contact details", "Your address, hours and map so local customers can find you."),
        ],
        deliver="The website is designed, built and prepared for launch by our team.",
        stay="We stay available for changes as your business and services change.",
        faqs=[
            ("Do you build websites for small businesses?",
             "Yes. Panambara Business Solutions builds business websites for startups, SMEs and companies, with clear service pages and easy ways for customers to call or message. Contact us with your business details and what you want the site to do."),
            ("Will my website work on mobile phones?",
             "Yes. We design websites to work well on phones as well as computers, because many customers browse on mobile. Contact Panambara Business Solutions to discuss the pages and features your business needs."),
            ("Can my website include WhatsApp and call buttons?",
             "Yes. We add call, WhatsApp and contact options so customers can reach your business in one tap. Panambara Business Solutions can also show your address, hours and map. Contact us to discuss your site."),
            ("Can you help customers find my website on Google?",
             "We build sites with a search-friendly structure and can set up your Google Business Profile so local customers find you. No one can promise a specific search ranking. Contact Panambara Business Solutions to discuss your goals."),
        ],
    ),
    dict(
        slug="digital-marketing", title="Digital Marketing", nav="Digital Marketing", icon="s-marketing",
        short="Facebook, LinkedIn, TikTok and Google profile set-up and management.",
        meta="Digital marketing in Eheliyagoda, Sri Lanka: Facebook, LinkedIn, TikTok and Google Business Profile set-up and management for businesses.",
        overview=("Panambara Business Solutions provides digital marketing in Eheliyagoda, Sri Lanka. It sets up and manages business profiles on Facebook, LinkedIn, "
                  "TikTok and Google, so customers can find, recognize and contact a business, with consistent branding and contact details across "
                  "every channel."),
        audience=["Startups", "SMEs", "Companies", "Professionals"],
        chips=["Facebook", "LinkedIn", "TikTok", "Google"],
        handle=[
            ("Facebook page", "Set-up and management of your business page."),
            ("LinkedIn page", "A professional company presence."),
            ("TikTok profile", "A business profile and short-video presence."),
            ("Google Business Profile", "Your listing on Google Search and Maps."),
            ("Consistent business details", "Name, address and phone number matching across channels."),
            ("Content and posting", "Planned posts that fit your brand."),
        ],
        deliver="Profiles are set up, branded and kept active by our team.",
        stay="Posting and profile management carry on month after month.",
        faqs=[
            ("Which social media platforms do you manage?",
             "Panambara Business Solutions sets up and manages business profiles on Facebook, LinkedIn and TikTok, plus a Google Business Profile. Contact us to choose the channels that suit your customers and your budget."),
            ("What is a Google Business Profile?",
             "A Google Business Profile is a free listing that shows a business's name, address, phone number, hours and reviews on Google Search and Maps. Panambara Business Solutions can set up and manage yours. Contact us to get started."),
            ("Why should business details match across profiles?",
             "Matching name, address and phone number across your website, Google profile and social pages helps customers trust you and helps search and AI tools recognize your business correctly. We keep these details consistent for you."),
            ("Can you create posts for my business pages?",
             "Yes. We can plan and publish posts on your business pages so they stay active and consistent with your brand. Tell Panambara Business Solutions about your business and we agree what suits you."),
        ],
    ),
]

SERVICE_PHOTO = {
    "taxation-tax-consultancy": "card-4", "financial-management-accounting": "card-1", "audit-assurance": "card-6",
    "business-advisory-consultancy": "card-5", "corporate-compliance": "card-3", "payroll-management": "card-1",
    "web-development": "card-6", "digital-marketing": "card-5",
}
PRIMARY = ["taxation-tax-consultancy", "financial-management-accounting", "audit-assurance", "business-advisory-consultancy"]
OTHER = ["corporate-compliance", "payroll-management", "web-development", "digital-marketing"]

_LOCATION = ("Panambara Business Solutions is at 240/A, Old Railway Street, Eheliyagoda, Sri Lanka. The office is open Monday to Friday, "
             "9:00 am to 5:00 pm, and Saturday, 9:00 am to 1:00 pm. It is closed on Sunday.")
_CONTACT = ("Call or WhatsApp 071 666 4111, or call 070 167 9811, 074 244 8951 or 036 226 0888. You can also email info@panambara.lk or use the "
            "contact form, which opens WhatsApp or your email app with your message ready.")
_COST = ("Fees depend on the work involved, so Panambara Business Solutions confirms the scope and fee with you directly. Call 071 666 4111 or message "
         "us on WhatsApp with what you need, and we explain how fees work for your case.")


def common_faqs(s):
    """Questions every service page answers: cost, location and how to get in touch."""
    return [
        (f"How much do {s['nav']} services cost?", _COST),
        ("Where is Panambara Business Solutions located?", _LOCATION),
        ("How do I contact Panambara Business Solutions?", _CONTACT),
    ]


FAQ_GENERAL = [
    ("What services does Panambara Business Solutions offer?",
     "Panambara Business Solutions offers taxation, financial management and accounting, audit and assurance, business advisory, corporate compliance, payroll management, web development and digital marketing from its office in Eheliyagoda, Sri Lanka."),
    ("Where is Panambara Business Solutions located?", _LOCATION),
    ("What are the office hours of Panambara Business Solutions?",
     "The office is open Monday to Friday from 9:00 am to 5:00 pm and on Saturday from 9:00 am to 1:00 pm. It is closed on Sunday. You can call or message us on WhatsApp at 071 666 4111."),
    ("How do I book a consultation with Panambara Business Solutions?",
     "Call or WhatsApp 071 666 4111, or use the contact form on this website. The form opens WhatsApp or your email app with your message ready to send. Tell us what you need and we arrange the next step."),
    ("Who does Panambara Business Solutions work with?",
     "Panambara Business Solutions works with individuals, startups, SMEs, partnerships and companies. Whether you need a personal tax return, payroll, company registration or a business website, one team in Eheliyagoda handles it."),
    ("When was Panambara Business Solutions established?",
     "Panambara Business Solutions was established in 2015. It operates from Old Railway Street in Eheliyagoda, Sri Lanka, and provides tax, accounting, compliance, advisory, payroll and digital services to individuals and businesses."),
    ("Does Panambara Business Solutions offer web development and digital marketing?",
     "Yes. Panambara Business Solutions builds business websites and sets up and manages business profiles on Facebook, LinkedIn, TikTok and Google, so customers can find and contact a business easily. Contact us to discuss your needs."),
    ("Can Panambara Business Solutions help with a tax return?",
     "Yes. Panambara Business Solutions prepares personal income tax and corporate tax returns and supports VAT, APIT and withholding tax. Call 071 666 4111 or message us on WhatsApp with your situation and we confirm what you need."),
    ("Do you handle EPF and ETF for employers?",
     "Yes. Panambara Business Solutions handles Employees' Provident Fund (EPF) and Employees' Trust Fund (ETF) as part of payroll management for startups, SMEs and companies. Call us to discuss your team."),
    ("Can you help me register a company?",
     "Yes. Company registration is part of our corporate compliance service, and business registration is covered in business advisory. Contact Panambara Business Solutions and we explain the steps and what you need to provide."),
    ("Can you help if I received an IRD notice?",
     "Yes. Contact Panambara Business Solutions with the notice and we look at it with you and explain the next steps. Call 071 666 4111 or message us on WhatsApp so we can see the notice as soon as possible."),
    ("How much do your services cost?", _COST),
]
HOME_FAQ_PICK = [0, 2, 3, 4, 6, 7]   # which FAQ_GENERAL entries the home page shows
