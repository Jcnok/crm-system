{{ config(materialized='view') }}

-- KPI: Número de Vendas por Vendedor (por Ano)
-- Calcula a quantidade de vendas realizadas por cada vendedor em um ano específico.

SELECT
    email,
    COUNT(*) AS sales_per_salesperson
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}
GROUP BY
    email