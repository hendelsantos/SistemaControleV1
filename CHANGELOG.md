# Changelog

Todas as mudanças importantes deste projeto serão documentadas aqui.

## [1.2.0] - 2025-07-05
### Adicionado
- Gráfico de barras vertical no dashboard GI semanal.
- Opção de gráfico de pizza para comparação de GI Realizado x GI Pendente.

### Alterado
- Label "GI Devido" alterado para "GI Pendente" em todas as telas, gráficos e formulários.

### Corrigido
- Removido campo "ano" do modelo GiPendenteSemana e ajustes nas views, admin e templates.


## [1.1.0] - 2025-06-22
### Adicionado
- Filtros de busca nas telas de **Demandas** e **Pedidos**.
- Possibilidade de filtrar por vários campos (ID, Solicitante, Descrição, Catálogo, Quantidade, Data, Etapa, etc).
- Layout dos filtros integrado ao Bootstrap.

### Corrigido
- Ajuste na lógica dos filtros para evitar erros de tipo.
- Melhoria na documentação e organização dos arquivos do projeto.

## [1.0.0] - 2025-06-20
### Adicionado
- Primeira versão funcional do SistemaControleV1.
- Cadastro, listagem e gerenciamento de demandas e pedidos.
- Painel administrativo via Django Admin.
- Dashboard com contadores de status das demandas.

---

> **Obs:** Siga este padrão para documentar futuras mudanças, correções ou melhorias!
