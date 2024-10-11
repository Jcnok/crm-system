

-- KPI: Vendas por Mês (por Ano)
-- Calcula o número de vendas realizadas em cada mês em um ano específico.

SELECT
    EXTRACT(MONTH FROM data) AS sales_month,
    COUNT(*) AS sales_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024
GROUP BY
    sales_month
ORDER BY
    sales_month ASC