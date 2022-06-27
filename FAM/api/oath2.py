from typing import Dict
from jose import jwt,JWTError
from datetime import date, datetime, timedelta
from .schemas import TokenData,db
from fastapi import Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(payload: Dict):
    to_encode = payload.copy()
    expiration_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expiration_time})

    jw_token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return jw_token

def verify_access_token(token:str, credential_exception):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("id")
        if not id:
            raise credential_exception
        
        token_data = TokenData(id=id)
        return token_data
    except:
        raise credential_exception

async def get_current_user(token: str= Depends(oauth2_scheme)):
    credential_exceeption =HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token could not be verify",
        headers={"WWW-AUTHENTICATE":"Bearer"}
    )
    current_user_id = verify_access_token(token,credential_exceeption).id
    current_user = await db["users"].find_one({"_id":current_user_id})

    return current_user



