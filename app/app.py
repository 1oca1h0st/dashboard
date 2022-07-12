from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.routes.web import router
from core.configs.logs import logger

app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
app.include_router(router)
