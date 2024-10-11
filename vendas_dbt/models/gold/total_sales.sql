{{ config(materialized='view') }}

-- KPI: Número Total de Vendas (por Ano)
-- Calcula a quantidade total de vendas realizadas em um ano específico.

SELECT
    COUNT(*) AS total_sales
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}