from typing import Optional
from typing import List
from fastapi import APIRouter, Depends, Request

from models import UserType, UserState
from schemas.request.owner_objects import OwnerObjectsIn
from schemas.response.owner_objects import ObjectsToRentOut
from managers.owner_objects import OwnerObjectsManager
from managers.auth import oauth2_scheme,is_user

router = APIRouter(tags=["Owner-Objects"])

# API Rest: CRUD
# Post   -> Create
# Get    -> Read
# Put    -> Update
# Delete -> Delete

@router.post("/owner-objects/", dependencies=[Depends(oauth2_scheme), Depends(is_user)], response_model=ObjectsToRentOut)
async def create_owner_objects(request: Request, owner_objects: OwnerObjectsIn):
    user = request.state.user
    return await OwnerObjectsManager.create_owner_objects(owner_objects, user)
