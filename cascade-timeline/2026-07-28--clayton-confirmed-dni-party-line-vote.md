---
type: timeline_event
id: 2026-07-28--clayton-confirmed-dni-party-line-vote
date: '2026-07-28'
title: "Senate Confirms Jay Clayton as Director of National Intelligence, 51-47, on a Party-Line Roll Call"
importance: 7
status: confirmed
tags:
  - dni
  - agency-purges
  - succession
  - surveillance-industrial-complex
  - senate-confirmation
  - 2020-election-denial
  - financial-capture
actors:
  - Jay Clayton
  - U.S. Senate
  - Bill Pulte
  - Donald Trump
  - Mark Warner
sources:
  - title: "Roll Call Vote 211: On the Nomination (Confirmation: Walter Clayton, of N.Y., to be Director of National Intelligence), PN1092"
    url: https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00211.htm
    publisher: U.S. Senate
    date: '2026-07-28'
    tier: 1
  - title: "Senate confirms Jay Clayton as Trump's national intelligence director"
    url: ""
    publisher: "AP News (URL not independently confirmed this pass -- see gap note)"
    date: '2026-07-28'
    tier: 1
  - title: "Senate panel advances Jay Clayton's nomination for director of national intelligence"
    url: ""
    publisher: "PBS (URL not independently confirmed this pass -- see gap note)"
    date: '2026-07-21'
    tier: 1
  - title: "Trump's pick to head national intelligence, Jay Clayton, won't tell senators Biden won the 2020 election"
    url: ""
    publisher: "CNBC (URL not independently confirmed this pass -- see gap note)"
    date: '2026-07-15'
    tier: 1
  - title: "'I'm not an election denier': Clayton, Trump's DNI pick, faces tense questions on 2020 election"
    url: ""
    publisher: "ABC News (URL not independently confirmed this pass -- see gap note)"
    date: '2026-07-15'
    tier: 1
  - title: "Trump administration profile: Jay Clayton"
    url: https://www.opensecrets.org/news/2026/07/trump-administration-profile-jay-clayton
    publisher: OpenSecrets (Sarah Gross)
    date: '2026-07-31'
    tier: 2
    access_note: "Fetch blocked (HTTP 403) this pass; cited per cascade-research/actors/clayton-jay.md, which recorded it tier 2 with a working URL as of 2026-08-06. Not independently re-verified here."
---

**Premise correction on the source ticket title:** the ticket that generated this entry read "Jay Clayton confirmed DNI" as if that needed hedging against his better-known SEC-chair identity. It doesn't need hedging -- both are true of the same person at different times. Jay Clayton (legal name Walter Joseph Clayton Jr., per financial-disclosure indexing) was SEC chair 2017-2020, U.S. Attorney for the Southern District of New York April 2025-July 2026, and was nominated for -- and by this event, confirmed to -- Director of National Intelligence, a distinct fourth role. The Senate's own roll call vote record identifies the confirmed nominee as "Walter Clayton, of N.Y., to be Director of National Intelligence," consistent with the same legal name used elsewhere in this corpus's actor file. This is not a mixed-up title; it is a person who has held multiple senior federal roles in sequence.

**The party-line characterization checks out as arithmetic, not just description.** Senate Roll Call Vote 211 (119th Congress, 2nd session), taken July 28, 2026 at 6:21 PM, confirmed the nomination 51-47. Every senator who voted Yea was a Republican (51 of 53 Republicans; Lindsey Graham and Mitch McConnell did not vote). Every Democrat (43) and both independents (Angus King, Bernie Sanders) voted Nay. There were no crossover votes in either direction. A cloture motion the prior day, Roll Call Vote 210 (July 27, 2026), was agreed to 51-43 on the same partisan alignment.

## What happened

Clayton was nominated by Trump on June 11, 2026 -- the same day Section 702 of FISA lapsed for the first time since 2008, amid controversy over Bill Pulte's installation as acting DNI (see [[2026-06-12--fisa-702-lapses-first-time-since-2008-pulte-dni-house-vote-fails]]). His confirmation hearing before the Senate Intelligence Committee was held July 15, 2026. At that hearing, Democratic senators repeatedly pressed Clayton on whether Joe Biden won the 2020 presidential election; Clayton was initially evasive before telling Sen. Mark Warner that Biden was "fairly and duly elected under our process" -- a formulation reported as short of a direct affirmation, and one several outlets (CNBC, ABC News) covered as costing him previously expected bipartisan support. The Senate Intelligence Committee advanced the nomination July 21, 2026. The full Senate invoked cloture July 27 (51-43) and confirmed Clayton July 28 (51-47). He was sworn in August 3, 2026, succeeding Tulsi Gabbard as the ninth Director of National Intelligence, with Pulte's acting tenure ending.

## Date-kind discipline

- **Nomination date**: June 11, 2026 (Trump's announcement)
- **Confirmation-hearing date**: July 15, 2026 (Senate Intelligence Committee)
- **Committee-vote date**: July 21, 2026 (advanced to the floor, party-line per PBS coverage)
- **Cloture-vote date**: July 27, 2026 (Roll Call 210, 51-43)
- **Confirmation-vote date** (this entry's `date:` field): July 28, 2026 (Roll Call 211, 51-47)
- **Swearing-in date**: August 3, 2026 (not this entry's date; a distinct downstream event)

## Sourcing note / gaps

The Senate roll call vote (both the HTML landing page and the underlying XML at senate.gov) was fetched directly and is the load-bearing tier-1 source for the vote tally and party breakdown; the full 100-member name/party/vote roster was cross-tabulated and independently checked (100 total, 53R/43D/2I party composition, 51 Yea/47 Nay/2 Not Voting, 51 Republican Yea and zero Democratic Yea) rather than taken on a summarized characterization alone.

Several outlet pieces (AP, PBS, CNBC, ABC News) were identified via Google News RSS by real headline, publisher, and publication date, but WebFetch could not resolve their direct publisher URLs this pass -- Google News RSS redirect links 400 to automated clients, and direct guesses at AP/PBS/CNBC/ABC/Reuters/NYT URL patterns returned 403s, 404s, or fetch-tool errors ("unable to fetch from [host]"), not verified absences. Those citations are recorded above with the outlet, headline, and date, and an explicit note that the URL was not independently confirmed, rather than filling the `url:` field with a guessed or homepage URL. OpenSecrets' own July 31, 2026 profile (the ticket's suggested primary source) also 403'd on direct fetch this pass; it is cited per the pre-existing citation in `cascade-research/actors/clayton-jay.md`, which recorded a working URL as of 2026-08-06, not independently re-verified here.

No Federal Register appointment notice was located for this confirmation (DNI is a Senate-confirmed executive appointment; Federal Register notices are more typically associated with rulemaking and some categories of executive orders/proclamations, not directly with Senate confirmations, so this is not flagged as a surprising absence).
