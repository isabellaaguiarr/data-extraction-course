# Dicionário de Dados – Salário TI Nacional 2023

| Variável | Tipo | Descrição | %  Nulos | Anomalias Encontradas |
|----------|------|-----------|---------|------------------------|
| cargo | Texto | Cargo exercido pelos profissionais de TI | 0% | Inconsistência de padronização (maiúsculas/minúsculas e variações de escrita). |
| especialidade | Texto | Área específica de atuação dentro do cargo de TI | 55.95% | Alto volume de valores nulos. |
| clt | Inteiro | Salário médio mensal para contratação CLT | 0% | Nenhuma anomalia estrutural. |
| pj | Decimal | Salário médio mensal para contratação PJ | 2.38% | Pequeno volume de valores nulos. |
| uf | Texto | Sigla da Unidade Federativa| 0% | Redundante. |
| estado | Texto | Nome completo dos estados | 0% | Redundante. |

## Observações Gerais

- A base apresenta boa integridade estrutural (sem duplicatas).
- O principal problema identificado está na variável `especialidade`, que apresenta mais de 55% de valores nulos.
- Há necessidade de padronização textual na variável `cargo`.
- As variáveis `uf` e `estado` apresentam redundância.

