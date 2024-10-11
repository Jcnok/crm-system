

-- KPI: Valor Médio da Venda (por Ano)
-- Calcula o valor médio das vendas em um ano específico.

SELECT
    AVG(valor) AS average_sale_value
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024