from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Log(BaseModel):
    name: str

@app.get("/")
async def root(req: Request):
    return {"api": "0.0.1"}

@app.get("/{name}")
async def test(name: str):
    return Log(name=name)