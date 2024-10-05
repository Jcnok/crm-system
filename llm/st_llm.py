import os

import streamlit as st
from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType  # Import da classe AgentType
from langchain_community.agent_toolkits.sql.base import (
    create_sql_agent,  # Import da função create_sql_agent
)
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase  # Import da classe SQLDatabase
from langchain_google_genai import (
    ChatGoogleGenerativeAI,  # Import da classe ChatGoogleGenerativeAI
)

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Cria a instância do LLM (ChatGoogleGenerativeAI)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Carrega credenciais do banco de dados (presume que estejam no .env)
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Conecta ao banco de dados PostgreSQL
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)

# Cria o toolkit do agente SQL
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Cria o agente baseado em SQL
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# Streamlit
st.title("Chat SQL com LangChain")

user_input = st.text_input("Digite sua pergunta SQL:")

if user_input:
    with st.spinner("Executando a consulta..."):
        try:
            response = agent_executor.run(user_input)
            st.success(f"Resposta: {response}")
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")
