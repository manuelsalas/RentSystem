from asyncpg import UniqueViolationError
from fastapi import HTTPException
from passlib.context import CryptContext

from db import database
from managers.auth import AuthManager
from models import UserState, UserType, user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    @staticmethod
    async def register(user_data):
        data = user_data
        data["password"] = pwd_context.hash(data["password"])
        q = user.insert().values(**data)
        try:
            id_ = await database.execute(q)
        except UniqueViolationError:
            raise HTTPException(status_code=400, detail="User with this email already exists")
        user_do = await database.fetch_one(user.select().where(user.c.id == id_))
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def login(user_data):
        user_do = await database.fetch_one(user.select().where(user.c.email == user_data["email"]))
        if not user_do:
            raise HTTPException(status_code=400, detail="Wrong email or password")
        elif not pwd_context.verify(user_data["password"], user_do["password"]):
            raise HTTPException(status_code=400, detail="Wrong email or password")
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_user_by_email(email):
        return await database.fetch_all(user.select().where(user.c.email == email))

    @staticmethod
    async def get_users():
        return await database.fetch_all(user.select())

    @staticmethod
    async def change_user_type(type: UserType, user_id: int):
        user_do = await database.fetch_one(user.select().where(user.c.id == user_id))
        if user_do["user_type"] == type:
            raise HTTPException(status_code=400, detail="Same type - It doesn't need to change")
        await database.execute(user.update().where(user.c.id == user_id).values(user_type=type))

    @staticmethod
    async def change_user_state(state: UserState, user_id: int):
        user_do = await database.fetch_one(user.select().where(user.c.id == user_id))
        if user_do["user_state"] == state:
            raise HTTPException(status_code=400, detail="Same State - It doesn't need to change")
        await database.execute(user.update().where(user.c.id == user_id).values(user_state=state))

    @staticmethod
    async def reset_user_password(email:str, new_password: str):
        new_password_hash = pwd_context.hash(new_password)
        user_do = await database.fetch_one(user.select().where(user.c.email == email))
        if not user_do:
            raise HTTPException(status_code=400, detail="User email doesn't exist")
        await database.execute(user.update().where(user.c.id == user_do["id"]).values(password=new_password_hash))


