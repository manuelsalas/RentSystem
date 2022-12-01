import sqlalchemy as sqlalchemy
from db import metadata
from models.enum import UserType, UserState

user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(120), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column("first_name", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("phone", sqlalchemy.String(20)),
    sqlalchemy.Column("photo_url", sqlalchemy.String(200), nullable=True),
    sqlalchemy.Column("user_type", sqlalchemy.Enum(UserType), nullable=False, server_default=UserType.user.name),
    sqlalchemy.Column("user_state", sqlalchemy.Enum(UserState), nullable=False, server_default=UserState.enable.name),
)

