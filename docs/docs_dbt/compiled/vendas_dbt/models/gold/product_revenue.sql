

-- KPI: Receita por Produto (por Ano)
-- Calcula o faturamento total gerado por cada produto em um ano específico.

SELECT
    produto,
    SUM(valor) AS product_revenue
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024
GROUP BY
    produto