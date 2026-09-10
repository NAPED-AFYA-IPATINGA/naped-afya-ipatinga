# NAPED-15 — QA funcional, acessibilidade, performance e conteúdo

**Prioridade:** P0 · **Estimativa:** 2–3 dias úteis · **Dependências:** NAPED-07 a 14.

## Resultado esperado

Revisão integrada do site gerado e do caminho de atualização, com falhas corrigidas antes de abrir o lançamento público.

## Trabalho

- Funcional: abrir todos os itens de menu, filtro/busca, página de ação, mês, projeto e evidência; testar estado vazio.
- Conteúdo: comparar dados publicados com inventário aprovado, examinar grafia de nomes, datas, direitos e números; checar nenhuma foto/ação de outra unidade.
- Acessibilidade: estrutura de headings, texto alternativo, foco visível, menu e filtros por teclado, contraste, tabela legível, movimento reduzido.
- Responsividade: 360, 390, 768, 1024 e 1440 px; ausência de corte de foto essencial ou rolagem horizontal acidental.
- Performance: imagens otimizadas, dimensões declaradas, carregamento adiado fora da dobra, CSS/JS pequeno; registrar medidas antes/depois de correções.
- SEO/social: título, descrição, idioma, canonical/site-url e prévia de compartilhamento representam NAPED Ipatinga.
- Validação/CI: adicionar arquivo de teste inválido em ambiente seguro e comprovar falha compreensível; retirar teste depois.
- Verificar caminhos no domínio `jeffersonnetto.github.io` com prefixo do repositório.

## Critérios de aceite

- Sem links ou imagens quebrados em páginas publicáveis.
- Fluxos principais funcionam em mobile e teclado.
- Métricas derivadas e cobertura concordam com ações reais.
- Erros bloqueantes resolvidos; limitações menores registradas com dono e prioridade.

## Verificação

Checklist executado sobre `_site` e URL do Pages; capturas das páginas-chave e log das correções.
