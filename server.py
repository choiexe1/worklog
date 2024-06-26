from pydantic import BaseModel, Field
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, Integer, String
from db import Base, SessionLocal, engine
from sqlalchemy.orm import Session

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
    return templates.TemplateResponse(
        "index.html", {"request": req, "companies": companies}
    )


@app.get("/admin")
def root(req: Request, db: Session = Depends(get_db)):
    companies = crud.get_companies(db)
    return templates.TemplateResponse(
        "admin.html", {"request": req, "companies": companies}
    )


@app.post("/company")
async def create(req: Request, db: Session = Depends(get_db)):
    l = await req.body()
