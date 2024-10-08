

-- KPI: Vendas por Mês
-- Calcula o número de vendas realizadas em cada mês.

SELECT
    EXTRACT(MONTH FROM data) AS sales_month,
    COUNT(*) AS sales_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    sales_month
ORDER BY
    sales_month ASC