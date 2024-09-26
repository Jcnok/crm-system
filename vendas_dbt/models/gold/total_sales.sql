{{ config(materialized='view') }}

-- KPI: Número Total de Vendas
-- Calcula a quantidade total de vendas realizadas.

SELECT
    COUNT(*) AS total_sales
FROM
    {{ ref('silver_vendas') }}