import json
from fastapi import HTTPException
from db import database
from models import object_to_rent, owner

# CRUD object to rent
# The owner is created with the first objects

class CreateOwner:
    @staticmethod
    async def create_owner(user):
        ow_data = {}
        owner_do = await database.fetch_one(owner.select().where(owner.c.user_id == user["id"]))
        try:
            if not owner_do:
                ow_data["user_id"] = user["id"]
                q_owner = owner.insert().values(**ow_data)
                try:
                    owner_id = await database.execute(q_owner)
                except:
                    raise HTTPException(status_code=400, detail="Error DB query")
                owner_do = await database.fetch_one(owner.select().where(owner.c.id == owner_id))
        except:
            raise HTTPException(status_code=400, detail="Error DB query")
        return owner_do

class OwnerObjectsManager:
    @staticmethod
    async def create_owner_object(object_data, user):
        owner_do = CreateOwner.create_owner(user)
        obj_data = object_data.dict()
        obj_data["owner_id"] = owner_do["id"]
        q_object = object_to_rent.insert().values(**obj_data)
        try:
            id_object_to_rent = await database.execute(q_object)
        except:
            raise HTTPException(status_code=400, detail="Error DB query")
        return await database.fetch_one(object_to_rent.select().where(object_to_rent.c.id == id_object_to_rent))


    @staticmethod
    async def create_owner_object_list(object_data_list, user):
        owner_do = CreateOwner.create_owner(user)
        print(object_data_list.__dict__)
        s = str(object_data_list)
        obj_data_list = json.loads(s)
        for i in range(len(obj_data_list)):
            obj_data_list[i]["owner_id"] = owner_do["id"]
        q_objects = object_to_rent.insert().values(**obj_data_list)
        try:
            id_object_to_rent = await database.execute(q_objects)
        except:
            raise HTTPException(status_code=400, detail="Error DB query")
        return await database.fetch_one(object_to_rent.select().where(object_to_rent.c.id == id_object_to_rent))