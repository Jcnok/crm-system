{{ config(materialized='view') }}

-- KPI: Vendas por Mês
-- Calcula o número de vendas realizadas em cada mês.

SELECT
    EXTRACT(MONTH FROM data) AS sales_month,
    COUNT(*) AS sales_per_month
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    sales_month