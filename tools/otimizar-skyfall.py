#!/usr/bin/env python3
"""Correção cirúrgica do loop Skyfall. Mantém gráficos, física e assets intactos."""
from pathlib import Path
p = Path("games/skyfall/game.js")
s = p.read_text(encoding="utf-8")
old = "function loop(now){let dt=clamp((now-lastFrame)/1000,.001,.10);lastFrame=now;if(running&&!paused){let n=Math.min(6,Math.max(1,Math.ceil(dt/.018)));for(let i=0;i<n;i++)step(dt/n)}updateRoadAudio();updateFlightWarnings();"
new = "function loop(now){if(document.hidden){lastFrame=now;requestAnimationFrame(loop);return;}let dt=clamp((now-lastFrame)/1000,.001,.10);lastFrame=now;if(running&&!paused){let n=Math.min(6,Math.max(1,Math.ceil(dt/.018)));for(let i=0;i<n;i++)step(dt/n)}if(running){updateRoadAudio();updateFlightWarnings();}"
if new in s:
    print("Skyfall já otimizado; sem alterações")
elif s.count(old) == 1:
    p.write_text(s.replace(old, new), encoding="utf-8")
    print("Skyfall: GPU suspensa em aba oculta e tarefas de áudio/alerta somente durante partida")
else:
    raise SystemExit("Padrão do loop original não encontrado uma única vez; nenhuma alteração realizada")
