{{ config(materialized='view') }}

-- KPI: Vendedor com Mais Vendas (em Quantidade)
-- Encontra o vendedor com maior número de vendas.

SELECT
    email,
    COUNT(*) AS salesperson_total_sales
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    email
ORDER BY
    salesperson_total_sales DESC
LIMIT 1