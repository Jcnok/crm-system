

-- KPI: Faturamento Total
-- Calcula a soma do valor total de todas as vendas.

SELECT
    SUM(valor) AS total_revenue
FROM
    "crmdatabase_92cf"."public"."silver_vendas"