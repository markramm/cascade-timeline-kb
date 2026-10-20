---
type: timeline_event
id: 2026-09-25--ice-awards-radeco-1-3m-sole-source-order-four-cerberus-spot-robots
title: "ICE Signs a $1,304,296 Not-Competed Purchase Order With RADeCO for Customized Spot Quadruped Robots; The Vendor Is a Boston Dynamics Distributor, Not Boston Dynamics"
date: '2026-09-25'
lane: ice-procurement
importance: 7
status: confirmed
tier: 1
pattern: sole-source-tactical-procurement
named_actors:
  - U.S. Immigration and Customs Enforcement
  - RADeCO, Inc.
  - Boston Dynamics
  - GovTRobotics
location: Plainfield, Connecticut
tags:
  - ice-procurement
  - robotics
  - surveillance-tech
  - sole-source
  - quadruped
sources:
  - url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_70CMSW26P00000067_7012_-NONE-_-NONE-/
    title: "USAspending award record for the RADeCO purchase order (fetched 2026-10-19)"
  - url: https://sam.gov/api/prod/opps/v2/opportunities/d302c9fa6d234522ad2e0a63c8638177
    title: "SAM.gov Justification notice for the CERBERUS SPOT AV robot (fetched 2026-10-19)"
  - url: https://www.bostonglobe.com/2026/09/29/business/ice-robot-dog-boston-dynamics-contract/
    title: "Boston Globe report on the ICE robot purchase (fetched 2026-10-19)"
verification: source-verified
claims:
- id: c1
  type: figure
  value: $1,304,296
  qualifier: total obligation
  span: '"total_obligation":1304296.0,"subaward_count":0,"total_subaward_amount":null,"date_signed":"2026-09-25","base_exercised_options":1304296.0,"base_and_all_options":1304296.0'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_70CMSW26P00000067_7012_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-19'
- id: c2
  type: date
  value: '2026-09-25'
  qualifier: date signed
  span: '"total_obligation":1304296.0,"subaward_count":0,"total_subaward_amount":null,"date_signed":"2026-09-25","base_exercised_options":1304296.0,"base_and_all_options":1304296.0'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_70CMSW26P00000067_7012_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-19'
- id: c3
  type: date
  value: '2026-11-24'
  qualifier: end date
  span: '"period_of_performance":{"start_date":"2026-09-25","end_date":"2026-11-24","last_modified_date":"2026-09-25"'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_70CMSW26P00000067_7012_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-19'
- id: c4
  type: posture
  value: NOT COMPETED
  qualifier: ONLY ONE SOURCE
  span: '"solicitation_procedures_description":"ONLY ONE SOURCE","extent_competed_description":"NOT COMPETED","other_than_full_and_open":"ONE"'
  url: https://api.usaspending.gov/api/v2/awards/CONT_AWD_70CMSW26P00000067_7012_-NONE-_-NONE-/
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-19'
- id: c5
  type: date
  value: '2026-09-28'
  qualifier: postedDate
  span: '"postedDate":"2026-09-28T15:09:13.363+00:00","modifiedDate":"2026-10-14T05:08:52.660+00:00"'
  url: https://sam.gov/api/prod/opps/v2/opportunities/d302c9fa6d234522ad2e0a63c8638177
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-19'
- id: c6
  type: figure
  value: four
  qualifier: about $1.3 million
  span: US Immigration and Customs Enforcement will spend about $1.3 million on four of the robots in a deal with Connecticut company
  url: https://www.bostonglobe.com/2026/09/29/business/ice-robot-dog-boston-dynamics-contract/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-19'
- id: c7
  type: attribution
  value: authorized distributer and industry partner of Boston Dynamics
  qualifier: According to Radeco's website
  span: According to Radeco’s website, the company is a supplier to all branches of the US military, NATO, and armies in Israel, Spain, Italy, Germany, and Brazil. It describes itself as an authorized distributer and industry partner of Boston Dynamics.
  url: https://www.bostonglobe.com/2026/09/29/business/ice-robot-dog-boston-dynamics-contract/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-19'
- id: c8
  type: quote
  value: additional tool to safely assess potentially dangerous situations before placing personnel or the public at risk
  qualifier: an ICE spokesperson said
  span: The robots will be used as an “additional tool to safely assess potentially dangerous situations before placing personnel or the public at risk,” an ICE spokesperson said.
  url: https://www.bostonglobe.com/2026/09/29/business/ice-robot-dog-boston-dynamics-contract/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-19'
- id: c9
  type: quote
  value: any suggestion that these robots will be used to support immigrant detentions or deportations is false
  qualifier: a spokesperson for Boston Dynamics
  span: a spokesperson for Boston Dynamics, said “any suggestion that these robots will be used to support immigrant detentions or deportations is false,” and that the language in the contract is “boilerplate.”
  url: https://www.bostonglobe.com/2026/09/29/business/ice-robot-dog-boston-dynamics-contract/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-19'
- id: c10
  type: quote
  value: plans to spend as much as $2 million to purchase robot 'dogs'
  qualifier: according to a government funding document reviewed by NBC News
  span: Immigration and Customs and Enforcement plans to spend as much as $2 million to purchase robot 'dogs' that the agency would use in immigration enforcement operations, according to a government funding document reviewed by NBC News.
  url: https://www.nbcnews.com/politics/immigration/ice-buy-robot-dogs-immigration-enforcement-rcna594897
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-19'
event_date_claim: c2
---

- Date signed (this entry's date, per USAspending): ICE signed a purchase order with RADeCO, Inc. of Plainfield, Connecticut. The USAspending record shows a total obligation and base-and-all-options value of $1,304,296, so this is an obligated figure, not a ceiling. The period of performance is about two months.
- Competition coding: solicitation procedures ONLY ONE SOURCE, extent competed NOT COMPETED.
- SAM.gov posted date, a few days after signing: the Justification for Other Than Full and Open Competition was posted, after signing.
- Press: the Boston Globe then reported the purchase of four robots.

## The vendor, and corrections to the ticket's premises

- The awardee is RADeCO, Inc., not Boston Dynamics. Boston Dynamics holds no ICE or DHS award in USAspending. RADeCO sells a customized package called CERBERUS built on the Boston Dynamics Spot robot. The Globe reports that RADeCO describes itself as an authorized distributer and industry partner of Boston Dynamics; that is RADeCO's own description and was not confirmed with Boston Dynamics.
- NBC's August report said ICE "plans to spend as much as $2 million to purchase robot 'dogs'" according to a government funding document it reviewed; that is a planning figure. The signed amount is $1,304,296.
- See the correction note on [[2026-08-27--ice-solicits-boston-dynamics-spot-robots-fort-benning]].

## What the robots are for

The ICE spokesperson described the robots as an "additional tool to safely assess potentially dangerous situations before placing personnel or the public at risk." A Boston Dynamics spokesperson told the Globe that "any suggestion that these robots will be used to support immigrant detentions or deportations is false." The justification document itself lists enforcement operations, custodial transportation of detainees, civil disturbances around detention facilities and immigration enforcement among the missions; see the research note on the procurement for the passage and the line items.

## Not established

- Where the robots will be stationed; the public justification does not say.
- Whether follow-on orders exist; USAspending shows one transaction.
