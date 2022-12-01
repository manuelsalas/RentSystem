from pydantic import BaseModel
from datetime import datetime
from typing import List
from models import Period


class OwnerOut(BaseModel):
    id: int
    created_at: datetime
    user_id: int


class ObjectsToRentOut(BaseModel):
    id: int
    title: str
    description: str
    photo_url: str
    price: float
    price_period: Period
    owner_id: int


class OwnerObjectsOut(BaseModel):
    owner: OwnerOut
    objects_to_rent: List[ObjectsToRentOut]