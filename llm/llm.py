import os

import psycopg2
from dotenv import load_dotenv
from langchain.chains import create_sql_query_chain
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

llm.invoke("how can langsmith help with testing?")
# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port="5432"
)
cursor = conn.cursor()

# Initialize LangChain
chain = create_sql_query_chain(llm, conn)
response = chain.invoke({"question": "Show all vendas"})
print(response)


# Close the database connection
cursor.close()
conn.close()
