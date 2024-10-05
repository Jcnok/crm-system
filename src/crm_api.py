import os

# import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from sqlalchemy import text

load_dotenv()  # Carrega as variáveis do arquivo .env

# Configuração do banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"  # Monta a URL da conexão

engine = sqlalchemy.create_engine(DATABASE_URL)

app = FastAPI()


# Endpoint para obter o Faturamento Total
@app.get("/total_revenue")
async def get_total_revenue():
    with engine.connect() as conn:
        stmt = text(
            "SELECT total_revenue FROM total_revenue"
        )  # Usa a função text() para executar a consulta
        result = conn.execute(stmt).fetchone()
        if result:
            return {"total_revenue": result[0]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Número Total de Vendas
@app.get("/total_sales")
async def get_total_sales():
    with engine.connect() as conn:
        stmt = text("SELECT total_sales FROM  total_sales")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"total_sales": result[0]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Valor Médio da Venda
@app.get("/average_sale_value")
async def get_average_sale_value():
    with engine.connect() as conn:
        stmt = text("SELECT average_sale_value FROM  average_sale_value")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"average_sale_value": result[0]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter a Quantidade Média de Produtos por Venda
@app.get("/average_products_per_sale")
async def get_average_products_per_sale():
    with engine.connect() as conn:
        stmt = text("SELECT average_products_per_sale FROM  average_products_per_sale")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"average_products_per_sale": result[0]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Ticket Médio
@app.get("/average_ticket")
async def get_average_ticket():
    with engine.connect() as conn:
        stmt = text("SELECT average_ticket FROM  average_ticket")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"average_ticket": result[0]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Produto Mais Vendido (em Valor)
@app.get("/best_selling_product_value")
async def get_best_selling_product_value():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM  best_selling_product_value")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"produto": result[0], "total_product_revenue": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Produto Mais Vendido (em Quantidade)
@app.get("/best_selling_product_quantity")
async def get_best_selling_product_quantity():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM  best_selling_product_quantity")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"produto": result[0], "total_product_quantity": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter a Receita por Produto
@app.get("/product_revenue")
async def get_product_revenue():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  product_revenue")).fetchall()
        if results:
            return [{"produto": row[0], "product_revenue": row[1]} for row in results]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Vendedor com Mais Vendas (em Valor)
@app.get("/top_salesperson_value")
async def get_top_salesperson_value():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM  top_salesperson_value")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"email": result[0], "salesperson_total_revenue": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Vendedor com Mais Vendas (em Quantidade)
@app.get("/top_salesperson_quantity")
async def get_top_salesperson_quantity():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM  top_salesperson_quantity")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"email": result[0], "salesperson_total_sales": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Número de Vendas por Vendedor
@app.get("/sales_per_salesperson")
async def get_sales_per_salesperson():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  sales_per_salesperson")).fetchall()
        if results:
            return [
                {"email": row[0], "sales_per_salesperson": row[1]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Vendedor
@app.get("/revenue_per_salesperson")
async def get_revenue_per_salesperson():
    with engine.connect() as conn:
        results = conn.execute(
            text("SELECT * FROM  revenue_per_salesperson")
        ).fetchall()
        if results:
            return [
                {"email": row[0], "revenue_per_salesperson": row[1]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter as Vendas por Dia
@app.get("/sales_per_day")
async def get_sales_per_day():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  sales_per_day")).fetchall()
        if results:
            return [
                {"sales_date": str(row[0]), "sales_per_day": row[1]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter as Vendas por Mês
@app.get("/sales_per_month")
async def get_sales_per_month():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  sales_per_month")).fetchall()
        if results:
            return [
                {"sales_month": row[0], "sales_per_month": row[1]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter as Vendas por Ano
@app.get("/sales_per_year")
async def get_sales_per_year():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  sales_per_year")).fetchall()
        if results:
            return [{"sales_year": row[0], "sales_per_year": row[1]} for row in results]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Dia
@app.get("/revenue_per_day")
async def get_revenue_per_day():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  revenue_per_day")).fetchall()
        if results:
            return [
                {"revenue_date": str(row[0]), "revenue_per_day": row[1]}
                for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Mês
@app.get("/revenue_per_month")
async def get_revenue_per_month():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  revenue_per_month")).fetchall()
        if results:
            return [
                {"revenue_month": row[0], "revenue_per_month": row[1]}
                for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Ano
@app.get("/revenue_per_year")
async def get_revenue_per_year():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM  revenue_per_year")).fetchall()
        if results:
            return [
                {"revenue_year": row[0], "revenue_per_year": row[1]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("crm_api:app", host="0.0.0.0", port=5000, reload=True)
