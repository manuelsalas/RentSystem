from typing import Optional, List
from fastapi import APIRouter, Depends, Request

from models import UserType, UserState
from schemas.request.owner_objects import ObjectIn, ObjectInList
from schemas.response.owner_objects import ObjectToRentOut, ObjectToRentListOut
from managers.owner_objects import OwnerObjectsManager
from managers.auth import oauth2_scheme,is_user

router = APIRouter(tags=["Owner-Objects"])

# API Rest: CRUD
# Post   -> Create
# Get    -> Read
# Put    -> Update
# Delete -> Delete

@router.post("/owner-object/", dependencies=[Depends(oauth2_scheme), Depends(is_user)], response_model=ObjectToRentOut)
async def create_owner_object(request: Request, object: ObjectIn):
    user = request.state.user
    return await OwnerObjectsManager.create_owner_object(object, user)

@router.post("/owner-object-list/", dependencies=[Depends(oauth2_scheme), Depends(is_user)], response_model=ObjectToRentListOut)
async def create_owner_object_list(request: Request, object_list: ObjectInList):
    user = request.state.user
    return await OwnerObjectsManager.create_owner_object_list(object_list, user)


