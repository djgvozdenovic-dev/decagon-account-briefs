#!/usr/bin/env python3
"""Builds the Decagon APAC founder-brief microsite.
One HTML page per account, shared styles.css / app.js.
Add an account: append to ACCOUNTS, drop a _<slug>_main.html beside it, re-run.
"""
import os

# slug, display name, status: 'live' | 'queued', short sidebar label
ACCOUNTS = [
    ("woolworths", "Woolworths Group",          "live",   "Woolworths Group"),
    ("telstra",    "Telstra",                   "live",   "Telstra"),
    ("iag",        "Insurance Australia Group", "live",   "Insurance Australia Grp"),
    ("coles",      "Coles Group",               "live",   "Coles Group"),
    ("medhealth",  "MedHealth",                 "live",   "MedHealth"),
    ("bupa",       "Bupa Australia",            "live",   "Bupa Australia"),
    ("nib",        "nib",                       "live",   "nib"),
    ("teg",        "TEG",                       "live",   "TEG"),
    ("entain",     "Entain ANZ",                "live",   "Entain ANZ"),
    ("wesfarmers", "Wesfarmers group",          "live",   "Wesfarmers group"),
    ("star",       "The Star Entertainment",    "live",   "The Star Entertainment"),
    ("neuron",     "Neuron Mobility",           "live",   "Neuron Mobility"),
    ("sportsbet",  "Sportsbet",                 "live",   "Sportsbet"),
    ("betfair",    "Betfair",                   "live",   "Betfair"),
    ("vgw",        "VGW",                       "live",   "VGW"),
    ("nine",       "Nine Entertainment Co",     "live",   "Nine Entertainment"),
    ("foxtel",     "Foxtel Group",              "live",   "Foxtel Group"),
    ("whitespace", "Whitespace accounts",       "queued", "Whitespace (9)"),
]

# per-account in-page section nav: (anchor, label)
NAV = {
    "woolworths": [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel"), ("timeline","Timeline"), ("gaps","Open questions")],
    "vgw":        [("situation","Where we are"), ("governance","Ownership & governance"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Brands & structure"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("gaps","Open questions")],
    "betfair":    [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("gaps","Open questions")],
    "nine":       [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("gaps","Open questions")],
    "foxtel":     [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("gaps","Open questions")],
    "sportsbet":  [("meeting","Meeting prep — Niall Keating"), ("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "neuron":     [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Structure & the merger"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "star":       [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Star vs Crown"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "wesfarmers": [("situation","Where we are"), ("structure","Structure & ownership"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "entain":     [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "teg":        [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Investor & network hooks"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "nib":        [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "bupa":       [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "medhealth":  [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "coles":      [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "iag":        [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
    "telstra":    [("situation","Where we are"), ("asks","Suggestions to move forward"),
                   ("org","Org chart & scorecard"), ("meddpicc","MEDDPICC & deal health"),
                   ("brands","Group structure"), ("routes","Warm-intro routes"),
                   ("intel","Deal intel & competition"), ("timeline","Timeline"),
                   ("gaps","Open questions")],
}

HEAD = '''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{name} — Founder Brief | Decagon APAC</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap">
<link rel="stylesheet" href="styles.css">
<script>
// Applied before first paint so no content flashes before the gate.
(function(){{var K='dcg-briefs-ok',H=1358338935;try{{if(sessionStorage.getItem(K)===String(H))return;}}catch(e){{}}
document.documentElement.className+=' gated';}})();
</script>
</head>
<body>

<div id="gate">
  <div class="gate-card">
    <div class="brand">
      <div class="brand-mark">D</div>
      <div>
        <div class="brand-text">Founder Briefs</div>
        <div class="brand-sub">Decagon · APAC Strategic</div>
      </div>
    </div>
    <h1>Internal &amp; confidential</h1>
    <p>Enter the access word to continue.</p>
    <div class="gate-row">
      <input id="gatePw" type="password" placeholder="Access word" autocomplete="off" spellcheck="false">
      <button id="gateGo" type="button">Enter</button>
    </div>
    <div id="gateErr"></div>
    <div class="gate-foot">Contains named individuals, commercial figures and account strategy. Do not forward outside Decagon.</div>
  </div>
</div>

<div class="mtop">
  <button id="navBtn" type="button" aria-label="Open account menu" aria-expanded="false">&#9776;</button>
  <div class="brand-mark">D</div>
  <div class="mtop-title">{name}</div>
</div>
<div id="navScrim"></div>

<div class="shell">
'''

def sidebar(cur):
    rows = []
    for slug, name, status, label in ACCOUNTS:
        live = status == "live"
        href = f"{slug}.html" if slug != "woolworths" else "index.html"
        cls = ' aria-current="true"' if slug == cur else ''
        tag = "Live" if live else "Queued"
        if live:
            rows.append(f'        <a class="acct" data-ready="yes" href="{href}"{cls}>'
                        f'<span class="dot"></span> {label} <span class="tag">{tag}</span></a>')
        else:
            rows.append(f'        <span class="acct is-off"><span class="dot"></span> {label} '
                        f'<span class="tag">{tag}</span></span>')
    jump = "\n".join(f'        <a href="#{a}">{l}</a>' for a, l in NAV.get(cur, []))
    return f'''  <aside>
    <div class="brand">
      <div class="brand-mark">D</div>
      <div>
        <div class="brand-text">Founder Briefs</div>
        <div class="brand-sub">Decagon · APAC Strategic</div>
      </div>
    </div>

    <div>
      <div class="side-label">Accounts</div>
      <div class="acct-list">
{chr(10).join(rows)}
      </div>
    </div>

    <div>
      <div class="side-label">On this page</div>
      <nav class="jump">
{jump}
      </nav>
    </div>

    <div class="side-foot">
      <button class="tbtn" id="themeBtn" type="button">
        <span id="themeIcon">◐</span> <span id="themeLbl">Dark mode</span>
      </button>
      <div class="stamp">
        Compiled 19 Aug 2026<br>
        Salesforce · Slack · ZoomInfo<br>Granola · Gmail · public filings<br>
        <strong>Internal &amp; confidential</strong>
      </div>
    </div>
  </aside>
'''

FOOT = '''  </main>
</div>
<script src="app.js"></script>
</body>
</html>
'''

def build():
    for slug, name, status, label in ACCOUNTS:
        src = f"_{slug}_main.html"
        if not os.path.exists(src):
            continue
        out = "index.html" if slug == "woolworths" else f"{slug}.html"
        body = open(src).read()
        html = HEAD.format(name=name) + sidebar(slug) + "  <main>\n" + body + "\n" + FOOT
        open(out, "w").write(html)
        print("built", out, len(html))

if __name__ == "__main__":
    build()
