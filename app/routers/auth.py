from typing import Annotated
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import os

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=os.getenv('ALGORITHM'))
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail = "Invalidated user")
        return{'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail = "Invalidated user")