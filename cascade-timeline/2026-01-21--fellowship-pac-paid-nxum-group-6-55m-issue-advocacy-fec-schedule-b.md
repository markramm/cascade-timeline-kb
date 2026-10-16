---
type: timeline_event
id: 2026-01-21--fellowship-pac-paid-nxum-group-6-55m-issue-advocacy-fec-schedule-b
date: '2026-01-21'
title: 'FEC Filings Show Fellowship PAC Paid Nxum Group LLC $6.55 Million in Five Disbursements, Jan. 21 to Apr. 9, 2026, Reported as Advertising'
importance: 5
status: confirmed
event_date_claim: c1
tags:
  - crypto-finance
  - fec
  - super-pac
  - nxum
actors:
  - Fellowship PAC
  - Nxum
sources:
  - title: "FEC bulk operating-expenditures file oppexp26 (Schedule B line 21B rows, committee C00915181, payee NXUM GROUP LLC)"
    url: "https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip"
    publisher: "Federal Election Commission"
    date: '2026-10-11'
    tier: 1
  - title: "FEC bulk committee master file cm26 (C00915181, FELLOWSHIP PAC)"
    url: "https://www.fec.gov/files/bulk-downloads/2026/cm26.zip"
    publisher: "Federal Election Commission"
    date: '2026-10-15'
    tier: 1
claims:
- id: c1
  type: date
  value: 01/21/2026
  qualifier: first disbursement date (transaction date) in the Q1 2026 report, file 1963591
  span: "C00915181|N|2026|Q1|202604159857299556|21B|F3X|SB|NXUM GROUP LLC|DOVER|DE|19901|01/21/2026|1000000||ISSUE ADVOCACY ADVERTISING|004|Advertising Expenses"
  url: https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip
  read: fetched
  source_kind: primary
- id: c2
  type: figure
  value: '2000000'
  qualifier: disbursement dated 01/26/2026, purpose "ISSUE ADVOCACY ADVERTISING" (Q1 report)
  span: "C00915181|N|2026|Q1|202604159857299557|21B|F3X|SB|NXUM GROUP LLC|DOVER|DE|19901|01/26/2026|2000000||ISSUE ADVOCACY ADVERTISING|004"
  url: https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip
  read: fetched
  source_kind: primary
- id: c3
  type: figure
  value: '2000000 and 300000'
  qualifier: two disbursements dated 04/07/2026 (purposes "ISSUE ADVOCACY ADVERTISING" and "ADVERTISING"), May monthly report, file 1977948
  span: "C00915181|N|2026|M5|202605209870111852|21B|F3X|SB|NXUM GROUP LLC|DOVER|DE|19901|04/07/2026|2000000||ISSUE ADVOCACY ADVERTISING ... 04/07/2026|300000||ADVERTISING"
  url: https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip
  read: fetched
  source_kind: primary
- id: c4
  type: figure
  value: '1250000'
  qualifier: disbursement dated 04/09/2026, purpose "PRE-PAYMENT ADVERTISING"
  span: "C00915181|N|2026|M5|202605209870111853|21B|F3X|SB|NXUM GROUP LLC|DOVER|DE|19901|04/09/2026|1250000||PRE-PAYMENT ADVERTISING|004"
  url: https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip
  read: fetched
  source_kind: primary
- id: c5
  type: figure
  value: '6550000'
  qualifier: sum of the five rows (1,000,000 + 2,000,000 + 2,000,000 + 300,000 + 1,250,000), computed by the researcher, not a filed total
  span: "five rows, payee NXUM GROUP LLC, DOVER DE 19901, committee C00915181"
  url: https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip
  read: fetched
  source_kind: primary
---

FEC bulk operating-expenditure data (Schedule B, line 21B) lists five disbursements from Fellowship PAC (committee C00915181, a committee registered with the FEC as a PAC, treasurer Mitchell Nobel) to NXUM GROUP LLC of Dover, Delaware. Amounts and transaction dates: $1,000,000 (Jan. 21, 2026), $2,000,000 (Jan. 26), $2,000,000 (Apr. 7), $300,000 (Apr. 7) and $1,250,000 (Apr. 9). They total $6,550,000, matching the figure a secondary relay gave. The January rows are in the Q1 2026 report (file 1963591); the April rows are in the May monthly report (file 1977948). Stated purposes are "issue advocacy advertising" for three rows, "advertising" for one and "pre-payment advertising" for one; all carry FEC category 004, Advertising Expenses. All five rows are original filings (amendment indicator N). Nxum is the only payee above $20,000 among the committee's ten operating-expenditure rows in the 2026 file (the other five rows total about $46,600: compliance consulting, legal, a legal-research subscription). The 2024-cycle file holds no rows for the committee.

What the filings do not show: who Nxum's principals are, what Nxum did with the money, or any link to the Tether payments described in [[2026-10-14--wsj-nxum-hines-one-third-stake-tether-payments-genius-act]]. The Nxum named in that reporting and the Nxum Group LLC of Dover, DE in these rows share a name only; this entry does not establish they are the same entity. Data are from the bulk file downloaded Oct. 15, 2026 (file dated Oct. 11); later reports may add rows. The FEC document-query pages returned 403 and the OpenFEC API was rate-limited to the shared demo key, so the images were not viewed.
