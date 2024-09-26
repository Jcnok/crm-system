{{ config(materialized='view') }}

-- KPI: Ticket Médio
-- Calcula o valor médio das compras realizadas pelos clientes.

SELECT
    AVG(valor) AS average_ticket
FROM
    {{ ref('silver_vendas') }}