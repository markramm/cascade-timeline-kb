---
type: timeline_event
id: 2026-01-20--doj-confirms-doge-social-security-data-breach
date: 2026-01-20
status: reported
verification: source-verified
title: "DOJ Notice Says DOGE Team Members Shared SSA Data Through Cloudflare, a Server Not Approved for SSA Data; the NUMIDENT-Copy Allegation Remains the Whistleblower's"
importance: 9
actors:
- Department of Government Efficiency
- Department of Justice
- Social Security Administration
- Elon Musk
tags:
- doge
- data-privacy
- government-restructuring
- institutional-capture
- whistleblower-retaliation
sources:
- url: https://larson.house.gov/media-center/press-releases/larson-neal-demand-full-criminal-investigation-doge-leak-private-0
  title: Larson, Neal Demand Full Criminal Investigation into DOGE Leak of Private Records to Musk Associates
  outlet: Office of Rep. John Larson
  date: '2026-01-20'
  tier: 1
- url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  title: Notice of Corrections to the Record, AFSCME v. SSA, ECF 197 (D. Md., filed 2026-01-16)
  outlet: U.S. District Court, D. Md.
  date: '2026-01-16'
  tier: 1
- url: https://www.cnn.com/2026/01/20/politics/doge-social-security-data-unauthorized-server
  title: DOGE shared Social Security data to unauthorized server, according to court filing
  outlet: CNN
  date: '2026-01-20'
  tier: 2
- url: https://www.pbs.org/newshour/show/whistleblower-responds-after-doj-confirms-doge-mishandled-social-security-data
  title: Whistleblower responds after DOJ confirms DOGE mishandled Social Security data
  outlet: PBS
  date: '2026-01-20'
  tier: 1
- url: https://whistleblower.org/press/doj-issues-corrections-validating-whistleblowers-claim-of-doge-mismanagement-at-social-security-administration/
  title: DOJ Issues Corrections Validating Whistleblower's Claim of DOGE Mismanagement at Social Security Administration
  outlet: Government Accountability Project
  date: '2026-01-20'
  tier: 2
capture_lanes:
- Executive Power Expansion
- Digital and Tech Capture
- Surveillance Infrastructure
corrections:
- date: '2026-10-21'
  was: "The DOJ filing revealed that DOGE employees created a copy of the agency's Numerical Identification System (NUMIDENT) database without following required security protocols, bypassing strict security measures for federal databases. The copy allegedly lacked security oversight from SSA or tracking to determine who accessed the data."
  now: "The Notice (ECF 197) does not say DOGE created a copy of NUMIDENT. It says one DOGE Team member ran PII searches on SSA's own copy of the Numident within the Enterprise Data Warehouse on the morning of March 24, 2025. The claim of a vulnerable copy lacking oversight is from Charles Borges's whistleblower disclosure, which CNN reports and the agency denied; Borges told PBS that piece of his disclosure \"has not yet been validated or refuted yet with any documentation.\""
  why: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf (no creation of a NUMIDENT copy; Section I, p. 2); https://www.cnn.com/2026/01/20/politics/doge-social-security-data-unauthorized-server (attributes the copy claim to the whistleblower disclosure and notes the agency denied it); https://www.pbs.org/newshour/show/whistleblower-responds-after-doj-confirms-doge-mishandled-social-security-data (Borges: third piece not validated)"
  found_by: "editorial verification, 2026-10-21"
- date: '2026-10-21'
  was: "retained access to data even after a judge temporarily halted it"
  now: "The Notice discloses that SSA granted DOGE Team members PII access after the TRO: on March 26, 2025 (SSA says never used) and on April 9, 2025 (a call-center profile; SSA does not know whether PII was accessed). It does not say access was retained after the TRO; it says access to all PII was terminated at about noon on March 24, 2025, after PII searches that morning."
  why: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf (Sections I and III, pp. 2-3)"
  found_by: "editorial verification, 2026-10-21"
- date: '2026-10-21'
  was: "improperly shared sensitive personal data of more than 300 million Americans to an unauthorized Cloudflare server"
  now: "The 300-million figure belongs to Borges's disclosure as CNN reports it, and Borges told PBS it \"was just initial news reporting.\" The Notice says Cloudflare is not approved for storing SSA data and that SSA cannot determine what data were shared, and identifies one encrypted file believed to hold names and addresses of approximately 1,000 people, emailed to DHS."
  why: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf (Sections II and VI); https://www.pbs.org/newshour/show/whistleblower-responds-after-doj-confirms-doge-mishandled-social-security-data"
  found_by: "editorial verification, 2026-10-21"
- date: '2026-10-21'
  was: "SSA admitted it still had \"little knowledge of what data was shared\" and could not verify the extent of violations; Privacy experts noted the violations likely breached the Privacy Act; Borges stated the revelations were \"disappointing to be proven right\" and called for congressional investigation; sent password-protected files of private records to DOGE affiliates outside the agency"
  now: "Removed or narrowed: the quoted phrases \"little knowledge of what data was shared\" and \"disappointing to be proven right\" were not found in ECF 197, CNN or PBS as re-read, and no source read supports the Privacy-Act-experts sentence. The Notice says SSA \"has not been able to determine exactly what data were shared to Cloudflare\"; it describes one encrypted file emailed to DHS, copying a senior DOGE advisor and a DOGE-affiliated Department of Labor employee. Borges told PBS that validation of two of his three concerns was \"disappointing.\" Kept and now sourced: Reps. Larson and Neal's statement that the matter \"could very well be the largest data breach in our nation's history.\""
  why: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf (Sections II and VI); https://www.pbs.org/newshour/show/whistleblower-responds-after-doj-confirms-doge-mishandled-social-security-data ; https://larson.house.gov/media-center/press-releases/larson-neal-demand-full-criminal-investigation-doge-leak-private-0 (the quoted statement, conditional: 'could very well be')"
  found_by: "editorial verification, 2026-10-21"
- date: '2026-10-21'
  was: "date: 2026-01-20 (as the filing's date)"
  now: "The Notice was filed 2026-01-16. 2026-01-20 is the date of the CNN report and of the Larson-Neal statement this entry summarizes (the PBS interview is dated 2026-01-27). The date is kept so the id and ordering stay stable."
  why: "https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf (Filed 01/16/26); https://larson.house.gov/media-center/press-releases/larson-neal-demand-full-criminal-investigation-doge-leak-private-0 (January 20, 2026); PBS page metadata article:published_time 2026-01-27"
  found_by: "editorial verification, 2026-10-21"
date_is_publication_date: true
event_date_claim: c15
claims:
- id: c12
  type: quote
  value: could very well be the largest data breach in our nation’s history
  qualifier: continued
  span: “The time for talk is over. Chairman Smith and every Republican on the Ways and Means Committee must break their silence on what could very well be the largest data breach in our nation’s history and as we have now learned, may have implications for election security,” they continued.
  url: https://larson.house.gov/media-center/press-releases/larson-neal-demand-full-criminal-investigation-doge-leak-private-0
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c15
  type: date
  value: January 20, 2026
  qualifier: Press
  span: January 20, 2026 Press Release Washington, D.C. - Today, House Social Security Subcommittee Ranking Member John B. Larson
  url: https://larson.house.gov/media-center/press-releases/larson-neal-demand-full-criminal-investigation-doge-leak-private-0
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c14
  type: quote
  value: first acknowledgement that DOGE employees inappropriately handled highly sensitive Social Security data
  qualifier: acknowledgement
  span: The filing is the Trump administration’s first acknowledgement that DOGE employees inappropriately handled highly sensitive Social Security data – a charge that a top agency official levied last summer.
  url: https://www.cnn.com/2026/01/20/politics/doge-social-security-data-unauthorized-server
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-21'
- id: c1
  type: date
  value: January 16, 2026
  qualifier: Dated
  span: 'Case 1:25-cv-00596-ELH Dated: January 16, 2026'
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c2
  type: quote
  value: Cloudflare is not approved for storing SSA data
  qualifier: approved
  span: Cloudflare is not approved for storing SSA data and when used in this manner is outside SSA’s security protocols.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c3
  type: quote
  value: SSA has not been able to determine exactly what data were shared to Cloudflare
  qualifier: determine
  span: Because Cloudflare is a third-party entity, SSA has not been able to determine exactly what data were shared to Cloudflare or whether the data still exist on the server.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c4
  type: figure
  value: approximately 1,000 people
  qualifier: believes
  span: SSA believes that the encrypted attachment contained PII derived from SSA systems of record, including names and addresses of approximately 1,000 people.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c5
  type: quote
  value: ran PII searches on SSA’s copy of the Numident
  qualifier: morning
  span: SSA has now determined that, during the morning (Eastern Time) of Monday, March 24, 2025, one member of the then-SSA DOGE Team ran PII searches on SSA’s copy of the Numident (SSA System of Records Notice 60-0058) within the Enterprise Data Warehouse (“EDW”), with the last search occurring on or about 9:30am ET.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c6
  type: date
  value: March 26, 2025
  qualifier: granted
  span: Namely, on March 26, 2025, one DOGE Team member was granted access to ten EDW schema containing PII.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c7
  type: date
  value: April 9, 2025
  qualifier: granted
  span: This access was granted on April 9, 2025, and revoked on June 11, 2025.
  url: https://storage.courtlistener.com/recap/gov.uscourts.mdd.577321/gov.uscourts.mdd.577321.197.0.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-10-21'
- id: c8
  type: quote
  value: warned in a whistleblower complaint that DOGE employees put the records of more than 300 million Americans at risk
  qualifier: warned
  span: Charles Borges, who had served as Social Security’s chief data officer between late January and late August, warned in a whistleblower complaint that DOGE employees put the records of more than 300 million Americans at risk by creating a copy of the data in a vulnerable cloud computing server.
  url: https://www.cnn.com/2026/01/20/politics/doge-social-security-data-unauthorized-server
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-21'
- id: c9
  type: quote
  value: The agency denied the claim
  qualifier: denied
  span: The agency denied the claim, and Borges was forced to “involuntarily resign” shortly afterwards.
  url: https://www.cnn.com/2026/01/20/politics/doge-social-security-data-unauthorized-server
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-21'
- id: c10
  type: quote
  value: The third piece has not yet been validated or refuted yet with any documentation
  qualifier: validated
  span: This court filing validates the first two pieces of that puzzle. The third piece has not yet been validated or refuted yet with any documentation.
  url: https://www.pbs.org/newshour/show/whistleblower-responds-after-doj-confirms-doge-mishandled-social-security-data
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-21'
- id: c11
  type: quote
  value: that was just initial news reporting
  qualifier: reporting
  span: As far as the 300 million, that was just initial news reporting.
  url: https://www.pbs.org/newshour/show/whistleblower-responds-after-doj-confirms-doge-mishandled-social-security-data
  read: fetched
  source_kind: secondary
  outcome: verified
  checked: '2026-10-21'
---

The Department of Justice filed a Notice of Corrections in *AFSCME v. SSA* (D. Md.) on January 16, 2026; CNN published its report on January 20. The Notice says SSA has learned that DOGE Team members shared data through links on the third-party server Cloudflare, and that "Cloudflare is not approved for storing SSA data." SSA says it "has not been able to determine exactly what data were shared to Cloudflare." CNN called the filing the administration's first acknowledgement that DOGE employees inappropriately handled sensitive Social Security data; that characterization is CNN's, not the filing's.

The Notice also discloses an encrypted, password-protected file emailed to the Department of Homeland Security that SSA believes held names and addresses of approximately 1,000 people, and that SSA has been unable to open. It discloses that one DOGE Team member ran PII searches on SSA's own copy of the Numident on the morning of March 24, 2025, before access was cut at about noon, and that SSA granted DOGE Team members PII access after the TRO, on March 26, 2025 (which SSA says was never used) and April 9, 2025 (a call-center profile; SSA does not know whether PII was accessed).

## What is the whistleblower's allegation, not the filing's

Charles Borges, SSA's former chief data officer, "warned in a whistleblower complaint that DOGE employees put the records of more than 300 million Americans at risk" by creating a copy of the agency database in a vulnerable cloud server, CNN reported; the agency denied the claim and Borges "involuntarily" resigned. The Notice does not describe such a copy. Borges told PBS that the filing validates part of his disclosure, and "The third piece has not yet been validated or refuted yet with any documentation." Of the 300 million figure he said "that was just initial news reporting."

On January 20, Reps. John Larson and Richard Neal demanded a criminal investigation and wrote that the matter "could very well be the largest data breach in our nation's history." That is their characterization of the whole episode, including the whistleblower's allegation; the Notice itself does not size a breach.
