---
type: timeline_event
id: 2026-06-29--scotus-chatrie-location-data-fourth-amendment-geofence-warrant
date: '2026-06-29'
title: "SCOTUS in Chatrie v. United States Holds Obtaining Google Location History Was a Fourth Amendment Search, Leaves the Geofence Warrant Question on Remand"
importance: 9
event_date_claim: c3
status: confirmed
tags:
  - surveillance
  - fourth-amendment
  - scotus
  - location-data
  - data-brokers
actors:
  - Supreme Court of the United States
  - Electronic Frontier Foundation
  - Department of Justice
sources:
  - title: "Chatrie v. United States, 609 U.S. 605 (2026), preliminary print"
    url: https://www.supremecourt.gov/opinions/25pdf/609us2r64_7mio.pdf
    publisher: Supreme Court of the United States
    date: '2026-06-29'
    tier: 1
  - title: "Victory! Supreme Court Says Constitution Protects People's Location Data"
    url: https://www.eff.org/deeplinks/2026/06/victory-supreme-court-says-constitution-protects-peoples-location-data
    publisher: Electronic Frontier Foundation
    date: '2026-06-29'
    tier: 2
  - title: "What to know about the court's five latest rulings"
    url: https://www.scotusblog.com/2026/06/what-to-know-about-the-court-s-five-latest-rulings/
    publisher: SCOTUSblog
    date: '2026-06-29'
    tier: 1
coverage:
  - daily-capture-reports/headline/2026-06-29--chatrie-scotus-geofence-fourth-amendment-data-broker-threat.md  # consumed 2026-09-14
corrections:
- date: '2026-11-16'
  was: "First paragraph: the Court ruled that individuals have a Fourth Amendment expectation of privacy in location data revealing their physical movements, that even short-term surveillance is a search requiring a warrant, and that the ruling directly constrains law-enforcement and immigration agencies using geofence warrants without individualized warrant requirements; second paragraph: it bears directly on warrantless data-broker purchases."
  now: "The Court held that police conducted a Fourth Amendment search when they acquired Chatrie's location data from Google (a compelled production under a geofence warrant), because an individual has a reasonable expectation of privacy in his cell-phone location information. It left to the Fourth Circuit whether the warrant made the search reasonable and did not address good faith. The 'short-term' and 'broad implications' language is EFF's characterisation. The opinion does not reach purchases from data brokers."
  found_by: recheck-canon-medicaid-palantir-chatrie-702-lapse-obadal-entries (2026-11-16); read against the slip opinion, 609 U.S. 605
verification: source-verified
claims:
- id: c1
  type: attribution
  value: an individual has a reasonable expectation of privacy in his cell-phone location information
  qualifier: ''
  span: 'Held: Police officers conducted a Fourth Amendment search when they acquired Chatrie''s location data from Google because an individual has a reasonable expectation of privacy in his cell-phone location information.'
  url: https://www.supremecourt.gov/opinions/25pdf/609us2r64_7mio.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-16'
- id: c2
  type: attribution
  value: we do not address whether the good-faith exception
  qualifier: ''
  span: In line with our grant of certiorari, we do not address whether the good-faith exception to the exclusionary rule still allows the admission of the Location History data in this case.
  url: https://www.supremecourt.gov/opinions/25pdf/609us2r64_7mio.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-16'
- id: c3
  type: date
  value: June 29, 2026
  qualifier: ''
  span: No. 25–112. Argued April 27, 2026—Decided June 29, 2026
  url: https://www.supremecourt.gov/opinions/25pdf/609us2r64_7mio.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-16'
- id: c4
  type: quote
  value: Amazon purchase history
  qualifier: ''
  span: Do the police need a warrant to obtain a person's Amazon purchase history?
  url: https://www.supremecourt.gov/opinions/25pdf/609us2r64_7mio.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-16'
- id: c5
  type: attribution
  value: even short-term surveillance of these movements is a search subject to the Fourth Amendment
  qualifier: ''
  span: You have an expectation of privacy in location data that reveals your movements in the physical world, and even short-term surveillance of these movements is a search subject to the Fourth Amendment, the U.S. Supreme Court ruled today in Chatrie v. United States.
  url: https://www.eff.org/deeplinks/2026/06/victory-supreme-court-says-constitution-protects-peoples-location-data
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-16'
---

On June 29, 2026, the Supreme Court held in *Chatrie v. United States* that police conducted a Fourth Amendment search when they acquired Chatrie's location data from Google, because an individual has a reasonable expectation of privacy in his cell-phone location information. The Court left to the Fourth Circuit whether the multi-step geofence warrant made that search reasonable, and did not address the good-faith exception to the exclusionary rule. The case was vacated and remanded.

The Electronic Frontier Foundation reads the decision more broadly: that even short-term surveillance of a person's movements is a search subject to the Fourth Amendment, with implications for other app data. That is EFF's reading; the holding above is the Court's own statement in its syllabus.

The holding concerns data the police obtained from Google under a warrant that compelled production. Purchases of location data from data brokers are not the question the Court decided. The word "purchase" turns up in the opinion set only in Justice Alito's dissent, in a question about a person's Amazon purchase history, not about data brokers. Whether *Chatrie*'s reasoning reaches purchased data is open.

Related: [[2026-03-18--patel-fbi-confirms-warrantless-purchase-commercial-data]], [[2026-06-16--vermont-data-privacy-online-surveillance-act-broker-deletion-rights]], and, in the Fourth Amendment lineage, [[1972-06-19--keith-case-fourth-amendment-domestic-surveillance-warrant]] and [[1976-06-23--united-states-v-miller-bank-records-third-party-doctrine]].

For ICE's legal theory on purchased location data, see [[purchase-versus-search-doctrine-ice-legal-theory-cabining-carpenter-chatrie]].

## Correction (2026-11-16)

See the corrections field above.
