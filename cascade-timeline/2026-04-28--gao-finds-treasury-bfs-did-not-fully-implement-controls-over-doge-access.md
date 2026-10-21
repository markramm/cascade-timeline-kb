---
type: timeline_event
id: 2026-04-28--gao-finds-treasury-bfs-did-not-fully-implement-controls-over-doge-access
date: '2026-04-28'
title: "GAO Finds Treasury's Fiscal Service Did Not Fully Implement Security Controls Over DOGE Payment-System Access, and a DOGE Employee Sent Unencrypted PII Outside the Bureau"
importance: 7
status: reported
tags:
  - gao
  - doge
  - treasury
  - fisma
  - pii
  - privacy-rules-ledger
actors:
  - Government Accountability Office
  - Bureau of the Fiscal Service
  - Department of the Treasury
  - Department of Government Efficiency (DOGE)
sources:
  - title: "GAO-26-108131, Department of Government Efficiency: Treasury Needs to Fully Implement Data Protection Controls"
    url: "https://web.archive.org/web/20260917052003id_/https://www.gao.gov/assets/gao-26-108131.pdf"
    publisher: "U.S. Government Accountability Office (Wayback copy; gao.gov returns 403 to scripted fetches)"
    date: '2026-04-28'
    tier: 1
  - title: "GAO-26-108192, DOGE: Congress and the Public Lack Assurance That Systems and Data Were Protected at Multiple Agencies"
    url: "https://web.archive.org/web/20261004144658id_/https://www.gao.gov/assets/gao-26-108192.pdf"
    publisher: "U.S. Government Accountability Office (Wayback copy)"
    date: '2026-09-29'
    tier: 1
related_events:
  - 2025-02-03--2025-02-03--doge-gains-access-treasury-payment-systems
  - 2026-09-29--gao-six-agencies-could-not-show-doge-access-or-controls-gao-26-108192
capture_lanes:
  - Surveillance Infrastructure
  - Digital and Tech Capture
event_date_claim: c1
verification: captured
claims:
- id: c1
  type: date
  value: Apr. 28, 2026
  qualifier: GAO-26-108131
  span: 'Implement Data Protection Controls, GAO-26-108131 (Washington, D.C.: Apr. 28, 2026).'
  url: https://web.archive.org/web/20261004144658id_/https://www.gao.gov/assets/gao-26-108192.pdf
  read: fetched
  source_kind: primary
  outcome: unreachable
  checked: '2026-10-21'
- id: c2
  type: figure
  value: five of the 14 selected controls
  qualifier: fully implemented
  span: The bureau fully implemented five of the 14 selected controls for ensuring that DOGE team employees with access to BFS systems follow its IT security rules.
  url: https://web.archive.org/web/20260917052003id_/https://www.gao.gov/assets/gao-26-108131.pdf
  read: fetched
  source_kind: primary
  outcome: unreachable
  checked: '2026-10-21'
- id: c3
  type: quote
  value: did not encrypt PII sent to another agency or obtain approval for sharing this information prior to sending it
  qualifier: employee B
  span: On January 30, 2025, employee B did not encrypt PII sent to another agency or obtain approval for sharing this information prior to sending it.
  url: https://web.archive.org/web/20260917052003id_/https://www.gao.gov/assets/gao-26-108131.pdf
  read: fetched
  source_kind: primary
  outcome: unreachable
  checked: '2026-10-21'
- id: c4
  type: quote
  value: As of September 2026, BFS has not implemented the recommendations.
  qualifier: not implemented
  span: As of September 2026, BFS has not implemented the recommendations.
  url: https://web.archive.org/web/20261004144658id_/https://www.gao.gov/assets/gao-26-108192.pdf
  read: fetched
  source_kind: primary
  outcome: unreachable
  checked: '2026-10-21'
---
The Government Accountability Office reported on Treasury DOGE team access to the Bureau of the Fiscal Service payment systems. The bureau fully implemented five of the 14 selected controls GAO tested for making sure DOGE team employees followed its IT security rules. GAO also found that a Treasury DOGE employee "did not encrypt PII sent to another agency or obtain approval for sharing this information prior to sending it".

**Follow-up.** "As of September 2026, BFS has not implemented the recommendations."

**Ledger class.** FOUND (GAO audit). The yardstick is federal IT-security and privacy controls, not a legal holding under the Privacy Act.
