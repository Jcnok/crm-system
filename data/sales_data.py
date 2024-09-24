# Generate 200 fake sales data samples
import pandas as pd
from datetime import datetime, timedelta
from faker import Faker
from enum import Enum

class Product(Enum):
    PRODUCT_A = "Product A"
    PRODUCT_B = "Product B"
    PRODUCT_C = "Product C"

fake = Faker()

data = []
for _ in range(200):
    email = fake.email()
    data_venda = fake.date_time_between(start_date='-1y', end_date='now')
    valor = fake.pyfloat(min_value=10, max_value=1000, right_digits=2)
    quantidade = fake.random_int(min=1, max=20)
    produto = fake.random_element(Product)
    data.append({
        'email': email,
        'data': data_venda,
        'valor': valor,
        'quantidade': quantidade,
        'produto': produto.value
    })

sales_df = pd.DataFrame(data)

# Save the data to a CSV file
sales_df.to_csv('data/sales_data.csv', index=False)