import os
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from langchain_community.agent_toolkits.sql.base import (
    create_sql_agent,  # Import da função create_sql_agent
)
from langchain_community.utilities import SQLDatabase  # Import da classe SQLDatabase
from langchain_google_genai import (
    ChatGoogleGenerativeAI,  # Import da classe ChatGoogleGenerativeAI
)
from pydantic import ValidationError

from contract import Produto, Vendas
from database import (
    delete_all_sales_data,
    obter_dados_api,
    salvar_no_postgres,
    salvar_no_postgres_em_lote,
)

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Carrega credenciais do banco de dados (presume que estejam no .env)
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
google_api_key = os.getenv("GOOGLE_API_KEY")


# Configuração da página
st.set_page_config(page_title="CRM System", layout="wide")

# Variável para armazenar a chave da API (inicialmente None)
# google_api_key = None


def home():
    # Define a capa do projeto
    st.title("CRM System")
    st.markdown("## Dashboard Interativo com LangChain & Streamlit")

    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/diagrama.gif?raw=true",
        width=800,
    )

    st.markdown("---")

    st.markdown(
        """
      Este projeto demonstra um sistema de CRM (Customer Relationship Management) construído com Python e o Streamlit, utilizando LangChain para a integração com o Google Gemini. Você pode inserir dados de vendas manualmente, importar dados de um arquivo CSV, consultar o banco de dados com com linguagem natural e visualizar indicadores(KPIs) de forma interativa.
      """
    )

    st.markdown("## Arquitetura do Projeto")
    st.markdown(
        """
      **Frontend:**
      - Streamlit: Interface web interativa.

      **Backend:**
      - Python: Linguagem de programação.
      - PostgreSQL: Banco de dados relacional.
      - FastAPI: Framework para API RESTful.
      - DBT: Ferramenta para transformação de dados.

      **Inteligência Artificial:**
      - LangChain: Framework para a integração com LLMs (Large Language Models).
      - Google Gemini: Modelo LLM escolhido para o projeto.
      """
    )

    # Seção de Contato e Agradecimento
    st.markdown("---")
    st.header("Curtiu o Projeto? 😊")
    st.write(
        "Se este projeto te ajudou ou te inspirou de alguma forma, me deixaria muito feliz se você pudesse dar uma olhada no repositório e deixar uma estrelinha ⭐. É rapidinho e me ajuda bastante! 😉"
    )
    st.markdown(
        "[https://github.com/Jcnok/crm-system](https://github.com/Jcnok/crm-system)"
    )

    st.write(
        "E se você tiver alguma dúvida, sugestão ou simplesmente quiser trocar uma ideia sobre o projeto, me chame no LinkedIn! Adoraria conectar! 😄"
    )
    st.markdown(
        "[https://www.linkedin.com/in/juliookuda/](https://www.linkedin.com/in/juliookuda/)"
    )

    st.header("Open Source e Flexibilidade 🚀")
    st.write(
        "Uma das coisas que mais me motivou a criar este projeto foi a possibilidade de usar apenas ferramentas open source e gratuitas. Nada de sustos com a fatura do cartão de crédito no final do mês! 😅 (Quem nunca esqueceu um servidor ligado na AWS que atire a primeira pedra, rs... 💸)"
    )
    st.write(
        "Além disso, a estrutura do projeto é totalmente flexível e pode ser facilmente migrada para outras clouds como AWS, Azure, GCP, etc. A escolha é sua! 😎"
    )

    st.markdown("## Usabilidade")

    st.markdown("- **Entrada de Dados:** Inserir dados de vendas manualmente.")
    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/insert.gif?raw=true",
        width=1000,
    )
    st.markdown("---")

    st.markdown("- **Entrada de Dados:** Inserir dados de um arquivo CSV.")
    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/insert_lot.gif?raw=true",
        width=1000,
    )
    st.markdown("---")

    st.markdown(
        "- **Dashboard Interativo:** Visualize KPIs de vendas em gráficos interativos."
    )
    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/dash.gif?raw=true",
        width=1000,
    )
    st.markdown("---")

    st.markdown(
        "- **Consulta com LangChain:** Faça perguntas em linguagem natural e obtenha respostas de consultas SQL."
    )
    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/chat_sql.gif?raw=true",
        width=1000,
    )
    st.markdown("---")

    st.markdown(
        "- **Documentação:** Visualize a documentação do projeto criada com mkdocs."
    )
    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/docs.gif?raw=true",
        width=1000,
    )
    st.markdown("---")

    st.markdown(
        "- **Apagar Dados:** Apagar todos os dados do banco de dados! (Botão do Pânico 🚨)"
    )
    st.image(
        "https://github.com/Jcnok/crm-system/blob/master/img/delete.gif?raw=true",
        width=1000,
    )
    st.markdown("---")


# Função para renderizar o formulário de entrada de dados
def render_data_entry():
    st.title("CRM System")
    st.write("Este é um sistema de CRM construído com Streamlit.")

    # Cria os campos de entrada para os dados da venda
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data em que a venda foi realizada", format="DD/MM/YYYY")
    hora = st.time_input("Hora em que a venda foi realizada")
    valor = st.number_input("Valor da venda")
    quantidade = st.number_input("Quantidade de produtos vendidos")
    produto = st.selectbox("Escolha o produto vendido", [p.value for p in Produto])

    # Botão para salvar os dados da venda
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=Produto(produto),
            )
            salvar_no_postgres(venda)
            st.success("Venda salva com sucesso!")
            st.write(venda)
        except ValidationError as e:
            st.error(f"Erro de validação: {e}")

    # Adiciona a funcionalidade de importar dados de arquivo CSV
    st.subheader("Importar dados de vendas (arquivo CSV)")
    st.markdown(
        """Copie o link e cole em 'Browse files' para usar o arquivo de exemplo:
           https://raw.githubusercontent.com/Jcnok/crm-system/refs/heads/master/data/sales_data.csv
        """
    )
    st.write("O arquivo CSV deve estar no seguinte formato:")
    st.markdown(
        """
        - Colunas: email, data, valor, quantidade, produto
        - Formato da data: AAAA-MM-DD HH:MM:SS
        - Formato do valor: número decimal com duas casas decimais (ex: 10.50)
        - Formato da quantidade: número inteiro
        - Produto: um dos valores definidos na enum Produto (Produto 1, Produto 2, Produto 3)
        """
    )
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        try:
            # Carrega os dados do arquivo CSV
            sales_data = pd.read_csv(uploaded_file)

            # Converte as colunas para o formato esperado
            sales_data["data"] = pd.to_datetime(sales_data["data"])
            sales_data["valor"] = sales_data["valor"].astype(float)
            sales_data["quantidade"] = sales_data["quantidade"].astype(int)
            sales_data["produto"] = sales_data["produto"].apply(lambda x: Produto(x))

            # Cria uma lista de objetos Vendas a partir dos dados do CSV
            vendas = [
                Vendas(
                    email=row["email"],
                    data=row["data"],
                    valor=row["valor"],
                    quantidade=row["quantidade"],
                    produto=row["produto"],
                )
                for _, row in sales_data.iterrows()
            ]

            # Salva os dados em lote no banco de dados
            if salvar_no_postgres_em_lote(vendas):
                st.success("Dados importados do CSV com sucesso!")
            else:
                st.error("Erro ao importar dados do CSV.")
        except Exception as e:
            st.error(f"Erro ao importar dados do CSV: {e}")


# Função para apagar todo o banco de dados
def del_database():
    # Botão para deletar todos os dados do banco de dados
    st.subheader("Apagar todos os dados do banco de dados! (Botão do Pânico 🚨)")
    if st.button("Deletar todos os dados"):
        if delete_all_sales_data():
            st.success("Todos os dados foram deletados do banco de dados.", icon="🔥")
        else:
            st.error("Erro ao deletar os dados do banco de dados.")


# Função para renderizar o dashboard
def render_dashboard():
    st.title("CRM System Dashboard")

    # Visão Geral
    st.header("Visão Geral das Vendas")
    col1, col2, col3 = st.columns(3)

    ano_selecionado = st.selectbox(
        "Selecione o ano", options=[2023, 2024], index=1
    )  # Adiciona o seletor de ano

    total_revenue = obter_dados_api(f"total_revenue/{ano_selecionado}")
    with col1:
        st.metric("Faturamento Total", value=f"R$ {total_revenue['total_revenue']:.2f}")

    total_sales = obter_dados_api(f"total_sales/{ano_selecionado}")
    with col2:
        st.metric("Número Total de Vendas", value=f"{total_sales['total_sales']}")

    average_ticket = obter_dados_api(f"average_ticket/{ano_selecionado}")
    with col3:
        st.metric("Ticket Médio", value=f"R$ {average_ticket['average_ticket']:.2f}")

    # Botão para atualizar os dados
    if st.button("Atualizar Dados"):
        st.rerun()  # Reinicia a execução do dashboard

    # Análise de Produtos
    st.header("Análise de Produtos")
    product_revenue = obter_dados_api(f"product_revenue/{ano_selecionado}")
    product_revenue_df = pd.DataFrame(product_revenue)
    fig_pie = px.pie(
        product_revenue_df,
        values="product_revenue",
        names="produto",
        title="Participação dos Produtos na Receita",
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # Desempenho de Vendedores
    st.header("Desempenho de Vendedores")
    revenue_per_salesperson = obter_dados_api(
        f"revenue_per_salesperson/{ano_selecionado}"
    )
    revenue_per_salesperson_df = pd.DataFrame(revenue_per_salesperson)
    fig_bar = px.bar(
        revenue_per_salesperson_df.sort_values(
            by="revenue_per_salesperson", ascending=False
        ),
        x="email",
        y="revenue_per_salesperson",
        title="Faturamento por Vendedor",
        labels={"email": "Vendedor", "revenue_per_salesperson": "Faturamento"},
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # Tendências Temporais
    st.header("Tendências Temporais")

    # Obter os dados
    revenue_per_month = obter_dados_api(f"revenue_per_month/{ano_selecionado}")
    revenue_per_month_df = pd.DataFrame(revenue_per_month)

    # Criar o gráfico de linha filtrado
    fig_line = px.line(
        revenue_per_month_df,
        x="revenue_month",
        y="revenue_per_month",
        title=f"Evolução do Faturamento Mensal - {ano_selecionado}",
        labels={"revenue_month": "Mês", "revenue_per_month": "Faturamento"},
    )

    # Exibir o gráfico
    st.plotly_chart(fig_line, use_container_width=True)

    # Top 3 Vendedores (Valor)
    st.header("Top 3 Vendedores (Valor)")
    top_salesperson_value = obter_dados_api(f"top3_salesperson_value/{ano_selecionado}")
    top_salesperson_value_df = pd.DataFrame(top_salesperson_value)
    fig_bar_top_sales = px.bar(
        top_salesperson_value_df,
        x="email",
        y="salesperson_total_revenue",
        title="Top 3 Vendedores (Valor)",
        labels={"email": "Vendedor", "salesperson_total_revenue": "Faturamento"},
    )
    st.plotly_chart(fig_bar_top_sales, use_container_width=True)

    # Top 3 Vendedores (Quantidade)
    st.header("Top 3 Vendedores (Quantidade)")
    top_salesperson_quantity = obter_dados_api(
        f"top3_salesperson_quantity/{ano_selecionado}"
    )
    top_salesperson_quantity_df = pd.DataFrame(top_salesperson_quantity)
    fig_bar_top_sales_quantity = px.bar(
        top_salesperson_quantity_df,
        x="email",
        y="salesperson_total_sales",
        title="Top 3 Vendedores (Quantidade)",
        labels={"email": "Vendedor", "salesperson_total_sales": "Vendas"},
    )
    st.plotly_chart(fig_bar_top_sales_quantity, use_container_width=True)

    # Vendas por Dia
    st.header("Vendas por Dia")
    sales_per_day = obter_dados_api(f"sales_per_day/{ano_selecionado}")
    sales_per_day_df = pd.DataFrame(sales_per_day)
    fig_line_day = px.line(
        sales_per_day_df,
        x="sales_date",
        y="sales_per_day",
        title="Vendas por Dia",
        labels={"sales_date": "Data", "sales_per_day": "Vendas"},
    )
    st.plotly_chart(fig_line_day, use_container_width=True)

    # Vendas por Mês
    st.header("Vendas por Mês")
    sales_per_month = obter_dados_api(f"sales_per_month/{ano_selecionado}")
    sales_per_month_df = pd.DataFrame(sales_per_month)
    fig_bar_month = px.bar(
        sales_per_month_df,
        x="sales_month",
        y="sales_per_month",
        title="Vendas por Mês",
        labels={"sales_month": "Mês", "sales_per_month": "Vendas"},
    )
    st.plotly_chart(fig_bar_month, use_container_width=True)

    # Vendas por Ano
    st.header("Vendas por Ano")
    sales_per_year = obter_dados_api("sales_per_year")
    sales_per_year_df = pd.DataFrame(sales_per_year)
    fig_bar_year = px.bar(
        sales_per_year_df,
        x="sales_year",
        y="sales_per_year",
        title="Vendas por Ano",
        labels={"sales_year": "Ano", "sales_per_year": "Vendas"},
    )
    st.plotly_chart(fig_bar_year, use_container_width=True)

    # Faturamento por Dia
    st.header("Faturamento por Dia")
    revenue_per_day = obter_dados_api(f"revenue_per_day/{ano_selecionado}")
    revenue_per_day_df = pd.DataFrame(revenue_per_day)
    fig_line_revenue_day = px.line(
        revenue_per_day_df,
        x="revenue_date",
        y="revenue_per_day",
        title="Faturamento por Dia",
        labels={"revenue_date": "Data", "revenue_per_day": "Faturamento"},
    )
    st.plotly_chart(fig_line_revenue_day, use_container_width=True)

    # Faturamento por Mês
    st.header("Faturamento por Mês")
    revenue_per_month = obter_dados_api(f"revenue_per_month/{ano_selecionado}")
    revenue_per_month_df = pd.DataFrame(revenue_per_month)
    fig_bar_revenue_month = px.bar(
        revenue_per_month_df,
        x="revenue_month",
        y="revenue_per_month",
        title="Faturamento por Mês",
        labels={"revenue_month": "Mês", "revenue_per_month": "Faturamento"},
    )
    st.plotly_chart(fig_bar_revenue_month, use_container_width=True)

    # Faturamento por Ano
    st.header("Faturamento por Ano")
    revenue_per_year = obter_dados_api("revenue_per_year")
    revenue_per_year_df = pd.DataFrame(revenue_per_year)
    fig_bar_revenue_year = px.bar(
        revenue_per_year_df,
        x="revenue_year",
        y="revenue_per_year",
        title="Faturamento por Ano",
        labels={"revenue_year": "Ano", "revenue_per_year": "Faturamento"},
    )
    st.plotly_chart(fig_bar_revenue_year, use_container_width=True)


# Função para consulta sql por Chat com langchain;
def st_llm():
    # Verifica se a chave da API foi inserida
    # global google_api_key  # Declara a variável global para modificá-la dentro da função
    # if google_api_key is None:
    #    google_api_key = st.text_input(
    #        "Insira sua chave da API do Google AI:", type="password"
    #    )
    #    st.markdown(
    #        "Para criar uma chave da API do Google Gemini, siga as instruções: [Criar uma Chave API do Google Gemini](https://aistudio.google.com/app/apikey)"
    #    )
    #    if not google_api_key:
    #        st.error("É necessário inserir a chave da API para utilizar o Chat SQL.")
    #        return

    # Cria a instância do LLM (ChatGoogleGenerativeAI)
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", temperature=0, api_key=google_api_key
    )

    # Conecta ao banco de dados PostgreSQL
    db = SQLDatabase.from_uri(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )

    # Cria o toolkit do agente SQL
    # toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Cria o agente baseado em SQL
    agent_executor = create_sql_agent(
        llm=llm,
        # toolkit=toolkit,
        db=db,
        verbose=True,
        agent_type="tool-calling",
    )

    # Streamlit
    st.title("Chat SQL com LangChain")

    # Exibe um exemplo da estrutura da tabela 'vendas'
    st.subheader("Exemplo da Estrutura da Tabela 'vendas':")
    st.table(
        pd.DataFrame(
            {
                "id": [1, 2, 3, 4, 5],
                "email": [
                    "vendedor3@email.com",
                    "vendedor3@email.com",
                    "vendedor1@email.com",
                    "vendedor2@email.com",
                    "vendedor1@email.com",
                ],
                "data": [
                    "2024-01-10 10:00:00",
                    "2024-01-10 11:30:00",
                    "2024-01-15 14:00:00",
                    "2024-01-16 16:30:00",
                    "2024-01-17 18:00:00",
                ],
                "valor": [350, 499, 899, 350, 499],
                "quantidade": [20, 10, 30, 10, 20],
                "produto": [
                    "Product A",
                    "Product B",
                    "Product C",
                    "Product A",
                    "Product B",
                ],
            }
        )
    )

    # Seção informativa sobre o Chat SQL
    st.markdown(
        """
    ## Explore seus Dados com Linguagem Natural!

    Nesta seção, você pode fazer **qualquer pergunta** relacionada aos dados de venda armazenados na tabela `vendas`.

    **Imagine:**
    - Deseja saber o faturamento total de um produto específico?
    - Quer descobrir a quantidade de vendas realizadas por um vendedor em um determinado período?
    - Precisa identificar os produtos mais vendidos em quantidade ou valor?

    **Basta digitar sua pergunta em português, de forma natural, que o sistema se encarregará de traduzi-la em uma consulta SQL e buscar a resposta diretamente no banco de dados.**

    Para facilitar, você pode se basear na estrutura da tabela `vendas` exibida acima.

    **Não tem certeza por onde começar?** Sem problemas! Explore os exemplos de perguntas abaixo e compare os resultados com as informações do Dashboard.
    """
    )

    # Exibe exemplos de perguntas para o usuário
    st.subheader("Exemplos de Perguntas:")
    st.markdown(
        """
    - Qual o total de receita por produto em 2024?
    - Qual o total de vendas por vendedor em 2024?
    - Qual o  produto mais vendidos em quantidade e valor no ano atual?
    - Qual o ticket médio das vendas em 2024?
    - Qual o ticket médio de vendas realizadas em Janeiro de 2024?
    """
    )

    # Armazena as últimas 5 consultas do usuário (temporariamente durante a sessão)
    if "ultimas_consultas" not in st.session_state:
        st.session_state.ultimas_consultas = []

    user_input = st.text_input("Digite sua pergunta sobre o banco de dados:")

    if user_input:
        with st.spinner("Executando a consulta..."):
            try:
                response = agent_executor.run(user_input)
                st.write(response)

                # Armazena a consulta e a resposta
                st.session_state.ultimas_consultas.append(
                    {"pergunta": user_input, "resposta": response}
                )

                # Mantém apenas as últimas 5 consultas
                if len(st.session_state.ultimas_consultas) > 5:
                    st.session_state.ultimas_consultas.pop(0)

            except Exception as e:
                st.error(f"Erro ao executar a consulta: {e}")

    # Exibe o histórico de consultas (se houver)
    if st.session_state.ultimas_consultas:
        st.subheader("Histórico de Consultas:")
        for consulta in st.session_state.ultimas_consultas:
            st.write(f"**Pergunta:** {consulta['pergunta']}")
            st.write(f"**Resposta:** {consulta['resposta']}")
            st.markdown("---")


def documention():
    doc_url = "https://jcnok.github.io/crm-system/"
    st.markdown(
        f'<iframe src="{doc_url}" width="100%" height="800px"></iframe>',
        unsafe_allow_html=True,
    )


# Função principal
def main():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio(
        "Ir para",
        [
            "Home",
            "Entrada de Dados",
            "Dashboard",
            "Chat SQL",
            "Documentação",
            "Apagar Dados",
        ],
    )
    if page == "Home":
        home()
    elif page == "Entrada de Dados":
        render_data_entry()
    elif page == "Dashboard":
        render_dashboard()
    elif page == "Chat SQL":
        st_llm()
    elif page == "Documentação":
        documention()
    elif page == "Apagar Dados":
        del_database()


if __name__ == "__main__":
    main()
