# Dicionário de Dados – Salário TI Nacional 2023

| Variável | Tipo | Descrição | % Nulos | Anomalias Encontradas |
|----------|------|-----------|---------|------------------------|
| cargo | Texto | Cargo exercido pelo profissional de TI | 0% | Inconsistência de padronização textual (maiúsculas/minúsculas e variações de escrita). |
| especialidade | Texto | Área específica de atuação dentro do cargo de TI | 55.95% | Alto volume de valores nulos, comprometendo análise segmentada. |
| clt | Inteiro | Salário médio mensal para contratação CLT (em reais) | 0% | Nenhuma anomalia estrutural identificada. |
| pj | Decimal | Salário médio mensal para contratação PJ (em reais) | 2.38% | Pequeno volume de valores nulos. |
| uf | Texto | Sigla da Unidade Federativa (UF) | 0% | Necessário validar padronização de siglas. |
| estado | Texto | Nome completo do estado correspondente à UF | 0% | Nenhuma anomalia aparente, mas redundância com a variável UF. |

## Observações Gerais

- A base apresenta boa integridade estrutural (sem duplicatas).
- O principal problema identificado está na variável `especialidade`, que apresenta mais de 55% de valores ausentes.
- Há necessidade de padronização textual na variável `cargo` para evitar inconsistências analíticas.
- As variáveis `uf` e `estado` apresentam possível redundância.

