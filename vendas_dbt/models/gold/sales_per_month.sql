{{ config(materialized='view') }}

-- KPI: Vendas por Mês
-- Calcula o número de vendas realizadas em cada mês.

SELECT
    EXTRACT(YEAR FROM data) AS sales_year,
    EXTRACT(MONTH FROM data) AS sales_month,
    COUNT(*) AS sales_per_month
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    sales_year, sales_month
ORDER BY
    sales_year ASC, sales_month ASC
