{{ config(materialized='view') }}

-- KPI: Quantidade Média de Produtos por Venda (por Ano)
-- Calcula a quantidade média de produtos vendidos por venda em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    AVG(quantidade) AS average_products_per_sale
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year