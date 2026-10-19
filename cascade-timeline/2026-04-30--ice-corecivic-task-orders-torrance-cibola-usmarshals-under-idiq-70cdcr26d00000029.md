---
type: timeline_event
id: 2026-04-30--ice-corecivic-task-orders-torrance-cibola-usmarshals-under-idiq-70cdcr26d00000029
date: '2026-04-30'
title: ICE Signs CoreCivic IDIQ With Separate Torrance and Cibola Task Orders; a Marshals Service Order Also Runs Under It
importance: 7
status: reported
tags:
  - detention-igsa
  - corecivic
  - new-mexico
  - no-bid-contract
  - usaspending
actors:
  - CoreCivic
  - Immigration and Customs Enforcement
  - U.S. Marshals Service
related_events:
  - 2026-05-01--corecivic-direct-federal-contract-torrance-cibola-bypasses-nm-hb9
  - 2026-03-10--ice-posts-notice-of-intent-sole-source-corecivic-torrance-cibola-sam-gov
coverage: []
sources:
  - title: USAspending.gov award record, IDIQ 70CDCR26D00000029 (CoreCivic)
    url: https://www.usaspending.gov/award/CONT_IDV_70CDCR26D00000029_7012
    publisher: USAspending.gov
    date: '2026-04-30'
    tier: 1
  - title: USAspending.gov award API, delivery orders 70CDCR26FR0000058, 70CDCR26FR0000060, 15M40026FA3500020
    url: https://api.usaspending.gov/api/v2/idvs/awards/
    publisher: USAspending.gov
    date: '2026-04-30'
    tier: 1
  - title: New Mexico Immigrant Law Center v. ICE, complaint (D.N.M. 1:26-cv-03471)
    url: https://www.aclu-nm.org/app/uploads/2026/10/1.pdf
    publisher: ACLU of New Mexico (court filing)
    date: '2026-10-16'
    tier: 1
verification: captured
verification_note: 'Conductor QC 2026-10-19: written after 2026-10-01 without claims (structured USAspending/docket data the claim gate cannot span-bind), so captured/reported, not confirmed. Figures are from the worker read of the primary record; rebind when the gate supports JSON or docket sources.'
---

The CoreCivic IDIQ covering Torrance and Cibola was signed April 30, 2026 (USAspending `date_signed` field on the IDV and on each order). USAspending shows the money moving through three delivery orders written against it, not through the IDIQ itself.

## What the award record shows

- The IDIQ (PIID 70CDCR26D00000029) records a base and all options value of $135,421,013.76 and obligations of $0. That figure is a ceiling, not spending.
- Torrance has its own delivery order (70CDCR26FR0000058) with $14,085,950 obligated. Cibola has a separate one (70CDCR26FR0000060) with $8,783,769.24 obligated. Both are recorded as not competed, with the solicitation procedure "only one source".
- A third order, 15M40026FA3500020, was placed by the U.S. Marshals Service (Department of Justice) against the ICE vehicle for detention and transportation at the Torrance facility. It has $3,360,704.25 obligated and a base and all options value of $13,406,431.45. Its recipient is CoreCivic at a Brentwood, Tennessee place of performance.
- This resolves a gap left in the earlier entry on this contract, which could not say whether Cibola had its own order: it does, and the Marshals order is a separate agency's use of the same vehicle.

## Which number the lawsuit uses

ACLU-NM's complaint describes the contract as "valued at $26.2 million, with a potential award amount up to $36.3 million". Those match the child-order totals on USAspending (the three orders together), not the IDIQ ceiling. Any reader comparing the complaint to the $135 million figure should know the two measure different things.

## Method

Each figure was read from the USAspending API record for that award (`/api/v2/awards/<id>/`; child orders listed via `/api/v2/idvs/awards/`) on 2026-10-19 (a retrieval date). The three orders' obligations sum to $26,230,423.49 and their base and all options values to $36,276,150.69, per the IDV amounts endpoint. The API's `period_of_performance` for the Torrance and Cibola orders ran from May 1, 2026 to September 30, 2026; the Marshals order runs to April 30, 2027. No follow-on Torrance or Cibola order appeared in the child list at retrieval, which may be reporting lag. This entry was written without per-claim spans because the source is structured JSON; the gate treats it as a legacy `captured` entry.

## Not established here

The written justification for the sole-source award has not been published, and the contract documents have not been released. That is what the FOIA suit seeks.
