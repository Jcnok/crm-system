{{ config(materialized='view') }}

-- KPI: os 3 Vendedores com Mais Vendas (em Valor)
-- Encontra os 3 melhores vendedores que geraram os maiores valores de vendas.

SELECT
    email,
    SUM(valor) AS salesperson_total_revenue
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}    
GROUP BY
    email
ORDER BY
    salesperson_total_revenue DESC
LIMIT 3