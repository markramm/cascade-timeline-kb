---
type: timeline_event
id: 2026-01-05--nnsa-awards-aws-10m-genesis-demonstrator-purchase-order-without-competition
date: '2026-01-05'
title: "NNSA Awards Amazon Web Services a $10,000,000 Purchase Order Named AWS Genesis Demonstrator, Not Competed"
importance: 6
actors:
- Department of Energy
- Amazon Web Services
tags:
- genesis-mission
- department-of-energy
- nnsa
- ai-industry
- procurement
- usaspending
sources:
- title: 'USAspending award record 89233126PNA000208'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  outlet: USAspending.gov
  date: '2026-01-05'
  tier: 1
- title: 'NNSA taps AWS for $10M Genesis Mission pilot'
  url: https://fedscoop.com/nnsa-aws-ai-contract-genesis-mission-pilot/
  outlet: FedScoop
  date: '2026-01-13'
  tier: 2
status: reported
event_date_claim: c1
claims:
- id: c1
  type: date
  value: '2026-01-05'
  qualifier: date signed
  span: '"subaward_count":0,"total_subaward_amount":null,"date_signed":"2026-01-05","base_exercised_options":10426927.4'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
- id: c2
  type: figure
  value: $10,000,000
  qualifier: total_obligation
  span: '"description":"AWS GENESIS DEMONSTRATOR","total_obligation":10000000.0'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
- id: c3
  type: quote
  value: NOT COMPETED
  qualifier: extent_competed
  span: '"solicitation_procedures_description":"ONLY ONE SOURCE","extent_competed_description":"NOT COMPETED","other_than_full_and_open":"BND"'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
- id: c4
  type: quote
  value: BRAND NAME DESCRIPTION (FAR 6.302-1(C))
  qualifier: other_than_full_and_open
  span: '"other_than_full_and_open":"BND","other_than_full_and_open_description":"BRAND NAME DESCRIPTION (FAR 6.302-1(C))"'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
- id: c5
  type: figure
  value: '30694999.77'
  qualifier: base_and_all_options
  span: '"base_exercised_options":10426927.4,"base_and_all_options":30694999.77,"total_account_outlay":7666.73'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
- id: c6
  type: quote
  value: The Genesis Demonstrator is an initial pilot phase with AWS designed to rapidly validate core AI concepts
  qualifier: initial
  span: The Genesis Demonstrator is an initial pilot phase with AWS designed to rapidly validate core AI concepts
  url: https://fedscoop.com/nnsa-aws-ai-contract-genesis-mission-pilot/
  read: fetched
  source_kind: secondary
- id: c7
  type: quote
  value: AWS GENESIS DEMONSTRATOR
  qualifier: description
  span: '"description":"AWS GENESIS DEMONSTRATOR","total_obligation":10000000.0'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_89233126PNA000208_8900_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
---

The National Nuclear Security Administration signed a purchase order with Amazon Web Services in early January. Its award description reads "AWS GENESIS DEMONSTRATOR". Its total obligation is $10,000,000.

The record codes the award "NOT COMPETED". The record gives the exception as a brand-name description. Its ceiling with all options is 30694999.77 dollars.

An NNSA spokesperson described it to FedScoop this way: "The Genesis Demonstrator is an initial pilot phase with AWS designed to rapidly validate core AI concepts".

AWS is also on the Energy Department's Genesis Mission memorandum-of-understanding list; see [[2025-12-18--doe-signs-genesis-mission-mous-with-24-organizations-no-service-contracts-no-dollar-terms-disclosed]] and [[genesis-mission-partners]]. The parent-contract field is empty. Details, the justification search and the McKinsey order are in [[genesis-mission-aws-and-mckinsey-orders]].
