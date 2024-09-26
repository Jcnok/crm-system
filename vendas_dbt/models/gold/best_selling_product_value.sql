{{ config(materialized='view') }}

-- KPI: Produto Mais Vendido (em Valor)
-- Encontra o produto que gerou o maior valor de vendas.

SELECT
    produto,
    SUM(valor) AS total_product_revenue
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    produto
ORDER BY
    total_product_revenue DESC
LIMIT 1