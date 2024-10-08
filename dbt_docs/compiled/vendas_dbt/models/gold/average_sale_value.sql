

-- KPI: Valor Médio da Venda
-- Calcula o valor médio das vendas.

SELECT
    AVG(valor) AS average_sale_value
FROM
    "crmdatabase_92cf"."public"."silver_vendas"