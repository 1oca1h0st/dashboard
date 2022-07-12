from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.routes.web import router
from core.configs.settings import get_settings

settings = get_settings()
print(f'{settings.TEST_ENV}')

app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
app.include_router(router)
