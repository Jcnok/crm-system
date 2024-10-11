{{ config(materialized='view') }}

-- KPI: Faturamento Total (por Ano)
-- Calcula a soma do valor total de todas as vendas em um ano específico.

SELECT
    SUM(valor) AS total_revenue
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}