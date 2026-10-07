# Autopsia

Ver por si mesmo. Em latim, *autopsia* é exatamente isso: testemunho direto, sem intermediários.

## Por que este projeto existe

Em 2016, a Lava Jato divulgou 52 gravações de escutas telefônicas envolvendo o ex-presidente Lula. O que chegou ao público, na maior parte das vezes, foram cortes — fragmentos escolhidos, fora do contexto, servidos com manchete pronta.

O estopim deste projeto foi pessoal: ouvi um trecho da conversa entre Lula e o prefeito Eduardo Paes e o enviei a um amigo, que o usou para declarar a inocência de Lula. Só depois descobri que o áudio estava incompleto — na íntegra, Paes liga para consolar Lula sobre um escândalo "sem fundamento" e, no meio da conversa, ironiza por que ele teria comprado um sítio e uns barcos "num lugar daquele". O corte contava outra história.

Decidi então construir um lugar onde qualquer pessoa pode ouvir os áudios **na íntegra**, navegar pelas conversas por pessoas, datas e assuntos (Triplex/OAS, Sítio de Atibaia, Odebrecht, Lava Jato, Instituto Lula, campanha, cargos no governo) e chegar às suas próprias conclusões — sem a manipulação direta da mídia.

A conclusão não é minha pra dar. A escuta é livre.

## O que tem aqui

- `index.html` — site com mapa mental interativo:
  - nós = pessoas (cor por categoria, tamanho por número de conversas)
  - arestas = conversas; clique toca o áudio; clique duplo numa pessoa toca todas as dela
  - filtros por categoria, pessoa, assunto, texto e período
- `audios/` — os 52 áudios completos (MP3)
- `data/grampos.json` / `data.js` — metadados estruturados (data, hora, participantes, papéis, assuntos, link da matéria original)
- `scrape.py`, `dl.sh`, `ids.txt` — scripts usados na coleta (fonte: matérias do [G1](https://g1.globo.com/politica/operacao-lava-jato/noticia/2016/03/confira-transcricoes-das-escutas-envolvendo-o-ex-presidente-lula.html))

## Como rodar

Abra `index.html` direto no navegador, ou sirva localmente:

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## Aviso

Os áudios são reproduções de material divulgado pela Justiça e veiculado pela Globo. Este projeto tem fim exclusivamente informativo e jornalístico. As transcrições e gravações pertencem aos seus detentores originais de direitos.
