# 🎮 Murilo Game Lab

Laboratório de jogos e simuladores do Murilo.

## Portal
O portal está em [index.html](./index.html). Para publicar com GitHub Pages: **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.

Após a publicação, o endereço esperado será: https://olirumtecapp-debug.github.io/murilo-game-lab/

## Jogos disponíveis no repositório

| Jogo | Pasta | Situação |
| --- | --- | --- |
| Vortex Drive V8 | [games/vortex-drive](./games/vortex-drive/) | Publicado no repositório |
| Bombs'n Roses V23 | [games/bombs-n-roses](./games/bombs-n-roses/) | Publicado no repositório |
| Tornado Simulator clássico | [games/tornado-classic](./games/tornado-classic/) | Publicado no repositório |
| Crash Garage V5.5 | [games/crash-garage](./games/crash-garage/) | Extraído dos ZIPs e integrado ao portal |
| Skyfall CXIV | [games/skyfall](./games/skyfall/) | Extraído dos ZIPs e integrado ao portal |

Os arquivos ZIP originais do Crash Garage e Skyfall foram preservados em `games/crash-garage/` como cópias de origem. O fluxo `.github/workflows/importar-jogos.yml` faz a extração automática no GitHub Actions.

**Importante:** presença dos arquivos e links no portal foi verificada; testes completos de execução gráfica dos jogos no navegador ainda estão pendentes. O GitHub Pages precisa estar ativado para abrir os links pela hospedagem pública.

## Estrutura e regras

- `index.html`: portal.
- `games/<nome>/`: um projeto por pasta.
- Ao refatorar, separar HTML, CSS, JavaScript e recursos em `assets/` sem modificar o comportamento.
- Manter uma cópia da versão original e verificar integridade antes de substituir.
- Não publicar senhas, tokens ou dados privados.
- GitHub público permite consultar o código-fonte; dividir arquivos não impede cópias.

## Próximos passos

1. Importar Crash Garage e Skyfall com todos os recursos.
2. Adicionar cartões dos dois jogos ao portal após a importação.
3. Ativar GitHub Pages nas configurações do repositório.
4. Testar cada jogo pelo endereço publicado.
