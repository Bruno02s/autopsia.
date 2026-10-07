#!/bin/sh
dl_one() {
  id="$1"; out="$2"
  [ -s "$out" ] && return 0
  /home/bruno/Documents/Projects/Investigacao/.venv/bin/yt-dlp -x --audio-format mp3 --audio-quality 5 -o "$out" "https://globoplay.globo.com/v/$id/" --no-progress -q && echo "OK $out" || echo "FALHOU $id"
}
export -f dl_one 2>/dev/null || true
cat /home/bruno/Documents/Projects/Investigacao/ids.txt | xargs -P 4 -n 2 sh -c 'dl_one "$0" "$1"' 
