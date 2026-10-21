---
type: timeline_event
id: 2026-04-10--fourth-circuit-en-banc-vacates-afscme-v-ssa-injunction-irreparable-harm-only
date: '2026-04-10'
title: "Fourth Circuit En Banc Vacates the SSA-DOGE Injunction on Irreparable Harm Alone, Leaving the Privacy Act Merits Unreviewed (AFSCME v. SSA)"
importance: 8
status: confirmed
tags:
  - privacy-act
  - doge
  - ssa
  - judicial-ruling
  - appellate-reversal
  - privacy-rules-ledger
actors:
  - U.S. Court of Appeals for the Fourth Circuit
  - Judge Toby Heytens
  - Judge Ellen Lipton Hollander
  - Social Security Administration
  - Department of Government Efficiency (DOGE)
  - American Federation of State County and Municipal Employees (AFSCME)
sources:
  - title: "Opinion, AFSCME v. SSA, No. 25-1411 (4th Cir. en banc)"
    url: "https://www.ca4.uscourts.gov/opinions/251411.P.pdf"
    publisher: "U.S. Court of Appeals for the Fourth Circuit"
    date: '2026-04-10'
    tier: 1
  - title: "Memorandum Opinion, AFSCME v. SSA, 1:25-cv-00596-ELH (D. Md.), ECF 146"
    url: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.146.0.pdf"
    publisher: "US District Court, D. Md."
    date: '2025-04-17'
    tier: 1
  - title: "SSA v. AFSCME, No. 24A1063, order granting stay"
    url: "https://www.supremecourt.gov/opinions/24pdf/24a1063_6j37.pdf"
    publisher: "Supreme Court of the United States"
    date: '2025-06-06'
    tier: 1
related_events:
  - 2025-04-17--2025-04-17--judge-blocks-doge-social-security-data-access
  - 2026-01-16--afscme-v-ssa-notice-corrections-doge-unauthorized-access-prosecutorial-predicate
  - 2026-06-26--hollander-holds-ssa-admissions-show-tro-noncompliance-questions-orders-discovery
capture_lanes:
  - Surveillance Infrastructure
  - Digital and Tech Capture
event_date_claim: c1
verification: source-verified
claims:
- id: c1
  type: date
  value: April 10, 2026
  qualifier: Decided
  span: 'Argued: September 11, 2025 Decided: April 10, 2026'
  url: https://www.ca4.uscourts.gov/opinions/251411.P.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c2
  type: quote
  value: We now vacate the current preliminary injunction
  qualifier: vacate
  span: The district court granted a preliminary injunction, which the Supreme Court stayed pending this appeal and any further Supreme Court review. We now vacate the current preliminary injunction and return the case to the district court for further proceedings.
  url: https://www.ca4.uscourts.gov/opinions/251411.P.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c3
  type: quote
  value: without addressing whether plaintiffs satisfy the remaining three Winter factors
  qualifier: irreparable harm
  span: For these reasons, we hold that plaintiffs did not show—based on the record before the district court when it entered this preliminary injunction—that they were “likely to suffer irreparable harm in the absence of preliminary relief.” Winter, 555 U.S. at 20 (emphasis added). We thus vacate the preliminary injunction without addressing whether plaintiffs satisfy the remaining three Winter factors.
  url: https://www.ca4.uscourts.gov/opinions/251411.P.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c4
  type: quote
  value: All statements to the contrary in AFT are abrogated
  qualifier: abrogated
  span: Plaintiffs need not clear a different or additional hurdle in cases involving multiple issues or defenses. All statements to the contrary in AFT are abrogated.
  url: https://www.ca4.uscourts.gov/opinions/251411.P.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c5
  type: quote
  value: in violation of the Privacy Act and the APA
  qualifier: likely to succeed
  span: They are also likely to succeed on their claim that the Agency’s actions are arbitrary and capricious, and in violation of the Privacy Act and the APA.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.146.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c6
  type: quote
  value: SSA may proceed to afford members of the SSA DOGE Team access to the agency records in question
  qualifier: may proceed
  span: We conclude that, under the present circumstances, SSA may proceed to afford members of the SSA DOGE Team access to the agency records in question in order for those members to do their work.
  url: https://www.supremecourt.gov/opinions/24pdf/24a1063_6j37.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
---
The Fourth Circuit, sitting en banc, decided *AFSCME v. SSA* and wrote: "We now vacate the current preliminary injunction". The ground was irreparable harm only. The court held the plaintiffs had not shown it on the record before the district court and vacated "without addressing whether plaintiffs satisfy the remaining three Winter factors", which include likelihood of success on the merits.

**What was vacated.** Judge Ellen Lipton Hollander's Maryland preliminary injunction had found the plaintiffs likely to succeed on the claim that SSA's grant of access to its DOGE team was arbitrary and capricious and "in violation of the Privacy Act and the APA". The Supreme Court had already stayed that injunction, writing that "SSA may proceed to afford members of the SSA DOGE Team access to the agency records in question".

**What the ruling does not do.** It does not hold that SSA complied with the Privacy Act. No appellate court reached that question. The district court's likely-violation finding no longer has any operative effect, but it was never reversed on the merits. The en banc court also disavowed the panel's multiplicative probability test from the companion Treasury, Education and OPM case: "All statements to the contrary in AFT are abrogated".

**Ledger classification.** FOUND at the district court (preliminary). STAYED by the Supreme Court. VACATED by the en banc court on a non-merits ground. The case went back to Maryland, where the government's own corrections to the record became the basis for discovery; see [[2026-06-26--hollander-holds-ssa-admissions-show-tro-noncompliance-questions-orders-discovery]].
