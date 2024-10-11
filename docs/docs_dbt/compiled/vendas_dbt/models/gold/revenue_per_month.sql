

-- KPI: Faturamento por Mês (por Ano)
-- Calcula o faturamento total gerado em cada mês em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    EXTRACT(MONTH FROM data) AS revenue_month,
    SUM(valor) AS revenue_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year,revenue_month
ORDER BY
    revenue_month ASC