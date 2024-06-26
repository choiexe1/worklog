from sqlalchemy.orm import Session
import models


def get_companies(db: Session):
    return db.query(models.Company).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_company(db: Session, name: str):
    new_company = models.Company(name)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


# TODO: 제품 추가 함수 구현
def create_product(db: Session, name: str, code: str, type: str):
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company
