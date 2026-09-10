# NAPED-13 — Documentação editorial adaptada a VS Code

**Prioridade:** P1 · **Estimativa:** 2–3 dias úteis · **Dependências:** NAPED-05/06/14.

## Resultado esperado

A documentação interna explica à equipe de Ipatinga como cadastrar ações pelo **VS Code local** e como o projeto é montado e mantido. Ela acompanha o fluxo real do repositório.

## Trabalho

- Documentar: abrir pasta do repo no VS Code, atualizar `main`, copiar `_modelo.qmd`, adicionar/otimizar fotos, preencher campos, executar validação e preview, revisar, commit/push e acompanhar Actions.
- Explicar campos e taxonomia com exemplos **sintéticos** claramente identificados, sem sugerir que ocorreram em Ipatinga.
- Documentar mensagens de erro comuns: data/nome divergentes, foto faltante, YAML inválido, métrica textual, categoria errada e build vermelho.
- Explicar como corrigir/retirar uma ação, abrir um mês novo e inserir projeto/evidência; mudanças de menu permanecem tarefa de implementação.
- Documentar arquitetura Quarto, diretórios, scripts, decisão sobre métricas e publicação GitHub Pages; incluir passos de desenvolvimento em VS Code.
- Manter a documentação em Markdown no repositório, sem página pública correspondente.
- Atualizar os exemplos sempre que o contrato ou workflow mudar.

## Critérios de aceite

- Um editor que não criou o projeto consegue adicionar uma ação válida seguindo a documentação.
- Comando, pastas, campos e telas descritos correspondem ao repo implementado.
- A documentação não depende de Positron e não reproduz conteúdos da outra unidade.
- Qualquer exemplo fictício está rotulado como tal.

## Verificação

Ensaio com uma ação de teste no VS Code, sem instrução oral; corrigir trechos ambíguos.
