---
type: timeline_event
id: 2026-10-14--cloudflare-yandex-outage-analysis-bots-migrated-not-stopped
title: "Cloudflare Publishes Yandex-Outage Analysis: Search-Crawler Traffic Fell, Yandex.Cloud Automation Moved to Other Russian Hosts, No Social-Media Shift Seen in Its Data"
date: '2026-10-14'
lane: data-colonialism
importance: 4
status: reported
tier: 1
verification: source-verified
pattern: infrastructure-targeting
named_actors:
  - Cloudflare
  - Yandex
tags:
  - russia
  - yandex
  - cloudflare
  - bots
  - data-centres
sources:
  - url: https://blog.cloudflare.com/yandex-outage/
    title: "Cloudflare blog, 'Yandex outage: data shows that instead of going dark, malicious bots went on the move' (page metadata published 2026-10-14T20:24Z)"
claims:
  - {id: c1, type: figure, value: "99.5%", qualifier: "share of requests classified automated, Yandex SEARCH ASN AS13238 only", span: "Cloudflare classified 99.5% of its requests as automated, and 93.6% of its bot requests as", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
  - {id: c2, type: figure, value: "95.0%", qualifier: "share of scored requests that were bots, Yandex.Cloud AS200350; none verified", span: "Approximately 95.0% of its scored requests were bots, but none of its observed bot requests were verified by Cloudflare.", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
  - {id: c3, type: figure, value: "99% / 90% below baseline", qualifier: "Oct 11 traffic, AS13238 / AS200350", span: "traffic plummeted to 99% below baseline for Yandex Search (AS13238) and 90% for Yandex.Cloud (AS200350)", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
  - {id: c4, type: figure, value: "167.7 million to 170.1 million (+1.4%)", qualifier: "Russian bot requests to gambling accounts over the week", span: "Russian bot traffic targeting gambling accounts remained essentially flat over the week, moving from 167.7 million to 170.1 million requests (+1.4%).", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
  - {id: c5, type: event, value: "identical requests appeared from Radist and Selectel", qualifier: "after the Oct 8 disruption; same JA4 fingerprint, paths/headers, User-Agent strings", span: "identical requests began appearing from other Russian hosting ASNs, including Radist and Selectel.", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
  - {id: c6, type: figure, value: "0.6% decrease Russia-origin; 1.2% increase global", qualifier: "total social-media traffic over the event period, Cloudflare's network only", span: "no unexpected changes in traffic either from Russian-origin IPs (0.6% decrease in total traffic over the event period) or globally (1.2% increase in total traffic over the event period)", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
  - {id: c7, type: quote, value: "cannot conclusively say there is no connection", qualifier: "Cloudflare's own limit on its social-media finding", span: "without further analysis with data outside of Cloudflare, we cannot conclusively say there is no connection.", url: "https://blog.cloudflare.com/yandex-outage/", read: fetched, source_kind: primary}
---

Date kind: publication date of Cloudflare's post (page metadata, 2026-10-14 20:24 UTC), not the strike dates (see [[2026-10-08--yandex-three-data-centres-knocked-out-by-drones-oct-8-11-reuters]]).

What the text says, bound to Cloudflare's wording. Two Yandex ASNs, two different pictures. The 99.5% automated figure belongs to the search-engine ASN (AS13238), where the drop was almost entirely verified search crawlers; the cloud ASN (AS200350) was about 95% bots, unverified, and supplied about 2% of Russia-origin bot requests and 0.01% of the global total. Cloudflare's gambling-customer case shows one workload moving from Yandex.Cloud to other Russian hosts the day of the Oct 8 disruption, with an unchanged fingerprint. Its social-media endpoints check found no unexpected shift, with the stated limit in c7.

Limits: this is Cloudflare's own analysis of its own network; the post lists no author. The post's text gives a pre-event baseline of 36.1% automated (global) and 35.8% (Russia), which differs from figures in its own table; the discrepancy is unexplained in the post. Cloudflare does not attribute the migrated traffic to any actor ("it does not necessarily tell us who is responsible").
