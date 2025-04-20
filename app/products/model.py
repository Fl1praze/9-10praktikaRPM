from sqlalchemy import DECIMAL,Column, Integer,String,JSON

from app.database import Base

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    price = Column(DECIMAL,nullable=False)
    description = Column(String)
