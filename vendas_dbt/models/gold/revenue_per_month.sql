{{ config(materialized='view') }}

-- KPI: Faturamento por Mês
-- Calcula o faturamento total gerado em cada mês.

SELECT
    EXTRACT(MONTH FROM data) AS revenue_month,
    SUM(valor) AS revenue_per_month
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    revenue_month