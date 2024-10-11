

-- KPI: Produto Mais Vendido (em Valor) (por Ano)
-- Encontra o produto que gerou o maior valor de vendas em um ano específico.

SELECT
    produto,
    EXTRACT(YEAR FROM data) AS year,
    SUM(valor) AS total_product_revenue
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year, produto
ORDER BY
    total_product_revenue DESC
LIMIT 1