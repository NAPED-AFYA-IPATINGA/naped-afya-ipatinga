# NAPED-06 — Derivar vitrine, meses e dados sem edição duplicada

**Prioridade:** P0 · **Estimativa:** 2–3 dias úteis · **Dependências:** NAPED-05.

## Resultado esperado

Criar uma ação aprovada em `acoes/` atualiza a vitrine, filtros, página do mês, busca e dados do painel no próximo render, sem editar menu, home ou configuração.

## Trabalho

- Usar `listing`/glob do Quarto para as ações e um único leitor de metadados para índices e métricas.
- Gerar página mensal `meses/AAAA-MM` quando existir ação publicada; separar anos pelo par ano-mês e ordenar meses cronologicamente.
- Derivar eixos dos arquivos ou de taxonomia controlada, conforme decisão NAPED-02, sem lista duplicada no painel.
- Definir ordenação por data descendente na vitrine; `ordem` apenas quando houver curadoria de mês.
- Regenerar métricas a cada build; não ativar cache/freeze que mantenha painel antigo após ação nova.
- Garantir links entre cartão, detalhe, mês e projeto quando aplicável.
- Exibir estado vazio explícito para categoria sem ação, evitando cards quebrados.

## Critérios de aceite

- Adicionar um único arquivo de teste muda todos os lugares esperados.
- Adicionar ação de 2027 cria mês próprio, sem alterar 2026; o escopo público inicial continua selecionável para 2026.
- Remover/arquivar ação retira o item dos índices e ajusta totais no build seguinte.
- Nenhum número é digitado em paralelo na home e no painel.

## Verificação

Teste de integração com duas ações em meses diferentes e uma terceira em ano futuro; conferir contagens e URLs geradas.
