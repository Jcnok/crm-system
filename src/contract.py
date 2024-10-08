from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

# from typing import Tuple


# Define os produtos como um Enum para garantir a consistência e legibilidade
class Produto(str, Enum):
    """
    Enum para representar os produtos disponíveis.
    """

    produto1 = "Product A"
    produto2 = "Product B"
    produto3 = "Product C"


class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        quantidade (PositiveInt): quantidade de produtos
        produto (Produto): categoria do produto
    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: Produto
