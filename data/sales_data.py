from enum import Enum

import pandas as pd
from faker import Faker


# Definição dos produtos
class Product(Enum):
    PRODUCT_A = "Product A"
    PRODUCT_B = "Product B"
    PRODUCT_C = "Product C"


# Dicionário para mapear o valor correto para cada produto
product_prices = {
    Product.PRODUCT_A: 350,
    Product.PRODUCT_B: 499,
    Product.PRODUCT_C: 899,
}

fake = Faker()

# Cria uma lista com 10 emails de vendedores únicos
sellers_emails = [fake.email(domain="nihontec.com") for _ in range(10)]
data = []
for _ in range(200):
    email = fake.random_element(sellers_emails)  # Escolhe um email aleatório da lista
    data_venda = fake.date_time_between(start_date="-1y", end_date="now")
    quantidade = fake.random_int(min=1, max=20)
    produto = fake.random_element(Product)  # Seleciona o produto aleatoriamente
    valor = product_prices[produto]  # Atribui o valor correspondente ao produto

    # Adiciona os dados à lista
    data.append(
        {
            "email": email,
            "data": data_venda,
            "valor": valor,
            "quantidade": quantidade,
            "produto": produto.value,
        }
    )

# Cria um DataFrame com os dados de vendas
sales_df = pd.DataFrame(data)

# Salva os dados em um arquivo CSV
sales_df.to_csv("data/sales_data.csv", index=False)

print("Arquivo CSV gerado com sucesso!")
