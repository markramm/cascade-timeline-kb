---
type: "timeline_event"
id: "2025-05-13--tiny-company-with-china-ties-announces-big-purchase-of-trump"
date: "2025-05-13"
title: "GD Culture Group Signs Up-to-$300M Stock Purchase Agreement With an Unnamed Investor; Proceeds, \"If Any,\" for Bitcoin and OFFICIAL TRUMP"
description: "GD Culture Group, a Nasdaq-listed company, disclosed a Common Stock Purchase Agreement under which it holds the right to require an unnamed investor to buy up to $300,000,000 of its stock. The filing names Bitcoin and OFFICIAL TRUMP as possible uses of proceeds, if any. It is an equity line, not a commitment to buy crypto."
status: "confirmed"
importance: 7
location: "Washington, D.C."
actors:
- "GD Culture Group"
tags:
- "crypto"
- "equity-line"
- "nasdaq"
capture_type: "regulatory_capture"
sources:
- date: "2025-05-13"
  outlet: "SEC EDGAR (Form 8-K, acc. 0001213900-25-042662)"
  title: "GD Culture Group Limited, Form 8-K, Item 1.01"
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  tier: 1
- date: "2025-05-14"
  outlet: "FXStreet"
  title: "GD Culture Group's $300M TRUMP coin purchase fails to sustain meme coin rally"
  url: "https://www.fxstreet.com/cryptocurrencies/news/trump-meme-coin-loses-steam-as-china-linked-gd-culture-group-invests-300m-in-bitcoin-and-trump-202505140559"
  tier: 2
- date: "2025-05-12"
  outlet: "The New York Times"
  title: "Tiny company with China ties announces big purchase of Trump cryptocurrency"
  url: "https://www.nytimes.com/2025/05/13/us/politics/trump-crypto-purchase.html"
  tier: 1
- date: "2025-05-13"
  outlet: "GlobeNewswire"
  title: "GD Culture Group Limited Announces $300 Million Funding Commitment to Build Cryptocurrency Reserve of Bitcoin and Trump Coin"
  url: "https://www.globenewswire.com/news-release/2025/05/12/3079197/0/en/GD-Culture-Group-Limited-Announces-300-Million-Funding-Commitment-to-Build-Cryptocurrency-Reserve-of-Bitcoin-and-Trump-Coin.html"
  tier: 3
connections:
- "Equity-line financing at a distressed Nasdaq issuer"
patterns:
verification: "captured"
event_date_claim: "c1"
claims:
- id: "c1"
  type: "date"
  value: "May 13, 2025"
  qualifier: "Date"
  span: "Date: May 13, 2025 By: /s/ Xiao Jian Wang"
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c2"
  type: "quote"
  value: "an investor"
  qualifier: "investor"
  span: "On May 11, 2025, GD Culture Group Limited. (the “Company”) entered into a Common Stock Purchase Agreement (the “Agreement”) with an investor (the “Investor”)."
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c3"
  type: "quote"
  value: "shall have the right to require the Investor to purchase, from time to time, up to a cumulative total of $300,000,000 worth of the Company’s common stock"
  qualifier: "right"
  span: "Under the Agreement, the Company shall have the right to require the Investor to purchase, from time to time, up to a cumulative total of $300,000,000 worth of the Company’s common stock."
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c4"
  type: "figure"
  value: "$0.44"
  qualifier: "lower"
  span: "but shall in no event be lower than $0.44"
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c5"
  type: "figure"
  value: "4.99%"
  qualifier: "beneficially"
  span: "the Company may not require any purchase by the Investor to the extent that such purchase would result in the Investor beneficially owning more than 4.99% of the Company’s common stock immediately thereafter"
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c6"
  type: "figure"
  value: "3,357,407"
  qualifier: "shares"
  span: "The Company may not issue more than 3,357,407 shares of common stock to the Investor (equal to 19.99% of the Company’s outstanding shares of common stock on the date of the Agreement) unless or until shareholder approval of such issuances is obtained."
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c7"
  type: "quote"
  value: "if any, to invest in Bitcoin and OFFICIAL TRUMP and for general corporate purposes"
  qualifier: "proceeds"
  span: "The Company plans to use proceeds from the offering, if any, to invest in Bitcoin and OFFICIAL TRUMP and for general corporate purposes."
  url: "https://www.sec.gov/Archives/edgar/data/1641398/000121390025042662/ea0241820-8k_gdculture.htm"
  read: "fetched"
  source_kind: "primary"
- id: "c8"
  type: "quote"
  value: "has announced a colossal purchase of the Official Trump meme coin worth $300 million"
  qualifier: "announced"
  span: "GD Culture Group, a technology firm with ties to China, has announced a colossal purchase of the Official Trump meme coin worth $300 million."
  url: "https://www.fxstreet.com/cryptocurrencies/news/trump-meme-coin-loses-steam-as-china-linked-gd-culture-group-invests-300m-in-bitcoin-and-trump-202505140559"
  read: "fetched"
  source_kind: "secondary"
- id: "c9"
  type: "quote"
  value: "an unnamed entity domiciled in the British Virgin Islands"
  qualifier: "According"
  span: "According to The New York Times, this investment channel proceeds from a stock sale to an unnamed entity domiciled in the British Virgin Islands."
  url: "https://www.fxstreet.com/cryptocurrencies/news/trump-meme-coin-loses-steam-as-china-linked-gd-culture-group-invests-300m-in-bitcoin-and-trump-202505140559"
  read: "fetched"
  source_kind: "secondary"
capture_lanes:
- "Financial Capture"
related_events:
- "2025-09-29--gd-culture-pallas-capital-btc-acquisition-bvi-related-party"
---
GD Culture Group Limited (Nasdaq: GDC) signed a Common Stock Purchase Agreement with "an investor." The current report says GDC "shall have the right to require the Investor to purchase, from time to time, up to a cumulative total of $300,000,000 worth of the Company’s common stock." The deal is an equity line: GDC holds the put, and the investor's obligation is limited by a price floor of $0.44, an ownership cap of 4.99% and a cap of 3,357,407 shares absent shareholder approval.

## What the filing says about use of proceeds

The filing says GDC plans to use proceeds from the offering, "if any, to invest in Bitcoin and OFFICIAL TRUMP and for general corporate purposes." The token name is the only Trump reference in the filing. It does not name the investor, does not state where the investor is organized, and does not link the transaction to any person associated with Trump.

## How it was reported

FXStreet wrote that GD Culture Group "has announced a colossal purchase of the Official Trump meme coin worth $300 million" and, citing The New York Times, that the proceeds come from a stock sale to "an unnamed entity domiciled in the British Virgin Islands." Those are the outlet's characterizations.

## Related

GDC's crypto acquisition came through a separate deal: [[2025-09-29--gd-culture-pallas-capital-btc-acquisition-bvi-related-party]].

## Corrected 2026-10-20

The title and body previously called this a cryptocurrency investment, named a British Virgin Islands entity as the buyer, and framed it as Trump-linked foreign influence. They were rewritten to match the filing. Statements about a delisting notice, congressional letters and an unfunded commitment were removed as unverified.
