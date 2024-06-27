from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, unique=True, index=True)
    type = Column(String)
    name = Column(String, unique=True, index=True)

    company_id = Column(Integer, ForeignKey("companies.id"))
