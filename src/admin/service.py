from sqlalchemy.orm import Session
from companies.models import Company
from products.models import Product


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


def create_product(db: Session, company: str, name: str, code: str, type: str):
    exist_name = db.query(Product).filter_by(name=name).first()
    exist_code = db.query(Product).filter_by(code=code).first()

    if not exist_name:
        if not exist_code:
            company = get_company_by_name(db, company)

            new_product = Product()
            new_product.company_id = company.id
            new_product.name = name
            new_product.code = code
            new_product.type = type
            db.add(new_product)

            db.commit()
            db.refresh(new_product)
            return {"success": True, "message": "제품 등록 성공"}
        else:
            return {"success": False, "message": "이미 존재하는 코드입니다."}
    else:
        return {"success": False, "message": "이미 존재하는 제품명입니다."}


# TODO: 조회 시 Pagination
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
