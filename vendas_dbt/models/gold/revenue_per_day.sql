{{ config(materialized='view') }}

-- KPI: Faturamento por Dia
-- Calcula o faturamento total gerado em cada dia.

SELECT
    DATE(data) AS revenue_date,
    SUM(valor) AS revenue_per_day
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    revenue_date