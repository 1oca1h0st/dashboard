from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from core.routes.models import test
from core.curd.deps import get_db
from core.curd.demo import get_demo
from core import schemas
from core.configs.settings import get_settings

from core.requests.demo import DemoRequests


def is_auth(request: Request):
    print(request.scope["path"])
    if request.url:
        print("111")


settings = get_settings()

router = APIRouter(dependencies=[Depends(is_auth)])
templates = Jinja2Templates(directory="views/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/ping")
async def ping_pong():
    return {"message": "pong"}


@router.get("/login", response_class=HTMLResponse)
async def view_login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.get("/db/{t_id}", response_model=schemas.DemoBase)
def get_demo_by_id(t_id: int, db: Session = Depends(get_db)):
    return get_demo(db, t_id)


@router.post("/validate")
def test_validate(data: DemoRequests):
    return {"msg": "ok"}


@router.get("/cache")
def get_cache():
    return {"msg": settings.TEST_ENV}


router.include_router(test.router, prefix="/test")
