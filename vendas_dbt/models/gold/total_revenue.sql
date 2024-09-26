{{ config(materialized='view') }}

-- KPI: Faturamento Total
-- Calcula a soma do valor total de todas as vendas.

SELECT
    SUM(valor) AS total_revenue
FROM
    {{ ref('silver_vendas') }}