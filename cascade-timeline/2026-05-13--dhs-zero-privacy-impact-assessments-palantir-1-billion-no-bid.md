---
type: timeline_event
id: 2026-05-13--dhs-zero-privacy-impact-assessments-palantir-1-billion-no-bid
date: '2026-05-13'
title: "DHS Privacy Impact Assessment Filings Collapse in 2026 While the Agency Operates a $1B No-Bid Palantir Surveillance Network"
importance: 9
status: disputed
tags:
  - surveillance
  - government-contracts
  - no-bid-contract
  - dhs
  - ice
  - institutional-capture
  - procurement-abuse
  - privacy-violation
actors:
  - Department of Homeland Security
  - Palantir Technologies
  - CBP
  - ICE
  - FEMA
  - CISA
sources:
  - title: "DHS Surveillance Shopping Spree: What $1 Billion Buys From Palantir"
    url: https://stateofsurveillance.org/news/dhs-billion-dollar-palantir-ai-surveillance-shopping-spree-2026/
    publisher: State of Surveillance
    date: '2026-05-13'
    tier: 2
  - title: "Goldman, Wyden, Velázquez Demand Answers on ICE Use of Palantir-developed Technologies to Fuel Mass Surveillance"
    url: https://goldman.house.gov/media/press-releases/goldman-wyden-velazquez-demand-answers-ice-use-palantir-developed-technologies
    publisher: Office of Rep. Daniel Goldman
    date: '2026-04-14'
    tier: 2
  - title: "DHS AI Surveillance Arsenal Grows as Agency Defies Courts"
    url: https://www.techpolicy.press/dhs-ai-surveillance-arsenal-grows-as-agency-defies-courts/
    publisher: Tech Policy Press
    date: '2026-05-13'
    tier: 2
  - title: "All the Ways Palantir is Assisting Trump's Abusive Removal Campaign"
    url: https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup
    publisher: ACLU
    date: '2026-05-01'
    tier: 2
---

DHS posted five new or updated Privacy Impact Assessments (PIAs) dated 2026 through early October, against 51 in 2024 and 22 in 2025 on the same document count (DHS's own PDFs, re-audited 2026-10-08): a steep decline, not zero. Federal law — the E-Government Act of 2002 — requires agencies to file a PIA before developing or procuring any IT system that collects or disseminates information about the public, including when the agency intends to identify U.S. citizens alongside other data elements. The privacy-assessment blackout is concurrent with DHS's $1 billion Palantir deal signed in February 2026, which grants every major DHS component — CBP, ICE, FEMA, CISA — access to Palantir's surveillance platforms without competitive bidding. Documents reveal DHS plans to spend additional hundreds of millions on AI-powered mobile surveillance trucks and 198 border watch towers within the same umbrella arrangement. The DHS Inspector General has accused the agency of "obstructing audits" of biometric data management and immigration enforcement activities.

The 2026 decline in PIA postings runs alongside the Palantir procurement expansion; no PIA was found for ELITE or ImmigrationOS on DHS's component pages (bounded search, 2026-10-08).

## Sourcing note — 2026-08-28 pattern-projection audit

The phrase **"without competitive bidding"** applied to the February 2026 DHS Palantir arrangement needs qualifying against the vehicle's own contracting record.

The arrangement is **PIID `70RTAC26A00000001`**, a **single-award Blanket Purchase Agreement** signed 2026-02-12 with a five-year ordering period to 2031-02-11, recipient Palantir Technologies Inc. (UEI FSY4LVSBGWB7), placed against **GSA Federal Supply Schedule contract `47QTCA24D004L`** (FSS, MULTIPLE AWARD). Its FPDS competition fields read `extent_competed` = **"A" (FULL AND OPEN COMPETITION)** and `solicitation_procedures` = **"MAFO"** — but **`number_of_offers_received` = 1**, and `fair_opportunity_limited_sources` and `other_than_full_and_open` are both null.

So the accurate statement is narrower and, if anything, more damning than "no-bid": DHS ran the award as a *formally competitive* fair-opportunity solicitation off the GSA schedule and **received exactly one bid**. It is not coded non-competitive in FPDS, so a flat "no-bid" or "without competitive bidding" characterization is contestable on the record — a hostile reader with the FPDS printout can say the entry is wrong. Preferred phrasing: *"a single-award BPA that drew one offer."*

**Also distinguish obligated from ceiling.** The BPA base itself shows **$0 total obligation** — normal for a BPA. Actual money moves through calls against it: `70CTD026FC0000012` ($86,271,599.30, ERO modernization) and `70CTD026FC0000018` ($45,848,616.80, HSI/ICM modernization) are the two largest on the record as of this audit — roughly **$132M obligated**, not $1B. The "$1 billion" is a ceiling/press figure, not money committed. Do not write "$1 billion contract" without the ceiling qualifier.

The entry's central claim — zero PIAs filed in 2026 against 24 in 2024 and 8 in 2025 — is untouched by this note and was not re-audited here. **Re-audited 2026-10-08: the zero figure is false** — five 2026 PIAs on DHS's server (e.g. DHS/ICE/PIA-067, https://www.dhs.gov/sites/default/files/2026-01/26_0129_priv_pia-ice-067-bondmanagement.pdf; DHS/USSS/PIA-034, https://www.dhs.gov/sites/default/files/2026-07/26_0729_privacy-usss-pia034-helix.pdf); the 24/8 baselines match DHS's library listing, not a document count. The body above was corrected; the filename/id keep the old slug so links resolve.

---

## MATERIAL CORRECTION, 2026-09-20 — the "zero" figure is WRONG

**The central claim of this entry — that DHS filed ZERO Privacy Impact Assessments in 2026 — is false**, and the title has been changed accordingly. Status downgraded to `disputed` pending a full re-audit.

**How it was caught.** A fact-checker working a draft that cited this entry ([[drafts/anthropic-refused-lin-ruling]]) went to dhs.gov rather than to this note, and found published 2026 PIAs. Independently re-verified here the same day:

- **DHS/USSS/PIA-034 (HELIX)**, dated **2026-07-29** — `https://www.dhs.gov/sites/default/files/2026-07/26_0729_privacy-usss-pia034-helix.pdf` returns **HTTP 200**, a 587,549-byte PDF, served from a `2026-07/` path. A Secret Service assessment covering video and image data for protective and law-enforcement missions.
- A DHS Office of Health Affairs PIA on a `2026-05/` path, also HTTP 200.
- A bond-process PIA reported as updated 2026-01-29.

At least three, therefore, not zero.

**Why the error survived this long — the instructive part.** The DHS **index page** (`dhs.gov/privacy-impact-assessments`) lists no 2026 publications even though the documents exist at 2026-dated paths on DHS's own server. Anyone checking the index rather than searching for the documents would conclude, reasonably and wrongly, that the year was empty. **An agency index is not the agency's record.** This is [[feedback_absence_in_wrong_document]] exactly: a zero-hit search only proves absence if the document searched could have held the answer.

The source chain compounded it. The figure came from secondary write-ups (State of Surveillance, Tech Policy Press); a 2026-08-19 note on this entry re-verified an adjacent dollar figure and stated in terms that "the entry's central claim — zero PIAs filed in 2026 — is untouched by this note and was not re-audited here." The caveat was recorded and then not acted on for a month, while the claim kept being cited.

**What survives.** The structural argument — that PIA filings collapsed while surveillance procurement expanded — may well hold; "three" against 24 in 2024 and 8 in 2025 is still a steep decline. **But "collapsed" and "zero" are different claims, and only one of them was ever checked.** The 24/2024 and 8/2025 baselines are also unaudited and inherit the same index-vs-documents problem.

**Do not cite a 2026 PIA count from this entry until the re-audit lands.** A ticket should enumerate 2026 PIAs from the documents themselves, not the index.
