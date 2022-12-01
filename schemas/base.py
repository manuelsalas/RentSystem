from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class OwnerObjectsBase(BaseModel):
    user_id: int