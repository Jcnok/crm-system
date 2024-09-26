{{ config(materialized='view') }}

-- KPI: Número de Vendas por Vendedor
-- Calcula a quantidade de vendas realizadas por cada vendedor.

SELECT
    email,
    COUNT(*) AS sales_per_salesperson
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    email