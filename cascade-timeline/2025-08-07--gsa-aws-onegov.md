---
type: timeline_event
id: 2025-08-07--gsa-aws-onegov
title: GSA announces OneGov agreement with AWS offering up to $1 billion in credits
date: 2025-08-07
importance: 7
location: Washington, D.C.
actors:
- General Services Administration
- AWS
tags:
- cloud
- procurement
- vendor-concentration
- aws
- government-contracts
- monopoly-risk
- gsa
- ai-infrastructure
citations:
- https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025
- https://fedscoop.com/aws-gsa-onegov-deal-1-billion-savings/
- https://www.nextgov.com/acquisition/2025/08/gsa-amazon-sign-new-centralized-cloud-pact/407277/
notes: 'GSA announced the agreement on 2025-08-07. The vendor-concentration and antitrust concerns raised in earlier drafts of this entry are analysis, not findings of the GSA release, and are not asserted here.'
status: reported
sources:
- title: GSA Announces OneGov Agreement with Amazon Web Services; Provides up to $1 Billion in Savings to Accelerate IT Transformation and Catalyze American AI Leadership
  url: https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025
  outlet: General Services Administration
  date: '2025-08-07'
  tier: 1
- title: GSA inks governmentwide deal with AWS, touting $1B in potential savings
  url: https://fedscoop.com/aws-gsa-onegov-deal-1-billion-savings/
  outlet: FedScoop
  date: '2025-08-07'
  tier: 2
- title: GSA, Amazon sign onto new centralized cloud pact
  url: https://www.nextgov.com/acquisition/2025/08/gsa-amazon-sign-new-centralized-cloud-pact/407277/
  outlet: Nextgov/FCW
  date: '2025-08-07'
  tier: 2
corrections:
- date: '2026-10-21'
  was: "Title and body: \"GSA enters $1B OneGov cloud agreement with AWS\" / \"a $1 billion 'OneGov' cloud agreement\""
  now: "GSA announced a OneGov agreement under which AWS provides up to $1 billion in direct incentive credits (AWS, modernization and training credits), aggregated across federal civilian agencies, through December 31, 2028. The figure is a ceiling on credits, not a $1 billion contract value."
  why: "https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025 — release states 'up to a total of $1 billion in direct incentive credits aggregated across Federal civilian agencies'"
  found_by: "vendor-verification worker, conductor QC 2026-10-21"
- date: '2026-10-21'
  was: "Primary citation https://www.gsa.gov/about-us/newsroom/news-releases/gsa-enters-into-1b-onegov-cloud-agreement-with-aws (GSA release, dated 2025-07-18 in sources)"
  now: "https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025; release dated 2025-08-07"
  why: "the old URL returns 404; the live release is at the new URL and is dated August 7, 2025, not July 18"
  found_by: "vendor-verification worker, conductor QC 2026-10-21"
- date: '2026-10-21'
  was: "Sources list included FTC commissioner rulings, GENIUS Act coverage, the Trump v. WSJ suit and IRS workforce reports, plus a Reuters 'Amazon inks $1 billion cloud deal' link dated 2025-07-18"
  now: "Sources limited to the GSA release, FedScoop and Nextgov. The unrelated items were removed. The Reuters link returned HTTP 401 and could not be read, and its July 18 date precedes the August 7 announcement, so it is not retained."
  why: "none of the removed items concern the AWS agreement (or could not be verified); FedScoop and Nextgov fetched and describe the same up-to-$1B credits and December 2028 end date"
  found_by: "vendor-verification worker, conductor QC 2026-10-21"
- date: '2026-10-21'
  was: "This agreement centralizes government cloud services under Amazon ... through December 31, 2028 ... raises concerns about vendor concentration, competitive fairness, and potential conflicts of interest; notes: single-vendor contract raises antitrust concerns, follows GSA's mass layoffs"
  now: "Body limited to what the release states. Nextgov describes the pact as non-exclusive, so 'centralizes ... under Amazon' and 'single-vendor contract' are removed; the concern and layoff statements are unsourced characterisations and are removed. Entry status set to reported."
  why: "https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025; https://www.nextgov.com/acquisition/2025/08/gsa-amazon-sign-new-centralized-cloud-pact/407277/ ('non-exclusive'); no fetched source supports the concern or layoff language"
  found_by: "vendor-verification worker, conductor QC 2026-10-21"
verification: source-verified
claims:
- id: c1
  type: date
  value: August 07, 2025
  qualifier: Announces
  span: August 07, 2025 GSA Announces OneGov Agreement with Amazon Web Services; Provides up to $1 Billion in Savings to Accelerate IT Transformation and Catalyze American AI Leadership
  url: https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c2
  type: figure
  value: $1 billion
  qualifier: up to; credits
  span: The agreement offers up to a total of $1 billion in direct incentive credits aggregated across Federal civilian agencies
  url: https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c3
  type: date
  value: December 31, 2028
  qualifier: through
  span: Today, the U.S. General Services Administration (GSA) announced an innovative OneGov agreement with Amazon Web Services (AWS) to provide up to $1 billion in savings for cloud adoption, modernization, and training for federal agencies through December 31, 2028.
  url: https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-onegov-agreement-with-aws-08072025
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
event_date_claim: c3
source_published_date: '2025-08-07'
capture_lanes:
- Financial Capture
---


The U.S. General Services Administration announced a OneGov agreement with Amazon Web Services providing up to $1 billion in direct incentive credits, aggregated across federal civilian agencies, for AWS cloud services, modernization support and training, through December 31, 2028. GSA's release describes the credits as savings for agencies; the agreement is a credit offer, not a stated contract value.
