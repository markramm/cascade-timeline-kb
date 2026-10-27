---
type: timeline_event
id: 2026-10-26--cisa-adds-php2shell-cves-to-kev-binding-federal-civilian-agencies-only-due-oct-29
date: '2026-10-26'
title: CISA Adds the PHP Remote-Code-Execution Flaws to Its Known Exploited Vulnerabilities Catalog; the Fix Deadline Binds Federal Civilian Agencies Only
importance: 6
status: confirmed
event_date_claim: c0
verification: source-verified
claims:
- id: c0
  type: date
  value: Oct. 26, 2026
  span: CISA has updated this Alert to reflect the addition of CVE-2026-109618 and CVE-2026-109619 to its Known Exploited Vulnerabilities (KEV) Catalog on Oct. 26, 2026.
  url: https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c1
  type: figure
  value: CVE-2026-109618 and CVE-2026-109619
  span: CISA has updated this Alert to reflect the addition of CVE-2026-109618 and CVE-2026-109619 to its Known Exploited Vulnerabilities (KEV) Catalog on Oct. 26, 2026.
  url: https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c2
  type: date
  value: '2026-10-29'
  span: 'Stakeholders are responsible for evaluating each asset''s internet exposure and ensuring adherence to BOD 26-04 patching guidelines.", "dueDate": "2026-10-29", "knownRansomwareCampaignUse": "Unknown", "forensicTriage": "Yes",'
  url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c3
  type: figure
  value: BOD 26-04
  span: 'Stakeholders are responsible for evaluating each asset''s internet exposure and ensuring adherence to BOD 26-04 patching guidelines.", "dueDate": "2026-10-29", "knownRansomwareCampaignUse": "Unknown", "forensicTriage": "Yes",'
  url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c4
  type: quote
  value: a compulsory direction to federal, executive branch, departments, and agencies
  span: A Binding Operational Directive is a compulsory direction to federal, executive branch, departments, and agencies for purposes of safeguarding federal information and information systems.
  url: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c5
  type: quote
  value: does not apply to contractors
  span: Unless directed by the governing procurement contract, this Directive does not apply to contractors, but FCEB agencies must review all contracts to determine what modifications are necessary to comply with the required actions of this Directive, in consultation with the Contracting Officer.
  url: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c6
  type: quote
  value: within the timeline (three days) and carry out a forensic triage
  span: The text “& forensic triage” means that the agency must complete remediation or mitigation action within the timeline (three days) and carry out a forensic triage of the asset to assess whether the system is compromised.
  url: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
- id: c7
  type: quote
  value: reliable evidence that execution of malicious code was performed by an actor on a system without permission of the system owner
  span: active exploitation is one for which there is reliable evidence that execution of malicious code was performed by an actor on a system without permission of the system owner.
  url: https://www.cisa.gov/known-exploited-vulnerabilities
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-27'
tags:
- election-security
- cisa
- cybersecurity
- php2shell
- kev
- midterms
actors:
- Cybersecurity and Infrastructure Security Agency
- PHP Group
sources:
- title: Known Exploited Vulnerabilities Catalog (JSON feed, catalog version 2026.10.26)
  publisher: CISA
  date: '2026-10-26'
  url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  tier: 1
- title: 'BOD 26-04: Prioritizing Security Updates Based on Risk'
  publisher: CISA
  date: '2026-06-10'
  url: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
  tier: 1
- title: Criteria for Known Exploited Vulnerabilities
  publisher: CISA
  url: https://www.cisa.gov/known-exploited-vulnerabilities
  tier: 1
lane: Electoral Manipulation
---

CISA added CVE-2026-109618 and CVE-2026-109619, the PHP remote-code-execution flaws, to its Known Exploited Vulnerabilities catalog on Oct. 26, 2026 (catalog listing date). Both catalog entries carry a dueDate (the catalog's remediation deadline) three days after the listing date. CISA lists a flaw in the catalog when there is "reliable evidence that execution of malicious code was performed by an actor on a system without permission of the system owner." Its earlier alert had said CISA had not yet observed exploitation ([[2026-10-21--cisa-alert-urges-immediate-patching-of-php2shell-php-flaws]]).

The due date comes from Binding Operational Directive BOD 26-04. The directive is "a compulsory direction to federal, executive branch, departments, and agencies." Unless a contract says otherwise, it "does not apply to contractors." Both entries are marked for forensic triage, which under the directive means an agency must remediate "within the timeline (three days) and carry out a forensic triage." Nothing in the directive binds a state, a county or an election vendor, so it sets no deadline for the offices running the general election.
