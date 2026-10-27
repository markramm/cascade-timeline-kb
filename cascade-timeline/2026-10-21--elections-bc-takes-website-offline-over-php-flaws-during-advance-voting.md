---
type: timeline_event
id: 2026-10-21--elections-bc-takes-website-offline-over-php-flaws-during-advance-voting
date: '2026-10-21'
title: Elections B.C. Takes Its Website Offline Over the PHP Flaws During Advance Voting and Restores It the Same Day
importance: 4
status: confirmed
event_date_claim: c0
claims:
- id: c0
  type: date
  value: 'Oct 21, 2026'
  qualifier: Posted
  span: 'Posted: Oct 21, 2026 6:22 PM EDT'
  url: https://www.cbc.ca/news/canada/british-columbia/elections-bc-php-website-down-9.7390794
  read: fetched
  source_kind: secondary
- id: c1
  type: quote
  value: temporarily shut down to allow for system maintenance after a "global security vulnerability" was identified
  span: In a statement, an Elections B.C. spokesperson said the website was temporarily shut down to allow for system maintenance after a "global security vulnerability" was identified. It was restored as of 3:20 p.m. PT.
  url: https://www.cbc.ca/news/canada/british-columbia/elections-bc-php-website-down-9.7390794
  read: fetched
  source_kind: secondary
- id: c2
  type: quote
  value: restored as of 3:20 p.m. PT
  span: In a statement, an Elections B.C. spokesperson said the website was temporarily shut down to allow for system maintenance after a "global security vulnerability" was identified. It was restored as of 3:20 p.m. PT.
  url: https://www.cbc.ca/news/canada/british-columbia/elections-bc-php-website-down-9.7390794
  read: fetched
  source_kind: secondary
- id: c3
  type: quote
  value: the website outage was a precautionary measure and none of the organization's information systems were breached
  span: PHP is widely used across the web, and Elections B.C. said the website outage was a precautionary measure and none of the organization's information systems were breached.
  url: https://www.cbc.ca/news/canada/british-columbia/elections-bc-php-website-down-9.7390794
  read: fetched
  source_kind: secondary
- id: c4
  type: quote
  value: voters can still use the where to vote application to find their polling station
  span: The spokesperson said that voters can still use the where to vote application to find their polling station, with advance voting underway for the upcoming provincial election, and they can call the organization for assistance.
  url: https://www.cbc.ca/news/canada/british-columbia/elections-bc-php-website-down-9.7390794
  read: fetched
  source_kind: secondary
tags:
- election-security
- cybersecurity
- php2shell
- canada
- british-columbia
lane: Electoral Manipulation
actors:
- Elections B.C.
- PHP Foundation
sources:
- title: Elections B.C. website taken down amid global outages blamed on PHP programming language
  publisher: CBC News
  date: '2026-10-21'
  url: https://www.cbc.ca/news/canada/british-columbia/elections-bc-php-website-down-9.7390794
  tier: 2
---

Elections B.C., the provincial election authority in British Columbia, Canada, took its website offline on Wednesday, Oct. 21, the day PHP released its fixes ([[2026-10-21--cisa-alert-urges-immediate-patching-of-php2shell-php-flaws]]). CBC News (posted Oct 21, 6:22 p.m. EDT) quotes a spokesperson saying the site was "temporarily shut down to allow for system maintenance after a 'global security vulnerability' was identified," and that it was "restored as of 3:20 p.m. PT." A later statement confirmed the vulnerability was the PHP one. Elections B.C. said "the website outage was a precautionary measure and none of the organization's information systems were breached."

Advance voting for the provincial election was underway. The spokesperson said "voters can still use the where to vote application to find their polling station."

Elections B.C. is a Canadian election authority, outside the US scope of the election-office check. Compare the Florida vendor outage the same day: [[2026-10-21--vr-systems-pulls-florida-county-election-lookup-tools-over-php-flaws]].
