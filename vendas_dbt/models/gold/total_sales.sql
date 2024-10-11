{{ config(materialized='view') }}

-- KPI: Número Total de Vendas (por Ano)
-- Calcula a quantidade total de vendas realizadas em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    COUNT(*) AS total_sales
    
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year
