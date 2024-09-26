{{ config(materialized='view') }}

-- KPI: Quantidade Média de Produtos por Venda
-- Calcula a quantidade média de produtos vendidos por venda.

SELECT
    AVG(quantidade) AS average_products_per_sale
FROM
    {{ ref('silver_vendas') }}