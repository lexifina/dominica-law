"""Dominica: Electronic Evidence Act, 2010 (Act 13 of 2010) as corpus.d/30-electronic-evidence-act-2010.json, from the
Government of Dominica PDF (text layer). Deterministic; reads .cache2/pdf/eevidence-2010.pdf only. Verifies every unit
against the PDF text (all characters of the body, whitespace aside, in order, minus running heads and margin notes)."""
import hashlib, json, os, re, subprocess
from pathlib import Path

H = Path(__file__).parent
PDF = H / '.cache2' / 'pdf' / 'eevidence-2010.pdf'
URL = 'https://dominica.gov.dm/laws/2010/Electronic%20Evidence%20no.%2013.pdf'
sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
raw = subprocess.run(['pdftotext', '-enc', 'UTF-8', str(PDF), '-'], capture_output=True, check=True).stdout.decode('utf8')
pages = raw.split('\f')
lines = [l.strip() for l in '\n'.join(pages[2:]).split('\n')]

def clean(t):
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('–', '-'), ('—', '-'), (' ', ' ')):
        t = t.replace(a, b)
    return re.sub(r' {2,}', ' ', t).strip()

# section headings from the arrangement of sections (page 1)
arr = pages[0].split('SECTION', 1)[1]
TOC = {int(n): h.strip() for n, h in re.findall(r'(\d+)\. (.+?)\.(?=\s+\d+\. |\s*$)', ' '.join(arr.split()))}
assert sorted(TOC) == list(range(1, 15)), TOC
NOTES = sorted({h + '.' for h in TOC.values()}, key=len, reverse=True)
RUNNING = {'2010', 'ELECTRONIC EVIDENCE', 'ACT 13'}

start = next(i for i, l in enumerate(lines) if l.startswith('1. This Act may be cited'))
stop = next(i for i, l in enumerate(lines) if l.startswith('Passed in the House of Assembly'))
body, dropped = [], []
for l in lines[start:stop]:
    if not l or re.fullmatch(r'\d{3}', l) or l in RUNNING:
        dropped.append(l); continue
    t = l
    for note in NOTES:  # margin notes, alone on a line or run into the text
        if t == note:
            break
        t = t.replace(' ' + note + ' ', ' ')
    else:
        if t in ('Proof by affidavit. Cross Examination.', 'Repeal. Cap. 64.'):
            dropped.append(l); continue
        body.append((l, t)); continue
    dropped.append(l)

units, cur = {}, None
for l, t in body:
    m = re.match(r'^(\d+)\. (.*)$', t)
    if m and int(m.group(1)) == (cur or 0) + 1:
        cur = int(m.group(1))
        units[cur] = [m.group(2)]
    else:
        units[cur].append(t)
assert sorted(units) == list(range(1, 15)), sorted(units)
out = {}
for n, ps in units.items():
    out['sec-%03d' % n] = {'label': 'Section %d' % n, 'kind': 'section',
                           'text': '# %d. %s\n' % (n, clean(TOC[n])) + ''.join(clean(p) + '\n' for p in ps)}

# verification
src = re.sub(r'\s+', '', clean(''.join(t for _, t in body)))
uni = re.sub(r'\s+', '', clean(''.join('%d. ' % n + ''.join(ps) for n, ps in units.items())))
assert src == uni
removed = sum(len(l) - len(t) for l, t in body)
print(len(out), 'units; verified', len(src), 'chars; dropped lines:', sorted(set(dropped) - {''}), '; inline note chars removed:', removed)

LAW = 'act-13-2010'
part = {
    'laws': {LAW: {'label': 'Act 13 of 2010', 'title': 'Electronic Evidence Act, 2010', 'kind': 'law', 'enacted': '2010-06-10',
                   'published': '2010-06-17', 'url': URL, 'temporary_until': None, 'restores': None, 'note': None}},
    'acts': [{'slug': 'electronic-evidence-act-2010', 'short': 'Electronic Evidence Act',
              'title': 'Electronic Evidence Act, 2010 (Act 13 of 2010)', 'url': URL, 'first_law': LAW, 'earlier_laws': [],
              'versions': [{'from': '2010-06-17', 'source_url': URL, 'sha256': sha, 'units': out,
                            'credits': {k: [LAW] for k in out}}]}],
    'sources': [{'name': 'Laws of Dominica (Government of Dominica web portal): Electronic Evidence Act, 2010', 'url': URL,
                 'retrieved': '2026-10-30', 'licence': 'No licence stated on the portal; official government publication of the laws.',
                 'notes': f'Act as passed, PDF with a text layer (sha256 {sha}), copy archived by Common Crawl.'}],
    'decisions': ['Electronic Evidence Act, 2010 (Act 13 of 2010): the evidence statute available as text; the Evidence Act '
                  '(Chapter 4:60 of the 1990 Revised Laws) is a scan without a text layer and is not used. The Act has no '
                  'commencement clause, so it is dated from its publication in the Gazette, 17 June 2010 (assent 10 June 2010). '
                  'One version, the Act as enacted, credited to Act 13 of 2010. Section headings come from the arrangement of '
                  'sections; margin notes, running heads and the margin citation "Cap. 64." are left out of the text.'],
}
p = H / 'corpus.d' / '30-electronic-evidence-act-2010.json'
p.parent.mkdir(exist_ok=True)
tmp = p.with_suffix('.tmp')
tmp.write_text(json.dumps(part, ensure_ascii=False, indent=1) + '\n', encoding='utf8', newline='\n')
os.replace(tmp, p)
