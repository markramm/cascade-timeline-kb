---
type: timeline_event
id: 2026-08-01--california-drop-platform-live-first-centralized-data-broker-deletion
date: '2026-08-01'
title: "California's DROP Platform Goes Live — First US Centralized Data-Broker Deletion Mechanism, 45-Day Check Cycle"
importance: 7
status: confirmed
tags:
  - data-brokers
  - privacy-law
  - surveillance
  - state-regulation
  - california
actors:
  - California Privacy Protection Agency
  - California data brokers
sources:
  - title: "Information for Data Brokers"
    url: https://cppa.ca.gov/data_brokers/
    publisher: California Privacy Protection Agency
    date: '2026-08-01'
    tier: 1
  - title: "Data Broker Registration Explained (2026): How to Register Under U.S. Privacy Laws"
    url: https://secureprivacy.ai/blog/data-broker-registration
    publisher: Secure Privacy
    date: '2026-08-01'
    tier: 2
  - title: "U.S. Privacy Laws That Take Effect in 2026"
    url: https://vaultjs.com/resources/us-privacy-laws-and-key-provisions-that-take-effect-or-become-enforceable-in-2026/
    publisher: Vault JS
    date: '2026-08-01'
    tier: 2
  - title: "CalPrivacy Announces Second Data Broker Enforcement Action in Less Than a Week"
    url: https://privacy.ca.gov/2026/08/calprivacy-announces-second-data-broker-enforcement-action-in-less-than-a-week/
    publisher: California Privacy Protection Agency
    date: '2026-08-13'
    tier: 1
  - title: "New Law and Regulations Expand California's Data Broker Oversight"
    url: https://technologylaw.fkks.com/post/102lp8c/new-law-and-regulations-expand-californias-data-broker-oversight
    publisher: Frankfurt Kurnit Klein & Selz
    date: '2026-08-19'
    tier: 2
  - title: "DROP Is Live: What Data Brokers Need to Know as CalPrivacy Ramps Up Oversight"
    url: https://www.freshfields.com/en/our-thinking/blogs/a-fresh-take/drop-is-live-what-data-brokers-need-to-know-as-calprivacy-ramps-up-oversight-102nqhf
    publisher: Freshfields
    date: '2026-08-13'
    tier: 2
  - title: "CalPrivacy Settles with Two Data Brokers Over Registration Failures and Privacy Violations"
    url: https://www.hunton.com/privacy-and-cybersecurity-law-blog/calprivacy-settles-with-two-data-brokers-over-registration-failures-and-privacy-violations
    publisher: Hunton Andrews Kurth
    date: '2026-08-13'
    tier: 2
---

California's Data Removal Platform (DROP), the centralized deletion mechanism created by the Delete Act, became operational on August 1, 2026. Registered data brokers must check DROP at least every 45 days and process consumer deletion requests within 90 days, with per-request civil penalties for non-compliance that accrue independently and can exceed the liability for failing to register at all. A single consumer request now propagates to hundreds of registered brokers at once. It is the first centralized opt-out enforcement mechanism in the United States, arriving alongside a wave of state privacy laws — Connecticut, Arkansas, and Utah effective July 1; Indiana, Kentucky, and Rhode Island effective January 1.

The structural significance is the inversion of transaction costs. Every prior deletion regime required the individual to identify each broker holding their data and file separately, which meant the right existed on paper and almost never in practice — the asymmetry between one person's time and hundreds of firms' inertia was the entire defense. A centralized registry collapses that. The corpus has been tracking the state-level accumulation: New Jersey's data broker law (2026-06-30--new-jersey-enacts-costliest-data-broker-law-a5328), Vermont's Data Privacy and Online Surveillance Act (2026-06-16--vermont-data-privacy-online-surveillance-act-broker-deletion-rights), the FTC barring Kochava from selling sensitive location data (2026-05-07--ftc-bars-kochava-selling-sensitive-location-data-settlement). The unresolved question is the one that matters most for the capture beat: whether DROP reaches government purchasers of broker records or only commercial use. DHS buys location data from the same brokers (2026-08-12--brennan-center-dhs-29b-domestic-surveillance-architecture), and a deletion right that stops at the point of federal acquisition leaves the surveillance pipeline intact while giving consumers the impression it has been severed.

## Update: 345,000 deletion requests, two enforcement settlements, and the sanctuary-circumvention rationale

Within days of DROP going live, more than 345,000 deletion requests had been submitted through the platform. The California Privacy Protection Agency followed with back-to-back enforcement settlements in less than a week: **LocateSmarter LLC**, which demanded unnecessary sensitive data from consumers in order to process their opt-out requests — a practice the agency treated as a CCPA violation in its own right, not merely a registry failure — and **Cybba Inc.**, which paid **$52,400** for failing to register by the 2025 deadline. The two actions read as the agency using the launch as an activation event for the registry as a whole rather than as isolated cases. The operative statute is the **Delete Act (SB 362)**, under which registered brokers must access DROP at least every 45 days, report on the requests they receive, and undergo periodic third-party audits. Seven states now have active data-broker laws: California, Oregon, Texas, Vermont, Montana, Connecticut, and New Jersey.

The most load-bearing item is the rationale the legislature itself put on the record. **SB 361**, signed October 2025, cites the concern that federal agencies were circumventing California's sanctuary and privacy protections by *purchasing* consumer data from brokers rather than seeking access to protected government databases. That is not a privacy-advocate inference; it is a state legislature naming the commercial-purchase workaround as the reason for the law. The same mechanism is documented across this corpus from the buyer's side: Maryland's attorney general complaint against Penlink and Thomson Reuters over geolocation data sold into ICE ([[2026-08-20--maryland-ag-complaint-penlink-thomson-reuters-geolocation-ice]]), DHS's no-bid Penlink PLX contract for warrantless real-time interception ([[2026-04-29--dhs-penlink-plx-no-bid-contract-warrantless-realtime-interception]]), ICE's bulk facial-recognition contracting through LexisNexis and Palantir ([[2026-08-10--ice-lexisnexis-palantir-bulk-facial-recognition-contract]]), and HSI soliciting a private contractor for voter-registration files under a fraud-detection framing ([[2026-08-26--hsi-solicits-private-contractor-voter-registration-files-fraud-detection]]). New Jersey's own broker statute is the nearest state-level cousin ([[2026-06-30--new-jersey-enacts-costliest-data-broker-law-a5328]]).

What SB 361's rationale does *not* settle is the question the original entry left open. Naming commercial purchase as the circumvention route establishes legislative intent; it does not establish that DROP deletion requests reach records already sold to or held by a federal purchaser. A statute can identify the leak and still not plug it, and nothing in the August activation or the two settlements demonstrates that a consumer deletion propagates past the point of federal acquisition.
