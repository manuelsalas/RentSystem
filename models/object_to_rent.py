import sqlalchemy as sqlalchemy
from db import metadata
from models.enum import Period

object_to_rent = sqlalchemy.Table(
    "objects_to_rent",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("photo_url", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("price_period", sqlalchemy.Enum(Period), nullable=False, server_default=Period.hour.name),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("owner_id", sqlalchemy.ForeignKey("owners.id"), nullable=False),
)
