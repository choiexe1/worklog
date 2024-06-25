from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from db import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)

    # products = Relationship("product")

# class Product(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     code = Column(String, unique=True, index=True)
#     name = Column(String, unique=True, index=True)

#     company_id = Column(Integer, ForeignKey("companies.id"))

# class Type(Base):
#     __tablename__ = "types"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String, unique=True, index=True)