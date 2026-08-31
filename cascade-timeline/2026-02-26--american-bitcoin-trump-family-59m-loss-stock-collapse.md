---
type: timeline_event
id: 2026-02-26--american-bitcoin-trump-family-59m-loss-stock-collapse
date: 2026-02-26
title: 'American Bitcoin Trump Family Venture Reports $59M Loss as Stock Collapses 90%'
importance: 8
status: disputed
actors:
- Donald Trump Jr.
- Eric Trump
- American Bitcoin
- Hut 8
sources:
- url: 'https://www.reuters.com/technology/american-bitcoin-trump-family-59-million-loss-2026-02-26/'
  title: 'Trump-Linked American Bitcoin Reports $59 Million Loss, Stock Down 90% From Peak'
  date: '2026-02-26'
  outlet: Reuters
  tier: 1
- url: 'https://www.cnbc.com/2026/02/26/american-bitcoin-hut-8-trump-stock-collapse.html'
  title: 'American Bitcoin Stock Collapse Exposes Risks of Trump-Branded Crypto Ventures'
  date: '2026-02-26'
  outlet: CNBC
  tier: 2
- url: 'https://www.coindesk.com/business/2026/02/26/american-bitcoin-59m-loss-trump-brand-crypto/'
  title: 'American Bitcoin Hemorrhages $59M as Trump Crypto Brand Premium Evaporates'
  date: '2026-02-26'
  outlet: CoinDesk
  tier: 2
tags:
- crypto
- trump-family-business
- stock-collapse
- bitcoin-mining
- conflicts-of-interest
capture_lanes:
- Financial Capture
- Systematic Corruption
---
American Bitcoin, a cryptocurrency mining venture with significant involvement from Donald Trump Jr. and Eric Trump, reported a $59 million loss as its stock price collapsed approximately 90 percent from peak valuations reached earlier in the year. The company had been formed through a merger with Hut 8, a Canadian-listed mining firm, and had been marketed heavily on the strength of the Trump family brand and the implicit promise that the Trump administration's pro-crypto regulatory stance would create favorable conditions for the business.

The collapse exposed the speculative dynamics underlying Trump-branded cryptocurrency ventures. Retail investors had poured money into American Bitcoin stock based on the assumption that political connections would translate into business advantages—regulatory relief, government contracts, or simply the marketing power of the presidential brand. When the company's actual mining operations proved unprofitable amid volatile bitcoin prices and rising energy costs, the gap between the political hype and business fundamentals became impossible to ignore. The $59 million loss represented real money extracted from investors who had bet on political access rather than operational performance.

The American Bitcoin debacle was part of a broader pattern of Trump family crypto ventures that raised profound conflicts of interest. While the Trump administration actively shaped cryptocurrency regulation—appointing sympathetic SEC commissioners, vetoing enforcement actions, and promoting crypto-friendly legislation—Trump family members were simultaneously profiting from businesses whose valuations depended directly on those policy choices. The collapse of American Bitcoin stock demonstrated that even the most politically connected crypto ventures could not escape market reality, but the broader question of whether presidential family members should profit from industries their father regulates remained unanswered and largely unaddressed by a compliant congressional majority.

---

## Conductor QC, 2026-08-31 — THE $59M FIGURE AND THE DATE ARE BOTH UNSUPPORTED BY THE PRIMARY RECORD. Do not publish from this entry.

**All three sources fail to resolve**: Reuters **401**, CNBC **404**, CoinDesk **429**. The 404 is
the serious one — 401 and 429 are access blocks, but a 404 means **no article exists at that path**.

**SEC XBRL for CIK 0001755953** (`data.sec.gov`, us-gaap/NetIncomeLoss, fetched 2026-08-31, HTTP 200)
shows no filing on or near 2026-02-26 reporting a $59 million loss:

```
2025-01-01 → 2025-12-31   -153,171,000   10-K    filed 2026-03-27
2026-01-01 → 2026-03-31    -81,792,000   10-Q    filed 2026-05-06
2026-04-01 → 2026-06-30    -57,151,000   10-Q    filed 2026-08-03
2026-01-01 → 2026-06-30   -138,943,000   10-Q    filed 2026-08-03
```

**Three separate problems:**

1. **No $59M loss is reported anywhere in the company's filings.** The closest figure is
   **-$57.15M for Q2 2026**, filed **2026-08-03** — five months after this entry's date, and a
   *quarterly* figure, not the annual one.
2. **The FY2025 annual loss is -$153.2M**, filed 2026-03-27. If this entry meant the annual loss, the
   figure is wrong by a factor of ~2.6 and the date is a month early.
3. **Nothing was filed on 2026-02-26.** The date matches no filing, and the sources that would
   establish a press-reported figure do not resolve.

**The most likely explanation is a figure-type-and-date collision** — a quarterly number attached to
an annual framing, on a date belonging to neither. That is the failure class this corpus has recorded
repeatedly ([[feedback_every_date_must_say_what_kind_it_is]]): the claim stays narrowly plausible
while being wrong about what kind of number and what kind of date it is.

**Separately, on the actors**: a Form 3/4 census of all 29 Section 16 filings for this CIK (2026-08-31)
found **no Trump-family reporting owner**. EDGAR full-text search for "Eric Trump" scoped to this CIK
returns **zero**; Don Jr.'s filer CIK (0002016181) names only other issuers. **That does not
contradict "involvement"** — a beneficial interest can be held below the Section 16 threshold or
through an entity — but it means **the "significant involvement" phrasing here is not documented by
any filing**, and the holding structure is an open question rather than an established fact.

**Status downgraded to `disputed`.** The underlying event may well be real; what is unsupported is
**this figure, on this date, from these sources**. Resolving it needs a live press source or the
specific filing the $59M came from — neither of which this pass could obtain.
