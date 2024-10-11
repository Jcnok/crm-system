{{ config(materialized='view') }}

-- KPI: Ticket Médio (por Ano)
-- Calcula o valor médio das compras realizadas pelos clientes em um ano específico.

SELECT
    EXTRACT(YEAR FROM data) AS year,
    AVG(valor) AS average_ticket
FROM
    {{ ref('silver_vendas') }}
GROUP BY   
    year