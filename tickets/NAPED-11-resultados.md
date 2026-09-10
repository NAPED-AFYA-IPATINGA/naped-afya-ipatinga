# NAPED-11 — Painel de resultados e Em Números 2026

**Prioridade:** P0 · **Estimativa:** 3–4 dias úteis · **Dependências:** NAPED-05/06/07.

## Resultado esperado

Painel automático e recortes 2026.1/2026.2 apresentam dados reais, com cobertura e limites claros. Os arquivos e visual podem estar prontos agora; valores só aparecem quando houver ações aprovadas.

## Trabalho

- Reutilizar o leitor de ações para volume mensal, eixos, meses cobertos, participantes, horas, públicos/cursos e tabela consultável.
- Excluir rascunhos, `_modelo.qmd` e páginas permanentes das contagens.
- Mostrar `X de Y ações com participantes/horas`; esconder ou explicar blocos sem dados. Não chamar soma de presenças de “pessoas únicas”.
- Explicar que ação com dois eixos pode contar duas vezes no gráfico temático.
- Separar recortes semestrais pela data do evento, preservando a mesma regra do painel; páginas Em Números podem adicionar narrativa/evidências aprovadas.
- Definir como tratar horas com o usuário (carga horária de formação ou outra unidade) antes de publicar esse indicador.
- Construir tabela acessível com busca/ordenação, que funcione no celular sem dependência pesada desnecessária.
- Não usar cache de execução que deixe painel antigo após adicionar uma ação.

## Critérios de aceite

- Painel, home, meses e Em Números concordam nos totais e período.
- Sem ações, os estados vazios não exibem `0 pessoas` como resultado institucional.
- Com dado parcial, denominador e regra de soma aparecem junto ao indicador.
- Uma ação acrescentada altera painel no build seguinte, sem edição manual.

## Verificação

Teste com três ações: uma sem métricas, uma com métricas e uma com dois eixos; conferir totais e explicações.
