

-- KPI: Ticket Médio (por Ano)
-- Calcula o valor médio das compras realizadas pelos clientes em um ano específico.

SELECT
    AVG(valor) AS average_ticket
FROM
    "crmdatabase_92cf"."public"."silver_vendas"
WHERE EXTRACT(YEAR FROM data) = 2024