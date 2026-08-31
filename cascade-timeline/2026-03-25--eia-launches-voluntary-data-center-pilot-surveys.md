---
type: timeline_event
id: 2026-03-25--eia-launches-voluntary-data-center-pilot-surveys
date: '2026-03-25'
title: "EIA launches three voluntary pilot field studies on data-center energy use — first federal data-collection attempt since the 2024 crypto-mining survey was litigated away, but data-center-wide rather than crypto-specific"
importance: 6
status: confirmed
tags:
  - investigation-6
  - crypto-mining
  - eia-862
  - energy-data
  - transparency
  - data-centers
  - tristan-abbey
  - crypto-energy-gap
actors:
  - U.S. Energy Information Administration
  - Tristan Abbey
  - Department of Energy
sources:
  - title: "EIA launches pilot survey on energy use at data centers"
    url: https://www.eia.gov/pressroom/releases/press585.php
    publisher: U.S. Energy Information Administration (press release)
    date: '2026-03-25'
    tier: 1
  - title: "Cryptocurrency Mining and the Electricity Sector"
    url: https://www.everycrsreport.com/reports/R48914.html
    publisher: Congressional Research Service (R48914)
    date: '2026-04-22'
    tier: 1
  - title: "EIA to Ditch Some Existing Reports and Launch New Surveys on Minerals, Data Centers"
    url: https://www.reuters.com/business/energy/eia-ditch-some-existing-reports-launch-new-surveys-minerals-data-centers-2025-12-05/
    publisher: Reuters (Arathy Somasekhar)
    date: '2025-12-05'
    tier: 1
capture_lanes:
  - Environmental Capture
  - Regulatory Capture
  - Transparency and Accountability
coverage: []
---

## Opening

On March 25, 2026, EIA announced it was launching three voluntary pilot field studies "to evaluate energy consumption in data centers," with web-based surveys in Texas and Washington state and in-person interviews in Northern Virginia and Washington, DC. This is the first EIA attempt at systematic energy-consumption data collection touching the crypto-mining/data-center sector since the mandatory Cryptocurrency Mining Facilities Survey (Form EIA-862) was withdrawn under litigation settlement in March 2024 (see [[2024-03-01--doe-eia-settle-riot-suit-withdraw-crypto-survey-destroy-data]]) — but it is explicitly broader (data centers generally) and, critically, voluntary rather than mandatory.

## What Happened / Key Facts

**Scope**: per EIA's own press release, the agency identified 196 companies operating data centers across the three target regions; each is asked to report energy use for at least one facility, covering energy sources, electricity consumption, site characteristics, server metrics, and cooling systems.

**Not a crypto-mining survey**: nothing in the press release singles out cryptocurrency-mining facilities as a distinct category. A crypto-mining operation that also functions as (or has converted to) an AI/HPC data center — the miner-to-AI-hosting pivot documented at [[2025-02-01--core-scientific-590mw-coreweave-conversion-miner-to-ai-pivot]] — could be captured incidentally, but pure proof-of-work mining facilities that have not pivoted to hosting are not the pilot's target population.

**Context**: EIA Administrator Tristan Abbey framed the pilots as part of a broader modernization: "A tremendous amount of excellent work goes into our retrospective consumption surveys, but they were conceived decades ago. Going forward, that excellent work will be geared toward faster cycles and finer detail." A companion pilot on critical minerals (graphite, vanadium, zirconium) had launched in February 2026.

**The mandatory-survey commitment remains unfulfilled and now explicitly conditional**: per an April 9, 2026 letter from Abbey to Senators Josh Hawley and Elizabeth Warren (cited in CRS R48914), EIA states it will consider developing "a mandatory survey(s) under the notice and public comment procedures of the Paperwork Reduction Act" only "[f]ollowing evaluation of the pilot studies and resulting data" — no committed timeline, and no explicit reference to reviving a crypto-specific instrument distinct from the general data-center pilots.

## Why This Event Matters

This is the closest thing to a "successor data-collection effort" that exists as of this research pass, and the precise, accurate characterization matters: it is **not** a re-launch of the crypto-mining survey industry litigation killed in 2024. It is voluntary, broader in scope (all data centers, not crypto-mining specifically), and its eventual conversion to a mandatory instrument is explicitly contingent and undated. The public record therefore continues to support the finding that no authoritative, mandatory federal dataset on crypto-miner-specific power consumption exists, more than two years after the one such dataset was ordered destroyed.

## Broader Context

See [[the-crypto-energy-data-gap]] for the full synthesis and [[bitcoin-mining-as-electricity-price-floor]] Part 4 for how this absence blocks a national-scale adjudication of crypto mining's price effects.

## Research Gaps

- [ ] Whether the pilot studies' 196-company sample includes any facilities also registered under Texas SB 1929 as crypto-mining operations (would require cross-referencing EIA's target list, not publicly itemized, against the PUCT SB 1929 registry — itself contested, see [[2025-08-11--puct-sues-ag-paxton-crypto-mining-data]]).
- [ ] No public timeline exists for "evaluation of the pilot studies" concluding or a subsequent notice-and-comment mandatory survey being proposed; track EIA press releases and the Federal Register going forward.

## Related Entries

- [[2024-02-22--riot-texas-blockchain-council-sue-doe-eia-862-tro]]
- [[2024-03-01--doe-eia-settle-riot-suit-withdraw-crypto-survey-destroy-data]]
- [[the-crypto-energy-data-gap]]
- [[bitcoin-mining-as-electricity-price-floor]]
- [[2025-02-01--core-scientific-590mw-coreweave-conversion-miner-to-ai-pivot]]
- [[epic-inv6-energy-systems-convergent-demand-shock]]
