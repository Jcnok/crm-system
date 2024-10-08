
  create view "crmdatabase_92cf"."public"."top_salesperson_quantity__dbt_tmp"
    
    
  as (
    

-- KPI: Vendedor com Mais Vendas (em Quantidade)
-- Encontra o vendedor com maior número de vendas.

SELECT
    email,
    COUNT(*) AS salesperson_total_sales
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    email
ORDER BY
    salesperson_total_sales DESC
LIMIT 1
  );