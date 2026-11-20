---
type: timeline_event
id: 2022-04-25--thiel-gives-protect-ohio-values-pac-15-million-in-three-contributions
previous_ids: ["2022-04-01--thiel-funds-vance-senate"]
date: 2022-04-25
date_kind: last of three contributions
title: 'Peter Thiel Funds Protect Ohio Values PAC, a Super PAC Backing J.D. Vance, Not His Campaign, With Gifts From March 2021 to April 2022'
title_corrected: '2026-11-19: earlier title said "Provides 15 Million to J.D. Vance''s Ohio Senate Campaign" and was dated 2022-04-01; FEC Schedule A shows contributions to a super PAC, the last on 2022-04-25'
description: 'Peter Thiel gave Protect Ohio Values PAC 10000000 dollars in March 2021, 3500000 dollars in April 2022 and 1500000 dollars later in April 2022. The PAC is an independent-expenditure committee supporting J.D. Vance, not his campaign committee.'
importance: 8
tags:
- jd-vance
- peter-thiel
- campaign-finance
- ohio-senate
- super-pac
- billionaire-politics
- protect-ohio-values
- political-investment
actors:
- J.D. Vance
- Peter Thiel
- protect-ohio-values-pac
capture_lane: political
status: confirmed
sources:
- outlet: Politico
  date: '2022-04-15'
  url: 'https://www.politico.com/news/2022/04/15/thiel-vance-ohio-senate-00025503'
  title: Thiel pours record $15 million into Vance super PAC
  tier: 1
- outlet: The New York Times
  date: '2022-05-03'
  url: 'https://www.nytimes.com/2022/05/03/us/politics/jd-vance-ohio-republican-senate.html'
  title: Vance Wins Ohio Republican Senate Primary
  tier: 1
- outlet: OpenSecrets
  date: '2022-11-08'
  url: 'https://www.opensecrets.org/news/2022/11/peter-thiel-jd-vance-ohio/'
  title: 'Peter Thiel''s investment in J.D. Vance pays off'
  tier: 1
connections:
- 2019-01-01--thiel-funds-narya-capital
- 2022-04-15--trump-endorses-vance
- 2024-07-15--vance-vp-nomination
patterns:
- oligarch-politics
- democracy-capture
- billionaire-kingmaking
notes: 'Corrected 2026-11-19. The earlier entry was dated 2022-04-01, which matches none of the three contributions, and said the money went to Vance''s campaign. The three lines are coded line 17, receipt type 10 (contribution to a non-contribution account). Their sum is 15 million dollars (our arithmetic). The earlier share figure had no stated base and is replaced by the committee-total comparison in the body.'
capture_lanes:
- Legislative Capture
event_date_claim: c6
claims:
- id: c1
  type: figure
  value: '10000000'
  qualifier: contribution_receipt_amount
  span: '"contribution_receipt_amount":10000000.0,"contribution_receipt_date":"2021-03-12"'
  url: https://api.open.fec.gov/v1/schedules/schedule_a/?api_key=DEMO_KEY&committee_id=C00770495&contributor_name=Thiel&per_page=10
  read: fetched
  source_kind: primary
- id: c2
  type: figure
  value: '3500000'
  qualifier: contribution_receipt_amount
  span: '"contribution_receipt_amount":3500000.0,"contribution_receipt_date":"2022-04-18"'
  url: https://api.open.fec.gov/v1/schedules/schedule_a/?api_key=DEMO_KEY&committee_id=C00770495&contributor_name=Thiel&per_page=10
  read: fetched
  source_kind: primary
- id: c3
  type: figure
  value: '1500000'
  qualifier: contribution_receipt_amount
  span: '"contribution_receipt_amount":1500000.0,"contribution_receipt_date":"2022-04-25"'
  url: https://api.open.fec.gov/v1/schedules/schedule_a/?api_key=DEMO_KEY&committee_id=C00770495&contributor_name=Thiel&per_page=10
  read: fetched
  source_kind: primary
- id: c4
  type: date
  value: '2021-03-12'
  qualifier: contribution_receipt_date
  span: '"contribution_receipt_amount":10000000.0,"contribution_receipt_date":"2021-03-12"'
  url: https://api.open.fec.gov/v1/schedules/schedule_a/?api_key=DEMO_KEY&committee_id=C00770495&contributor_name=Thiel&per_page=10
  read: fetched
  source_kind: primary
- id: c5
  type: date
  value: '2022-04-18'
  qualifier: contribution_receipt_date
  span: '"contribution_receipt_amount":3500000.0,"contribution_receipt_date":"2022-04-18"'
  url: https://api.open.fec.gov/v1/schedules/schedule_a/?api_key=DEMO_KEY&committee_id=C00770495&contributor_name=Thiel&per_page=10
  read: fetched
  source_kind: primary
- id: c6
  type: date
  value: '2022-04-25'
  qualifier: contribution_receipt_date
  span: '"contribution_receipt_amount":1500000.0,"contribution_receipt_date":"2022-04-25"'
  url: https://api.open.fec.gov/v1/schedules/schedule_a/?api_key=DEMO_KEY&committee_id=C00770495&contributor_name=Thiel&per_page=10
  read: fetched
  source_kind: primary
- id: c7
  type: figure
  value: '19797824.15'
  qualifier: receipts
  span: '"political_party_committee_contributions":0.0,"receipts":19797824.15,"refunded_individual_contributions":4800.0,"refunded_other_political_committee_contributions":0.0'
  url: https://api.open.fec.gov/v1/committee/C00770495/totals/?api_key=DEMO_KEY&per_page=20
  read: fetched
  source_kind: primary
---
Peter Thiel gave Protect Ohio Values PAC 10000000 dollars in March 2021. He gave the PAC 3500000 dollars in April 2022 and 1500000 dollars later that month. The PAC is an independent-expenditure committee supporting J.D. Vance's bid for the Republican Senate nomination in Ohio, not his campaign committee.

The PAC took in 19797824.15 dollars in the 2021-2022 cycle. Thiel's gifts are most of that total (our arithmetic).

Vance won the May 2022 Republican primary. Vance had worked at Thiel Capital before entering politics.
