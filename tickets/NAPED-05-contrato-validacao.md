# NAPED-05 — Modelo de ação e validação antes de publicar

**Prioridade:** P0 · **Estimativa:** 2–3 dias úteis · **Dependências:** NAPED-01/04.

## Resultado esperado

O editor local copia `acoes/_modelo.qmd`, preenche metadados e texto, e recebe diagnóstico claro antes de qualquer build inválido. Uma ação é a fonte única para vitrine, mês e painel.

## Trabalho

- Definir contrato versionado para título, descrição, data, eixos, foto/texto alternativo, participantes, horas, público, cursos, local, resultado, evidências, estado e ordem.
- Adotar `acoes/AAAA-MM-slug.qmd`; validar mês/ano do nome contra `date`, data real, campos obrigatórios e valores numéricos não negativos.
- Validar eixos da taxonomia, fotos/links locais existentes, arquivo sem espaços/acentos e evidências que podem ser públicas.
- Tratar `status: rascunho` ou alternativa Quarto equivalente, impedindo indexação/publicação até aprovação.
- Mensagem de erro em português deve apontar arquivo, campo, valor recebido e correção; eixos novos intencionais podem gerar aviso, não erro, conforme política aceita.
- Cobrir ações com foto ausente, métricas parciais, dois eixos, ano futuro, nome repetido e modelo ignorado.
- Integrar validação ao `pre-render` e a comando executável antes do commit.

## Critérios de aceite

- Um arquivo válido aparece no render; um inválido interrompe publicação com mensagem útil.
- Data e nome divergentes são bloqueados; janeiro/2027 não aparece em janeiro/2026.
- `_modelo.qmd` e rascunhos não entram no site nem nas métricas.
- Arquivo que cita imagem inexistente falha antes do deploy.

## Verificação

Casos de teste significativos: ação válida, data inválida, mês divergente, foto faltante, participante textual e rascunho. Conferir que a última versão publicada permanece válida após falha de CI.
