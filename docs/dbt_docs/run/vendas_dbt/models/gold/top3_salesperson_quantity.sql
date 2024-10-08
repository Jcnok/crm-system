
  create view "crmdatabase_92cf"."public"."top3_salesperson_quantity__dbt_tmp"
    
    
  as (
    

-- KPI: Os 3 Vendedore com Mais Vendas (em Quantidade)
-- Encontra o 3 vendedores com maior número de vendas.

SELECT
    email,
    COUNT(*) AS salesperson_total_sales
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    email
ORDER BY
    salesperson_total_sales DESC
LIMIT 3
  );