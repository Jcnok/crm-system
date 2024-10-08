
  create view "crmdatabase_92cf"."public"."total_sales__dbt_tmp"
    
    
  as (
    

-- KPI: Número Total de Vendas
-- Calcula a quantidade total de vendas realizadas.

SELECT
    COUNT(*) AS total_sales
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
  );