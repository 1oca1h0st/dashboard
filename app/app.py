from beanie import init_beanie
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.authentication import AuthenticationMiddleware

from commands.kernel import scheduler
from core.db.mongo import mongo
from core.middleware.auth import BasicAuthBackend
from core.models.mongo.users import Users
from core.routes.web import router

app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
app.include_router(router)


@app.on_event("startup")
async def commands():
    scheduler.start()
    print("定时任务启动成功..")


@app.on_event("startup")
async def start_db():
    await init_beanie(database=mongo, document_models=[Users])
