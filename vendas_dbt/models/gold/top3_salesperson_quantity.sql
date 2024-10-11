{{ config(materialized='view') }}

-- KPI: Os 3 Vendedores com Mais Vendas (em Quantidade)
-- Encontra o 3 vendedores com maior número de vendas.

SELECT
    email,
    EXTRACT(YEAR FROM data) AS year,
    COUNT(*) AS salesperson_total_sales
FROM
    {{ ref('silver_vendas') }}
GROUP BY
    year,email
ORDER BY
    salesperson_total_sales DESC
LIMIT 3