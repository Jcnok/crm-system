{{ config(materialized='view') }}

-- KPI: Faturamento por Vendedor (por Ano)
-- Calcula o valor total de vendas gerado por cada vendedor em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    email,
    SUM(valor) AS revenue_per_salesperson
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year, email

