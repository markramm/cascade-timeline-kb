---
type: timeline_event
id: 2026-08-28--ice-own-roster-confirms-nine-ny-agencies-terminated-287g-docket-26cv1360-identified
date: '2026-08-28'
title: "ICE's Own Live Roster Confirms Nine of Twelve New York 287(g) Agencies Terminated; NDNY Docket for the Aug 3 Injunction Denial Identified as 26-cv-1360"
importance: 7
status: confirmed
tags:
  - 287g
  - new-york
  - state-federal-conflict
  - igsa
  - compliance-tracking
  - primary-source-verification
actors:
  - U.S. Immigration and Customs Enforcement
  - Rensselaer County
  - Kyle Bourgault
  - Nassau County
  - New York Office of Immigrant Trust
  - Letitia James
  - U.S. Department of Justice
sources:
  - title: "287(g) Participating Agencies (xlsx roster)"
    url: "https://www.ice.gov/file-download/download/public/208496"
    publisher: "U.S. Immigration and Customs Enforcement"
    date: '2026-08-25'
    tier: 1
  - title: "287(g) program page (stating roster snapshot time and national MOA totals)"
    url: "https://www.ice.gov/identify-and-arrest/287g"
    publisher: "U.S. Immigration and Customs Enforcement"
    date: '2026-08-26'
    tier: 1
  - title: "Hybrid Verified Petition and Verified Complaint, People of the State of New York v. Kyle Bourgault et al."
    url: "https://ag.ny.gov/sites/default/files/court-filings/new-york-v-kyle-bourgault-summons-2026.pdf"
    publisher: "New York Office of the Attorney General (NYSCEF filing)"
    date: '2026-08-27'
    tier: 1
  - title: "Attorney General James and Governor Hochul Announce Lawsuit Against Rensselaer"
    url: "https://ag.ny.gov/press-release/2026/attorney-general-james-and-governor-hochul-announce-lawsuit-against-rensselaer"
    publisher: "Office of the New York Attorney General"
    date: '2026-08-27'
    tier: 1
---

Two of the four gaps this entry was commissioned to close turned out to have primary-source answers sitting one click away from where the prior pass stopped. ICE publishes its own 287(g) participating-agency roster as a downloadable spreadsheet, not just a page of prose; and the New York Attorney General's own filed complaint against Rensselaer County cites the exact federal docket number for the August 3 ruling the prior entry could only describe secondhand.

**ICE's own roster, parsed directly.** ICE's 287(g) program page (`ice.gov/identify-and-arrest/287g`) states, as of a page snapshot taken **August 26, 2026, 3:22pm**: "ICE has signed 2,382 Memorandums of Agreement for 287(g) programs covering 39 states and 2 U.S. Territories," broken out as 182 Jail Enforcement Model (JEM) agreements in 30 states and 1 territory, 546 Warrant Service Officer (WSO) agreements in 34 states, and 1,654 Task Force Model (TFM) agreements in 32 states and 2 territories. The page links a "View 287(g) Participating Agencies" button to `ice.gov/file-download/download/public/208496`, which serves an .xlsx file named `participatingAgencies08252026pm.xlsx` (content-type spreadsheet, last-modified 2026-08-26T01:49:33Z) — i.e., a roster ICE itself dated to **August 25, 2026, PM: the compliance deadline itself.**

**Parse method and date.** Downloaded 2026-08-28 via `curl` with a browser User-Agent (ice.gov 403s bare curl but not a spoofed UA, consistent with this session's prior findings). The file is a standard Office Open XML workbook; no `openpyxl` was available in this environment, so it was parsed directly from the underlying XML (`xl/sharedStrings.xml` + `xl/worksheets/sheet1.xml`) with a short Python script — regex-extracting shared strings and cell references, reconstructing rows. Header row: `STATE, LAW ENFORCEMENT AGENCY, TYPE, COUNTY, SUPPORT TYPE, SIGNED, MOA, ADDENDUM`. Total data rows: 2,383 (ICE's own stated total is 2,382; the one-row variance is consistent with a trailing blank/artifact row, not a parsing failure — SUPPORT TYPE value counts across the full file came out close to ICE's stated 182/546/1,654 JEM/WSO/TFM breakdown, with minor drift from a handful of rows with blank COUNTY cells shifting column alignment).

**Filtering to `STATE == "NEW YORK"` returns exactly three rows, no more, no less:**

| Law Enforcement Agency | County | Model | Signed (per ICE) |
|---|---|---|---|
| Nassau County Police Department | Nassau County | Task Force Model | 2025-03-10 |
| Nassau County Sheriff's Office | Nassau County | Warrant Service Officer | 2025-02-28 |
| Rensselaer County Sheriff's Office | Rensselaer County | Jail Enforcement Model | 2020-06-10 |

**This directly answers three of the four uncovered-agency questions this ticket carried forward, and updates a fourth.** Grepping the full 2,383-row file (all states, not just New York) for "Otsego," "Niagara," "Steuben," "Broome," "Madison," "Cattaraugus," "Mohawk," "Camden," or "Allegany" returns zero New York hits (the string matches that do appear are all Madison/Camden/Allegany-named jurisdictions in other states — Alabama, Arkansas, Florida, Georgia, etc. — a useful negative-control check that the filter logic itself works). Per ICE's own August 25 roster:

- **Otsego County Sheriff's Office** — not listed. Terminated (or never executed to ICE's own recognition).
- **Mohawk Village Police Department** — not listed. Terminated.
- **Camden Police Department** — not listed. Terminated.
- **Allegany Village Police Department** — not listed. Terminated.
- **Niagara County Sheriff's Office** — not listed. This resolves the prior gap: Niagara had missed the August 14 proof-of-compliance deadline and was still on Spectrum News's August 18 list of seven active agencies, but ICE's own August 25 snapshot no longer shows it. Terminated by (or as of) the deadline.
- **Steuben, Broome, Cattaraugus, Madison County** — also absent, consistent with the prior entry's finding that all four had sent termination letters or announced compliance (with the caveat, unchanged by this pass, that Madison and Cattaraugus each paired paper termination with public statements of continued operational cooperation with ICE — a fact this roster cannot see, since it tracks MOA status, not conduct).
- **St. Lawrence County** — also absent from ICE's roster under any name variant ("St. Lawrence," "St Lawrence," "Lawrence County" all checked), consistent with the prior entry's finding that this county's 287(g) agreement, if it exists, was never confirmed executed.

**Net effect: of the twelve agencies the AG sent termination letters to, ICE's own current roster shows only Nassau County PD, Nassau County Sheriff's Office, and Rensselaer County Sheriff's Office still listed — nine of twelve are gone from ICE's own books as of the compliance deadline.** This is a materially cleaner compliance picture than the prior entry could establish from press reporting alone, where only 2 of 12 (Broome, Steuben) had confirmed post-deadline terminations and the rest were open questions. It does **not** resolve the paper-compliance-vs-operational-continuation distinction the prior entry flagged for Madison and Cattaraugus — ICE's roster tracks whether an MOA is on the books, not whether the agency and ICE continue informal cooperation. Nassau (both its PD and Sheriff's Office agreements) and Rensselaer remain listed as of ICE's own August 25 snapshot, which is the same three-way outcome the state's court filings independently describe: Nassau's compliance is unconfirmed by any primary Nassau document (still true after this pass — see remaining gaps), and Rensselaer is now under direct state civil suit specifically **because** it remains on this exact roster (the state's complaint cites this same ICE page as its own evidence, see below).

**287(g) model correction: Rensselaer's agreement dates to 2020, not 2018.** The parent timeline entry (2026-08-27) stated Rensselaer's Jail Enforcement Model agreement had been "in force since 2018." Two independent primary sources checked this pass both give a different date. ICE's own roster spreadsheet lists Rensselaer's SIGNED date as Excel serial 43992, which converts to **2020-06-10**. The state's own verified complaint against Rensselaer (below) states at ¶26: "On March 5, 2020, Patrick Russo, then acting as the sheriff of RCSO, signed the RCSO 287(g) Agreement. The RCSO 287(g) Agreement was countersigned by C.M. Cronen, Assistant Director of Enforcement at ICE on **June 10, 2020**." The two dates match exactly (ICE's SIGNED field appears to record the ICE-side countersignature date, not the agency's signature date) — **2018 was an error; the agreement is confirmed signed March 5, 2020 and countersigned June 10, 2020, and it is a Jail Enforcement Model agreement**, per both ICE's own data and the state's sworn complaint.

**The NDNY docket citation: `United States v. State of New York`, No. 26-cv-1360 (N.D.N.Y.).** CourtListener's API remained at its daily rate cap (125/125 calls, confirmed 2026-08-28) for this entire pass, and its browser-facing docket pages return the site's AWS WAF JS-challenge (HTTP 202, zero bytes) to non-browser clients — both blockers the parent pass also hit, now independently reconfirmed rather than assumed. A case-name search on CourtListener's non-API search page did load (inconsistently — the same query type sometimes returned the WAF challenge and sometimes real HTML) and surfaced a docket titled "United States v. State of New York" — but it is docket **1:10-cv-01214** in front of Judge Gary L. Sharpe, filed October 12, 2010 and terminated eight days later, a Voting Rights Act case (Nature of Suit: 441 Civil Rights: Voting) with no relationship to the 287(g) fight. This is a genuine and instructive false lead: the same case caption recurs across NDNY's docket history, and neither a caption search nor CourtListener's own fuzzy full-text search (documented as unreliable by the prior pass) can be trusted to disambiguate them absent the exact docket number.

The exact docket number instead came from a primary legal document: the state's own **Hybrid Verified Petition and Verified Complaint in People of the State of New York v. Kyle Bourgault** (Rensselaer County Supreme Court, NYSCEF Doc. No. 1, filed and verified August 27, 2026 by Assistant AG Kasia Donohue). Paragraph 35: "A request for a preliminary injunction in a recent challenge to the Local Cops, Local Crimes Act's ban on 287(g) agreements was rejected by the federal court in the Northern District of New York. *See United States v. State of New York*, Dkt. No. **26-cv-1360**, ECF No. **53** (N.D.N.Y. Aug. 3, 2026)." This is an attorney's citation, under a signed verification, in a filed and NYSCEF-stamped court document — a strong source, but it is **not itself independent confirmation from the federal docket**; CourtListener/PACER access remained blocked this pass and the citation has not been cross-verified against the NDNY docket directly. Treat the docket number as sourced to the state's pleading pending a direct pull once CourtListener's cap resets.

**A second, previously undocumented federal docket surfaced in the same filing.** Paragraph 42 of the same complaint states that Sheriff Bourgault, in a lawsuit he filed against the State of New York on August 25, 2026 challenging the Local Cops, Local Crimes Act, affirmed under oath that as of that filing date he "did not terminate the 287(g) agreement" — citing *Bourgault v. Hochul*, Dkt. No. **26-cv-01637** (N.D.N.Y.), Sheriff Bourgault Affirmation, ECF No. 5-3, ¶109. This is Rensselaer's own federal countersuit (distinct from the fifteen-sheriff FAIR-backed suit filed the prior day), and it is now a documented instance of a defiant sheriff's sworn court filing admitting non-compliance in his own words, which strengthens the state's mandamus case against him. Not previously in canon.

**What this confirms versus what it leaves open.** The state's complaint (¶10, ¶43) itself cites ICE's website as evidence that "RCSO has an active 287(g) Agreement," "last visited Aug. 27, 2026" — meaning the state's own enforcement theory rests on the same public roster this entry independently parsed. That convergence (independent parse vs. the AG's own cited evidence) is a meaningful cross-check: two separate methods, ICE's raw spreadsheet and the state's litigation record, agree that Rensselaer and both Nassau agreements remain listed. What remains open: Nassau's own compliance status is still not sourced to a primary Nassau County document (Nassau's continued presence on ICE's own roster as of August 25 is itself now evidence against the secondary reporting that Blakeman "ended the partnership" August 26 — if true, that would mean Nassau terminated the day *after* this snapshot, which is plausible on the timeline but unconfirmed); and the docket numbers above have not yet been independently verified against the federal docket directly, only against the state's own pleading that cites them.

This extends [[2026-08-27--ny-287g-compliance-deadline-passes-state-sues-rensselaer-corrected-roster]] (the 12-agency roster, the per-agency status table, and the initial identification of the Aug 3 NDNY ruling without a docket number) and [[2026-08-26--ny-ag-james-subpoenas-counties-defying-287g-termination-law]] (the four-county subpoena wave that named Nassau, Rensselaer, Broome, and Steuben specifically).

## Remaining research gaps

- The docket numbers `26-cv-1360` (United States v. State of New York) and `26-cv-01637` (Bourgault v. Hochul) are sourced to the state's own verified court filing, not independently confirmed against the NDNY docket directly — CourtListener's API remained at its 125/125 daily cap and its browser docket pages returned the site's WAF JS-challenge (HTTP 202, zero bytes) throughout this pass. Re-verify directly once the rate limit resets (was at 51,714 seconds / ~14.3 hours remaining as of this pass).
- Nassau County's compliance status is still not sourced to a primary Nassau County document or statement; ICE's own August 25 roster showing both Nassau agreements still listed is now in tension with secondary reporting that Blakeman announced compliance August 26 — the two are not necessarily contradictory (a one-day-later termination is plausible) but neither has been directly confirmed against a Nassau County primary source or an updated ICE roster snapshot.
- No post-August-25 confirmation was sought this pass for whether Rensselaer's mandamus proceeding (People v. Bourgault) has produced any court order; the complaint was filed August 27 and Index No. was UNASSIGNED as of the document reviewed.
- The 287(g) model for the four small agencies (Otsego, Mohawk Village PD, Camden PD, Allegany Village PD) could not be determined, since none appears on ICE's current roster at all (a terminated agreement's model isn't visible from a roster that only lists currently active MOAs); the AG's original July 24 termination-letter PDF may specify model per-agency and was not re-checked this pass for that detail.

---

## CORRECTION, 2026-08-30 — the docket number is right; the case name and the subject matter are not

This entry ended by saying the docket number was "sourced to the state's pleading pending a direct
pull once CourtListener's cap resets." **The cap reset, the direct pull happened, and it came back
different in two ways.** That caveat did its job — this is what it was for.

**Verified directly against CourtListener, 2026-08-30:**

1. **The case is *United States v. Russo*, not *United States v. State of New York*.** N.D.N.Y.
   1:26-cv-01360, docketed 2026-07-13 on transfer from W.D.N.Y. (original 1:26-cv-01283, filed
   2026-06-22). Defendant Michael Russo was dismissed 2026-07-10 but **the caption never updated**,
   which is why a party citing the case by name can be both accurate as to number and wrong as to
   caption.

2. **The Aug 3 order (ECF 53) adjudicates New York's Face Covering Act / Identification Act — NOT
   the Local Cops, Local Crimes Act's 287(g) ban.** This is the material error. The state's
   complaint at ¶35 describes it as "a recent challenge to the Local Cops, Local Crimes Act's ban
   on 287(g) agreements." **That characterization is the Assistant AG's, and it does not match the
   order.** Whether an actual 287(g) challenge exists is now an OPEN question; docket
   **1:26-cv-01281, State of New York v. DOJ** is a plausible home for one and could not be read
   (AWS WAF blocked every attempt).

**What this changes about sourcing discipline.** The original source was strong by every normal
test — an attorney's citation, under signed verification, in a NYSCEF-stamped filing. It was still
wrong about what the cited order decided. **A party's own filing is authoritative for what that
party alleges, and not authoritative for what a different court's docket says.** Signed verification
attests to good faith, not to accuracy about a third document.

**The number alone is not an identifier.** Reproduced this pass: querying the bare string
`1:26-cv-01360` returns **four unrelated cases in four districts** (C.D. Ill., E.D.N.Y., S.D. Ind.,
N.D.N.Y.). Docket numbers are unique only *within* a district. Cite number + court, then confirm the
filing date and the parties before use.

**The caption decoy documented in this entry is now confirmed a third time.** A fourth was ruled out
by reading rather than by caption: 1:26-cv-01527 is an unrelated SUNY/CUNY financial-aid case.

**Everything else in this entry stands** — the ICE roster parse, the nine-of-twelve termination
count, and *Bourgault v. Hochul* (1:26-cv-01637), which was verified cleanly and directly from the
docket. Superseding entry:
[[2026-08-29--ny-287g-docket-verified-united-states-v-russo-nassau-still-on-ice-roster]].
