# NAPED-04 — Fundação Quarto no repositório existente

**Prioridade:** P0 · **Estimativa:** 1–2 dias úteis · **Dependências:** NAPED-02.

## Resultado esperado

Projeto Quarto mínimo, renderizável para `_site`, no repositório [de destino](https://github.com/JeffersonNetto/portifolio-naped-afya-ipatinga). Sem copiar código ou conteúdo de outra unidade como se fosse material próprio.

## Trabalho

- Criar `_quarto.yml`, `.gitignore`, diretórios, páginas-base e README com execução em editor local.
- Configurar `site-url`, idioma `pt-BR`, navegação, busca, recursos e renderização de `acoes/*.qmd` e páginas permanentes.
- Configurar caminhos internos sob `/portifolio-naped-afya-ipatinga/`; evitar imagens com `/fotos/...` absoluto que apontem à raiz do domínio.
- Fixar versões de Quarto/runtime no workflow e documentar pré-requisitos para preview local.
- Ignorar `_site`, caches e arquivo `_modelo.qmd` nos índices/contagens; definir convenção de nomes em minúsculas, sem acentos.
- Preparar páginas geradas por mês sem assumir 2026 na lógica, embora o lançamento mostre apenas 2026.

## Critérios de aceite

- `quarto render` gera home e páginas-base sem erro no ambiente configurado.
- Todas as URLs e recursos funcionam como site de projeto GitHub Pages.
- O README explica execução local, estrutura e comandos de render/preview.
- A árvore não contém dados nem imagens da referência de São João del-Rei.

## Verificação

Render local ou em CI e inspeção dos links gerados em `_site`.
