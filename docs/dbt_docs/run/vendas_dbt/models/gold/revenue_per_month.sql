
  create view "crmdatabase_92cf"."public"."revenue_per_month__dbt_tmp"
    
    
  as (
    

-- KPI: Faturamento por Mês
-- Calcula o faturamento total gerado em cada mês.

SELECT
    EXTRACT(MONTH FROM data) AS revenue_month,
    SUM(valor) AS revenue_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    revenue_month
ORDER BY
    revenue_month ASC
  );