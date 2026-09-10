# Backlog — Portfólio NAPED Afya Ipatinga

O [plano de implementação](../PLANO_IMPLEMENTACAO.md) reúne decisões, arquitetura e critérios gerais. Estes arquivos são tickets executáveis. **P0** bloqueia a entrega; **P1** integra a primeira versão; **P2** é refinamento desejável. Estimativas em dias úteis são aproximações de trabalho técnico, sem contar espera por materiais e aceite editorial.

| ID | Ticket | Prioridade | Estimativa | Dependências |
| --- | --- | --- | --- | --- |
| NAPED-01 | [Inventário e governança do conteúdo](NAPED-01-inventario-conteudo.md) | P0 | 1–2 d | Materiais do usuário |
| NAPED-02 | [Mapa do site e taxonomia](NAPED-02-arquitetura-informacao.md) | P0 | 1–2 d | 01 |
| NAPED-03 | [Direção visual e protótipo](NAPED-03-design-premium.md) | P0 | 2–4 d | 01, 02, guia |
| NAPED-04 | [Fundação Quarto](NAPED-04-fundacao-quarto.md) | P0 | 1–2 d | 02 |
| NAPED-05 | [Modelo e validação de ações](NAPED-05-contrato-validacao.md) | P0 | 2–3 d | 01, 04 |
| NAPED-06 | [Índices e derivados automáticos](NAPED-06-geracao-automatica.md) | P0 | 2–3 d | 05 |
| NAPED-07 | [Sistema visual responsivo](NAPED-07-componentes-visuais.md) | P0 | 3–5 d | 03, 04 |
| NAPED-08 | [Vitrine e detalhe da ação](NAPED-08-vitrine-acoes.md) | P0 | 2–4 d | 06, 07 |
| NAPED-09 | [Meses e projetos](NAPED-09-meses-projetos.md) | P1 | 2–3 d | 02, 06, 07 |
| NAPED-10 | [Equipe, sobre e comprovações](NAPED-10-institucional-evidencias.md) | P1 | 2–3 d | 01, 07 |
| NAPED-11 | [Painel e recortes semestrais](NAPED-11-resultados.md) | P0 | 3–4 d | 05–07 |
| NAPED-12 | [Conteúdo 2026 e acervo](NAPED-12-conteudo-2026.md) | P0 | 2–5 d | 01, 05, materiais |
| NAPED-13 | [Documentação editorial adaptada](NAPED-13-documentacao-editorial.md) | P1 | 2–3 d | 05, 06, 14 |
| NAPED-14 | [Workflow e GitHub Pages](NAPED-14-ci-pages.md) | P0 | 1–2 d | 04–06 |
| NAPED-15 | [QA, acessibilidade e performance](NAPED-15-qa.md) | P0 | 2–3 d | 07–14 |
| NAPED-16 | [Publicação e aceite](NAPED-16-publicacao-aceite.md) | P0 | 1–2 d | 15, acesso GitHub |

Cada ticket pode ser convertido em issue do GitHub depois que o escopo e os arquivos forem aprovados. Os Markdown locais são a fonte de planejamento nesta etapa.

**Execução atual (15/09/2026):** a estrutura de páginas, modelos editoriais, SCSS provisório, README e workflow inicial já foram criados localmente. Isso adianta parte de NAPED-04, 07, 09, 10, 11, 13 e 14, mas **não conclui seus critérios de aceite**. NAPED-05/06 (validação e automação de acervo), NAPED-12 (material real), QA de renderização e publicação no Pages continuam pendentes. Os arquivos locais não foram enviados ao remoto nesta etapa.
