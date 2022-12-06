from fastapi import APIRouter
from resources import auth, user, owner_objects


api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(user.router)
api_router.include_router(owner_objects.router)
