# NAPED-07 — Sistema visual responsivo e componentes

**Prioridade:** P0 · **Estimativa:** 3–5 dias úteis · **Dependências:** NAPED-03/04.

## Resultado esperado

Aplicar a direção visual aprovada em uma base compartilhada: home, páginas editoriais, listagens e painel mantêm identidade consistente em desktop e celular.

## Trabalho

- Transformar guia de marca em tokens SCSS de cor, fonte, escala, raio, sombra, espaçamento e breakpoints.
- Construir cabeçalho e menu móvel, rodapé institucional, hero, card de ação/projeto, badge de eixo, métrica com legenda, callout e galeria.
- Garantir largura de leitura, tabelas adaptativas, legendas, estados de carregamento quando aplicável e estilos de impressão.
- Definir hover/foco/ativo e `prefers-reduced-motion`; evitar autoplay intrusivo e manter navegação por teclado.
- Padronizar imagem com `object-fit`, recorte documentado, tamanhos responsivos e fallback visual.
- Não injetar textos técnicos no percurso do visitante; instruções operacionais permanecem na documentação interna do repositório.

## Critérios de aceite

- Componentes aprovados funcionam nas páginas-chave e não mudam de linguagem visual entre elas.
- Menu abre, fecha e é operável por teclado; foco sempre visível.
- Layout sem rolagem horizontal indevida em 360, 768 e 1440 px.
- Foto ausente não produz card vazio ou imagem quebrada; logo conserva proporção e área de proteção.

## Verificação

QA visual em home, ação e painel; inspeção de contraste, menu e redução de movimento.
