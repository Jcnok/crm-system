
  create view "crmdatabase_92cf"."public"."best_selling_product_quantity__dbt_tmp"
    
    
  as (
    

-- KPI: Produto Mais Vendido (em Quantidade)
-- Encontra o produto com maior quantidade de unidades vendidas.

SELECT
    produto,
    SUM(quantidade) AS total_product_quantity
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    produto
ORDER BY
    total_product_quantity DESC
LIMIT 1
  );