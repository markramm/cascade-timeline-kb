---
type: timeline_event
id: 2026-09-22--ice-5-idiq-awards-first-task-orders-10000-guaranteed-minimum-each
date: '2026-09-22'
title: "First Task Orders Under ICE's $7.3B Detention IDIQs Obligate $10,000 Each, a Guaranteed Minimum"
importance: 6
status: confirmed
lane: detention-industrial-complex
tags:
  - ice-detention
  - procurement
  - detention-reengineering-initiative
  - federal-contracting
actors:
  - U.S. Immigration and Customs Enforcement
  - Rapid Deployment Inc
  - GardaWorld Federal Services
  - Rudiarius Holdings
sources:
  - title: "USAspending API: award 362519502 (70CMSW26D00000013, Rapid Deployment Inc, El Paso)"
    url: https://api.usaspending.gov/api/v2/awards/362519502/
    publisher: USAspending.gov (Treasury)
    date: '2026-10-01'
    tier: 1
  - title: "USAspending API: IDV amounts for 70CMSW26D00000013"
    url: https://api.usaspending.gov/api/v2/idvs/amounts/CONT_IDV_70CMSW26D00000013_7012/
    publisher: USAspending.gov (Treasury)
    date: '2026-10-01'
    tier: 1
related_events:
  - 2026-09-21--dhs-awards-7-3b-idiq-detention-contracts-five-states
  - 2026-09-20--dhs-signs-1-2b-gardaworld-contract-florence-az-detention
---

Each of the five Office of Assets and Facility Management construction IDIQs signed September 20, 2026 (El Paso, Batavia, Florence, Miami, El Centro; $7.3 billion in ceilings) has had exactly one task order issued against it as of October 1, and each is described as a "guaranteed minimum" worth $10,000 with a period of performance starting September 22. Total obligation on every parent IDIQ reads $0.0. That is about $50,000 against the ceilings, the minimum a contractor is owed for the vehicle to be binding, not construction money.

By contrast, two earlier IDIQs to Burrow Global JV (signed September 12; Los Fresnos, TX and Fort Benning, GA) already carry real task orders issued September 21: $21,425,669.50 (design/build secure housing unit, Port Isabel) and $26,534,641.32 (design/build advanced training and operations complex).

## Claim spans (read 2026-10-01 from the USAspending API)

- Award 362519502: `"total_obligation": 0.0`, `"base_and_all_options": 2222732348.0`, `"date_signed": "2026-09-20"`, recipient `RAPID DEPLOYMENT INC`.
- IDV amounts: `"child_award_count":1`, `"child_award_total_obligation":10000.0`.
- Child award 70CMSW26FR0000091: `"GUARANTEED MINIMUM FOR SINGLE AWARD CONSTRUCTION CONTRACT (SACC) IDIQ ... AT EL PASO, TX AND CO-LO (ELP)."`, `"obligated_amount":10000.0`, start `2026-09-22`.
- Same read for 70CMSW26D00000012 (Batavia, 362519501), D14 (Florence, 362519503), D15 (Miami, 362519504), D16 (El Centro, 362519505): each `child_award_count 1`, `child_award_total_obligation 10000.0`, `total_obligation 0.0`.
- Burrow Global: 70CMSW26FR0000082 `obligated_amount 21425669.5`, 70CMSW26FR0000083 `26534641.32`, both start 2026-09-21 (idvs/awards child_awards endpoint).

Note: USAspending dates the five awards September 20; the 09-21 entry above uses September 21 (reporting date).
