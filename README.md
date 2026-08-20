# Decagon APAC — Founder Briefs

Account briefs for **Spencer Taylor** and **Zach Dicker**, covering DJ Gvozdenovic's APAC strategic accounts.

Static site. No build step, no dependencies. One HTML page per account plus shared `styles.css` and `app.js`.

---

## ⚠️ Read this before sharing the URL

The access word (`founders`) is enforced **client-side in `app.js`**. That is a **deterrent, not security** — anyone who views the page source can bypass it in seconds.

This content includes named executives, commercial figures, deal strategy, and on one page a reference to a contested legal matter. If the link needs to genuinely hold:

- **Use Netlify's built-in password protection** (Site configuration → Access & security → Visitor access → Password protection). That enforces at the edge, before any HTML is served. It is a paid Netlify feature and is the only option here that is actually secure.
- Or keep the repo private and share the files directly.

Treat the client-side gate as "stops a casual click-through", nothing more.

---

## Accounts

| Page | Account | State |
|---|---|---|
| `index.html` | Woolworths Group | $1.2M · S1 Discovery |
| `telstra.html` | Telstra | $1.0M · S1 Discovery |
| `iag.html` | Insurance Australia Group | $750K · S0 · Sarah Brady owns |
| `coles.html` | Coles Group | $500K · S0 · parked |
| `medhealth.html` | MedHealth | $150K · **S2 Scoping** |
| `bupa.html` | Bupa Australia | no opportunity |
| `nib.html` | nib | no opportunity |
| `teg.html` | TEG | no opportunity |
| `entain.html` | Entain ANZ | RevOps-owned |
| `wesfarmers.html` | Wesfarmers group | 5 list entries, 4 buying centres |
| `star.html` | The Star Entertainment | deprioritise — see brief |
| `neuron.html` | Neuron Mobility | **contracts expire mid-Oct** |
| `sportsbet.html` | Sportsbet | meeting: Niall Keating |
| `betfair.html` | Betfair | two entities — read first |
| `vgw.html` | VGW | $7.3B revenue, no CRM record |
| `nine.html` | Nine Entertainment Co | 2 disqualified opps |
| `foxtel.html` | Foxtel Group | 4.7M subs, 0 contacts |

---

## Editing

Content lives in the `_<slug>_main.html` partials. `build.py` wraps each one in the shared shell (head, sidebar, gate, footer) and writes the final page.

```bash
python3 build.py      # regenerates all pages
```

To add an account:
1. Write `_<slug>_main.html` (body content only — no `<html>`, no sidebar).
2. Append to `ACCOUNTS` in `build.py` and add its section nav to `NAV`.
3. Re-run `python3 build.py`.

Do **not** hand-edit the generated `*.html` files — `build.py` overwrites them.

---

## Deploying

**Netlify (recommended — it is the only route with real password protection):**
1. netlify.com → Add new site → Import from Git → pick this repo.
2. Build command: none. Publish directory: `.`
3. Site configuration → Access & security → Visitor access → set a site password.

**Or drag-and-drop:** zip the folder and drop it on app.netlify.com/drop. Fastest way to a URL; site password still needs the paid tier.

---

## Data caveats that apply site-wide

- **ZoomInfo credits are exhausted.** No enrichment, intent or scoop data. Contact discovery was impossible for Nine, Foxtel and Betfair Australia — those charts are thin because of tooling, not because the people don't exist.
- Every page carries its own **Open questions & caveats** section. Conflicting figures, unverified titles and contaminated records are flagged inline rather than silently resolved.
- Figures marked with a source chip (`SFDC`, `ZI`, `public`) indicate provenance. Unmarked structural claims need confirming before being quoted to a customer.

Compiled 19 August 2026.
