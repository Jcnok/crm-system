

-- KPI: Quantidade Média de Produtos por Venda (por Ano)
-- Calcula a quantidade média de produtos vendidos por venda em um ano específico.

SELECT
    AVG(quantidade) AS average_products_per_sale
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024