# Portfólio NAPED · Afya Ipatinga

Estrutura inicial do portfólio de ações e resultados do NAPED Afya Ipatinga, MG, para 2026. O site final será estático, gerado por **Quarto** e hospedado no GitHub Pages deste repositório.

**Estado atual:** páginas e navegação preparadas, sem ações ou métricas reais. A ligação automática dos arquivos de ações à vitrine, meses e painel está especificada nos tickets e ainda precisa ser implementada. A aparência é provisória até receber identidade oficial.

## No VS Code

Abra a pasta inteira deste repositório. Instale Quarto e execute:

```bash
quarto preview
quarto render
```

O resultado fica em `_site/` e não deve ser commitado. Os arquivos de conteúdo estão em `.qmd`; `_quarto.yml` concentra menu e configuração; `styles.scss` contém os tokens visuais.

## Publicação prevista

O workflow em `.github/workflows/publicar.yml` renderiza e envia `_site/` ao GitHub Pages. No GitHub, selecione **Settings → Pages → Source: GitHub Actions** antes do primeiro deploy. A URL de projeto prevista é `https://jeffersonnetto.github.io/portifolio-naped-afya-ipatinga/`. Confirme o endereço real após o workflow.

Nesta sessão local, `gh auth status` indicou autenticação inválida; não há envio ao remoto nesta entrega. A publicação fica para o ticket [NAPED-16](tickets/NAPED-16-publicacao-aceite.md).

## Próximos passos

Leia o [plano](PLANO_IMPLEMENTACAO.md), o [backlog](tickets/README.md) e a [lista de materiais](docs/MATERIAIS_NECESSARIOS.md). O [modelo de ação](acoes/_modelo.qmd) é apenas editorial, sem ligação automática com a vitrine nesta etapa.
