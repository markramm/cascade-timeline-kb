---
type: timeline_event
id: 2026-10-21--brennan-just-security-dhs-ai-inventory-elite-not-high-impact-hsi-osint-sentiment-analysis-vs-ice-policy
date: '2026-10-21'
title: "Brennan Center Authors Say DHS's AI Inventory Leaves ELITE Off Its High-Impact List and Shows HSI Using Sentiment Analysis an ICE Policy Bars"
importance: 6
status: confirmed
date_is_publication_date: true
verification: source-verified
event_date_claim: c1
claims:
- id: c1
  type: date
  value: October 21, 2026
  qualifier: Published on
  span: By Rachel Levinson-Waldman and Eoghan Stafford Published on October 21, 2026
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c2
  type: attribution
  value: does not classify the ELITE app as high-impact
  qualifier: ICE agents use it
  span: the inventory does not classify the ELITE app as high-impact, although ICE agents use it to find and arrest migrants who may be in the country illegally. The app uses large language models to extract addresses where migrants may live from government records, including data from the Department of Health and Human Services, and displays them on maps, along with "confidence scores" indicating the likelihood that the addresses are accurate, facilitating widescale raids.
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c3
  type: attribution
  value: Investigative Prioritization Aggregator
  qualifier: DHS also excludes
  span: DHS also excludes the Investigative Prioritization Aggregator software, which ranks suspects in criminal investigations by Homeland Security Investigations (HSI), a component of ICE, according to their likely importance to an investigation.
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c4
  type: quote
  value: Open-Source Intelligence for Investigations
  qualifier: An entry titled
  span: An entry titled "Open-Source Intelligence for Investigations" reveals that HSI uses software systems that search online content for undefined "risks" and suggest "investigative leads." These systems utilize sentiment analysis
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c5
  type: attribution
  value: prohibited from applying sentiment analysis technologies
  qualifier: official ICE policy
  span: The entry itself cites an official ICE policy that states the agency is prohibited from applying sentiment analysis technologies to online content during law enforcement investigations.
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c6
  type: quote
  value: Yes, sufficient monitoring protocols have been established
  qualifier: DHS simply selected
  span: 'In answer to a question about whether they monitor the use of Mobile Fortify for harms to privacy, civil rights, or civil liberties, DHS simply selected a response that says: "Yes, sufficient monitoring protocols have been established."'
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c7
  type: attribution
  value: waive any departmental policy governing AI
  qualifier: chief AI officer
  span: DHS issued a directive on the use and acquisition of artificial intelligence that permits the chief AI officer to waive any departmental policy governing AI, including any prohibitions on uses
  url: https://www.justsecurity.org/?p=159720
  read: fetched
  source_kind: reporting
  outcome: verified
  checked: '2026-10-22'
- id: c8
  type: attribution
  value: criminal records such as rap sheets and warrants
  qualifier: extract address information
  span: ELITE uses SI, specifically natural language processing (NLP) through large language models (LLMs), to identify and extract address information from criminal records such as rap sheets and warrants.
  url: https://www.dhs.gov/si/use-case-inventory/ice
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-22'
- id: c9
  type: attribution
  value: principal basis for decisions or actions with legal, material, binding, or significant effects on individuals
  qualifier: limited to normalized address data
  span: While ELITE provides actionable data to ERO officers, its outputs are limited to normalized address data and do not serve as a principal basis for decisions or actions with legal, material, binding, or significant effects on individuals.
  url: https://www.dhs.gov/si/use-case-inventory/ice
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-22'
- id: c10
  type: attribution
  value: sentiment and emotion detection
  qualifier: Additional SI capabilities include
  span: Additional SI capabilities include named entity recognition, sentiment and emotion detection, thematic clustering, image and object classification, and translation of multilingual content.
  url: https://www.dhs.gov/si/use-case-inventory/ice
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-22'
tags:
  - ai-governance
  - domestic-surveillance
  - immigration-enforcement
  - algorithmic-accountability
actors:
  - Department of Homeland Security
  - U.S. Immigration and Customs Enforcement
  - Homeland Security Investigations
  - Brennan Center for Justice
  - Rachel Levinson-Waldman
sources:
  - title: "DHS Use Case Inventory: ICE"
    url: https://www.dhs.gov/si/use-case-inventory/ice
    publisher: U.S. Department of Homeland Security
    date: '2026-10-22'
    tier: 1
  - title: "DHS's AI Inventory Reveals the Limits of Federal AI Transparency Law"
    url: https://www.justsecurity.org/?p=159720
    publisher: Just Security (Brennan Center authors)
    date: '2026-10-21'
    tier: 3
---

On October 21, Just Security published an analysis by Brennan Center authors Rachel Levinson-Waldman and Eoghan Stafford of DHS's AI use-case inventory. They say the inventory does not classify the ELITE app as high-impact even though ICE agents use it to find and arrest migrants, and they describe it as using large language models to extract addresses from government records, including Department of Health and Human Services data, and to display them on maps with confidence scores. DHS's own ICE entry for ELITE says the app extracts address information from criminal records such as rap sheets and warrants, and says its outputs are limited to normalized address data that do not serve as a principal basis for decisions or actions with legal, material, binding, or significant effects on individuals. The authors also say DHS excludes the Investigative Prioritization Aggregator, which ranks HSI suspects, and that an entry titled "Open-Source Intelligence for Investigations" shows HSI software using sentiment analysis, which the authors say an official ICE policy cited in the entry prohibits in law enforcement investigations. DHS's page for that entry lists sentiment and emotion detection among the platforms' capabilities. For Mobile Fortify, the authors say DHS answered the monitoring question with "Yes, sufficient monitoring protocols have been established." They add that DHS's AI directive permits the chief AI officer to waive any departmental policy governing AI, including any prohibitions on uses.

The Medicaid data transfer to the ELITE app is documented separately in [[2026-07-17--ice-medicaid-palantir-illegal-data-transfer]]. It extends the inventory coverage in [[2026-08-06--lawfare-documents-most-ice-ai-tools-absent-from-dhs-public-inventory]], [[2026-08-14--dhs-ai-inventory-200-use-cases-palantir-elite-confidence-scores-911-ingestion]] and [[2026-08-12--brennan-center-dhs-29b-domestic-surveillance-architecture]].
