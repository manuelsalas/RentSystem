from datetime import datetime, timedelta
from typing import Optional

from decouple import config
import jwt
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import ExpiredSignatureError, InvalidTokenError
from starlette.requests import Request
from db import database
from models import UserType, UserState


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            to_encode = {
                "sub": user["id"], 
                "exp":  datetime.utcnow() + timedelta(minutes=120)
            }
            return jwt.encode(to_encode, config('JWT_SECRET'), algorithm='HS256')
        except Exception as ex:
            raise ex


class CustomHTTPBearer(HTTPBearer):
    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        from models import user
        try:
            payload = jwt.decode(res.credentials, config('JWT_SECRET'), algorithms=['HS256'])
            user = await database.fetch_one(user.select().where(user.c.id == payload["sub"]))
            request.state.user = user
            return user
        except ExpiredSignatureError:
            raise HTTPException(401, "Token expired.")
        except InvalidTokenError:
            raise HTTPException(401, "Invalid token.")


oauth2_scheme = CustomHTTPBearer()

def is_enable(request: Request):
    if not request.state.user["user_state"] == UserState.enable:
        raise HTTPException(status_code=403, detail="Forbidden - user state not enable")

def is_admin(request: Request):
    if not request.state.user["user_type"] == UserType.admin:
        raise HTTPException(status_code=403, detail="Forbidden - user is not admin")


""" def is_owner(request: Request):
    if not request.state.user["role_type"] == RoleType.owner:
        raise HTTPException(status_code=403, detail="Forbidden - user is not owner")


def is_renter(request: Request):
    if not request.state.user["role_type"] == RoleType.renter:
        raise HTTPException(status_code=403, detail="Forbidden - user is not renter") """



