import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Função para obter dados da API
def obter_dados_api(endpoint):
    url = f"http://localhost:5000/{endpoint}"  # Endereço da sua API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Erro ao obter dados da API: {response.status_code}")


# Dashboard Streamlit
st.title("CRM System Dashboard")

st.markdown("---")

# Seção: Visão Geral
st.markdown("## Visão Geral das Vendas")

col1, col2 = st.columns(2)
with col1:
    # Faturamento Total
    total_revenue = obter_dados_api("total_revenue")
    st.metric(
        "Faturamento Total",
        value=total_revenue["total_revenue"],
        delta=1000,
        delta_color="normal",
    )
with col2:
    # Número Total de Vendas
    total_sales = obter_dados_api("total_sales")
    st.metric(
        "Número Total de Vendas",
        value=total_sales["total_sales"],
        delta=50,
        delta_color="normal",
    )

st.metric(
    "Ticket Médio",
    value=obter_dados_api("average_ticket")["average_ticket"],
    delta=10,
    delta_color="inverse",
)

# Botão para atualizar os dados
if st.button("Atualizar Dados"):
    st.rerun()  # Reinicia a execução do dashboard

st.markdown("---")

# Seção: Análise de Produtos
st.markdown("## Análise de Produtos")

# Gráfico de Pizza: Participação dos Produtos na Receita
product_revenue = obter_dados_api("product_revenue")
fig_pie = px.pie(
    pd.DataFrame(product_revenue),
    values="product_revenue",
    names="produto",
    title="Participação dos Produtos na Receita",
    color_discrete_sequence=px.colors.qualitative.Pastel,
)
st.plotly_chart(fig_pie)

st.markdown("---")

# Seção: Desempenho de Vendedores
st.markdown("## Desempenho de Vendedores")

# Gráfico de Barras: Faturamento por Vendedor
revenue_per_salesperson = obter_dados_api("revenue_per_salesperson")
fig_bar = px.bar(
    pd.DataFrame(revenue_per_salesperson),
    x="email",
    y="revenue_per_salesperson",
    title="Faturamento por Vendedor",
    labels={"email": "Vendedor", "revenue_per_salesperson": "Faturamento"},
)
st.plotly_chart(fig_bar)

st.markdown("---")

# Seção: Tendências Temporais
st.markdown("## Tendências Temporais")

# Gráfico de Linha: Evolução do Faturamento Mensal
revenue_per_month = obter_dados_api("revenue_per_month")
fig_line = px.line(
    pd.DataFrame(revenue_per_month),
    x="revenue_month",
    y="revenue_per_month",
    title="Evolução do Faturamento Mensal",
    labels={"revenue_month": "Mês", "revenue_per_month": "Faturamento"},
)
st.plotly_chart(fig_line)

st.markdown("---")

# Seção: Vendas por Dia
st.markdown("## Vendas por Dia")

# Gráfico de Barras: Vendas por Dia
sales_per_day = obter_dados_api("sales_per_day")
fig_bar_day = px.bar(
    pd.DataFrame(sales_per_day),
    x="sales_date",
    y="sales_per_day",
    title="Vendas por Dia",
    labels={"sales_date": "Data", "sales_per_day": "Vendas"},
)
st.plotly_chart(fig_bar_day)

st.markdown("---")

# Seção: Vendas por Mês
st.markdown("## Vendas por Mês")

# Gráfico de Barras: Vendas por Mês
sales_per_month = obter_dados_api("sales_per_month")
fig_bar_month = px.bar(
    pd.DataFrame(sales_per_month),
    x="sales_month",
    y="sales_per_month",
    title="Vendas por Mês",
    labels={"sales_month": "Mês", "sales_per_month": "Vendas"},
)
st.plotly_chart(fig_bar_month)

st.markdown("---")

# Seção: Vendas por Ano
st.markdown("## Vendas por Ano")

# Gráfico de Barras: Vendas por Ano
sales_per_year = obter_dados_api("sales_per_year")
fig_bar_year = px.bar(
    pd.DataFrame(sales_per_year),
    x="sales_year",
    y="sales_per_year",
    title="Vendas por Ano",
    labels={"sales_year": "Ano", "sales_per_year": "Vendas"},
)
st.plotly_chart(fig_bar_year)

st.markdown("---")

# Seção: Faturamento por Dia
st.markdown("## Faturamento por Dia")

# Gráfico de Barras: Faturamento por Dia
revenue_per_day = obter_dados_api("revenue_per_day")
fig_bar_revenue_day = px.bar(
    pd.DataFrame(revenue_per_day),
    x="revenue_date",
    y="revenue_per_day",
    title="Faturamento por Dia",
    labels={"revenue_date": "Data", "revenue_per_day": "Faturamento"},
)
st.plotly_chart(fig_bar_revenue_day)

st.markdown("---")

# Seção: Faturamento por Mês
st.markdown("## Faturamento por Mês")

# Gráfico de Barras: Faturamento por Mês
revenue_per_month = obter_dados_api("revenue_per_month")
fig_bar_revenue_month = px.bar(
    pd.DataFrame(revenue_per_month),
    x="revenue_month",
    y="revenue_per_month",
    title="Faturamento por Mês",
    labels={"revenue_month": "Mês", "revenue_per_month": "Faturamento"},
)
st.plotly_chart(fig_bar_revenue_month)

st.markdown("---")

# Seção: Faturamento por Ano
st.markdown("## Faturamento por Ano")

# Gráfico de Barras: Faturamento por Ano
revenue_per_year = obter_dados_api("revenue_per_year")
fig_bar_revenue_year = px.bar(
    pd.DataFrame(revenue_per_year),
    x="revenue_year",
    y="revenue_per_year",
    title="Faturamento por Ano",
    labels={"revenue_year": "Ano", "revenue_per_year": "Faturamento"},
)
st.plotly_chart(fig_bar_revenue_year)
