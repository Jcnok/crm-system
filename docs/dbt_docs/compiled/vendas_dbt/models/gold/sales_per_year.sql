

-- KPI: Vendas por Ano
-- Calcula o número de vendas realizadas em cada ano.

SELECT
    EXTRACT(YEAR FROM data) AS sales_year,
    COUNT(*) AS sales_per_year
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    sales_year