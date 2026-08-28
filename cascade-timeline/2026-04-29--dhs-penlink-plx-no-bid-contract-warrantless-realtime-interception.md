---
type: timeline_event
id: 2026-04-29--dhs-penlink-plx-no-bid-contract-warrantless-realtime-interception
date: '2026-04-29'
title: "DHS Holds $2.9M No-Bid Penlink PLX Contract for Warrantless Real-Time Phone, Text, Web Interception"
importance: 9
status: confirmed
tags:
  - surveillance-infrastructure
  - data-broker-loophole
  - warrantless-surveillance
  - immigration-system-capture
actors:
  - Department of Homeland Security
  - Penlink
  - Ron Wyden
  - LexisNexis
sources:
  - title: "DHS is buying access to real-time location data"
    url: "https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/"
    publisher: "Prism Reports"
    date: '2026-04-29'
    tier: 2
  - title: "Senators call for investigation of ICE/DHS warrantless location data purchases"
    url: "https://www.padilla.senate.gov/newsroom/press-releases/padilla-schiff-join-wyden-espaillat-colleagues-to-call-for-investigation-of-ice-dhs-warrantless-purchases-of-americans-location-data/"
    publisher: "Office of Sen. Alex Padilla"
    date: '2026-05-01'
    tier: 1
  - title: "Your data is everywhere. The government is buying it without a warrant."
    url: "https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic"
    publisher: "NPR"
    date: '2026-03-25'
    tier: 1
---

Prism Reports revealed on April 29, 2026 that DHS holds a $2.9 million no-bid contract (ceiling $8.3M) with Penlink, whose PLX platform intercepts live phone calls, texts, and web activity in real time and links the results directly to LexisNexis CLEAR personal-profile dossiers — with no warrant requirement and authority to target by location regardless of citizenship. When Senator Wyden's office sought a briefing on the contract, ICE cancelled with no explanation; more than 70 Democratic lawmakers subsequently demanded a DHS Inspector General investigation via Sen. Padilla's office.

The contract operationalizes the "data broker loophole" — executive-branch purchase of private surveillance capability that circumvents Fourth Amendment warrant requirements, the same loophole FBI Director Kash Patel confirmed using in March 2026 testimony ([[2026-03-18--patel-fbi-confirms-warrantless-purchase-commercial-data]]). It extends the same-quarter Clearview facial-recognition contract documented in [[2026-06-20--ice-largest-clearview-ai-contract-dhs-deletes-oversight-policy]] and feeds the same $513M/2026 surveillance-spending trajectory tracked in [[2026-07-14--ice-cbp-surveillance-spending-513m-palantir-backbone]]. It stands in tension with the Fourth Amendment location-data protections the Supreme Court articulated two months later in [[2026-06-29--scotus-chatrie-location-data-fourth-amendment-geofence-warrant]] — a ruling that does not reach warrantless purchase of already-aggregated commercial data.

## Sourcing note — 2026-08-28 pattern-projection audit

**"No-bid" is CONFIRMED for every Pen-Link/DHS award on the record. The specific dollar figures are NOT, and the entry may be attributing the wrong contract.**

Searched USAspending by recipient name (Pen-Link, Ltd., UEI TRJ2YRVP4A26) across contract award types. Every DHS award to Pen-Link is non-competitive:

| PIID | Component | Obligated | `extent_competed` | `solicitation_procedures` | Offers |
|---|---|---|---|---|---|
| `70CMSD22C00000001` | ICE | $26,155,762.25 | **NOT COMPETED (C)** | ONLY ONE SOURCE (SSS) | 1 |
| `70CMSD25P00000138` | ICE HSI (Cobweb/Tangles) | $2,284,750 | **NOT COMPETED (C)** | ONLY ONE SOURCE (SSS) | 1 |
| `70B03C25P00000508` | **CBP — "PENLINK PLX"** | $926,969 | NOT COMPETED UNDER SAP (G) | SIMPLIFIED ACQUISITION (SP1) | 1 |
| `70US0924C70093781` | DHS | $1,583,314 | — | — | — |
| `70VT1524P00003` | DHS | $282,291.55 | — | — | — |

**The problem**: the entry's "$2.9 million no-bid contract (ceiling $8.3M)" matches none of these obligated amounts, and the only award whose description names **PLX** specifically is a **CBP** purchase order at $926,969 — not the $2.9M ICE figure the entry implies. The closest ICE figure is the $2,284,750 HSI Cobweb/Tangles purchase order, which is a different Pen-Link product line. The $8.3M ceiling could not be located in any award's `base_and_all_options_value`.

**Disposition**: the load-bearing characterization ("no-bid") is independently confirmed against the primary record for all Pen-Link/DHS awards, so the entry's central claim stands and `status` is unchanged. But **the $2.9M/$8.3M figures and the ICE-vs-CBP attribution should be treated as unverified pending a re-read of the Prism Reports article against the specific PIID it describes.** Do not carry the $2.9M figure into a draft without resolving which award it refers to.

