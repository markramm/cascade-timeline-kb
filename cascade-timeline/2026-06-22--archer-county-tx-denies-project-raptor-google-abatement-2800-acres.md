---
type: timeline_event
id: 2026-06-22--archer-county-tx-denies-project-raptor-google-abatement-2800-acres
date: '2026-06-22'
title: "Archer County TX Denies Tax Abatement for 'Project Raptor' Data Center That Local Reporting Links to Google"
importance: 8
status: confirmed
tags:
  - datacenter-buildout
  - tax-abatements
  - google
  - local-resistance
  - texas
actors:
  - Archer County Commissioners Court
  - Randy Jackson
  - Dynamo Ventures LLC
  - Google (named by reporting; no on-record confirmation found)
sources:
  - title: "Archer County officials deny Google's data center tax break"
    url: https://www.texomashomepage.com/news/local-news/archer-county-officials-deny-googles-data-center-tax-break/
    publisher: Texoma's Homepage (KFDX/KJTL)
    date: '2026-06-22'
    tier: 2
  - title: "County Denies Project Raptor a Tax Abatement"
    url: https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement
    publisher: Archer County News
    date: '2026-06-22'
    tier: 2
  - title: "Archer County Commissioners deny tax abatement for proposed data center"
    url: https://www.newschannel6now.com/2026/06/22/archer-county-commissioners-deny-tax-abatement-proposed-data-center/
    publisher: NewsChannel 6 (Wichita Falls)
    date: '2026-06-22'
    tier: 3
corrections:
- date: '2026-11-18'
  was: "TITLE: Archer County TX Unanimously Denies Tax Abatement for Google's 2,800-Acre 'Project Raptor' Data Center || TEXT: The Archer County Commissioners Court voted unanimously on June 22, 2026 to deny a tax abatement request for Project Raptor, a Google data center development spanning roughly 2,800 acres along Three Way Road. The request had been submitted June 3 by Dynamo Ventures LLC, the entity fronting the project; more than 30 residents packed the Commissioners Court to oppose the incentive. County Judge Randy Jackson said commissioners wanted to see what regulations and incentives might come from the Texas Legislature before considering any reduction in local tax revenue. The denial does not stop the project \u2014 it removes the subsidy, not the permission.\n\nThe ledger captured this as an \"apparent\" Google project on a single tier-3 source; independent local reporting confirms the Google connection directly and supplies the project name and acreage. The special-purpose-entity pattern is the recurring structure worth noting: hyperscalers approach counties through shell developers like Dynamo Ventures, so the abatement request arrives without the name of the company that will actually own the load, and residents must reverse-engineer who they are subsidizing. Texas has become the densest theater for this fight \u2014 Leon County rejected a $34B Crusoe abatement (2026-07-14--leon-county-tx-rejects-crusoe-34b-tax-abatement), Guadalupe County residents sued over Cloudburst (2026-07-22--guadalupe-county-tx-residents-sue-cloudburst-tax-abatement), Bell County residents moved against Meta abatements (2026-07-07--bell-county-tx-residents-demand-end-meta-data-center-abatements), and Governor Abbott subsequently froze grid connections pending an ERCOT audit (2026-08-03--abbott-freezes-texas-data-center-grid-connections-ercot-audit). Judge Jackson's stated reason \u2014 wait for the Legislature \u2014 is the tell that county officials understand they are negotiating without the information or leverage the counterparty has."
  now: "Title and text attribute the Google identification to Archer County News (own voice) and KAUZ (unnamed sources); no record or on-record statement from Google, the county or Dynamo Ventures LLC confirming Google was found. Sentences not bound to a fetched span (30 residents, Judge Jackson's reasoning, the Texas cross-references, the shell-developer pattern) are removed here and kept in 'was'."
  why: "Fetched 2026-11-18: https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement; https://www.newschannel6now.com/2026/06/22/archer-county-commissioners-deny-tax-abatement-proposed-data-center/; https://www.archercountynews.com/news/more-information-released-1b-data-center-project (Google has not confirmed). texomashomepage.com returned 403 to the fetch tool and was not read. File id still carries 'google' and is historical."
  found_by: recheck-canon-bell-county-abatement-tabling-date-and-archer-project-raptor
claims:
- id: a1
  type: quote
  value: "Google's proposed data center project, known as Project Raptor."
  qualifier: "Google's"
  span: "The Archer County Commissioners Court voted unanimously Monday, June 22, to deny a tax abatement request related to Google's proposed data center project, known as Project Raptor."
  url: https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement
  read: fetched
  source_kind: secondary
- id: a2
  type: quote
  value: "is expected to eventually serve as infrastructure for Google, according to those familiar with the development."
  qualifier: "according to those familiar"
  span: "The project is expected to eventually serve as infrastructure for Google, according to those familiar with the development."
  url: https://www.newschannel6now.com/2026/06/22/archer-county-commissioners-deny-tax-abatement-proposed-data-center/
  read: fetched
  source_kind: secondary
- id: a3
  type: date
  value: "June 3"
  qualifier: "submitted"
  span: "The request, submitted June 3 by Dynamo Ventures, sought a tax abatement for the proposed facility, which would be located on approximately 2,800 acres along Three Way Road."
  url: https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement
  read: fetched
  source_kind: secondary
- id: a4
  type: quote
  value: "voted unanimously Monday, June 22"
  qualifier: "voted"
  span: "The Archer County Commissioners Court voted unanimously Monday, June 22, to deny a tax abatement request related to Google's proposed data center project, known as Project Raptor."
  url: https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement
  read: fetched
  source_kind: secondary
- id: a5
  type: quote
  value: "approximately 2,800 acres along Three Way Road."
  qualifier: "approximately"
  span: "The request, submitted June 3 by Dynamo Ventures, sought a tax abatement for the proposed facility, which would be located on approximately 2,800 acres along Three Way Road."
  url: https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement
  read: fetched
  source_kind: secondary
- id: a6
  type: quote
  value: "has drawn interest from Google,"
  qualifier: "drawn interest"
  span: "The project, which state officials say has drawn interest from Google, would be built on a 2,800 acre property along Three Way Road..."
  url: https://www.archercountynews.com/news/more-information-released-1b-data-center-project
  read: fetched
  source_kind: secondary
event_date_claim: a4
---

Archer County News reports that the Commissioners Court "voted unanimously Monday, June 22" to deny a tax abatement request tied to Project Raptor. The request, according to Archer County News, was submitted June 3 by Dynamo Ventures. Archer County News places the proposed facility on "approximately 2,800 acres along Three Way Road." The denial does not stop the project; it removes the subsidy, not the permission.

Who the end user is rests on reporting, not on a record. Archer County News describes the project in its own voice as "Google's proposed data center project, known as Project Raptor." KAUZ attributes the Google link to unnamed sources: the project "is expected to eventually serve as infrastructure for Google, according to those familiar with the development." Archer County News earlier reported that state officials say the project "has drawn interest from Google," and that Google has not confirmed it. The fetched coverage carries no statement from Google, from the county or from Dynamo Ventures LLC naming Google as the end user. The Texoma's Homepage article, whose headline calls it Google's data center tax break, was refused by the fetch tool and is unread.
