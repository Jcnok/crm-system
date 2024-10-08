

-- KPI: Número de Vendas por Vendedor
-- Calcula a quantidade de vendas realizadas por cada vendedor.

SELECT
    email,
    COUNT(*) AS sales_per_salesperson
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    email