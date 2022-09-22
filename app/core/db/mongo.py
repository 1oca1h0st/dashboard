import motor.motor_asyncio

from core.configs.settings import settings

MONGO_DATABASE_URI = "mongodb://{}:{}@{}/?retryWrites=true&w=majority".format(settings.MONGO_DB_USER,
                                                                              settings.MONGO_DB_PWD,
                                                                              settings.MONGO_DB_HOST)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DATABASE_URI)
mongo = client[settings.MONGO_DB_NAME]
