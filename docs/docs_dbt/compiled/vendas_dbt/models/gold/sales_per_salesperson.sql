

-- KPI: Número de Vendas por Vendedor (por Ano)
-- Calcula a quantidade de vendas realizadas por cada vendedor em um ano específico.

SELECT
    email,
    COUNT(*) AS sales_per_salesperson
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024
GROUP BY
    email