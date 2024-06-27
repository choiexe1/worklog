from fastapi import Depends, FastAPI, Request
from db import Base, engine
from sqlalchemy.orm import Session
from dependencies import get_db, templates
import uvicorn
import json

# Routers
from companies.router import router as companies_router
from admin.router import router as admin_router

# Services
from products.service import get_products
from companies.service import get_companies

app = FastAPI(redirect_slashes=False)

app.include_router(admin_router)
app.include_router(companies_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root(req: Request, db: Session = Depends(get_db)):
    companies = get_companies(db)
    products = get_products(db)

    return templates.TemplateResponse(
        "index.html", {"request": req, "companies": companies, "products": products}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
