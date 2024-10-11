

-- KPI: Vendas por Mês (por Ano)
-- Calcula o número de vendas realizadas em cada mês em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    EXTRACT(MONTH FROM data) AS sales_month,
    COUNT(*) AS sales_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year,sales_month
ORDER BY
    sales_month ASC