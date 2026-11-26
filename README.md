# Dominica: law history in git

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Dominica law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

The law of Dominica as a git history: one file per section, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to a section; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Dominica's national law, which global-law reads at `dominica/national/acts/`.

**What is in it now:** [`constitution/`](constitution/) holds the Constitution, one file per section, as printed in the Revised Laws of 1990 (amended to 1984); [`acts/`](acts/) the Acts of Parliament as passed and [`subsidiary/`](subsidiary/) the statutory rules and orders as made, from the Government's Laws of Dominica portal, one file per section, being added as they are read (the Children (Care and Adoption) Act 2023, the Domestic Violence Act 2023 and the Bail Act 2020 among them). The first three instruments stay in their own folders at the top. Instruments with no text layer are held back (see [`REPRODUCE.md`](REPRODUCE.md)).

Each instrument has its own folder: `acts/domestic-violence-act-2023/section-003.md` is section 3 of the Domestic Violence Act 2023, and `constitution/section-001.md` the Constitution's first section.

The text is in English, the official language, as the text layer of the Government's PDFs gives it; page headers and page numbers are removed. **The Constitution is the exception:** the Government's copy is a page scan, so its text is WIPO Lex's machine reading of the printed pages, as WIPO Lex serves it; no OCR is run here, and its commit says so in a `Text-source:` trailer.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to the Schedule of the Citizenship by Investment Regulations | `git log -p --word-diff -- citizenship-by-investment-regulations-2013/schedule.md` |
| Which law wrote each line of the Schedule? | `git blame citizenship-by-investment-regulations-2013/schedule.md` |
| Every version of the Regulations, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- citizenship-by-investment-regulations-2013 ':!*/README.md'` |
| The Schedule as in force on 1 January 2020 | `python tools/on.py 2020-01-01 citizenship-by-investment-regulations-2013 schedule` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Dominican law](https://global-law.lexifina.com/v1/try_claude?country=dominica)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=dominica)**: the same question in ChatGPT.
- **[Search Dominican law on our site](https://lexifina.com/law?country=dominica&q=citizenship+by+investment)**: a search for "citizenship by investment", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=citizenship+by+investment&jurisdiction=dominica)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add dominica/national/acts
python3 tools/law.py show 2026-01-01 dominica/national/acts/citizenship-by-investment-regulations-2013/schedule.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Dominica, on the day the instrument took effect, and carries it in its `In-force:` trailer, with the reason in `In-force-basis:`:

- the day the instrument's own commencement clause gives (the Electronic Filing Act: 1 October 2013, by section 1(2), although it was assented to on 18 November and gazetted on 28 November 2013);
- where it has none, the day it was published in the Gazette, then the day of assent, then the day it was made; where the text gives none of these, 31 December of its year, as a placeholder;
- the Constitution: 1 January 1991, the date of the Revised Laws pages it is printed on, as a placeholder; its text is as amended to 1984.

Each instrument is credited to itself, as enacted (`Act 20 of 2013 <act-2013-20@dominica.gov.dm.invalid>`, an address that cannot exist); the Constitution to the `Revised Laws of Dominica 1990`. Commits are appended in the order they are read, so `git log` is not in date order; ask for a date with `tools/on.py`.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and compares it with the corpus it was built from: 3 versions of 3 acts, 0 mismatches.
- Every commit's trailers parse; there are no merge commits, no commit dates that go backwards and none after the build.
- A second build from the same corpus gave identical hashes for all 3 law commits and 6 tags. The results, the corpus's sha256 and the builder's hashes are in [`REPRODUCE.md`](REPRODUCE.md).
- [vulnerabilities/](vulnerabilities/): possible drafting mistakes in this law, found by global-law's detectors and checked by hand. Not run yet.

## What it does not show

- **The Revised Laws of Dominica.** The portal's Revised Laws chapters (the criminal, evidence, labour and interpretation statutes among them) are scans without a text layer; no OCR was used, so they are not here. Only the Constitution is, from WIPO Lex's reading of the same pages.
- **Instruments without a text layer, and case law.** Older Acts and statutory rules and orders that are page scans are held back. Judgments are kept in a separate private repository.
- **Amendments.** The portal publishes each instrument as passed, not consolidated; later amending instruments are not applied, so this is not the text in force today.
- **The printed layout.** Marginal notes appear inside the section text where the PDF's text layer places them, and some words run together as it gives them.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Laws of Dominica](https://dominica.gov.dm/laws-of-dominica) (Government of the Commonwealth of Dominica) | Official legislation portal | no: Acts and statutory rules and orders as passed, not consolidated | PDFs with a text layer, retrieved 29 and 30 October and from 26 November 2026, one request every 30 seconds (the site's Crawl-delay) |
| [WIPO Lex](https://www.wipo.int/wipolex/en/text/492279) | The Constitution, as printed in the Revised Laws 1990 (WIPO Lex's machine-read text) | no | Retrieved 26 November 2026 |

## Licence

See [`LICENSE`](LICENSE). The laws are official publications of the Government of the Commonwealth of Dominica, whose portal states no reuse licence; the wording of the law is not changed. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote or changed legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## Visualisations

- [visualisations/](visualisations/): charts drawn from this repository. Not drawn yet.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
