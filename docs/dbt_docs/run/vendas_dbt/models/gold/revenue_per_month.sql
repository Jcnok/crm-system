
  create view "crmdatabase_92cf"."public"."revenue_per_month__dbt_tmp"
    
    
  as (
    

-- KPI: Faturamento por Mês
-- Calcula o faturamento total gerado em cada mês por ano.

SELECT
    EXTRACT(YEAR FROM data) AS revenue_year,
    EXTRACT(MONTH FROM data) AS revenue_month,
    SUM(valor) AS revenue_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    revenue_year, revenue_month
ORDER BY
    revenue_year ASC, revenue_month ASC
  );