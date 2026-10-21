---
type: timeline_event
id: 2026-06-26--hollander-holds-ssa-admissions-show-tro-noncompliance-questions-orders-discovery
date: '2026-06-26'
title: "Judge Hollander Refuses to Rescind DOGE Discovery, Citing SSA's Own Admissions of PII Searches and Access After the Restraining Order (AFSCME v. SSA)"
importance: 8
status: confirmed
tags:
  - privacy-act
  - doge
  - ssa
  - judicial-ruling
  - agency-admission
  - privacy-rules-ledger
actors:
  - Judge Ellen Lipton Hollander
  - Social Security Administration
  - Department of Government Efficiency (DOGE)
  - Department of Justice
  - American Federation of State County and Municipal Employees (AFSCME)
sources:
  - title: "Memorandum Opinion, AFSCME v. SSA, 1:25-cv-00596-ELH (D. Md.), ECF 236"
    url: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.236.0.pdf"
    publisher: "US District Court, D. Md."
    date: '2026-06-26'
    tier: 1
  - title: "Notice of Corrections to the Record, AFSCME v. SSA, ECF 197"
    url: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf"
    publisher: "US Department of Justice, Civil Division (filed for SSA)"
    date: '2026-01-16'
    tier: 1
related_events:
  - 2026-01-16--afscme-v-ssa-notice-corrections-doge-unauthorized-access-prosecutorial-predicate
  - 2026-04-10--fourth-circuit-en-banc-vacates-afscme-v-ssa-injunction-irreparable-harm-only
capture_lanes:
  - Surveillance Infrastructure
  - Digital and Tech Capture
event_date_claim: c1
verification: source-verified
claims:
- id: c1
  type: date
  value: June 26, 2026
  qualifier: Date
  span: 'For the foregoing reasons, I shall deny the Motion to Rescind. An Order follows, consistent with this Memorandum Opinion. Date: June 26, 2026'
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.236.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c2
  type: quote
  value: DOGE personnel received PII access on at least two occasions after the TRO was issued
  qualifier: admitted
  span: In particular, defendants have admitted that DOGE Team members ran PII searches on SSA systems on the morning of the very day compliance with the TRO was certified, and that DOGE personnel received PII access on at least two occasions after the TRO was issued.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.236.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c3
  type: quote
  value: Cloudflare is not approved for storing SSA data
  qualifier: security protocols
  span: Cloudflare is not approved for storing SSA data and when used in this manner is outside SSA’s security protocols.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c4
  type: quote
  value: names and addresses of approximately 1,000 people
  qualifier: approximately
  span: SSA believes that the encrypted attachment contained PII derived from SSA systems of record, including names and addresses of approximately 1,000 people.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c5
  type: quote
  value: This agreement was not reviewed or approved through the agency’s data exchange procedures.
  qualifier: not reviewed or approved
  span: Nor were they aware of the “Voter Data Agreement.” This agreement was not reviewed or approved through the agency’s data exchange procedures.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c6
  type: quote
  value: SSA has not yet seen evidence that SSA data were shared with the advocacy group
  qualifier: not yet seen evidence
  span: Email communications reviewed by SSA suggest that DOGE Team members could have been asked to assist the advocacy group by accessing SSA data to match to the voter rolls, but SSA has not yet seen evidence that SSA data were shared with the advocacy group.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c7
  type: quote
  value: SSA believed that statement to be accurate at the time it was made
  qualifier: believed
  span: SSA believed that statement to be accurate at the time it was made.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
---
Judge Ellen Lipton Hollander denied the government's motion to rescind her order allowing limited discovery in *AFSCME v. SSA*. She rested the ruling on the government's own corrections to the record, which she described as admissions that DOGE team members ran PII searches on the day compliance with the restraining order was certified, and that "DOGE personnel received PII access on at least two occasions after the TRO was issued".

**The admissions the court relied on (agency's own filing).** In its notice of corrections, filed by the Justice Department for SSA, the agency stated:
- DOGE team members had shared data through a third-party server, and "Cloudflare is not approved for storing SSA data". The notice dates this to the days before the restraining order. SSA said it could not determine what data went there.
- A DOGE team member emailed an encrypted file to DHS, copying a senior U.S. DOGE Service adviser. SSA believes the file held "names and addresses of approximately 1,000 people".
- A DOGE team member signed a voter-data agreement with a political advocacy group. SSA said "This agreement was not reviewed or approved through the agency’s data exchange procedures." It also said "SSA has not yet seen evidence that SSA data were shared with the advocacy group".

**Ledger class.** ADMITTED. The court's opinion treats the admissions as raising questions of noncompliance with a court order sufficient to justify discovery. It is not a contempt finding and not a holding that the Privacy Act was violated. For each earlier declaration it corrects, the notice repeats that "SSA believed that statement to be accurate at the time it was made".
