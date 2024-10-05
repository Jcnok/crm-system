# import getpass
import os

from dotenv import load_dotenv

# from langchain.agents import AgentExecutor  # Import da classe AgentExecutor
from langchain.agents.agent_types import AgentType  # Import da classe AgentType
from langchain_community.agent_toolkits.sql.base import (
    create_sql_agent,  # Import da função create_sql_agent
)

# from langchain.agents.agent_toolkits import SQLDatabaseToolkit  # Import da classe SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase  # Import da classe SQLDatabase
from langchain_google_genai import (
    ChatGoogleGenerativeAI,  # Import da classe ChatGoogleGenerativeAI
)

# Carrega variáveis de ambiente (.env)
# os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API Key: ")
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

# Executa o agente com a query
# print(agent_executor.run("Qual o total de vendas?"))

# Você pode descomentar e executar outras queries também
# print(agent_executor.run("Qual o número total de vendas?"))
# print(agent_executor.run("Qual o ticket médio?"))
# print(agent_executor.run("Qual o produto mais vendido em quantidade?"))
print(agent_executor.run("Qual o faturamento por vendedor?"))
