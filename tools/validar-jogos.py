#!/usr/bin/env python3
"""Extrai JS inline para verificação sintática sem modificar os jogos."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import tempfile

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture = False
        self.parts = []
        self.current = []
        self.kind = ""
    def handle_starttag(self, tag, attrs):
        if tag == "script":
            a = dict(attrs)
            self.capture = "src" not in a
            self.kind = "module" if a.get("type") == "module" else "classic"
            self.current = []
    def handle_data(self, data):
        if self.capture:
            self.current.append(data)
    def handle_endtag(self, tag):
        if tag == "script" and self.capture:
            self.parts.append((self.kind, "".join(self.current)))
            self.capture = False

paths = [
    Path("games/crash-garage/index.html"),
    Path("games/skyfall/index.html"),
    Path("games/vortex-drive/index.html"),
    Path("games/tornado-classic/index.html"),
    Path("games/bombs-n-roses/index.html"),
]
with tempfile.TemporaryDirectory() as folder:
    for html in paths:
        parser = Scripts()
        parser.feed(html.read_text(encoding="utf-8"))
        for index, (kind, content) in enumerate(parser.parts):
            if not content.strip():
                continue
            suffix = ".mjs" if kind == "module" else ".js"
            tmp = Path(folder) / (html.parent.name + "-" + str(index) + suffix)
            tmp.write_text(content, encoding="utf-8")
            subprocess.run(["node", "--check", str(tmp)], check=True)
            print("Sintaxe OK:", html, "script", index, kind)
    for path in [Path("games/skyfall/game.js"), Path("games/skyfall/detailed-road-assets.js")]:
        subprocess.run(["node", "--check", str(path)], check=True)
        print("Sintaxe OK:", path)
    for path in [
        Path("games/crash-garage/vehicles-a.js"),
        Path("games/crash-garage/vehicles-b.js"),
        Path("games/crash-garage/vehicles-c.js"),
    ]:
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit("Dependência ausente: " + str(path))
        print("Recurso presente:", path)
