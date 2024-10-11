

-- KPI: Faturamento Total (por Ano)
-- Calcula a soma do valor total de todas as vendas em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    SUM(valor) AS total_revenue
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year