from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.authentication import AuthenticationMiddleware

from core.routes.web import router
from core.configs.settings import get_settings
from core.middleware.auth import BasicAuthBackend

from commands.kernel import scheduler

settings = get_settings()
print(f'{settings.TEST_ENV}')

app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
app.include_router(router)


@app.on_event("startup")
async def commands():
    scheduler.start()
    print("定时任务启动成功..")
