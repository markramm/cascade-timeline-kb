---
type: timeline_event
id: 2026-06-24--mijente-report-ice-cbp-surveillance-spend-513m-fy2026
date: '2026-06-24'
title: "Mijente/Just Futures Law/Surveillance Resistance Lab Report Puts ICE+CBP Surveillance-Vendor Spend at $513M in FY2026, Up From $310M in FY2025"
importance: 6
status: reported
tags:
  - investigation-2
  - surveillance-infrastructure
  - procurement
  - palantir
  - anduril
  - ice
  - cbp
actors:
  - Mijente
  - Just Futures Law
  - Surveillance Resistance Lab
  - Palantir Technologies
  - Anduril Industries
  - Immigration and Customs Enforcement
  - Customs and Border Protection
sources:
  - title: "'We should be worried': report sheds light on ICE's booming arsenal of hi-tech surveillance tools"
    url: https://www.theguardian.com/us-news/2026/jun/24/ice-tech-surveillance-arsenal
    publisher: The Guardian
    date: '2026-06-24'
    tier: 1
  - title: "New Report Highlights Growing Partnership Between Surveillance Tech and ICE"
    url: https://truthout.org/articles/new-report-highlights-growing-partnership-between-surveillance-tech-and-ice/
    publisher: Truthout
    date: '2026-06-27'
    tier: 2
  - title: "The Tech Behind ICE: Oligarchs, Immigration Enforcement and the Threat to Democracy (report landing page)"
    url: https://thecrcr.org/library/tech-behind-ice/
    publisher: Collaborative Research Center for Resilience
    date: '2026-07'
    tier: 2
capture_lanes:
  - Surveillance Infrastructure
  - Corporate Capture
coverage: []
---

## Opening paragraph

A July 2026 report titled *The Tech Behind ICE: Oligarchs, Immigration Enforcement and the Threat to Democracy* — published by Mijente, Just Futures Law, and the Surveillance Resistance Lab (a project of the Collaborative Research Center for Resilience) — tracked ICE and CBP contracts with 11 named surveillance-technology companies from 2013 through 2026. The report's headline figure: combined obligations to those 11 vendors rose from under $50M in 2013 to just over $310M in 2025, then to a reported $513M in 2026, driven primarily by Palantir (data analytics/targeting) and Anduril (AI-powered border towers, drones, sensors). The Guardian covered the report June 24, 2026; Truthout independently confirmed the same $310M/$513M figures in its own coverage three days later.

## What Happened / Key Facts

- The $513M figure originates with this report's own dataset, not a government-published total — the researchers built it by tracking 11 named vendors' ICE/CBP contract history from 2013-2026. Neither Guardian nor Truthout names all 11 companies in their published text; both single out Palantir and Anduril as the drivers of the 2025→2026 spike.
- **This ticket traces a citation error in the daily-capture ledger.** The dropped ledger story (`2026-07-01--dhs-facial-recognition-1300-agencies-ice-surveillance`, cascade-research/daily-capture-reports) cited NPR's March 25, 2026 surveillance/data-brokers investigation as the tier-1 source for the $513M figure. Direct extraction of that NPR article (`--grep` for "513", "310", "surveillance technology spending", "FY202") returned **zero matches** — the figure is not in the NPR piece at all. The actual source is Truthout, citing the Mijente/Just Futures Law/Surveillance Resistance Lab report; the NPR citation in the ledger's fact-check was wrong, and the ledger's fact-check note claiming the dollar figures were "corroborated across multiple sources" happened to be true only by accident (Truthout and Guardian both independently report the same numbers from the same report) — the tier-1 anchor it named was not one of them.
- **USAspending corroborates the underlying mechanism, not the exact total.** Recipient-name searches for Palantir and Anduril (no ICE/CBP sub-agency filter available in the tool) surface real Department of Homeland Security-tagged awards with FY2026 action dates consistent with the report's narrative:
  - Anduril, award 353697130 (contract 70B02C26F00000035): **$362,974,500**, DHS, delivery order 2025-12-25→2027-06-17. PSC `Y1BG` (Construction of Electronic and Communications Facilities), NAICS `541512` (Computer Systems Design Services) — consistent with border-tower/sensor infrastructure, not generic IT.
  - Anduril, award 360657540: $61,699,633, DHS, 2026-07-21→2027-08-01. Same PSC/NAICS.
  - Anduril, award 291176129: $47,646,858, DHS, 2025-09-19→2027-06-30. Same PSC/NAICS.
  - Palantir, award 291199463 (contract 70CTD022FR0000170): $150,703,825, DHS, delivery order 2022-09-26→2026-05-04. PSC `DA01` (IT/Business Application Development Support Services), NAICS `511210` (Software Publishers).
  - Palantir, awards 357645746 and 359681596 (both BPA calls, DHS, FY2026 action dates): $86,271,599 and $45,848,617.
- **These DHS-tagged awards alone sum higher than the report's total.** Summed by award total-value (not FY2026 obligated cash), the FY2026-action-dated DHS awards found for just these two vendors total **~$852.7M** ($551.2M Anduril + $301.5M Palantir) — exceeding the report's $513M claim for all 11 companies combined. This is not a refutation of the report; it reflects a real methodological gap between the two figures: USAspending's award total-value is a multi-year contract ceiling (the $362.9M Anduril award alone runs through mid-2027), while the report's $513M appears to be a single-fiscal-year obligation/spend figure. The two are not directly comparable, and this worker could not reconstruct the report's exact FY2026-obligated-dollars number from `usaspending` alone — the tool has no agency-sub-component filter (DHS-wide, not ICE/CBP-specific) and, per this session's testing, `--sum` did not respect the `--from`/`--to` date bounds passed to it (returned the same all-time $2.76B/280-award total regardless of date range; see feedback log).
- No entry existed anywhere in cascade-research or cascade-timeline at the $513M magnitude prior to this task; the only prior near-match was an unrelated bed-count figure (513-775 beds, Pima County MTC facility).

## Why This Event Matters

The figure is real in the sense that two independent outlets (Guardian tier-1, Truthout tier-2) report it from the same named, dated, methodologically-described report — this is not a fabrication or a hallucinated round number. But it is an aggregate research figure from an advocacy-research coalition, not a government-published total, and this worker's USAspending spot-checks corroborate the *mechanism* (large, real, DHS-tagged Anduril/Palantir awards with FY2026 action dates, PSC-coded as surveillance infrastructure and data-platform development) without being able to independently reproduce the *exact total*. Any Surveillance Inc. or detention-pipeline piece using "$513M" should attribute it explicitly to the Mijente/Just Futures Law/Surveillance Resistance Lab report (cite Guardian and/or Truthout, not NPR) and should not present it as a government-disclosed or USAspending-verified sum.

## Broader Context

Palantir's ImmigrationOS ($30M, DHS contract through September 2027) and ELITE targeting platform, and Anduril's CBP autonomous-tower monopoly (see `[[investigate-cbp-autonomous-tower-certification-monopoly-only-anduril-towers-certified-post-hoc-certification-as-accountability-bypass-layer-captured-x-follow-on-instance]]` and `[[cbp-autonomous-tower-certification-post-hoc-standard-backfit]]`), are both already documented in the corpus as the load-bearing procurement threads this report's headline figure summarizes.

## Research Gaps

- [ ] The report's full 11-company list is not confirmed from secondary coverage alone — obtain the actual PDF (`thecrcr.org/library/tech-behind-ice/` links to a "DOWNLOAD FULL REPORT" that did not resolve to a direct file URL via text extraction) to get the exact per-vendor breakdown and stated methodology (obligated spend vs. award ceiling; FY2026 partial-year cutoff date).
- [ ] No sub-agency (ICE vs. CBP vs. other DHS component) filter exists in the `cascade-search usaspending` client; a precise ICE+CBP-only reconstruction would need FPDS/USAspending's agency-hierarchy filter directly, not just recipient-name search.
- [ ] `--sum` did not appear to respect `--from`/`--to` bounds in this session (see FEEDBACK.md) — worth re-testing after a fix before attempting the full reconstruction again.

## Related Entries

- [[investigate-cbp-autonomous-tower-certification-monopoly-only-anduril-towers-certified-post-hoc-certification-as-accountability-bypass-layer-captured-x-follow-on-instance]]
- [[cbp-autonomous-tower-certification-post-hoc-standard-backfit]]
- [[2026-06-20--ice-largest-clearview-ai-contract-dhs-deletes-oversight-policy]]
- [[2026-02-19--dhs-signs-billion-dollar-palantir-ice-surveillance-contract]]
- [[2026-05-13--dhs-zero-privacy-impact-assessments-palantir-1-billion-no-bid]]
