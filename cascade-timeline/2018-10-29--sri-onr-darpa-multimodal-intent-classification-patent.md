---
type: timeline_event
id: 2018-10-29--sri-onr-darpa-multimodal-intent-classification-patent
date: '2018-10-29'
title: "ONR and DARPA Fund SRI International Research Classifying the Intent of Social Media Posts; Patent Names Law-Enforcement Extremist Tracking as an Application"
importance: 7
status: confirmed
tags:
  - social-media-surveillance
  - intent-classification
  - protest-criminalization
  - darpa
  - office-of-naval-research
  - sri-international
  - capability-provenance
  - dual-use-research
  - domestic-terrorism-framework
actors:
  - SRI International
  - Ajay Divakaran
  - Karan Sikka
  - Julia Kruk
  - Xiao Lin
  - Jonah M. Lubin
  - Dan Jurafsky
  - Office of Naval Research
  - Defense Advanced Research Projects Agency
  - Army Research Office
sources:
  - title: "US 2020/0134398 A1 — Determining intent from multimodal content embedded in a common geometric space"
    url: https://patents.google.com/patent/US20200134398A1/en
    publisher: "US Patent and Trademark Office (appl. 16/383,437; priority 2018-10-29; published 2020-04-30; status: abandoned)"
    date: '2020-04-30'
    tier: 0
    note: 'PRIMARY DOCUMENT. Assignee SRI International. The "law enforcement — detecting threatening behavior and tracking extremist groups" application appears in the PATENT, not in the peer-reviewed paper.'
  - title: "Integrating Text and Image: Determining Multimodal Document Intent in Instagram Posts"
    url: https://aclanthology.org/D19-1469/
    publisher: "Proceedings of EMNLP-IJCNLP 2019 (Kruk, Lubin, Sikka, Lin, Jurafsky, Divakaran)"
    date: '2019-11-03'
    tier: 0
    note: 'PRIMARY DOCUMENT. Acknowledgments name ONR contract N00014-17C-1008 and DARPA Communicating with Computers via ARO prime contract W911NF-15-1-0462.'
  - title: "arXiv:1904.09073 — preprint of the EMNLP-IJCNLP paper"
    url: https://arxiv.org/abs/1904.09073
    publisher: arXiv
    date: '2019-04-19'
    tier: 0
  - title: "DHS LRBAA award 70RSAT19CB0000017 to SRI International — 'Automatic Speaker Verification for USCIS Applications' ($851,953)"
    url: https://github.com/micahflee/ice-contracts
    publisher: "DHS Office of Industry Partnership R&D catalog, via DDoSecrets / 'Department of Peace' leak (2023-03-01); derived dataset in kb-research/dhs-rd-pipeline"
    date: '2019-08-16'
    tier: 2
    note: 'LEAKED DATASET, not an official publication — the award should be confirmed against USASpending/FPDS before being treated as tier 1. Period of performance 2019-08-16 to 2020-08-15.'
---

On **October 29, 2018**, SRI International filed the priority application for what became **US 2020/0134398 A1**, *Determining intent from multimodal content embedded in a common geometric space*. The underlying research was published a year later at EMNLP-IJCNLP 2019 as *Integrating Text and Image: Determining Multimodal Document Intent in Instagram Posts*, and was funded by the **Office of Naval Research** under contract **N00014-17C-1008** and by **DARPA's Communicating with Computers** program under **ARO prime contract W911NF-15-1-0462**.

**What the system does.** It infers the *intent* behind a social media post by embedding the image and its caption together in a shared geometric space, so that posts with similar intent cluster near one another. The taxonomy has seven classes: **advocative** (political, social, or cultural advocacy), promotive, exhibitionist, expressive, informative, entertainment, and **provocative** — the last subdivided into *discriminative* (targeted attacks) and *controversial*. Reported accuracy was 85.6% using both modalities, against 82.6% text-only and 76.0% image-only. The training corpus was 1,299 labeled Instagram posts.

**The distinction that matters, and the limit of what this documents.** The peer-reviewed paper frames applications as computational advertising study, propaganda detection, news media analysis, social media event detection, and user engagement prediction. The **patent** — the same technique, same authors, filed by SRI — additionally names **law enforcement: detecting threatening behavior and tracking extremist groups**, alongside micro-targeting and predicting receptiveness to political figures. That gap between the academic framing and the patent's enumerated markets is the documentary fact here; patent applications routinely list every plausible application to broaden claim scope, so the naming is evidence of intended market, not of deployment.

**Status: abandoned.** The application was never granted and prosecution was not continued. Nothing here establishes that the technique was fielded, procured, or used against anyone. This entry records **capability provenance** — that federal defense research money in 2017-2019 produced a published method for machine-classifying whether a social media post is political advocacy or provocation, and that its assignee named extremist-tracking as a use.

**Why it belongs in the record.** The classification problem this research formalizes — sorting political speech into advocacy versus threat — is the same judgment later made administratively against protest activity: see [[2026-03-09--kyle-shideler-antifa-expert-witness-credentials-pro-israel-advocacy-background]], where an indictment's expert framing came from a think tank rather than academic or government credentialing, and [[2026-06-16--minnesota-us-attorney-indicts-15-direct-action-minnesota-antifa-ties]]. It sits in the vendor lineage alongside [[2009-01-01--dataminr-founded-real-time-social-media-surveillance]] and [[2011-01-01--geofeedia-founded-location-based-social-media-surveillance]] — the difference being that this one is not a startup but a defense-contracted research institute, and the funding line is documented in the paper's own acknowledgments.

**A separate, documented DHS relationship.** SRI is not only an ONR/DARPA grantee. The DHS Office of Industry Partnership R&D catalog — leaked to DDoSecrets in March 2023 and indexed locally as `dhs-rd-pipeline` — records one SRI award: **LRBAA 70RSAT19CB0000017, "Automatic Speaker Verification for USCIS Applications," $851,953**, period of performance 2019-08-16 to 2020-08-15, under the topic "Identity Management." SRI proposed delivering a voice-biometric identity-verification system to USCIS "with unlimited Government rights," verifying identity against a voice sample "such as one collected during a visa application," and explicitly extending to "remote authentication via voice of either cooperative or **non-cooperative**" subjects. This is a different technology from the intent-classification work above and there is no evidence the two were connected. It is recorded here because it establishes that SRI was selling biometric identification capability into the immigration system in the same period. The award comes from a leaked dataset and should be confirmed against USASpending/FPDS before being relied on as tier 1.

**Open questions** (tracked as research tasks): whether SRI holds DHS/ICE/CBP contracts; whether this technique or its authors moved into any fielded system; SRI's current ownership, leadership, and any financial ties to the current administration.
