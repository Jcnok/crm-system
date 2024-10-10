
  create view "crmdatabase_92cf"."public"."sales_per_month__dbt_tmp"
    
    
  as (
    

-- KPI: Vendas por Mês
-- Calcula o número de vendas realizadas em cada mês.

SELECT
    EXTRACT(YEAR FROM data) AS sales_year,
    EXTRACT(MONTH FROM data) AS sales_month,
    COUNT(*) AS sales_per_month
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    sales_year, sales_month
ORDER BY
    sales_year ASC, sales_month ASC
  );