import streamlit as st 

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
    st.success("Venda salva com sucesso!")
    data_hora = f"{data} {hora}"
    st.write("Email do vendedor:", email)
    st.write("Data-Hora da venda:", data_hora)
    st.write("Valor da venda:", valor)
    st.write("Quantidade de produtos vendidos:", quantidade)
    st.write("Produto vendido:", produto)


if __name__ == "__main__":
  main()
 