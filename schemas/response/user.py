from models import UserType, UserState
from schemas.base import UserBase


class UserOut(UserBase):
    id: int
    first_name: str
    last_name: str
    phone: str
    user_type: UserType
    user_state: UserState