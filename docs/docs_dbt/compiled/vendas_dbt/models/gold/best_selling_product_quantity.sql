

-- KPI: Produto Mais Vendido (em Quantidade) (por Ano)
-- Encontra o produto com maior quantidade de unidades vendidas em um ano específico.

SELECT
    produto,
    SUM(quantidade) AS total_product_quantity
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024
GROUP BY
    produto
ORDER BY
    total_product_quantity DESC
LIMIT 1