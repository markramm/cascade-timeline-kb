---
type: timeline_event
id: 2025-06-01--palantir-ice-surveillance-system
date: 2025-06-01
importance: 9
title: Palantir holds a $30 million ICE contract for ImmigrationOS; ten Democrats press Palantir over an IRS 'mega-database'
location: United States
actors:
- Palantir Technologies
- Immigration and Customs Enforcement (ICE)
- Peter Thiel
- Ron Wyden
- Rep. Alexandria Ocasio-Cortez
tags:
- mass-surveillance
- data-integration
- privacy-violation
- ai-surveillance
- tech-authoritarianism
capture_lanes:
- Media Capture and Control
- Regulatory Capture
sources:
- title: ICE to Use ImmigrationOS by Palantir, a New AI System, to Track Immigrants' Movements
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  outlet: American Immigration Council
  date: '2025-08-21'
  tier: 2
- title: Democrats demand details from Palantir on federal contracts after Social Security, IRS report
  url: https://thehill.com/policy/technology/5355388-democrats-request-data-from-palantir/
  outlet: The Hill
  date: '2025-06-17'
  tier: 2
- title: Democrats push Palantir for answers on reports of IRS 'mega-database'
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  outlet: FedScoop
  date: '2025-06-17'
  tier: 2
- title: Palantir's ImmigrationOS fuels Trump administration's immigrant removal agenda
  url: https://www.biometricupdate.com/202504/palantirs-immigrationos-fuels-trump-administrations-immigrant-removal-agenda
  outlet: Biometric Update
  date: '2025-04-21'
  tier: 2
- title: Markey Joins Wyden, Ocasio-Cortez to Demand Answers from Palantir About Plans to Build IRS Mega-Database
  url: https://www.markey.senate.gov/news/press-releases/markey-joins-wyden-ocasio-cortez-to-demand-answers-from-palantir-about-plans-to-build-irs-mega-database-of-american-citizens
  outlet: Office of Sen. Edward Markey
  date: '2025-06-17'
  tier: 1
- title: Letter to Palantir CEO Alex Karp
  url: https://www.finance.senate.gov/wp-content/uploads/media/doc/wyden_aoc_palantir_letter_061725.pdf
  outlet: Senate Committee on Finance
  date: '2025-06-17'
  tier: 1
status: confirmed
corrections:
- date: '2026-11-17'
  was: "Eight members of Congress warned this creates \"a surveillance nightmare\" and potential \"mega-database\" for targeting political enemies."
  now: "Ten Democrats in Congress signed the June 17, 2025 letter (FedScoop: ten; the letter's signature page: Wyden, Ocasio-Cortez, Warren, McGovern, Merkley, Jacobs, Markey, Tlaib, Lee, Tonko). The letter concerns a reported Palantir-built IRS database of taxpayer records, not ImmigrationOS; Palantir denies building a master database."
  why: "The Hill says the letter was 'signed by six other colleagues' (eight in all); FedScoop and Markey's press release say ten. The letter's own signature page lists ten. The entry also stated as fact that the platform integrates IRS and Social Security data and that the integration violates privacy laws; the sources give the first as the AIC's description and the second as the lawmakers' allegation. 'Delivered by September 2025' was a prototype date. The notes field's $113 million 'with DHS and Pentagon', '$228-542 million annually 2020-2024' and 'violates privacy laws' were not in the cited sources and were removed or restated. Source dates were corrected to the pages' own. The entry's date, 2025-06-01, matches no event in its sources (ICE awarded the contract in April 2025; the letter is June 17, 2025 and has its own entry, 2025-06-17--wyden-goldman-velazquez-letter-karp-palantir-ice-surveillance); the date and filename are left as they are because other entries link to this id, and the gate's event-date check therefore fails on that field alone."
  found_by: "canon-validate run 2026-11-17; corrected by cascade-research task recheck-canon-ten-sentences-in-nine-of-the-most-cited-unverified-entries-that"

coverage:
  - url: "https://theramm.substack.com/p/the-hammer-and-the-guardrail"
    title: "The Hammer and the Guardrail"
    date: '2026-02-27'
    publication: theramm
    note: "Describes how removing Anthropic's mass-surveillance guardrails would give Palantir's ImmigrationOS 'a brain' — AI-enabled targeting without constitutional friction"
  - url: https://theramm.transparencycascade.org/p/the-power-the-pope-warned-about-has
    title: "The Power the Pope Warned About Has a Guest List"
verification: captured
claims:
- id: c1
  type: date
  value: April 2025
  qualifier: awarded
  span: In April 2025, U.S. Immigration and Customs Enforcement (ICE) awarded a $30 million contract to Palantir Technologies to develop ImmigrationOS, a comprehensive digital platform aimed at streamlining and expanding the agency’s deportation apparatus
  url: https://www.biometricupdate.com/202504/palantirs-immigrationos-fuels-trump-administrations-immigrant-removal-agenda
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c2
  type: figure
  value: $30 million
  qualifier: ICE is paying
  span: ICE is paying Palantir $30 million for the platform.
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c3
  type: date
  value: September 25, 2025
  qualifier: prototype
  span: Palantir is slated to deliver a prototype of the ImmigrationOS platform by September 25, 2025, with the contract running through September 2027.
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c4
  type: date
  value: September 2027
  qualifier: contract running through
  span: Palantir is slated to deliver a prototype of the ImmigrationOS platform by September 25, 2025, with the contract running through September 2027.
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c5
  type: attribution
  value: IRS tax data
  qualifier: pull data
  span: Palantir’s systems pull data from across government databases —regardless of the veracity or accuracy of those databases—including passport records, Social Security files, IRS tax data, and even license-plate reader data.
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c6
  type: attribution
  value: three main components
  qualifier: government documents
  span: 'According to government documents, ImmigrationOS is ICE’s next-generation enforcement tool. It has three main components :'
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c7
  type: attribution
  value: concerns about the ethical burden
  qualifier: some engineers
  span: Some Palantir engineers themselves have raised concerns about the ethical burden of designing these tools.
  url: https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c8
  type: figure
  value: ten
  qualifier: congressional Democrats
  span: Ten congressional Democrats are demanding answers from Palantir about reports that it is aiding the IRS in building a searchable, governmentwide “mega-database” to house Americans’ sensitive information.
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c9
  type: figure
  value: seven
  qualifier: other Members of Congress
  span: Senator Edward J. Markey (D-Mass.), today joined Senator Ron Wyden (D-Ore.), Ranking Member of the Senate Finance Committee, Representative Alexandria Ocasio-Cortez (D-N.Y.), and seven other Members of Congress in questioning Palantir
  url: https://www.markey.senate.gov/news/press-releases/markey-joins-wyden-ocasio-cortez-to-demand-answers-from-palantir-about-plans-to-build-irs-mega-database-of-american-citizens
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: c10
  type: quote
  value: is a surveillance nightmare
  qualifier: wrote
  span: The unprecedented possibility of a searchable, ‘mega-database’ of tax returns and other data that will potentially be shared with or accessed by other federal agencies is a surveillance nightmare that raises a host of legal concerns, not least that it will make it significantly easier for Donald Trump’s Administration to spy on and target his growing list of enemies and other Americans,” the Democrats wrote.
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c11
  type: attribution
  value: Palantir employees have reportedly been installed at the Internal Revenue Service
  qualifier: reportedly
  span: According to press reports, Palantir employees have reportedly been installed at the Internal Revenue Service (“IRS”), where they are helping the agency use Palantir’s software to create a “single, searchable database” of taxpayer records.
  url: https://www.finance.senate.gov/wp-content/uploads/media/doc/wyden_aoc_palantir_letter_061725.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: c12
  type: quote
  value: Palantir is not building a master database
  qualifier: company
  span: “Palantir is not building a master database,” the company said in another statement.
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c13
  type: figure
  value: $113 million
  qualifier: since the January inauguration
  span: the data-mining giant has received $113 million since the president’s January inauguration plus another $795 million award from the Defense Department.
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c14
  type: figure
  value: $795 million
  qualifier: award from the Defense Department
  span: the data-mining giant has received $113 million since the president’s January inauguration plus another $795 million award from the Defense Department.
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c15
  type: attribution
  value: New York Times
  qualifier: reporting last month
  span: follows New York Times reporting last month that detailed the expansion of Palantir’s federal government work under the Trump administration
  url: https://fedscoop.com/palantir-irs-mega-database-democrats-letter/
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-11-17'
- id: c16
  type: date
  value: June 17, 2025
  qualifier: today
  span: Washington (June 17, 2025) - Senator Edward J. Markey (D-Mass.), today joined Senator Ron Wyden (D-Ore.), Ranking Member of the Senate Finance Committee, Representative Alexandria Ocasio-Cortez (D-N.Y.), and seven other Members of Congress in questioning Palantir about reports that Palantir is helping the IRS to build a government-wide, searchable, “mega-database,” connecting sensitive tax and other data the government holds about American citizens.
  url: https://www.markey.senate.gov/news/press-releases/markey-joins-wyden-ocasio-cortez-to-demand-answers-from-palantir-about-plans-to-build-irs-mega-database-of-american-citizens
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: c17
  type: quote
  value: Palantir's troubling assistance to the Trump Administration is not limited to its work for the IRS
  qualifier: troubling
  span: Palantir's troubling assistance to the Trump Administration is not limited to its work for the IRS.
  url: https://www.finance.senate.gov/wp-content/uploads/media/doc/wyden_aoc_palantir_letter_061725.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
---

Palantir Technologies holds a $30 million ICE contract for ImmigrationOS, an AI platform that ICE awarded in April 2025. The American Immigration Council reports Palantir was slated to deliver a prototype by September 25, 2025, with the contract running through September 2027, and that government documents give ImmigrationOS three main components: targeting and enforcement prioritization, self-deportation tracking and immigration lifecycle management. It says Palantir's systems pull data from across government databases, including passport records, Social Security files, IRS tax data and license-plate reader data. Some Palantir engineers have raised concerns about the ethical burden of designing these tools.

On June 17, 2025, ten congressional Democrats led by Sen. Ron Wyden and Rep. Alexandria Ocasio-Cortez wrote to Palantir CEO Alex Karp about reports that Palantir employees at the IRS are helping the agency build a single, searchable database of taxpayer records. The lawmakers called the possibility of a searchable "mega-database" of tax returns "a surveillance nightmare"; that language concerns the reported IRS database. The letter adds that "Palantir's troubling assistance to the Trump Administration is not limited to its work for the IRS." Palantir answered: "Palantir is not building a master database." Per the New York Times, as FedScoop relays it, Palantir had received $113 million since the January inauguration, plus another $795 million award from the Defense Department.
