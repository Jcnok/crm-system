{{ config(materialized='view') }}

-- KPI: Receita por Produto (por Ano)
-- Calcula o faturamento total gerado por cada produto em um ano específico.

SELECT
    produto,
    SUM(valor) AS product_revenue
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}
GROUP BY
    produto