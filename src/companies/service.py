from sqlalchemy.orm import Session
from .models import Company
from products.models import Product


def get_companies(db: Session):
    return db.query(Company).all()


def get_products_with_company(db: Session):
    return db.query(Company, Product).join(Product, Company.id == 1)


def create_company(db: Session, name: str):
    exist = db.query(Company).filter_by(name=name).first()

    if not exist:
        new_company = Company()
        new_company.name = name
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return {"success": True, "message": "업체 생성 성공"}
    else:
        return {"success": False, "message": "이미 존재하는 업체명입니다."}


def get_company_by_name(db: Session, name: str):
    return db.query(Company).filter_by(name=name).first()
