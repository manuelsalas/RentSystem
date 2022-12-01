from fastapi import HTTPException
from db import database
from managers.auth import AuthManager
from models import Period, owner, object_to_rent, OwnerObjectsBase, ObjectsToRentSaveBD


class OwnerObjectsManager:
    @staticmethod
    async def RegisterObjects(owner_objects_data):
        data_in = owner_objects_data
        owner_data: OwnerObjectsBase
        obj_to_rent: ObjectsToRentSaveBD

        # Create record - owner
        # pending: good practice is to create index in owner table by user_id
        owner_do = await database.fetch_one(owner.select().where(owner.c.user_id == data_in["user_id"]))
        try:
            if not owner_do:
                owner_data["user_id"] = data_in["user_id"]
                q_1 = owner.insert().values(**owner_data)
                try:
                    owner_id = await database.execute(q_1)
                except:
                    raise HTTPException(status_code=400, detail="Error DB query")
                owner_do = await database.fetch_one(owner.select().where(owner.c.id == owner_id))
        except:
            raise HTTPException(status_code=400, detail="Error DB query")

        # es una lista - corregir codigo    <------------
        # ***********************************************

        # Create record(s) - objects_to_rent
        obj_to_rent["title"] = data_in["title"]
        obj_to_rent["description"] = data_in["description"]
        obj_to_rent["photo_url"] = data_in["photo_url"]
        obj_to_rent["price"] = data_in["price"]
        obj_to_rent["price_period"] = data_in["price_period"]
        obj_to_rent["owner_id"] = owner_id

        q_2 = object_to_rent.insert().values(**obj_to_rent)
        try:
            id_object_to_rent = await database.execute(q_2)
        except:
            raise HTTPException(status_code=400, detail="Error DB query")
        object_to_rent_do = await database.fetch_one(object_to_rent.select().where(object_to_rent.c.id == id_object_to_rent))

        # esquema para response


        return AuthManager.encode_token(OwnerObjectsOut)
