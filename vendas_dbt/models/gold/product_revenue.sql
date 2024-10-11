{{ config(materialized='view') }}

-- KPI: Receita por Produto (por Ano)
-- Calcula o faturamento total gerado por cada produto em um ano específico.

SELECT
    produto,
    EXTRACT(YEAR FROM data) AS year,
    SUM(valor) AS product_revenue
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year,produto