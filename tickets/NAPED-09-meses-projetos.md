# NAPED-09 — Navegação por meses e páginas de projetos

**Prioridade:** P1 · **Estimativa:** 2–3 dias úteis · **Dependências:** NAPED-02/06/07.

## Resultado esperado

Meses organiza o acervo de 2026 e cria automaticamente páginas para meses com ações. Projetos oferece páginas permanentes para iniciativas **de Ipatinga**, com estrutura pronta agora e conteúdo editorial depois.

## Trabalho

- Construir grade de meses com contagem derivada; páginas `meses/AAAA-MM` incluem ano explícito, resumo e ações vinculadas.
- Criar tratamento para nenhum mês cadastrado: orientação curta, sem inventar cronograma.
- Preparar página Projetos com cards e modelo de página individual: finalidade, público, atividades, resultados, registros relacionados e evidências.
- Definir relação opcional `projeto` no cabeçalho da ação, para uma ação entrar na página de programa sem cópia manual.
- Exibir somente projetos aprovados no menu público; enquanto materiais não chegam, entregar arquivos-molde com marcação editorial “conteúdo a preencher”.
- Testar inclusão de novo mês/ano sem editar menu ou páginas antigas.

## Critérios de aceite

- Meses não mistura 2026 e 2027; contador da grade bate com ações publicadas.
- Projeto usa somente material local aprovado; arquivo-molde não se apresenta como fato.
- O visitante retorna do mês/projeto para vitrine e detalhe facilmente.

## Verificação

Criar ações de teste em meses distintos, renderizar e inspecionar navegação; excluir dados de teste antes do lançamento.
