

-- KPI: Ticket Médio
-- Calcula o valor médio das compras realizadas pelos clientes.

SELECT
    AVG(valor) AS average_ticket
FROM
    "crmdatabase_92cf"."public"."silver_vendas"