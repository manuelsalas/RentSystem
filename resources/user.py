from typing import Optional
from typing import List
from fastapi import APIRouter, Depends, Request

from managers.auth import oauth2_scheme, is_admin
from managers.user import UserManager
from models import UserType, UserState
from schemas.response.user import UserOut

router = APIRouter(tags=["Users"])


@router.get("/users/", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], response_model=List[UserOut])
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_users()


@router.put("/users/{user_id}/make-admin", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_user_type(UserType.admin, user_id)


@router.put("/users/{user_id}/make-user", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_user(user_id: int):
    await UserManager.change_user_type(UserType.user, user_id)


@router.put("/users/{user_id}/disable-user", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def disable_user(user_id: int):
    await UserManager.change_user_state(UserState.disable, user_id)


@router.put("/users/{user_id}/enable-user", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def enable_user(user_id: int):
    await UserManager.change_user_state(UserState.enable, user_id)


@router.put("/users/{email}/reset-password/{password}", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def reset_password(email: str, password: str ):
    await UserManager.reset_user_password(email, password)