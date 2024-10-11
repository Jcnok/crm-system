{{ config(materialized='view') }}

-- KPI: Vendas por Dia (por Ano)
-- Calcula o número de vendas realizadas em cada dia em um ano específico.

SELECT
    DATE(data) AS sales_date,
    COUNT(*) AS sales_per_day
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}
GROUP BY
    sales_date
ORDER BY
    sales_date ASC