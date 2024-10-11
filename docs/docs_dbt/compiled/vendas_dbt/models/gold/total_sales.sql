

-- KPI: Número Total de Vendas (por Ano)
-- Calcula a quantidade total de vendas realizadas em um ano específico.

SELECT
    COUNT(*) AS total_sales
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024