

-- KPI: Vendas por Dia (por Ano)
-- Calcula o número de vendas realizadas em cada dia em um ano específico.

SELECT
    DATE(data) AS sales_date,
    EXTRACT(YEAR FROM data) AS year,
    COUNT(*) AS sales_per_day
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year, sales_date
ORDER BY
    sales_date ASC