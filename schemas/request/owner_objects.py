from schemas.base import BaseModel, OwnerObjectsBase
from typing import List
from models import Period

# Owner id is created after record is save in DB, in request the id is user_id
class ObjectsToRentSaveBD(BaseModel):
    title: str
    description: str
    photo_url: str
    price: float
    price_period: Period
    owner_id: int


class ObjectsToRentIn(BaseModel):
    title: str
    description: str
    photo_url: str
    price: float
    price_period: Period


class OwnerObjectsIn(OwnerObjectsBase):
    OwnerObjects:List[ObjectsToRentIn]
