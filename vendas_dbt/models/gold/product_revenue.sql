{{ config(materialized='view') }}

-- KPI: Receita por Produto
-- Calcula o faturamento total gerado por cada produto.

SELECT
    produto,
    SUM(valor) AS product_revenue
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    produto