import databases
import sqlalchemy
from sqlalchemy import create_engine
from decouple import config

DATABASE_URL = f"{config('DB_NAME')}://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_SERVER')}:{config('DB_PORT')}/{config('DB_NAME_DATABASE')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# In order to call custom functions from database
engine = create_engine(DATABASE_URL, echo=True)
rawEngineConn = engine.raw_connection()