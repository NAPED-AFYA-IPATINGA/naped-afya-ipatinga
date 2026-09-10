# NAPED-08 — Home, vitrine e detalhe de uma ação

**Prioridade:** P0 · **Estimativa:** 2–4 dias úteis · **Dependências:** NAPED-06/07.

## Resultado esperado

Home apresenta o NAPED Ipatinga com fotografia autorizada, iniciativas recentes e indicadores confiáveis; a página Ações permite buscar e filtrar; o detalhe mostra contexto, atividades, resultado e evidência.

## Trabalho

- Home: título/localização/período claros, resumo institucional revisado, destaque curado, ações recentes e acesso ao acervo.
- Vitrine: cards derivados dos arquivos, busca por título/descrição, filtro por mês/eixo, ordenação, contagem e opção de limpar filtros.
- Filtros devem identificar ano e mês conjuntamente e manter uso confortável no celular; não depender exclusivamente da barra lateral da referência.
- Detalhe: título, data, eixos, objetivo, público, descrição da atividade, resultados/encaminhamentos, galeria com legendas e links autorizados.
- Definir breadcrumbs, ações relacionadas por eixo e compartilhamento com título/descrição/imagem correta quando houver.
- Implementar estado vazio e card sem foto; não preencher com foto aleatória de outra unidade.
- Indicadores da home reutilizam cálculo do painel e mostram cobertura quando dados parciais.

## Critérios de aceite

- Visitante encontra ação por palavra, mês e eixo; combinação de filtros funciona e pode ser desfeita.
- Card e detalhe mostram o mesmo título, data e imagem; foto abre em tamanho maior com texto alternativo.
- Home não mostra contagens inventadas ou dos exemplos.
- URL de uma ação pode ser compartilhada e resolve corretamente no prefixo do Pages.

## Verificação

Teste manual com ação nova, ação sem imagem e filtro sem resultado; checar navegação e metadados de compartilhamento.
