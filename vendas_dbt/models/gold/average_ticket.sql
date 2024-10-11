{{ config(materialized='view') }}

-- KPI: Ticket Médio (por Ano)
-- Calcula o valor médio das compras realizadas pelos clientes em um ano específico.

SELECT
    AVG(valor) AS average_ticket
FROM
    {{ ref('silver_vendas') }}
WHERE EXTRACT(YEAR FROM data) = {{ var('ano', default=2024) }}