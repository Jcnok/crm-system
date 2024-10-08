

-- KPI: Vendas por Dia
-- Calcula o número de vendas realizadas em cada dia.

SELECT
    DATE(data) AS sales_date,
    COUNT(*) AS sales_per_day
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    sales_date
ORDER BY
    sales_date ASC