---
type: timeline_event
id: 2026-11-17--nsa-classified-network-outage-dni-clayton-links-it-to-php2shell-patching
date: '2026-11-17'
title: NSA's Classified Internal Network Goes Offline; DNI Clayton Links the Outage to Patching After the PHP Flaws, While NSA Calls It Routine Maintenance
importance: 6
status: reported
event_date_claim: c0
source_published_date: '2026-11-18'
verification: source-verified
captured_by: capture-watch
cluster: ai-industry-policy
claims:
- id: c0
  type: date
  value: Tuesday
  span: The NSA's internal network, which is used to store and share classified information, went offline Tuesday, prompting the agency to stagger arrival times for some personnel at its headquarters at Fort Meade, Maryland.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c1
  type: quote
  value: used to store and share classified information
  span: The NSA's internal network, which is used to store and share classified information, went offline Tuesday, prompting the agency to stagger arrival times for some personnel at its headquarters at Fort Meade, Maryland.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c2
  type: attribution
  value: directly linked the NSA's classified network outage to urgent software updates
  span: Speaking on Fox Business Tuesday, Director of National Intelligence Jay Clayton directly linked the NSA's classified network outage to urgent software updates following the discovery of critical vulnerabilities in PHP.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c3
  type: quote
  value: caused some of these systems to not come back up when you patch them as expected
  span: And the patching that has gone on following that has caused some of these systems to not come back up when you patch them as expected.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c4
  type: quote
  value: That is what has happened at the NSA today.
  span: That is what has happened at the NSA today.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c5
  type: quote
  value: temporary degradation during scheduled routine maintenance
  span: The NSA said Tuesday the agency had experienced a "temporary degradation during scheduled routine maintenance," adding that its mission/critical capabilities were still fully operational.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c6
  type: attribution
  value: multiple sources told CBS News
  span: The National Security Agency's network outage Tuesday has been linked to an urgent patching of vulnerabilities in PHP, the programming language that powers the majority of all websites, multiple sources told CBS News.
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
- id: c7
  type: quote
  value: Code Gray
  span: There is no word yet on how long the agency will continue the staggered arrival schedule, known as "Code Gray."
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-19'
tags:
- cybersecurity
- php2shell
- nsa
- outages
- infrastructure
actors:
- National Security Agency
- Jay Clayton
sources:
- title: National Security Agency network outage linked to software vulnerability
  publisher: CBS News
  date: '2026-11-18'
  url: https://www.cbsnews.com/colorado/news/national-security-agency-network-outage-software-vulnerability/
  tier: 2
lane: Infrastructure Fragility
---

On Tuesday, the NSA's internal network, which CBS News describes as "used to store and share classified information," went offline, and the agency staggered arrival times at Fort Meade, a schedule known as "Code Gray." The NSA said it had experienced a "temporary degradation during scheduled routine maintenance."

Director of National Intelligence Jay Clayton, speaking on Fox Business the same day, directly linked the NSA's classified network outage to urgent software updates. He said the patching that followed "caused some of these systems to not come back up when you patch them as expected." "That is what has happened at the NSA today." Multiple sources told CBS News the same. The PHP flaws and the patch order are at [[2026-10-21--cisa-alert-urges-immediate-patching-of-php2shell-php-flaws]] and [[2026-10-26--cisa-adds-php2shell-cves-to-kev-binding-federal-civilian-agencies-only-due-oct-29]].
