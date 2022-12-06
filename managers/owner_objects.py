from fastapi import HTTPException
from typing import List
from db import database
from models import object_to_rent, owner

# CRUD object to rent
# The owner is created with the first objects

class OwnerObjectsManager:


    @staticmethod
    async def create_owner_objects(owner_objects_data, user):
        data = owner_objects_data.dict()

        # Create record - owner if it  are crating object by first time
        ow_data = {}
        owner_do = await database.fetch_one(owner.select().where(owner.c.user_id == user["id"]))
        try:
            if not owner_do:
                ow_data["user_id"] = user["id"]
                q_1 = owner.insert().values(**ow_data)
                try:
                    owner_id = await database.execute(q_1)
                except:
                    raise HTTPException(status_code=400, detail="Error DB query")
                owner_do = await database.fetch_one(owner.select().where(owner.c.id == owner_id))
        except:
            raise HTTPException(status_code=400, detail="Error DB query")

        # Create record - objects_to_rent
        data["owner_id"] = owner_do["id"]

        q_2 = object_to_rent.insert().values(**data)
        try:
            id_object_to_rent = await database.execute(q_2)
        except:
            raise HTTPException(status_code=400, detail="Error DB query")
        return await database.fetch_one(object_to_rent.select().where(object_to_rent.c.id == id_object_to_rent))