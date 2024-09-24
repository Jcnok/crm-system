import os
import pandas as pd
from datetime import datetime
import streamlit as st
from pydantic import ValidationError
from contract import Vendas, Produto
from database import salvar_no_postgres, salvar_no_postgres_em_lote, delete_all_sales_data

def main():
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
            sales_data['data'] = pd.to_datetime(sales_data['data'])
            sales_data['valor'] = sales_data['valor'].astype(float)
            sales_data['quantidade'] = sales_data['quantidade'].astype(int)
            sales_data['produto'] = sales_data['produto'].apply(lambda x: Produto(x))
            
            # Cria uma lista de objetos Vendas a partir dos dados do CSV
            vendas = [Vendas(
                email=row["email"],
                data=row["data"],
                valor=row["valor"],
                quantidade=row["quantidade"],
                produto=row["produto"],
            ) for _, row in sales_data.iterrows()]
            
            # Salva os dados em lote no banco de dados
            if salvar_no_postgres_em_lote(vendas):
                st.success("Dados importados do CSV com sucesso!")
            else:
                st.error("Erro ao importar dados do CSV.")
        except Exception as e:
            st.error(f"Erro ao importar dados do CSV: {e}")

    # Botão para deletar todos os dados do banco de dados
    st.subheader(f"Apagar todos os dados do banco de dados! (Botão do Pânico 🚨)")
    if st.button("Deletar todos os dados"):
        if delete_all_sales_data():
            st.success("Todos os dados foram deletados do banco de dados.", icon="🔥")
        else:
            st.error("Erro ao deletar os dados do banco de dados.")

if __name__ == "__main__":
    main()