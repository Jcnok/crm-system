{{ config(materialized='view') }}

-- KPI: Produto Mais Vendido (em Quantidade)
-- Encontra o produto com maior quantidade de unidades vendidas.

SELECT
    produto,
    SUM(quantidade) AS total_product_quantity
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    produto
ORDER BY
    total_product_quantity DESC
LIMIT 1