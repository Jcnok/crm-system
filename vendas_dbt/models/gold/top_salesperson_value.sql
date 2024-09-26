{{ config(materialized='view') }}

-- KPI: Vendedor com Mais Vendas (em Valor)
-- Encontra o vendedor que gerou o maior valor de vendas.

SELECT
    email,
    SUM(valor) AS salesperson_total_revenue
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    email
ORDER BY
    salesperson_total_revenue DESC
LIMIT 1