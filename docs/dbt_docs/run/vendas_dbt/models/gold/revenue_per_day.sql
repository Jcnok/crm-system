
  create view "crmdatabase_92cf"."public"."revenue_per_day__dbt_tmp"
    
    
  as (
    

-- KPI: Faturamento por Dia
-- Calcula o faturamento total gerado em cada dia.

SELECT
    DATE(data) AS revenue_date,
    SUM(valor) AS revenue_per_day
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    revenue_date
  );