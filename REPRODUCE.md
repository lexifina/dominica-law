# How this repository was made (Dominica)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Laws of Dominica (Government of Dominica web portal) | <https://dominica.gov.dm/laws-of-dominica> | 2026-10-29 | No licence stated on the portal; official government publication of the laws. |
| Laws of Dominica (Government of Dominica web portal): Electronic Evidence Act, 2010 | <https://dominica.gov.dm/laws/2010/Electronic%20Evidence%20no.%2013.pdf> | 2026-10-30 | No licence stated on the portal; official government publication of the laws. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `electronic-filing-act-2013` | Electronic Filing Act, 2013 (Act 20 of 2013) | 1 | 2013-10-01 to 2013-10-01 |
| `citizenship-by-investment-regulations-2013` | Commonwealth of Dominica Citizenship by Investment Regulations, 2013 (S.R.O. 43 of 2013) | 1 | 2014-01-09 to 2014-01-09 |
| `electronic-evidence-act-2010` | Electronic Evidence Act, 2010 (Act 13 of 2010) | 1 | 2010-06-17 to 2010-06-17 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 6 tags.

## Dates

Each commit is dated at noon (America/Dominica) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Regulations with no commencement clause are dated from their publication in the Gazette https://dominica.gov.dm/laws-of-dominica

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `b722a61185c72526007a242f6f06d6d2a91c80a3ba18de641593840f6a66575c` (48882 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

3 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 3 history commits and 6 tags (history tip `6a43434de88bfa17deb299b14f34299cc19ea831`).

## Decisions made by hand

- Only recent standalone instruments with a text layer were used; the Revised Laws chapters, including the Constitution (Chapter 1:01), are scans and were skipped (no OCR).
- Electronic Filing Act 2013: in force 1 October 2013 by its section 1(2), although assented 18 November 2013 and gazetted 28 November 2013.
- Citizenship by Investment Regulations 2013: no commencement clause in the text, so dated from the Gazette date, 9 January 2014.
- Each instrument is a single "as enacted" version; amendments are separate instruments on the portal and are not applied.
- Marginal notes of the printed text appear inside the section text where the PDF text layer places them.
- Electronic Evidence Act, 2010 (Act 13 of 2010): the evidence statute available as text; the Evidence Act (Chapter 4:60 of the 1990 Revised Laws) is a scan without a text layer and is not used. The Act has no commencement clause, so it is dated from its publication in the Gazette, 17 June 2010 (assent 10 June 2010). One version, the Act as enacted, credited to Act 13 of 2010. Section headings come from the arrangement of sections; margin notes, running heads and the margin citation "Cap. 64." are left out of the text.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
