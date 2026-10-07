import re, html, json, subprocess, urllib.request, time

raw = open('/tmp/g1.html', encoding='utf-8').read()
urls = sorted(set(re.findall(r'href="(https://g1\.globo\.com/politica/operacao-lava-jato/noticia/2016/03/grampo-de-lula-[^"]+?\.html)"', raw)))
print(len(urls), 'paginas')

items = []
for u in urls:
    amp = u.replace('.html', '.amp')
    req = urllib.request.Request(amp, headers={'User-Agent':'Mozilla/5.0'})
    t = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
    vid = re.search(r'videosids=(\d+)', t)
    title = re.search(r'<title[^>]*>(.*?)</title>', t, re.S)
    # transcrição: texto após "TRANSCRI" até "Facebook"
    txt = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', t, flags=re.S)
    txt = re.sub(r'<[^>]+>', '\n', txt)
    txt = html.unescape(txt)
    m = re.search(r'TRANSCRI[ÇC][ÃA]O\n(.*?)\nFacebook', txt, re.S | re.I)
    dur = re.search(r'DURA[ÇC][ÃA]O:\s*([0-9:]+)', txt)
    items.append({
        'id': vid.group(1) if vid else None,
        'url': u,
        'titulo': html.unescape(title.group(1)).split('|')[0].strip() if title else '',
        'duracao': dur.group(1) if dur else '',
        'transcricao': re.sub(r'\n{2,}', '\n', m.group(1)).strip() if m else '',
    })
    time.sleep(0.3)

json.dump(items, open('data/raw.json','w'), ensure_ascii=False, indent=1)
sem_id = [i for i in items if not i['id']]
print('sem video id:', len(sem_id))
for i in sem_id: print(' -', i['titulo'])
print('com transcricao:', sum(1 for i in items if i['transcricao']))
