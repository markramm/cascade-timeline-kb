---
type: timeline_event
id: 2025-10-07--tether-loan-lutnick-children-ucc-filing
date: '2025-10-07'
event_date_claim: c2
title: Tether Loan to Lutnick Children Revealed via UCC Filing
importance: 9
tags:
- tether
- lutnick
- cantor-fitzgerald
- crypto
- conflict-of-interest
actors:
- tether
- Howard Lutnick
- Cantor Fitzgerald
- Dynasty Trust A
sources:
- url: https://www.banking.senate.gov/imo/media/doc/20260429warrenwydenlettertolutnickretethercantorfitzgeraldloan.pdf
  title: Warren and Wyden letter to Secretary Lutnick, April 29, 2026
  tier: 1
- url: https://www.kucoin.com/news/flash/tether-loan-to-u-s-commerce-secretary-s-children-sparks-ethics-concerns
  title: KuCoin News, summary of Bloomberg's March 18, 2026 report
  tier: 3
- url: https://thechainobserver.com/swan-bitcoin-to-subpoena-cantor-fitzgerald/
  title: The Chain Observer, on Swan Bitcoin's 28 U.S.C. 1782 application
  tier: 3
status: reported
capture_lanes:
- financial-capture
- regulatory-capture
verification: source-verified
claims:
- id: c1
  type: date
  value: October 6, 2025
  qualifier: divested
  span: On October 6, 2025, after serving nearly eight months as Secretary of the Commerce Department, you finally divested your multi-billion dollar stake in Cantor Fitzgerald by selling your portion of the company to your children.
  url: https://www.banking.senate.gov/imo/media/doc/20260429warrenwydenlettertolutnickretethercantorfitzgeraldloan.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-15'
- id: c2
  type: date
  value: October 7
  qualifier: credit document filed in New York
  span: Recent Bloomberg reporting found that on the very next day, October 7, a credit document was filed in New York revealing that Tether lent an undisclosed amount to a trust called “Dynasty Trust A.”
  url: https://www.banking.senate.gov/imo/media/doc/20260429warrenwydenlettertolutnickretethercantorfitzgeraldloan.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-15'
- id: c3
  type: figure
  value: four
  qualifier: the trust's beneficiaries
  span: Your four children are the trust’s beneficiaries.
  url: https://www.banking.senate.gov/imo/media/doc/20260429warrenwydenlettertolutnickretethercantorfitzgeraldloan.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-15'
- id: c4
  type: quote
  value: all assets
  qualifier: reportedly secured by
  span: The loan is reportedly secured by “all assets” held by the trust, including “more than half the equity in Cantor Fitzgerald.”
  url: https://www.banking.senate.gov/imo/media/doc/20260429warrenwydenlettertolutnickretethercantorfitzgeraldloan.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-15'
- id: c5
  type: quote
  value: collateral agent
  qualifier: identified
  span: The filing also references a public UCC filing from October 2025 that identified Tether as collateral agent for Dynasty Trust A, which Swan links to the Lutnick family trust.
  url: https://thechainobserver.com/swan-bitcoin-to-subpoena-cantor-fitzgerald/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-15'
- id: c6
  type: figure
  value: 5%
  qualifier: said
  span: A Cantor executive familiar with the transaction said the loan is specifically collateralized by a convertible bond that gives Cantor the right to acquire a 5% equity stake in Tether.
  url: https://www.kucoin.com/news/flash/tether-loan-to-u-s-commerce-secretary-s-children-sparks-ethics-concerns
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-15'
previous_ids: ['2025-10-06--tether-loan-lutnick-children-ucc-filing']
---

A credit document filed in New York on October 7, 2025, the day after Howard Lutnick sold his stake in the financial-services firm to his children, shows Tether lending an undisclosed amount to "Dynasty Trust A," according to Bloomberg reporting as relayed in an April 2026 letter from Senators Warren and Wyden. The senators write that the trust's four beneficiaries are Lutnick's children and that the loan is reportedly secured by "all assets" the trust holds, including more than half of the firm's equity, in the senators' words. A court application by a party in a separate Tether dispute, as reported by a trade outlet, says a public UCC filing identified Tether as collateral agent for the trust. A summary of the Bloomberg report quotes a firm executive saying the loan is collateralized by a convertible bond that gives the firm the right to acquire a 5% stake in Tether.

The senators ask whether Tether helped finance the children's purchase; the loan's size and the price paid for the stake are not disclosed. We have not read the UCC filing itself.


## Corrections (2026-11-16)

- Date moved from the sale date to the filing date given in the senators' letter.
- Cut: the claim that the trust holds majority ownership of the firm and that the children owe their control of it to Tether. The senators say only that the loan is reportedly secured by more than half of the firm's equity and ask whether Tether helped finance the purchase.
- Cut: the statement that the filing exposes the loan as financing for the purchase. The senators frame it as a question; the loan's size and the purchase price are undisclosed.
- Cut: the circular-dependency framing and the statement that the Commerce Secretary's regulatory role benefits Tether. No fetched source bound to this entry states it as fact.
- Cut: the statement about the firm's custody relationship with Tether's reserves (no bound span).
- Attributed: the collateral-agent description now rests on a litigant's court application as reported by a trade outlet, not on the filing's own text.
- Removed the individual children from the actors list; the sources say only that there are four children.
