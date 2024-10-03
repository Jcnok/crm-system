{{ config(materialized='view') }}

-- KPI: Faturamento por Vendedor
-- Calcula o valor total de vendas gerado por cada vendedor.

SELECT
    email,
    SUM(valor) AS revenue_per_salesperson
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    email
ORDER BY
    revenue_per_salesperson DESC
