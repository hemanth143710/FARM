from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from database import(
    fetch_one_todo
)
origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers =["*"],
)

@app.get("/")
def read_root():
    return {"Hello":"world"}

@app.get ("/api/tudo")
async def get_tudo():
    return 1

@app.get("/api/tudo{id}")
async def get_tudo_by_id(id):
    return 1

@app.post ("/api/tudo")
async def get_tudo(tudo):
    return 1


@app.put ("/api/tudo{id}")
async def put_tudo(id, data):
    return 1


@app.delete ("/api/tudo{id}")
async def delete_tudo(id):
    return 1

