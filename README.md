# 🎮 Murilo Game Lab

Laboratório de jogos e simuladores do Murilo.

## Portal
O portal está em [index.html](./index.html). Para publicar com GitHub Pages: **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.

Após a publicação, o endereço esperado será: https://olirumtecapp-debug.github.io/murilo-game-lab/

## Jogos publicados no repositório

| Jogo | Pasta | Estado |
| --- | --- | --- |
| Vortex Drive V8 | [games/vortex-drive](./games/vortex-drive/) | HTML original publicado; validação gráfica no navegador pendente |
| Bombs'n Roses V23 | [games/bombs-n-roses](./games/bombs-n-roses/) | HTML publicado; validação no navegador pendente |
| Tornado Simulator clássico | [games/tornado-classic](./games/tornado-classic/) | HTML publicado; validação no navegador pendente |

## Jogos recebidos, ainda não importados

- **Crash Garage V5.5** — arquivo HTML de aproximadamente 62,6 MB, com modelos 3D incorporados e dependência externa de Three.js.
- **Skyfall CXIV** — arquivo HTML de aproximadamente 23,4 MB, com imagens incorporadas.

**Atenção:** os dois jogos acima não estão disponíveis nos botões do portal até a importação e a verificação. O GitHub possui limites para uploads por determinadas APIs; não vamos substituir os arquivos originais por versões incompletas.

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
