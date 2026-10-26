---
type: timeline_event
id: 2026-08-14--x-open-sources-for-you-feed-code-changelog-shows-brazil-election-filter-and-july-mutual-follow-boost-no-us-election-rule
date: '2026-08-14'
title: 'X''s open-sourced For You code lists two 2026 ranking changes: a July mutual-follow boost and an August Brazil election filter; no US-election rule appears'
importance: 5
status: confirmed
verification: source-verified
event_date_claim: c2
date_is_publication_date: false
claims:
- id: c1
  type: date
  value: '2026-01-19'
  qualifier: xai-org/x-algorithm repository created (GitHub API created_at 2026-01-19T23:12:35Z); description "Algorithm powering the For You feed on X"
  span: '"created_at": "2026-01-19T23:12:35Z" ... "description": "Algorithm powering the For You feed on X"'
  url: https://api.github.com/repos/xai-org/x-algorithm
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-26'
- id: c2
  type: quote
  value: For You now runs `Brazil2026ElectionFilter`
  qualifier: README "August 14th, 2026"; removes posts from accounts reported to Brazil's Electoral Court unless the viewer follows the account
  span: in accordance with Brazilian electoral law, For You now runs `Brazil2026ElectionFilter`, which removes posts from accounts reported to Brazil's Electoral Court for the 2026 election, unless the viewer explicitly follows the account.
  url: https://raw.githubusercontent.com/xai-org/x-algorithm/main/README.md
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-26'
- id: c3
  type: date
  value: '2026-07-13'
  qualifier: bidirectional follow reply boost rolled out at value 20 after a July 10 A/B test; cut to 15 on July 24
  span: On July 13, 2026, after seeing great initial results from the A/B test, we rolled out a boost value of 20 to many users
  url: https://raw.githubusercontent.com/xai-org/x-algorithm/main/docs/BIDIRECTIONAL_BOOST_CHANGE.md
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-26'
- id: c4
  type: quote
  value: We're rolling out a small tweak to boost visibility of your posts to your mutuals
  qualifier: Nikita Bier post announcing the boost, fetched via api.fxtwitter.com
  span: We're rolling out a small tweak to boost visibility of your posts to your mutuals (people who you follow back).
  url: https://x.com/nikitabier/status/2076747704248758617
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-26'
tags:
- x
- platform-power
- ranking
- midterms-2026
- brazil
actors:
- X
- xAI
- Nikita Bier
sources:
- title: xai-org/x-algorithm README
  url: https://github.com/xai-org/x-algorithm
  publisher: xAI / X
  date: '2026-10-24'
  tier: 1
capture_lanes:
- Platform Power
related_events:
- 2026-02-02--spacex-acquires-xai-holdings-and-x-effective-per-424b4-musk-82-4-percent-vote
---

X published the code behind its For You feed in the xai-org/x-algorithm repository, created January 19, 2026, and has pushed updates almost daily through October 24. The README's "Notable Updates" list three entries: August 13 (visibility-filtering and label systems added), August 14 and September 18 (a transparency tool now shows visibility limits imposed to comply with law).

Two ranking changes are documented in X's own materials. A "bidirectional follow" boost raised the predicted-reply weight for posts from mutual follows: an A/B test began July 10, a value of 20 went to many users on July 13, and it was cut to 15 on July 24. Nikita Bier's announcement describes it as "a small tweak to boost visibility of your posts to your mutuals". On August 14 X added a `Brazil2026ElectionFilter` that removes posts from accounts reported to Brazil's Electoral Court unless the viewer follows them; the list was cut to the Oct 25 runoff candidates on October 13.

A search of the repository's file tree (2,886 paths, October 26) finds an election filter only for Brazil; there is no US midterm filter or political-content rule. That is a statement about this repository, which does not include everything (the README has a "What's not in this repo?" section); it does not show that X applied no US political treatment. Earlier ranking changes are in the 2023-2024 timeline entries. The ownership structure is at [[2026-02-02--spacex-acquires-xai-holdings-and-x-effective-per-424b4-musk-82-4-percent-vote]].
