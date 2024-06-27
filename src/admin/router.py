from fastapi import Depends, Request, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db, templates
from companies import service as company_service

import json

router = APIRouter(prefix="/admin", dependencies=[Depends(get_db)])


@router.get("")
def admin(req: Request, db: Session = Depends(get_db)):
    companies = company_service.get_companies(db)
    return templates.TemplateResponse(
        "admin.html", {"request": req, "companies": companies}
    )


# @router.post("/company")
# async def createCompany(req: Request, db: Session = Depends(get_db)):
#     body_bytes = await req.body()
#     body = body_bytes.decode("utf-8")
#     name = json.loads(body)["name"]

#     return company_service.create_company(db, name)
