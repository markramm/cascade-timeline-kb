---
type: timeline_event
id: 2026-02-19--dhs-signs-billion-dollar-palantir-ice-surveillance-contract
date: 2026-02-19
title: 'DHS Signs Palantir Department-Wide Software BPA With a $1 Billion Ceiling; ICE and CBP Can Order Under It'
title_corrected: '2026-11-14: earlier title said "for Immigration Surveillance"; Wired and the award record describe department-wide commercial software'
importance: 9
status: reported
actors:
- DHS (Department of Homeland Security)
- Palantir
- Immigration and Customs Enforcement (ICE)
- U.S. Customs and Border Protection
sources:
- url: 'https://api.usaspending.gov/api/v2/awards/CONT_IDV_70RTAC26A00000001_7001/'
  title: 'USAspending award record, PIID 70RTAC26A00000001 (DHS single-award BPA, Palantir)'
  date: '2026-02-12'
  outlet: USAspending.gov
  tier: 1
- url: 'https://www.wired.com/story/department-homeland-security-ice-billion-dollar-agreement-palantir/'
  title: 'DHS Opens a Billion-Dollar Tab With Palantir'
  date: '2026-02-19'
  outlet: WIRED
  tier: 2
- url: 'https://siliconangle.com/2026/02/19/dhs-awards-palantir-1b-deploy-ai-data-analytics-platforms/'
  title: 'DHS Awards Palantir Up to $1B to Deploy AI and Data Analytics Platforms'
  date: '2026-02-19'
  outlet: SiliconANGLE
  tier: 3
- url: 'https://www.bloomberg.com/news/articles/2026-02-05/new-york-s-pension-funds-scrutinize-palantir-over-ice-contract'
  title: "New York Pension Funds Question Palantir on ICE, DHS Contracts"
  date: '2026-02-05'
  outlet: Bloomberg
  tier: 2
corrections:
- date: '2026-11-14'
  was: "DHS signed a $1 billion blanket purchase agreement with Palantir for immigration surveillance across ICE and CBP without competitive bidding."
  now: "DHS signed a single-award blanket purchase agreement with Palantir, ceiling $1 billion, to provide commercial software licenses, maintenance and implementation services department wide; ICE and CBP are named by Wired as examples of agencies that can order under it. $0 was obligated on the BPA itself. FPDS/USAspending codes the extent of competition 'full and open' with one offer received; Wired's own phrasing is that agencies can 'essentially skip the competitive bidding process for new purchases', which refers to task orders under the BPA."
  why: "Wired and the USAspending award record both describe the scope as department-wide commercial software, not immigration surveillance; the $1 billion is a ceiling. Found by the TGIE N2 fact-check (items 1 and 5), re-read at source 2026-11-14."
  found_by: "TGIE N2 fact-check pass 1, re-verified by task palantir-wired-bpa-and-2018-letter-check"
event_date_claim: c4
verification: source-verified
claims:
- id: c1
  type: date
  value: '2026-02-12'
  qualifier: date_signed
  span: '"description":"THE PURPOSE OF THIS SINGLE AWARD BLANKET PURCHASE AGREEMENT (BPA) IS TO PROVIDE PALANTIR COMMERCIAL SOFTWARE LICENSES, MAINTENANCE, AND IMPLEMENTATION SERVICES DEPARTMENT WIDE.","total_obligation":0.0,"subaward_count":0,"total_subaward_amount":null,"date_signed":"2026-02-12"'
  url: https://api.usaspending.gov/api/v2/awards/CONT_IDV_70RTAC26A00000001_7001/
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-14'
- id: c2
  type: figure
  value: $1 billion
  qualifier: up to
  span: allowing DHS agencies like Customs and Border Protection (CBP) and Immigration and Customs Enforcement (ICE) to essentially skip the competitive bidding process for new purchases of up to $1 billion in products and services from the company
  url: https://www.wired.com/story/department-homeland-security-ice-billion-dollar-agreement-palantir/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-14'
- id: c3
  type: posture
  value: department wide
  qualifier: department wide
  span: According to contracting documents published last week, the blanket purchase agreement (BPA) awarded “is to provide Palantir commercial software licenses, maintenance, and implementation services department wide.”
  url: https://www.wired.com/story/department-homeland-security-ice-billion-dollar-agreement-palantir/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-14'
- id: c4
  type: date
  value: FEBRUARY 19 2026
  qualifier: UPDATED
  span: SHARE UPDATED 17:45 EST / FEBRUARY 19 2026 AI DHS awards Palantir up to $1B to deploy AI and data analytics platforms by Duncan Riley
  url: https://siliconangle.com/2026/02/19/dhs-awards-palantir-1b-deploy-ai-data-analytics-platforms/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-14'
tags:
- surveillance
- palantir
- ice
- single-bid-competed-award
- immigration-enforcement
- corporate-profiteering
capture_lanes:
- Surveillance Infrastructure
- Immigration System Capture
- Corporate Capture
coverage:
  - path: daily-capture-reports/headline/2026-02-19--palantir-dhs-1billion-bpa-ice-cbp-2026.md
    note: "Further re-capture of the same $1B BPA award (SiliconANGLE); dropped as duplicate 2026-10-01."
  - url: https://theramm.substack.com/p/the-mercenaries-gardaworld-kvg-and
    title: "The Mercenaries: GardaWorld, KVG, and the $1.35 Billion Nobody Was Watching"
  - path: daily-capture-reports/headline/2026-02-19--dhs-palantir-1b-ai-analytics-blanket-purchase-agreement-2026.md
    note: "BPA detail — 5-year term, Gotham/Foundry named, task orders pre-approved to $1B ceiling without separate competition; $81M ICE 2025 + $97M ICE 2026 pre-BPA, $1.8B DHS/ICE total since Jan 2025. Consumed 2026-09-20 as duplicate."
  - path: daily-capture-reports/headline/2026-02-01--dhs-palantir-1b-no-bid-ai-surveillance-contract.md
    note: "SECOND re-capture of the $1B DHS-Palantir BPA (after the 02-19 story dropped 2026-09-20), this one dated 2026-02-01 -- the ledger has now captured one award at three different dates. Dropped as duplicate 2026-09-21. Names ImmigrationOS and ELITE as included platforms. CAUTION: one of its four cited sources is capturecascade.org itself, so its zero-Privacy-Impact-Assessments claim is this corpus citing itself, not independent corroboration -- see canon 2026-05-13 for that finding's own sourcing."
---

DHS signed a single-award blanket purchase agreement with Palantir. Wired reported that the agreement is for commercial software licenses, maintenance and implementation services department wide, and that agencies like CBP and ICE can skip the competitive bidding process for new purchases of up to $1 billion.
