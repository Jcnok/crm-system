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
@app.get("/total_revenue/{ano}")  # Adiciona o parâmetro 'ano'
async def get_total_revenue(ano: int):
    with engine.connect() as conn:
        stmt = text(
            f"SELECT * FROM  total_revenue WHERE year = {ano}"
        )  # Usa a função text() para executar a consulta
        result = conn.execute(stmt).fetchone()
        if result:
            return {"total_revenue": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Número Total de Vendas
@app.get("/total_sales/{ano}")  # Adiciona o parâmetro 'ano'
async def get_total_sales(ano: int):
    with engine.connect() as conn:
        stmt = text(f"SELECT * FROM  total_sales WHERE year = {ano}")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"total_sales": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Valor Médio da Venda
@app.get("/average_sale_value/{ano}")  # Adiciona o parâmetro 'ano'
async def get_average_sale_value(ano: int):
    with engine.connect() as conn:
        stmt = text(f"SELECT * FROM average_sale_value WHERE year = {ano}")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"average_sale_value": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter a Quantidade Média de Produtos por Venda
@app.get("/average_products_per_sale/{ano}")  # Adiciona o parâmetro 'ano'
async def get_average_products_per_sale(ano: int):
    with engine.connect() as conn:
        stmt = text(f"SELECT * FROM average_products_per_sale WHERE year = {ano}")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"average_products_per_sale": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Ticket Médio
@app.get("/average_ticket/{ano}")  # Adiciona o parâmetro 'ano'
async def get_average_ticket(ano: int):
    with engine.connect() as conn:
        stmt = text(f"SELECT * FROM average_ticket WHERE year = {ano}")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"average_ticket": result[1]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Produto Mais Vendido (em Valor)
@app.get("/best_selling_product_value/{ano}")  # Adiciona o parâmetro 'ano'
async def get_best_selling_product_value(ano: int):
    with engine.connect() as conn:
        stmt = text(f"SELECT * FROM best_selling_product_value WHERE year = {ano}")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"produto": result[0], "total_product_revenue": result[2]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Produto Mais Vendido (em Quantidade)
@app.get("/best_selling_product_quantity/{ano}")  # Adiciona o parâmetro 'ano'
async def get_best_selling_product_quantity(ano: int):
    with engine.connect() as conn:
        stmt = text(f"SELECT * FROM best_selling_product_quantity WHERE year = {ano}")
        result = conn.execute(stmt).fetchone()
        if result:
            return {"produto": result[0], "total_product_quantity": result[2]}
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter a Receita por Produto
@app.get("/product_revenue/{ano}")  # Adiciona o parâmetro 'ano'
async def get_product_revenue(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM product_revenue WHERE year = {ano}")
        ).fetchall()
        if results:
            return [{"produto": row[0], "product_revenue": row[2]} for row in results]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Vendedor com Mais Vendas (em Valor)
@app.get("/top3_salesperson_value/{ano}")  # Adiciona o parâmetro 'ano'
async def get_top3_salesperson_value(ano: int):
    with engine.connect() as conn:
        stmt = text(
            f"SELECT * FROM revenue_per_salesperson WHERE year = {ano} Order by revenue_per_salesperson Desc LIMIT 3"
        )
        results = conn.execute(stmt).fetchall()
        if results:
            return [
                {"email": row[1], "salesperson_total_revenue": row[2]}
                for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Vendedor com Mais Vendas (em Quantidade)
@app.get("/top3_salesperson_quantity/{ano}")  # Adiciona o parâmetro 'ano'
async def get_top3_salesperson_quantity(ano: int):
    with engine.connect() as conn:
        stmt = text(
            f"SELECT * FROM sales_per_salesperson WHERE year = {ano} Order by sales_per_salesperson Desc LIMIT 3"
        )
        results = conn.execute(stmt).fetchall()
        if results:
            return [
                {"email": row[0], "salesperson_total_sales": row[2]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Número de Vendas por Vendedor
@app.get("/sales_per_salesperson/{ano}")  # Adiciona o parâmetro 'ano'
async def get_sales_per_salesperson(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM sales_per_salesperson WHERE year = {ano}")
        ).fetchall()
        if results:
            return [
                {"email": row[0], "sales_per_salesperson": row[2]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Vendedor
@app.get("/revenue_per_salesperson/{ano}")  # Adiciona o parâmetro 'ano'
async def get_revenue_per_salesperson(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM revenue_per_salesperson WHERE year = {ano}")
        ).fetchall()
        if results:
            return [
                {"email": row[1], "revenue_per_salesperson": row[2]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter as Vendas por Dia
@app.get("/sales_per_day/{ano}")  # Adiciona o parâmetro 'ano'
async def get_sales_per_day(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM  sales_per_day WHERE year = {ano}")
        ).fetchall()
        if results:
            return [
                {"sales_date": str(row[0]), "sales_per_day": row[2]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter as Vendas por Mês
@app.get("/sales_per_month/{ano}")  # Adiciona o parâmetro 'ano'
async def get_sales_per_month(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM  sales_per_month WHERE year = {ano}")
        ).fetchall()
        if results:
            return [
                {"sales_year": row[0], "sales_month": row[1], "sales_per_month": row[2]}
                for row in results
            ]

        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter as Vendas por Ano
@app.get("/sales_per_year/{ano}")  # Adiciona o parâmetro 'ano'
async def get_sales_per_year(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM  sales_per_year WHERE sales_year = {ano}")
        ).fetchall()
        if results:
            return [{"sales_year": row[0], "sales_per_year": row[1]} for row in results]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Dia
@app.get("/revenue_per_day/{ano}")  # Adiciona o parâmetro 'ano'
async def get_revenue_per_day(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM  revenue_per_day WHERE year = {ano}")
        ).fetchall()
        if results:
            return [
                {"revenue_date": str(row[1]), "revenue_per_day": row[2]}
                for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Mês
@app.get("/revenue_per_month/{ano}")  # Adiciona o parâmetro 'ano'
async def get_revenue_per_month(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM  revenue_per_month WHERE year = {ano}")
        ).fetchall()
        if results:
            return [
                {
                    "revenue_year": row[0],
                    "revenue_month": row[1],
                    "revenue_per_month": row[2],
                }
                for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


# Endpoint para obter o Faturamento por Ano
@app.get("/revenue_per_year/{ano}")  # Adiciona o parâmetro 'ano'
async def get_revenue_per_year(ano: int):
    with engine.connect() as conn:
        results = conn.execute(
            text(f"SELECT * FROM  revenue_per_year WHERE revenue_year = {ano}")
        ).fetchall()
        if results:
            return [
                {"revenue_year": row[0], "revenue_per_year": row[1]} for row in results
            ]
        else:
            raise HTTPException(status_code=404, detail="KPI não encontrada")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("crm_api:app", host="0.0.0.0", port=5000, reload=True)
