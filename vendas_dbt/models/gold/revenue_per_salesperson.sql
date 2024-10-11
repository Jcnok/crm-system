{{ config(materialized='view') }}

-- KPI: Faturamento por Vendedor (por Ano)
-- Calcula o valor total de vendas gerado por cada vendedor em um ano específico.

SELECT
    email,
    SUM(valor) AS revenue_per_salesperson
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}
GROUP BY
    email
ORDER BY
    revenue_per_salesperson DESC
