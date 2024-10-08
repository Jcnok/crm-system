
  create view "crmdatabase_92cf"."public"."revenue_per_salesperson__dbt_tmp"
    
    
  as (
    

-- KPI: Faturamento por Vendedor
-- Calcula o valor total de vendas gerado por cada vendedor.

SELECT
    email,
    SUM(valor) AS revenue_per_salesperson
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    email
ORDER BY
    revenue_per_salesperson DESC
  );