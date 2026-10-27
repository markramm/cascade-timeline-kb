---
type: timeline_event
id: 2026-10-21--vr-systems-pulls-florida-county-election-lookup-tools-over-php-flaws
date: '2026-10-21'
title: Election Vendor VR Systems Takes Florida County Elections Sites' Voter Lookup Tools Offline Over the PHP Flaws During Early Voting
importance: 6
status: confirmed
event_date_claim: c0
verification: source-verified
claims:
- id: c0
  type: date
  value: Wednesday, Oct. 21
  span: 'Update: Web services were restored around 7 p.m. on Wednesday, Oct. 21, allowing voters to check their status online after an outage that began at 10 a.m.'
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c1
  type: quote
  value: around 7 p.m.
  span: 'Update: Web services were restored around 7 p.m. on Wednesday, Oct. 21, allowing voters to check their status online after an outage that began at 10 a.m.'
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c2
  type: quote
  value: an outage that began at 10 a.m.
  span: 'Update: Web services were restored around 7 p.m. on Wednesday, Oct. 21, allowing voters to check their status online after an outage that began at 10 a.m.'
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c3
  type: quote
  value: pulled some public-facing parts of its websites after the PHP Foundation
  span: VR Systems, the Tallahassee-based elections technology firm that Florida uses, pulled some public-facing parts of its websites after the PHP Foundation, which oversees the open-source programming language, identified critical vulnerabilities that could impact digital infrastructure across the world.
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c4
  type: quote
  value: took down the service at 10 a.m. Wednesday in response to warnings by the PHP programmers
  span: Ben Martin, the chief operations officer of VR Systems, told Suncoast Searchlight the company took down the service at 10 a.m. Wednesday in response to warnings by the PHP programmers.
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c5
  type: quote
  value: this does not affect the ability to vote, only the ability to look up information
  span: “It’s critical to understand that this does not affect the ability to vote, only the ability to look up information,” Martin said.
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c6
  type: quote
  value: This does not affect the voter rolls.
  span: “This does not affect the voter rolls.”
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c7
  type: quote
  value: voters cannot look at sample ballots or find voting locations
  span: On Sarasota County’s Supervisor of Elections website, for example, voters cannot look at sample ballots or find voting locations.
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c8
  type: quote
  value: I do not currently have a resolution time from the vendor.
  span: But I do not currently have a resolution time from the vendor.
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
- id: c9
  type: quote
  value: appears to still be active
  span: The voter registration tool operated by the Florida Department of State appears to still be active.
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-27'
tags:
- election-security
- cybersecurity
- php2shell
- election-vendors
- florida
- midterms
actors:
- VR Systems
- Sarasota County Supervisor of Elections
- PHP Foundation
sources:
- title: Voter lookup tools go down across Florida as early voting begins
  publisher: Suncoast Searchlight (republished by WGCU)
  date: '2026-10-21'
  url: https://suncoastsearchlight.org/florida-voter-lookup-tools-down-php-website/
  tier: 2
lane: Electoral Manipulation
---

On Wednesday, Oct. 21, during early voting, VR Systems took down public lookup tools on the county Supervisor of Elections websites it hosts across Florida. Suncoast Searchlight reported that the Tallahassee elections technology firm "pulled some public-facing parts of its websites after the PHP Foundation" disclosed critical PHP flaws ([[2026-10-21--cisa-alert-urges-immediate-patching-of-php2shell-php-flaws]]). VR Systems' chief operations officer, Ben Martin, said the company "took down the service at 10 a.m. Wednesday in response to warnings by the PHP programmers." In the report he points to the PHP programmers, not to CISA or the MS-ISAC. He said "this does not affect the ability to vote, only the ability to look up information," and "This does not affect the voter rolls."

On Sarasota County's elections site, "voters cannot look at sample ballots or find voting locations." The county office's spokesperson wrote: "I do not currently have a resolution time from the vendor." The Florida Department of State's own voter registration tool "appears to still be active." Suncoast Searchlight's update says service came back "around 7 p.m." after "an outage that began at 10 a.m." The report describes the vendor taking its own tools down and reports no compromise.
