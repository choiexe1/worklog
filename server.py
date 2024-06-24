from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Log(BaseModel):
    name: str

@app.get("/")
async def root(req: Request):
    return templates.TemplateResponse(
        request=req, name="index.html", context={"id": id}
    )


@app.get("/{name}")
async def test(name: str):
    return Log(name=name)
