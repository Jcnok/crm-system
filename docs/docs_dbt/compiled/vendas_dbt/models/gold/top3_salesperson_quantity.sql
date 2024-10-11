

-- KPI: Os 3 Vendedores com Mais Vendas (em Quantidade)
-- Encontra o 3 vendedores com maior número de vendas.

SELECT
    email,
    EXTRACT(YEAR FROM data) AS year,
    COUNT(*) AS salesperson_total_sales
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year,email
ORDER BY
    salesperson_total_sales DESC
LIMIT 3