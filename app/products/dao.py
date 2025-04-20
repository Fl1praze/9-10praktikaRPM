from app.dao.base import BaseDAO
from app.products.model import Products

class ProductsDAO(BaseDAO):
    model = Products