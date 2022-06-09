
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Todo
from database import fetch_one_todo,fetch_all_todos,create_todo,update_todo,remove_todo
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
    response = await fetch_all_todos()
    return response

@app.get("/api/tudo{title}", response_model=Todo)
async def get_tudo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"there is np TODO item with this title{title}")
@app.post ("/api/tudo", response_model=Todo)
async def get_tudo(tudo:Todo):
    response = await create_todo(tudo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")


@app.put ("/api/tudo{title}/")
async def put_tudo(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")


@app.delete ("/api/tudo{title}")
async def delete_tudo(title):
    response = await remove_todo(title)
    if response:
        return "Succesfully deleted todo item !"
    raise HTTPException(404, f"there is no TODO item with this title {title}")

