from fastapi import Depends, FastAPI, Request, APIRouter
from sqlalchemy.orm import Session
from ..dependencies import get_db, templates
import crud
import json

router = APIRouter(prefix="/products")


@router.post("/")
async def createProduct(req: Request, db: Session = Depends(get_db)):
    body_bytes = await req.body()
    body = body_bytes.decode("utf-8")
    body = json.loads(body)

    name = body["name"]
    type = body["type"]
    company = body["company"]
    code = body["code"]

    return crud.create_product(db, name=name, company=company, code=code, type=type)
