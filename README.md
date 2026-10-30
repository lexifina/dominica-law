# Dominica: law history in git

A first, small build of the law of Dominica as a git history: one file per section, one commit per law on the day it took effect, and the law that made the change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `dm/`.

Language: English (the official language).

## What is in it now

| Folder | Instrument | Versions | In force |
| --- | --- | ---: | --- |
| `electronic-evidence-act-2010/` | Electronic Evidence Act, 2010 (Act 13 of 2010): the evidence statute available as text | 1 | 17 June 2010 (Gazette date; the Act has no commencement clause); assented 10 June 2010 |
| `electronic-filing-act-2013/` | Electronic Filing Act, 2013 (Act 20 of 2013) | 1 | 1 October 2013 (section 1(2)); assented 18 November 2013, gazetted 28 November 2013 |
| `citizenship-by-investment-regulations-2013/` | Commonwealth of Dominica Citizenship by Investment Regulations, 2013 (S.R.O. 43 of 2013) | 1 | 9 January 2014 (Gazette date; the regulations have no commencement clause) |

Each is the text as published by the Government of Dominica. The portal publishes Acts and Statutory Rules and Orders as passed, not consolidated, so each instrument has one version: the oldest version available.

## What it does not show

- **The Constitution and the Revised Laws of Dominica.** The portal's Revised Laws chapters (including the Constitution Order, Chapter 1:01) are scanned images without a text layer. No OCR was used, so they are not in this record.
- **The core codes and statutes.** The criminal, criminal procedure, evidence, labour and interpretation statutes are Revised Laws chapters, which are scans without a text layer, and no complete text-layer copy of the Companies Act 1994 was found, so they are not in this record.
- **Amendments and the other Acts.** Later amending instruments are separate documents on the portal and are not applied. The Constitution of Dominica (Amendment) Act 2014 is published, but the Order that brought it into operation could not be read, so it is left out.
- **Marginal notes** of the printed text appear inside the section text where the PDF's text layer places them.

## Dates and authors

Each commit is dated at noon, America/Dominica, on the in-force day. The author is the law that made the change, with an address that cannot exist (for example `act-20-2013@dominica.gov.dm.invalid`). The first commit of each instrument is the instrument as published.

## Sources

| Source | Kind | Notes |
| --- | --- | --- |
| [Laws of Dominica](https://dominica.gov.dm/laws-of-dominica) | Official legislation (Government of the Commonwealth of Dominica) | Used: PDFs of the three instruments, retrieved 29 and 30 October 2026 |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The laws are official publications of the Government of Dominica; the portal states no reuse licence. See `LICENSE`. This repository is not legal advice and not an official publication. No AI model wrote or changed legal text.
