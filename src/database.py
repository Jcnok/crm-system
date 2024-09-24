import os
import psycopg2
from psycopg2.extras import execute_values
from psycopg2 import sql
from dotenv import load_dotenv
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
    except Exception as e:
        raise Exception(f"Erro ao criar a tabela de vendas: {e}")
    
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
        print("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        raise Exception(f"Erro ao salvar no banco de dados: {e}")    

# Função para salvar os dados validados no PostgreSQL em lote
def salvar_no_postgres_em_lote(vendas: list[Vendas]):
    """
    Salva uma lista de objetos Vendas no PostgreSQL em um único lote.
    """
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = conn.cursor()

        # Prepara os valores para inserção em lote
        values = [(
            venda.email,
            venda.data,
            venda.valor,
            venda.quantidade,
            venda.produto.value
        ) for venda in vendas]

        # Insere os dados na tabela de vendas em lote
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES %s"
        )
        execute_values(cursor, insert_query, values)
        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        raise Exception(f"Erro ao salvar no banco de dados: {e}")
        return False

def delete_all_sales_data():
    """
    Deleta todos os dados da tabela de vendas no PostgreSQL.
    """
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = conn.cursor()

        # Deleta todos os dados da tabela de vendas
        delete_query = sql.SQL("DELETE FROM vendas")
        cursor.execute(delete_query)
        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        return False, f"Erro ao deletar os dados do banco de dados: {e}"
criar_tabela_vendas()