from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt
from enum import Enum

# Define os produtos como um Enum para garantir a consistência e legibilidade
class Produto(str, Enum):
    """
    Enum para representar os produtos disponíveis.
    """
    produto1 = "Produto 1"
    produto2 = "Produto 2"
    produto3 = "Produto 3"


class Vendas(BaseModel):
    """
    Modelo Pydantic para representar uma venda.
    """
    email: EmailStr
    """
    Email do cliente.
    """
    data: datetime
    """
    Data da venda.
    """
    valor: PositiveFloat
    """
    Valor total da venda.
    """
    quantidade: PositiveInt
    """
    Quantidade de produtos vendidos.
    """
    produto: Produto
    """
    Produto vendido.
    """

@validate_call('produto')
def categoria_produto(cls, v):
    """
    Valida a categoria do produto.
    
    Args:
        cls: Classe do modelo.
        v: Valor da categoria do produto.
    
    Returns:
        O valor da categoria do produto.
    """
    return v