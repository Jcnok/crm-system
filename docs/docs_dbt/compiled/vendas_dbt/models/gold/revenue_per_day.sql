

-- KPI: Faturamento por Dia (por Ano)
-- Calcula o faturamento total gerado em cada dia em um ano específico.

SELECT
    DATE(data) AS revenue_date,
    SUM(valor) AS revenue_per_day
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024
GROUP BY
    revenue_date