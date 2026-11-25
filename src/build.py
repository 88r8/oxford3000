import json, glob, sys, os
DEST = sys.argv[1]
words = json.load(open('words.json'))
gen = {}
for f in sorted(glob.glob('out/c*_*.jsonl')):
    for l in open(f):
        l = l.strip()
        if l:
            try: o = json.loads(l); gen[o['id']] = o
            except Exception: pass
W = []
miss = 0
for e in words:
    g = gen.get(e['id'])
    if not g: miss += 1
    g = g or {}
    W.append({'i': e['id'], 'w': e['w'].replace('\u202f',' ').replace('’',"'"), 'p': ', '.join(dict.fromkeys(p for p, _ in e['pos'])), 'l': e['lvl'],
              'ipa': g.get('ipa', ''), 'ar': g.get('ar', ''), 'tr': g.get('tr', ''),
              'ex': [{'en': x['en'], 'ar': x['ar']} for x in g.get('ex', [])]})
K = []
for f in sorted(glob.glob('out/work_*.jsonl')):
    for l in open(f):
        l = l.strip()
        if l:
            try: o = json.loads(l)
            except Exception: continue
            K.append({'i': o['id'], 'w': o['w'], 'c': o['cat'], 'l': o['lvl'], 'ipa': o.get('ipa', ''), 'ar': o.get('ar', ''),
                      'tr': o.get('tr', ''), 'x': o.get('exp', ''), 'ex': [{'en': x['en'], 'ar': x['ar']} for x in o.get('ex', [])]})
K.sort(key=lambda o: o['i'])
dump = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = open('template.html').read()
html = html.replace('/*__WORDS__*/[]', dump(W)).replace('/*__WORK__*/[]', dump(K))
os.makedirs(os.path.dirname(DEST), exist_ok=True)
open(DEST, 'w').write(html)
print(f'words {len(W)} (missing data {miss}) | work {len(K)} | {os.path.getsize(DEST)/1e6:.2f} MB -> {DEST}')
