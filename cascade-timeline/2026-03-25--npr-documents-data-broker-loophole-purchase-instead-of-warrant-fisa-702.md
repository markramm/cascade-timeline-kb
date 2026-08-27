---
type: timeline_event
id: 2026-03-25--npr-documents-data-broker-loophole-purchase-instead-of-warrant-fisa-702
date: '2026-03-25'
title: "NPR Documents the Data-Broker Loophole as FISA 702 Reauthorization Nears; Patel Declines to Rule Out Location Buys"
importance: 9
status: confirmed
tags:
  - surveillance-infrastructure
  - data-broker
  - immigration-enforcement
  - procurement
  - fourth-amendment
  - congressional-oversight
actors:
  - Jude Joffe-Block
  - Kash Patel
  - Ron Wyden
  - Warren Davidson
  - Mike Lee
  - Zoe Lofgren
  - Jake Laperruque
  - Sean Vitka
  - Jeramie D. Scott
  - Dario Amodei
  - U.S. Immigration and Customs Enforcement
  - Homeland Security Investigations
  - Federal Bureau of Investigation
  - Penlink
  - Thomson Reuters
sources:
  - title: "Your data is everywhere. The government is buying it without a warrant"
    url: https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic
    publisher: NPR
    date: '2026-03-25'
    tier: 1
  - title: "FY26_RFI-Big Data & Ad Tech"
    url: https://sam.gov/workspace/contract/opp/411452e8b3614944b9c50cc3aa24fb42/view
    publisher: SAM.gov
    date: '2026-01-23'
    tier: 1
  - title: "DHS-built surveillance apparatus to surge in year ahead, documents show"
    url: https://fedscoop.com/dhs-surveillance-technology-ai-funding-document-spyware/
    publisher: FedScoop
    date: '2026-03-16'
    tier: 1
  - title: "The Data Brokers Fueling ICE's Deportation Machine—And the Union Shareholders Fighting Back"
    url: https://inthesetimes.com/article/ice-deportation-machine-surveillance-artificial-intelligence-thomson-reuters-clear-trump
    publisher: In These Times
    date: '2025-10-23'
    tier: 2
---

NPR's Jude Joffe-Block published a documented account of the federal government's data-broker purchasing practice on March 25, 2026, three weeks before Section 702 of the Foreign Intelligence Surveillance Act was set to expire on April 20. The reporting establishes the mechanism plainly: after a 2015 statutory change — the USA Freedom Act, passed after the Snowden disclosures — federal agencies are barred from collecting bulk data on Americans, and some agencies have responded by buying the same data from commercial brokers instead. At a Senate hearing the week before publication, Senator Ron Wyden asked FBI Director Kash Patel to commit to not buying Americans' location data. Patel declined, saying the Bureau "uses all tools" and "we do purchase commercially available information that's consistent with the Constitution and the laws under the Electronic Communications Privacy Act." An FBI spokesperson declined to say which commercial data the Bureau buys. In 2023, then-director Christopher Wray had indicated the FBI backed away from commercial databases carrying advertising-derived location data; Patel's answer is the reversal on the record.

The legal status of the practice is what the entry turns on, and it should be stated as the theory being relied on rather than as settled law. Courts have not ruled on whether the federal government may purchase in bulk what it would need a warrant to seize, which leaves the practice in an untested gray area that both sides read in their favor. Privacy advocates argue the purchases circumvent the Fourth Amendment and contradict the 2015 bulk-collection ban, and they invoke *Carpenter v. United States* (2018), where the Supreme Court held that police need a warrant for historical cell-site location records. Jake Laperruque of the Center for Democracy and Technology framed the objection by analogy: "We certainly wouldn't imagine a scenario where the police said, 'We're going to search your house. We don't have a warrant, but we paid your landlord $100 to give us a spare key.'" Representative Warren Davidson (R-Ohio), working with Senator Mike Lee, Representative Zoe Lofgren, and Wyden on bicameral reform legislation, described the purchases as sweeping in "data that really you would never get a warrant for, that kind of a broad dragnet sweep under normal warrant requirements." The White House and Speaker Mike Johnson pushed for a clean reauthorization with no reform attached; Johnson delayed the House vote to mid-April. Some 130 civil society organizations signed a letter urging Congress to close the loophole in the reauthorization, warning of "unprecedented expansion of warrantless mass surveillance." Sean Vitka of Demand Progress called it "very likely the only chance that Congress has this year to vote for meaningful privacy protections."

**This entry is the spine for the purchase-instead-of-warrant mechanism, and much of the corpus consists of its instances.** The procurement side is visible in the FY26 Big Data & Ad Tech RFI that ICE's Homeland Security Investigations posted to SAM.gov on January 23, 2026 (opportunity 411452e8b3614944b9c50cc3aa24fb42), seeking to "understand the current state of Ad Tech compliant and location data services available to federal investigative and operational entities" — market research, explicitly not a solicitation, with responses due February 2 and selected respondents invited to demonstrate their platforms live. The same HSI later took the commercial route to voter files ([[2026-08-26--hsi-solicits-private-contractor-voter-registration-files-fraud-detection]]), asking a vendor for records it could not compel states to hand over. ICE's Penlink contract for the Webloc phone-tracking program, cited in the NPR piece, sits alongside the no-bid PLX award for real-time interception ([[2026-04-29--dhs-penlink-plx-no-bid-contract-warrantless-realtime-interception]]) and the Maryland attorney general's complaint against Penlink and Thomson Reuters over geolocation sales to ICE ([[2026-08-20--maryland-ag-complaint-penlink-thomson-reuters-geolocation-ice]]). Thomson Reuters' CLEAR platform, which In These Times documented in October 2025 as central to ICE's targeting work, aggregates court records, driving records, business filings, and social media into individual dossiers sold without judicial oversight. The doctrinal root is older than any of it: *United States v. Miller* (1976) ([[1976-06-23--united-states-v-miller-bank-records-third-party-doctrine]]) held that records voluntarily conveyed to a third party carry no Fourth Amendment privacy interest — the premise every subsequent purchase rests on, and the one *Carpenter* limited without overruling.

The consolidation layer is where the purchases stop being separable. ImmigrationOS pulls Medicaid, IRS, and DMV records into a single Palantir-hosted platform that tracks U.S. citizens as well as immigrants ([[2026-04-01--immigrationos-palantir-tracking-us-citizens-medicaid-irs-dmv]]); CMS shared Medicaid data with ICE ([[2025-10-01--cms-shares-medicaid-data-with-ice]]) and a later transfer was found illegal ([[2026-07-17--ice-medicaid-palantir-illegal-data-transfer]]); DHS signed a billion-dollar Palantir blanket purchase agreement with zero privacy impact assessments completed ([[2026-02-19--dhs-signs-billion-dollar-palantir-ice-surveillance-contract]], [[2026-05-13--dhs-zero-privacy-impact-assessments-palantir-1-billion-no-bid]]); ICE and CBP surveillance-technology spending reached $513 million in 2026 with Palantir named the backbone ([[2026-07-14--ice-cbp-surveillance-spending-513m-palantir-backbone]]); and DHS's own AI inventory now runs to roughly 200 use cases ([[2026-08-14--dhs-ai-inventory-200-use-cases-palantir-elite-confidence-scores-911-ingestion]], [[2026-08-10--lawfare-documents-three-dhs-ai-systems-immigrationos-hurricane-score-asylum-analytics]]). Anthropic CEO Dario Amodei, quoted in the NPR piece, named the compounding problem: records the government can purchase can be assembled by AI into "a comprehensive picture of any person's life—automatically and at massive scale." Because Congress has not closed the loophole, the counter-pressure has moved to the states — New Jersey's broker law ([[2026-06-30--new-jersey-enacts-costliest-data-broker-law-a5328]]) and California's DROP deletion platform ([[2026-08-01--california-drop-platform-live-first-centralized-data-broker-deletion]]), whose SB 361 rationale names this exact mechanism. Kash Patel had already confirmed the FBI's warrantless commercial purchases a week before NPR ran ([[2026-03-18--patel-fbi-confirms-warrantless-purchase-commercial-data]]), and Attorney General Bondi's request for Minnesota's voter rolls framed them as an ICE-enforcement resource ([[2026-01-26--bondi-voter-rolls-request-minnesota-ice-enforcement]]).
