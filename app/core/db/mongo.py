import motor.motor_asyncio

from core.configs.settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_DATABASE_URI)
mongo = client["fastapi"]
