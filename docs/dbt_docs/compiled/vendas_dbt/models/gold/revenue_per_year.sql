

-- KPI: Faturamento por Ano
-- Calcula o faturamento total gerado em cada ano.

SELECT
    EXTRACT(YEAR FROM data) AS revenue_year,
    SUM(valor) AS revenue_per_year
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    revenue_year