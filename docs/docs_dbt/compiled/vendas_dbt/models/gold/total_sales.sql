

-- KPI: Número Total de Vendas (por Ano)
-- Calcula a quantidade total de vendas realizadas em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    COUNT(*) AS total_sales
    
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
GROUP BY
    year