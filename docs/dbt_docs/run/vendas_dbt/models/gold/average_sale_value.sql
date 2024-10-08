
  create view "crmdatabase_92cf"."public"."average_sale_value__dbt_tmp"
    
    
  as (
    

-- KPI: Valor Médio da Venda
-- Calcula o valor médio das vendas.

SELECT
    AVG(valor) AS average_sale_value
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
  );