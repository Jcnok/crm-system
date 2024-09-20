import os

import psycopg2
import streamlit as st
from dotenv import load_dotenv
from psycopg2 import sql

from contract import Vendas

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


# Função para criar a tabela de vendas no PostgreSQL
def criar_tabela_vendas():
    """
    Cria a tabela de vendas no PostgreSQL.
    """
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = conn.cursor()

        # Cria a tabela de vendas
        create_table_query = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS vendas (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                data TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                valor NUMERIC(10, 2) NOT NULL,
                quantidade INTEGER NOT NULL,
                produto VARCHAR(255) NOT NULL
            )
            """
        )
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
        # st.success("Tabela de vendas criada com sucesso!")
    except Exception as e:
        st.error(f"Erro ao criar a tabela de vendas: {e}")


# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    """
    Salva os dados validados no PostgreSQL.
    """
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = conn.cursor()

        # Insere os dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(
            insert_query,
            (
                dados.email,
                dados.data,
                dados.valor,
                dados.quantidade,
                dados.produto.value,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")


# Criar a tabela de vendas antes de usar a função salvar_no_postgres
criar_tabela_vendas()
