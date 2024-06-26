from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List
from db import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)

    products = relationship("Product", backref="companies", lazy=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, unique=True, index=True)
    type = Column(String, unique=True)
    name = Column(String, unique=True, index=True)

    company_id = Column(Integer, ForeignKey("companies.id"))
