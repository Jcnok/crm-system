import streamlit as st 
from contract import Vendas
from datetime import datetime
from pydantic import ValidationError


def main():   
  st.title("CRM System")
  st.write("This is a CRM system built with Streamlit.")
  email = st.text_input("email do vendedor")
  data = st.date_input("data em que a venda foi realizada",format = "DD/MM/YYYY") 
  hora = st.time_input("hora em que a venda foi realizada")
  valor = st.number_input("valor da venda")
  quantidade = st.number_input("quantidade de produtos vendidos")
  produto = st.selectbox("Escolha o produto vendido", ["Produto 1", "Produto 2", "Produto 3"])
  
  if st.button("Salvar"):
    try:
    data_hora = datetime.combine(data, hora)
    venda = Vendas(email=email
                  , data=data_hora
                  , valor=valor
                  , quantidade=quantidade
                  , produto=produto)
    st.success("Venda salva com sucesso!")
    except:
    data_hora = f"{data} {hora}"
      

if __name__ == "__main__":
  main()
 