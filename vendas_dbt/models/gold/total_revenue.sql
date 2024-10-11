{{ config(materialized='view') }}

-- KPI: Faturamento Total (por Ano)
-- Calcula a soma do valor total de todas as vendas em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    SUM(valor) AS total_revenue
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year