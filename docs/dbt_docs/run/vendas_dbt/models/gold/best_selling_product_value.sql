
  create view "crmdatabase_92cf"."public"."best_selling_product_value__dbt_tmp"
    
    
  as (
    

-- KPI: Produto Mais Vendido (em Valor)
-- Encontra o produto que gerou o maior valor de vendas.

SELECT
    produto,
    SUM(valor) AS total_product_revenue
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    produto
ORDER BY
    total_product_revenue DESC
LIMIT 1
  );