---
type: timeline_event
id: 2026-03-16--nyc-health-hospitals-katz-discloses-palantir-non-renewal-absolute-firewall-claim
date: '2026-03-16'
title: "NYC Health + Hospitals CEO Mitchell Katz Discloses Palantir Contract Will Not Be Renewed, Claims 'Absolute Firewall' Against ICE Data Sharing"
importance: 8
status: confirmed
tags:
  - palantir
  - health-data
  - data-colonialism
  - nyc-health-hospitals
  - medicaid
  - ice
  - firewall-claim
actors:
  - Mitchell Katz
  - NYC Health + Hospitals
  - Palantir Technologies
  - New York City Council
  - U.S. Immigration and Customs Enforcement
sources:
  - title: "Palantir Will No Longer Profit Off of New Yorkers' Health Data"
    url: https://theintercept.com/2026/03/24/palantir-new-york-city-hospitals-contract/
    publisher: The Intercept
    date: '2026-03-24'
    tier: 1
  - title: "Facing public outrage, NYC Hospital CEO announces Palantir contract will not be renewed"
    url: https://afsc.org/newsroom/facing-public-outrage-nyc-hospital-ceo-announces-palantir-contract-will-not-be-renewed
    publisher: American Friends Service Committee
    date: '2026-03'
    tier: 2
  - title: "NYC Health + Hospitals to end $4M Palantir contract"
    publisher: Becker's Hospital Review
    date: '2026-03'
    tier: 2
    note: "Reached via search-result extract; direct fetch returned HTTP 403 (bot wall). No url given — see Discipline note below."
  - title: "NYC Council Committee on Hospitals, Preliminary Budget Hearing - Hospitals (item T2026-1374)"
    publisher: New York City Council, Committee on Hospitals
    date: '2026-03-16'
    tier: 1
    note: "Hearing record confirmed via council.nyc.gov Legistar (MeetingDetail ID 1399750, GUID 88AF05C2-3300-4746-8E1C-2521909532B7), 11:30 AM, 250 Broadway 8th Floor Hearing Room 1. Video link on Legistar was a non-functional placeholder at time of research; minutes/agenda PDFs listed as available but not independently fetched in this pass. Katz's quotes are cited to The Intercept's reporting of the hearing, not to a directly-fetched transcript."
---

At a **March 16, 2026** New York City Council Committee on Hospitals preliminary budget hearing, NYC Health + Hospitals CEO **Mitchell Katz** disclosed that the system's contract with Palantir would **not be renewed**, ending in **October 2026**. NYC H+H had paid Palantir **nearly $4 million since 2023** for software used to improve billing efficiency for Medicaid and other public benefits, including **automated scanning of patient health notes**. Katz said the data-analysis work would be brought **in-house** after the contract lapses, characterizing the arrangement itself as **"a short-term solution"** that the system "always intended" to end.

Pressed on Palantir's ties to ICE and other government surveillance customers, Katz asserted an **"absolute firewall"** between NYC H+H patient data and Palantir's government clients, and said: **"We haven't had any problems."**

## What the firewall claim is, and is not

This corpus documents Palantir's ICE data-integration work in depth — including a confirmed instance of Medicaid data (a different agency's Medicaid data, not NYC H+H's) improperly reaching ICE and then Palantir's ELITE app ([[2026-07-17--ice-medicaid-palantir-illegal-data-transfer]]), and the broader ImmigrationOS build cross-referencing Medicaid, IRS, and DMV records ([[2026-04-01--immigrationos-palantir-tracking-us-citizens-medicaid-irs-dmv]]). Katz's assurance is notable precisely because it is made about the same vendor, in the same general data category (Medicaid billing), amid documented instances of that category of data reaching ICE through Palantir elsewhere in the federal system.

**No documented instance of NYC H+H patient data reaching ICE via Palantir has been established.** The finding here is structural, not an allegation of a transfer: a public-hospital CEO offered an unverified assurance about the same vendor this corpus shows moving comparable data categories to ICE in other jurisdictions. The assurance itself — "we haven't had any problems" — is a statement about the absence of *known* problems, not an audited claim about data-flow architecture.

## The unverified contract clause — not quoted here

Secondary reporting (via The Intercept) describes a clause said to permit Palantir to "de-identify protected health information (PHI) and utilize de-identified PHI for purposes other than research." **The Intercept does not quote this clause verbatim from the contract itself**, and the underlying NYC H+H–Palantir contract has not been obtained in this pass (candidate source: NYC Comptroller's Checkbook/contract database — not yet pulled). This clause language is **not verified and is not quoted as contract text** in this entry; it is recorded here only as an unresolved lead for a future pass with the contract in hand.

## Related entries

- [[2025-02-13--clark-minor-appointed-hhs-cto-from-palantir]] — the federal-personnel half of the Palantir/health-data story: a 12-year Palantir veteran running HHS IT, including CMS's Medicaid data, contemporaneous with this NYC-level contract dispute.
- [[2026-07-17--ice-medicaid-palantir-illegal-data-transfer]] — the documented instance of Medicaid data reaching Palantir's ICE-facing ELITE app, which is what makes Katz's firewall assurance the live wire.
- [[2026-04-01--immigrationos-palantir-tracking-us-citizens-medicaid-irs-dmv]] — the broader federal data-consolidation architecture Katz's assurance sits against.
- [[2026-04-18--nnu-protests-palantir-hca-frist-gala-nashville]] — the separate, private-sector HCA/Timpani relationship; a different customer, product, and question from NYC H+H's Medicaid-billing contract. Do not collapse the two.

## Research gaps

- The NYC H+H–Palantir contract itself has not been obtained; the "de-identify PHI...for purposes other than research" clause is unverified secondary-source language, not contract text.
- The Council hearing video/minutes were located (Legistar item T2026-1374) but not independently transcribed in this pass; Katz's quotes here are as reported by The Intercept, not fetched from a primary transcript.
- Becker's Hospital Review coverage was reached only via search-result extract (direct fetch blocked, HTTP 403); no url recorded per the no-fabricated-URL discipline.
