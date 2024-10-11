{{ config(materialized='view') }}

-- KPI: Produto Mais Vendido (em Valor) (por Ano)
-- Encontra o produto que gerou o maior valor de vendas em um ano específico.

SELECT
    produto,
    SUM(valor) AS total_product_revenue
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}
GROUP BY
    produto
ORDER BY
    total_product_revenue DESC
LIMIT 1