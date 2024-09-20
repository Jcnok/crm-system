from datetime import datetime

import streamlit as st
from pydantic import ValidationError

from contract import Vendas  # Importa o modelo de dados para as vendas
from database import (
    salvar_no_postgres,  # Importa a função para salvar no banco de dados
)


def main():
    """
    Função principal do aplicativo Streamlit.
    """
    st.title("CRM System")  # Define o título da página
    st.write(
        "This is a CRM system built with Streamlit."
    )  # Exibe uma mensagem de boas-vindas

    # Cria os campos de entrada para os dados da venda
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data em que a venda foi realizada", format="DD/MM/YYYY")
    hora = st.time_input("Hora em que a venda foi realizada")
    valor = st.number_input("Valor da venda")
    quantidade = st.number_input("Quantidade de produtos vendidos")
    produto = st.selectbox(
        "Escolha o produto vendido", ["Produto 1", "Produto 2", "Produto 3"]
    )

    # Botão para salvar os dados da venda
    if st.button("Salvar"):
        try:
            # Combina a data e a hora em um objeto datetime
            data_hora = datetime.combine(data, hora)
            # Cria uma instância do modelo Vendas com os dados da venda
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto,
            )
            # Exibe uma mensagem de sucesso e os dados da venda
            # st.success("Venda salva com sucesso!")
            # Salva os dados da venda no banco de dados
            salvar_no_postgres(venda)
            st.write(venda)

        except ValidationError as e:
            # Exibe uma mensagem de erro se houver um erro de validação
            st.error(f"Erro de validação: {e}")


if __name__ == "__main__":
    main()
