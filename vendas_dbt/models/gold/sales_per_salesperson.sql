{{ config(materialized='view') }}

-- KPI: Número de Vendas por Vendedor (por Ano)
-- Calcula a quantidade de vendas realizadas por cada vendedor em um ano específico.

SELECT
    email,
    EXTRACT(YEAR FROM data) AS year,
    COUNT(*) AS sales_per_salesperson
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year,email