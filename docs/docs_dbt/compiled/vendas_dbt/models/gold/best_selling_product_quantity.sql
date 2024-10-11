

-- KPI: Produto Mais Vendido (em Quantidade) (por Ano)
-- Encontra o produto com maior quantidade de unidades vendidas em um ano específico.

SELECT
    produto,
    EXTRACT(YEAR FROM data) AS year,
    SUM(quantidade) AS total_product_quantity
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
   year,produto
ORDER BY
    total_product_quantity DESC
LIMIT 1