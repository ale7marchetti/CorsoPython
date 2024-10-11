#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel


class ReverseModel(BaseModel):
    name: str


app = FastAPI()


@app.get("/hello")
async def _hello():
    return {"message": "Hello world!"}


@app.get("/hello/{name}")
async def _name(name: str):
    return {"message": f"Hello, {name}!", "name": name}


@app.post("/reverse")
async def _reverse_name(data: ReverseModel):
    rev = data.name[::-1]
    return {
        "message": f"Il tuo nome all'inverso: {rev}",
        "name": rev,
        "names": [data.name, rev],
        "dct": {"name": data.name, "rev": rev},
    }
