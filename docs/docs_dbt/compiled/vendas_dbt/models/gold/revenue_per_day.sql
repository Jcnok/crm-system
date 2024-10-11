

-- KPI: Faturamento por Dia (por Ano)
-- Calcula o faturamento total gerado em cada dia em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    DATE(data) AS revenue_date,
    SUM(valor) AS revenue_per_day
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year,revenue_date