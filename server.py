from pydantic import BaseModel, Field
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, Integer, String
from db import Base, SessionLocal, engine
from sqlalchemy.orm import Session
import json

import models
import crud

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Company(BaseModel):
    name: str = Field(min_length=1)


@app.get("/")
def root(req: Request, db: Session = Depends(get_db)):
    companies = crud.get_companies(db)
    products = crud.get_products(db)

    return templates.TemplateResponse(
        "index.html", {"request": req, "companies": companies, "products": products}
    )


@app.get("/admin")
def admin(req: Request, db: Session = Depends(get_db)):
    companies = crud.get_companies(db)
    return templates.TemplateResponse(
        "admin.html", {"request": req, "companies": companies}
    )


@app.get("/admin/registration")
def registration(req: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse()


@app.post("/company")
async def createCompany(req: Request, db: Session = Depends(get_db)):
    body_bytes = await req.body()
    body = body_bytes.decode("utf-8")

    name = json.loads(body)["name"]

    return crud.create_company(db, name)


@app.post("/product")
async def createProduct(req: Request, db: Session = Depends(get_db)):
    body_bytes = await req.body()
    body = body_bytes.decode("utf-8")
    body = json.loads(body)

    name = body["name"]
    type = body["type"]
    company = body["company"]
    code = body["code"]

    return crud.create_product(db, name=name, company=company, code=code, type=type)
