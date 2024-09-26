{{ config(materialized='view') }}

-- KPI: Valor Médio da Venda
-- Calcula o valor médio das vendas.

SELECT
    AVG(valor) AS average_sale_value
FROM
    {{ ref('silver_vendas') }}