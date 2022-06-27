import motor.motor_asyncio
from dotenv import dotenv_values
import os
from bson import ObjectId 
from pydantic import BaseModel, Field, EmailStr

#dotenv_values(".env")
creddentials = dotenv_values(".env")


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://hemanth:hemanth@cluster0.fabsan1.mongodb.net/test")
#client = motor.motor_asyncio.AsyncIOMotorClient(creddentials['MONGODB_URL'])
db = client.blog_api


#BSON and fastapi JSON
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate 
     
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectID")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders ={ObjectId: str}
        schema_extra ={
            "example":{
                "name":"hemanth",
                "email":"hemanth@gmail.com",
                "password":"secret_code"
            }
        }

class UserResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    
    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders ={ObjectId: str}
        schema_extra ={
            "example":{
                "name":"hemanth",
                "email":"hemanth@gmail.com" 
            }
        }

class TokenData(BaseModel):
    id: str

