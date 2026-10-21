---
type: timeline_event
id: 2026-06-11--trumprx-privacy-policy-drops-posthog-analytics-disclosure-no-posthog-award-in-usaspending
date: '2026-06-11'
title: TrumpRx Privacy Policy Drops Its PostHog Analytics Disclosure in a Revision Dated June 11; No PostHog Award Found in USAspending
importance: 6
status: confirmed
event_date_claim: c1
verification: captured
claims:
- id: c1
  type: date
  value: June 11, 2026
  qualifier: Updated
  span: 'Privacy Policy Last Updated: June 11, 2026 TrumpRx is committed to transparency about how we handle your information.'
  url: https://web.archive.org/web/20260628170734id_/https://trumprx.gov/privacy-policy
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c2
  type: quote
  value: PostHog Provides anonymous usage analytics to help us improve our service.
  qualifier: PostHog
  span: PostHog Provides anonymous usage analytics to help us improve our service.
  url: https://web.archive.org/web/20260523033341id_/https://trumprx.gov/privacy-policy
  read: fetched
  source_kind: primary
  outcome: unreachable
  checked: '2026-10-21'
- id: c3
  type: date
  value: February 2, 2026
  qualifier: Updated
  span: 'Privacy Policy Last Updated: February 2, 2026 TrumpRx is committed to transparency about how we handle your information.'
  url: https://web.archive.org/web/20260523033341id_/https://trumprx.gov/privacy-policy
  read: fetched
  source_kind: primary
  outcome: unreachable
  checked: '2026-10-21'
- id: c4
  type: quote
  value: This is the first PCLIA conducted for this program.
  qualifier: PCLIA
  span: The Treasury has oversight responsibilities for this system. This is the first PCLIA conducted for this program.
  url: https://home.treasury.gov/system/files/236/20260518-PCLIA-TrumpAccountsProgram-508.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c5
  type: quote
  value: The National Design Studio manages techforce.gov.
  qualifier: manages
  span: The National Design Studio manages techforce.gov.
  url: https://techforce.gov/privacy-policy
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
tags:
- trumprx
- posthog
- national-design-studio
- privacy
- pia
- usaspending
- surveillance-inc-layer-3
actors:
- National Design Studio
- Joe Gebbia
- PostHog
sources:
- title: TrumpRx privacy policy, archived snapshot (Internet Archive)
  url: https://web.archive.org/web/20260523033341id_/https://trumprx.gov/privacy-policy
  publisher: Internet Archive of trumprx.gov
  date: '2026-05-23'
  tier: 1
- title: TrumpRx privacy policy, archived snapshot of revised version (Internet Archive)
  url: https://web.archive.org/web/20260628170734id_/https://trumprx.gov/privacy-policy
  publisher: Internet Archive of trumprx.gov
  date: '2026-06-28'
  tier: 1
- title: Treasury PCLIA for the Trump Accounts Program
  url: https://home.treasury.gov/system/files/236/20260518-PCLIA-TrumpAccountsProgram-508.pdf
  publisher: U.S. Treasury
  date: '2026-05-18'
  tier: 1
- title: techforce.gov privacy policy
  url: https://techforce.gov/privacy-policy
  publisher: National Design Studio
  date: '2026-08-17'
  tier: 1
---

**Date kind.** June 11, 2026 is the "Last Updated" date printed on the revised TrumpRx privacy policy. The revised text was observed in an Internet Archive snapshot taken later; the prior text was observed in archived snapshots taken before it, so the date is bracketed by archive captures and is not an independent publication timestamp.

**What changed.** The earlier policy, dated February 2, 2026, listed third-party services including "PostHog Provides anonymous usage analytics to help us improve our service." The revised policy, dated June 11, 2026, contains no PostHog string in the archived HTML, and its third-party list names Cloudflare and AWS Location Service among others. Why the entry was removed is not known. The site's own JavaScript was not re-tested for this entry, so nothing here speaks to whether PostHog code runs on the live site; a policy edit and a script removal are separate acts.

**Federal awards.** A recipient-name search of USAspending award data at the time of writing, across all award types, returned zero results for PostHog, and a contracts-only recipient search for "POSTHOG INC" returned none either. The search tool lists its own gaps: awards below the reporting threshold and classified spending are not covered, and subawards, reseller purchases and card purchases are not visible in this data. The statement this entry can carry is limited to USAspending and does not extend to all federal payments.

**PIA wording, scoped.** The corpus's earlier shorthand "zero PIAs" is not supportable as written. The scoped statement is: GSA's PIA index page, checked at the time of writing, lists no entry naming the National Design Studio, PostHog or TrumpRx; the studio's own site policies cite no PIA or SORN; and for the Trump Accounts program Treasury has published a Privacy and Civil Liberties Impact Assessment of the Bank of New York Mellon system behind it, which says "This is the first PCLIA conducted for this program." That document covers the account-opening system, not the studio-built website layer. HHS, USDA, State and EAC PIA indexes could not be reached, so they are not covered. The techforce.gov policy says "The National Design Studio manages techforce.gov." and names OPM as the program owner, which is a reminder that the owning agency, not the studio, would be the entity with a PIA duty if the studio is part of the White House rather than an agency; that legal question has not been checked against OMB guidance. Full test and its limits: the research note [[nds-posthog-zero-pias-claim-test-2026-10-15]].

**Context.** The portal is TrumpRx, launched at [[2026-02-05--trumprx-gov-launches-at-white-house-event-with-nds-director-gebbia-crs-says-national-design-studio-designed-and-operates-it]]. The studio was created within the White House Office of the Executive Office of the President by [[2025-08-21--eo-14338-creates-nds-ndstudio-gov-pre-registered-day-prior]].
