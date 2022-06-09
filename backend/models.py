from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True