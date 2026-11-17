---
type: timeline_event
id: 1976-04-21--united-states-v-miller-bank-records-third-party-doctrine
previous_ids: [1976-06-23--united-states-v-miller-bank-records-third-party-doctrine]
date: '1976-04-21'
event_date_claim: n1
title: Supreme Court Holds in United States v. Miller That a Bank Depositor Has No Fourth Amendment Interest in the Bank's Subpoenaed Records
importance: 9
status: confirmed
actors:
  - Lewis Powell
  - William Rehnquist
  - Thurgood Marshall
  - William Brennan
  - Mitchell Miller
tags:
  - third-party-doctrine
  - fourth-amendment
  - bank-records
  - surveillance-infrastructure
  - supreme-court
sources:
  - title: "United States v. Miller, 425 U.S. 435 (1976)"
    url: https://supreme.justia.com/cases/federal/us/425/435/
    publisher: U.S. Supreme Court
    date: '1976-04-21'
    tier: 1
  - title: "United States v. Miller, 425 U.S. 435 (1976), United States Reports (Library of Congress)"
    url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
    publisher: Library of Congress
    date: '1976-04-21'
    tier: 1
  - title: "Smith v. Maryland, 442 U.S. 735 (1979)"
    url: https://supreme.justia.com/cases/federal/us/442/735/
    publisher: U.S. Supreme Court
    date: '1979-06-20'
    tier: 1
  - title: "Carpenter v. United States, 138 S. Ct. 2206 (2018)"
    url: https://supreme.justia.com/cases/federal/us/585/16-402/
    publisher: U.S. Supreme Court
    date: '2018-06-22'
    tier: 1
capture_lanes:
  - Surveillance Infrastructure
  - Financial Capture
coverage: []
corrections:
- date: '2026-11-17'
  was: 'Carpenter bullets: ''FBI obtained 127 days of cell-site location data for a robbery suspect without a warrant''; ''Holding (5-4): Fourth Amendment requires warrant for extended cell-site location data''; ''Court explicitly declined to overrule Miller or Smith. Ruling is narrow, applies only to extended location history, not to short-term or to other third-party data.'''
  now: The Government got the records by court orders under the Stored Communications Act. The Court held that acquiring seven days of historical cell-site records was a search and that a warrant is generally required; it called the decision narrow, said it did not disturb Smith and Miller, and left open shorter periods, real-time CSLI, tower dumps and other business records that might incidentally reveal location. 'Applies only to' turned those open questions into a ruling that they are excluded. The opinion prints no vote count; its syllabus names the Justices who joined it and who dissented.
  found_by: task put-the-carpenter-v-united-states-opinion-in-documents-and-bind-the-carpenter (2026-11-17); read against the slip opinion
- date: '2026-11-17'
  was: 'Dated June 23, 1976 ("effective date June 23, 1976 after rehearing denial"); a vote of 7-2; information shared with any third party loses protection "regardless of the circumstances under which it was shared"; "ATF issued subpoena"; "Brennan dissent (joined by Marshall)"; defendant named Mitch Miller; commercial data brokers described as a space Miller opened, where the government acquires what it could not constitutionally acquire through primary surveillance.'
  now: 'Decided April 21, 1976 per the opinion; no vote tally printed (the listing names the author, those who joined and the dissenters); the opinion says the rule applies even if the information is revealed on the assumption it will be used only for a limited purpose; ATF agents presented grand jury subpoenas completed by the United States Attorney''s office; Brennan and Marshall each filed a separate dissent; respondent is Mitchell Miller; whether a government purchase from a broker is a search is undecided.'
  found_by: task canon-leftovers-from-today-s-rechecks (2026-11-17); read against 425 U.S. 435, Library of Congress copy
approved_names:
  - Mitch Miller
  - Mitchell Miller
  - Held Miller
verification: source-verified
claims:
- id: m1
  type: figure
  value: 12,898
  qualifier: ''
  span: Altogether the Government obtained 12,898 location points cataloging Carpenter’s movements—an average of 101 data points per day.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m2
  type: figure
  value: 127 days
  qualifier: ''
  span: The first order sought 152 days of cell-site records from MetroPCS, which produced records spanning 127 days.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m3
  type: quote
  value: we hold that an individual maintains a legitimate expectation of privacy in the record of his physical movements as captured through CSLI
  qualifier: ''
  span: we hold that an individual maintains a legitimate expectation of privacy in the record of his physical movements as captured through CSLI.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m4
  type: quote
  value: accessing seven days of CSLI constitutes a Fourth Amendment search
  qualifier: ''
  span: It is sufficient for our purposes today to hold that accessing seven days of CSLI constitutes a Fourth Amendment search.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m5
  type: quote
  value: must generally obtain a warrant supported by probable cause before acquiring such records
  qualifier: ''
  span: we also conclude that the Government must generally obtain a warrant supported by probable cause before acquiring such records.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m6
  type: quote
  value: Our decision today is a narrow one.
  qualifier: ''
  span: Our decision today is a narrow one.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m7
  type: quote
  value: We do not disturb the application of Smith and Miller
  qualifier: ''
  span: We do not disturb the application of Smith and Miller or call into question conventional surveillance techniques and tools, such as security cameras.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m8
  type: quote
  value: Nor do we address other business records that might incidentally reveal location information.
  qualifier: ''
  span: Nor do we address other business records that might incidentally reveal location information.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m9
  type: quote
  value: we need not decide whether there is a limited period for which the Government may obtain an individual’s historical CSLI free from Fourth Amendment scrutiny
  qualifier: ''
  span: we need not decide whether there is a limited period for which the Government may obtain an individual’s historical CSLI free from Fourth Amendment scrutiny, and if so, how long that period might be.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m10
  type: quote
  value: 'We do not express a view on matters not before us: real-time CSLI'
  qualifier: ''
  span: 'We do not express a view on matters not before us: real-time CSLI'
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m11
  type: attribution
  value: court order issued under the Stored Communications Act
  qualifier: ''
  span: The Government acquired the cell-site records pursuant to a court order issued under the Stored Communications Act, which required the Government to show “reasonable grounds” for believing that the records were “relevant and
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: m12
  type: attribution
  value: BREYER, SOTOMAYOR, and KAGAN, JJ., joined
  qualifier: ''
  span: BURG, BREYER, SOTOMAYOR, and KAGAN, JJ., joined.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n1
  type: date
  value: April 21, 1976
  qualifier: ''
  span: No. 74-1179. Argued January 12, 1976-Decided April 21, 1976
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n2
  type: date
  value: January 12, 1976
  qualifier: ''
  span: No. 74-1179. Argued January 12, 1976-Decided April 21, 1976
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n3
  type: attribution
  value: POWELL, J., delivered the opinion of the Court
  qualifier: ''
  span: POWELL, J., delivered the opinion of the Court, in which BURGER, C. J., and STEWART, WHITE, BLACKMUN, REHNQUIST, and STEVENS, JJ., joined.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n4
  type: attribution
  value: REHNQUIST, and STEVENS
  qualifier: ''
  span: POWELL, J., delivered the opinion of the Court, in which BURGER, C. J., and STEWART, WHITE, BLACKMUN, REHNQUIST, and STEVENS, JJ., joined.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n5
  type: attribution
  value: filed dissenting opinions
  qualifier: ''
  span: BRENNAN, J., post, p. 447, and MARSHALL, J., po8t, p. 455, filed dissenting opinions.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n6
  type: quote
  value: Respondent possessed no Fourth Amendment interest in the bank records that could be vindicated by a challenge to the subpoenas
  qualifier: ''
  span: Respondent possessed no Fourth Amendment interest in the bank records that could be vindicated by a challenge to the subpoenas, and the District Court therefore did not err in denying the motion to suppress.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n7
  type: quote
  value: The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.
  qualifier: ''
  span: The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n8
  type: quote
  value: was convicted of possessing an unregistered still
  qualifier: ''
  span: Respondent was convicted of possessing an unregistered still, carrying on the business of a distiller without giving bond and with intent to defraud the Government of whiskey tax, possessing 175 gallons of whiskey upon which no taxes had been paid, and conspiring to defraud the United States of tax revenues.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n9
  type: quote
  value: agents from the Treasury Department's Alcohol, Tobacco and Firearms Bureau presented grand jury subpoenas issued in blank by the clerk of the District Court, and completed by the United States Attorney's office
  qualifier: ''
  span: agents from the Treasury Department's Alcohol, Tobacco and Firearms Bureau presented grand jury subpoenas issued in blank by the clerk of the District Court, and completed by the United States Attorney's office, to the presidents of the Citizens & Southern National Bank of Warner Robins and the Bank of Byron, where respondent maintained accounts.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n10
  type: quote
  value: The banks did not advise respondent that the subpoenas had been served
  qualifier: ''
  span: The banks did not advise respondent that the subpoenas had been served
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n11
  type: quote
  value: reversed on the ground that a depositor's Fourth Amendment rights are violated when bank records maintained pursuant to the Bank Secrecy Act are obtained by means of a defective subpoena
  qualifier: ''
  span: The Court of Appeals for the Fifth Circuit reversed on the ground that a depositor's Fourth Amendment rights are violated when bank records maintained pursuant to the Bank Secrecy Act are obtained by means of a defective subpoena.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n12
  type: quote
  value: Since we find that respondent had no protectable Fourth Amendment interest in the subpoenaed documents, we reverse the decision below.
  qualifier: ''
  span: Since we find that respondent had no protectable Fourth Amendment interest in the subpoenaed documents, we reverse the decision below.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n13
  type: quote
  value: these are the business records of the banks
  qualifier: ''
  span: Instead, these are the business records of the banks.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n14
  type: quote
  value: This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed.
  qualifier: ''
  span: This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n15
  type: quote
  value: not entirely volitional
  qualifier: ''
  span: the disclosure by individuals or business firms of their financial affairs to a bank is not entirely volitional, since it is impossible to participate in the economic life of contemporary society without maintaining a bank account.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n16
  type: quote
  value: I dissent because in my view the California Supreme Court correctly interpreted the relevant constitutional language.
  qualifier: ''
  span: I dissent because in my view the California Supreme Court correctly interpreted the relevant constitutional language.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n17
  type: quote
  value: Because the recordkeeping requirements of the Act order the seizure of customers' bank records without a warrant and probable cause, I believe the Act is unconstitutional and that respondent has standing to raise that claim.
  qualifier: ''
  span: Because the recordkeeping requirements of the Act order the seizure of customers' bank records without a warrant and probable cause, I believe the Act is unconstitutional and that respondent has standing to raise that claim.
  url: https://tile.loc.gov/storage-services/service/ll/usrep/usrep425/usrep425435/usrep425435.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
- id: n18
  type: quote
  value: This third-party doctrine largely traces its roots to Miller.
  qualifier: ''
  span: This third-party doctrine largely traces its roots to Miller.
  url: https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
  read: fetched
  source_kind: primary
  outcome: verified
  checked: '2026-11-17'
---

## Opening

The Supreme Court decided *United States v. Miller* on April 21, 1976, after argument on January 12, 1976. The syllabus states the holding: "Respondent possessed no Fourth Amendment interest in the bank records that could be vindicated by a challenge to the subpoenas". Justice Powell wrote that "The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government." Justice Powell delivered the opinion of the Court, in which Chief Justice Burger and Justices Stewart, White, Blackmun, Rehnquist and Stevens joined. Justices Brennan and Marshall filed dissenting opinions, each its own.

Later cases describe this reasoning as the third-party doctrine. In Carpenter the Court wrote: "This third-party doctrine largely traces its roots to Miller." Whether a government purchase of data from a commercial broker is a Fourth Amendment search is open; the Court has not decided it, and Miller did not involve a purchase. See [[fourth-amendment-and-location-data-law]].

## What Happened / Key Facts

Case background:

- **Respondent**: Mitchell Miller, who "was convicted of possessing an unregistered still" and of other federal offenses.
- **Subpoenas**: "agents from the Treasury Department's Alcohol, Tobacco and Firearms Bureau presented grand jury subpoenas issued in blank by the clerk of the District Court, and completed by the United States Attorney's office" to the presidents of the banks where the respondent kept his accounts. "The banks did not advise respondent that the subpoenas had been served".
- **Fifth Circuit**: the Court of Appeals "reversed on the ground that a depositor's Fourth Amendment rights are violated when bank records maintained pursuant to the Bank Secrecy Act are obtained by means of a defective subpoena".
- **Supreme Court**: "Since we find that respondent had no protectable Fourth Amendment interest in the subpoenaed documents, we reverse the decision below."

The opinion of the Court:

- **Business records**: the subpoenaed documents were not the respondent's private papers; "these are the business records of the banks".
- **Information revealed to a third party**: "This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed."

Dissenting opinions, each filed separately:

- **Justice Brennan** argued that disclosure to a bank is "not entirely volitional". He relied on the California Supreme Court's reading of its own constitution: "I dissent because in my view the California Supreme Court correctly interpreted the relevant constitutional language."
- **Justice Marshall** wrote: "Because the recordkeeping requirements of the Act order the seizure of customers' bank records without a warrant and probable cause, I believe the Act is unconstitutional and that respondent has standing to raise that claim."

Carpenter v. United States (2018) partial retreat (corrected against the slip opinion; see Correction below):

- **Facts**: Prosecutors obtained court orders under the Stored Communications Act, not warrants, directing wireless carriers to disclose a robbery suspect's cell-site records. The Government obtained 12,898 location points, including 127 days of records from one carrier.
- **Holding**: "we hold that an individual maintains a legitimate expectation of privacy in the record of his physical movements as captured through CSLI". The Court's narrowest statement is that "accessing seven days of CSLI constitutes a Fourth Amendment search", and it said the Government "must generally obtain a warrant supported by probable cause before acquiring such records". Chief Justice Roberts's opinion was joined by Justices Ginsburg, Breyer, Sotomayor and Kagan; Justices Kennedy, Thomas, Alito and Gorsuch dissented.
- **Limits stated by the Court**: "Our decision today is a narrow one." The Court wrote "We do not disturb the application of Smith and Miller" and "Nor do we address other business records that might incidentally reveal location information." It said "we need not decide whether there is a limited period for which the Government may obtain an individual’s historical CSLI free from Fourth Amendment scrutiny" and expressed no view on real-time CSLI or tower dumps. Those questions are left open, not decided either way.
- **Effect**: The third-party doctrine does not govern historical cell-site records compelled from carriers; Miller and Smith are left undisturbed for the records they covered.

## Correction (2026-11-17)

See the corrections field above. Read against the Carpenter slip opinion, saved in cascade-research/documents.

## Correction (2026-11-17, second pass: the Miller opinion itself)

The decision date in the earlier text was wrong; the opinion's own date line gives April 21, 1976, and this entry's filename, date field and text now carry it. The vote figure is removed: the opinion prints no tally, and its listing names the author, the Justices who joined, and the dissenters. Its sentence on information shared with a third party carries a qualification, so the earlier wording that the principle applied regardless of the circumstances is replaced by the opinion's own words. The earlier text said the subpoenas were issued by the ATF; the opinion says ATF agents presented grand jury subpoenas issued in blank by the court clerk and completed by the United States Attorney's office. It also said Justice Brennan's dissent was joined by Justice Marshall; each filed a separate dissent. The line that the commercial data-broker industry operates in a space Miller opened, and that the government acquires from brokers what it could not obtain through primary surveillance, treated an open question as decided and is removed. Unsourced context paragraphs on ECPA, bulk metadata collection, FinCEN, the Right to Financial Privacy Act and later cases are removed pending sources; the related entries are linked below.

## Related Entries

- [[1972-06-19--keith-case-fourth-amendment-domestic-surveillance-warrant]]
- [[1978-10-25--foreign-intelligence-surveillance-act-signed]]
- [[1986-10-21--electronic-communications-privacy-act-ecpa]]
- [[1990-04-25--fincen-founded-treasury-financial-surveillance]]
- [[2018-06-22--scotus-carpenter-v-united-states-cell-site-records-are-a-fourth-amendment-search]]
