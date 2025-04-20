from pydantic import BaseModel
from decimal import Decimal

from sqlalchemy import String


class ProductSchemas(BaseModel):
    name: str
    price: Decimal
    description: str

    class Config:
        from_attributes = True