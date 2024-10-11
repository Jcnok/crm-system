{{ config(materialized='view') }}

-- KPI: Valor Médio da Venda (por Ano)
-- Calcula o valor médio das vendas em um ano específico.

SELECT
    AVG(valor) AS average_sale_value
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}