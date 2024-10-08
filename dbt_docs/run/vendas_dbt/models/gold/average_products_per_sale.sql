
  create view "crmdatabase_92cf"."public"."average_products_per_sale__dbt_tmp"
    
    
  as (
    

-- KPI: Quantidade Média de Produtos por Venda
-- Calcula a quantidade média de produtos vendidos por venda.

SELECT
    AVG(quantidade) AS average_products_per_sale
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
  );