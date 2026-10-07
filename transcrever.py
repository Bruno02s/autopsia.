import json, subprocess, os

ids = open('/tmp/narrativos.txt').read().split()
items = json.load(open('data/grampos.json'))
por_id = {g['id']: g for g in items}
os.makedirs('transcricoes_whisper', exist_ok=True)

for gid in ids:
    g = por_id[gid]
    saida = f"transcricoes_whisper/{gid}"
    if not os.path.exists(saida + '.txt'):
        r = subprocess.run(['whisper-cli','-m','modelos/ggml-small.bin','-f',g['audio'],
                            '-l','pt','-t','4','-nt','-otxt','-of',saida],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print('FALHOU', gid, r.stderr[-200:]); continue
    txt = open(saida + '.txt', encoding='utf-8').read().strip()
    g['transcricao_g1'] = g.get('transcricao','')
    g['transcricao'] = txt
    g['transcricao_whisper'] = True
    print('OK', gid, len(txt), 'chars')

json.dump(items, open('data/grampos.json','w'), ensure_ascii=False, indent=1)
open('data.js','w').write('window.GRAMPOS = ' + json.dumps(items, ensure_ascii=False) + ';\n')
print('fim')
