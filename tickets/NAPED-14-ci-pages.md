# NAPED-14 — Renderização automática e GitHub Pages

**Prioridade:** P0 · **Estimativa:** 1–2 dias úteis · **Dependências:** NAPED-04/05/06.

## Resultado esperado

Workflow gera o site estático, valida conteúdo e publica o artifact no GitHub Pages do repositório existente. A automação fica preparada nesta etapa; o envio e ativação pública dependem do momento de publicação combinado com o usuário.

## Trabalho

- Criar `.github/workflows/publicar.yml` em `main` com gatilho de push e execução manual.
- Fazer checkout, instalar versão definida de Quarto/runtime, executar validação, `quarto render`, configurar Pages, enviar `_site` e fazer deploy.
- Definir permissões mínimas `contents: read`, `pages: write`, `id-token: write`, ambiente `github-pages` e dependência build→deploy.
- Conferir `site-url`, URLs relativas, imagens, links internos, favicon e Open Graph sob o caminho do projeto.
- Documentar em README a configuração `Settings → Pages → Source: GitHub Actions`, URL real e leitura de falhas em Actions.
- Evitar secrets e arquivos restritos no repo; não incluir artifact gerado em commit.
- Escolher versões atuais dos actions conferindo [documentação oficial GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) no momento da implementação.

## Critérios de aceite

- Workflow verde para conteúdo válido; falha de validação impede deploy e preserva versão anterior.
- Artifact contém `index.html` e todos os recursos no local esperado.
- URL publicada usa o repositório existente e funciona com HTTPS.
- README permite reproduzir a configuração sem depender do repositório de referência.

## Verificação

Executar workflow em GitHub e abrir home, mês, ação e painel na URL pública; registrar execução e link do Pages.
