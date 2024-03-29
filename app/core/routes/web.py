from typing import List

from fastapi import APIRouter, Request, Depends, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

import core.schemas.mongo
from core import schemas
from core.configs.settings import get_settings
from core.curd.demo import get_demo
from core.curd.deps import get_db
from core.db.mongo import mongo
from core.models.mongo.demo import DemoModel
from core.requests.demo import DemoRequests
from core.routes import deps
from core.routes.models import users, scans


def is_auth(request: Request):
    print(request.scope["path"])
    if request.url:
        print("111")


settings = get_settings()

router = APIRouter()
# 使用 Jinja2 模板的示例
# templates = Jinja2Templates(directory="views/templates")

# router.include_router(test.router, prefix="/test", tags=["test"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(scans.router, prefix="/scans", tags=["scans"], dependencies=[Depends(deps.get_current_user)])


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return {"message": "pong"}
    # 使用 Jinja2 模板，可在函数中直接返回 views
    # return templates.TemplateResponse("index.html", {"request": request})


@router.get("/ping")
async def ping_pong():
    return {"message": "pong"}


@router.get("/db/{t_id}", response_model=schemas.DemoBase, tags=["mysql"])
def get_demo_by_id(t_id: int, db: Session = Depends(get_db)):
    """
    使用 MySQL 的示例，使用 id 查询数据并返回
    :param t_id:
    :param db:
    :return:
    """
    return get_demo(db, t_id)


@router.get("/mongo/list/{d_id}", response_model=DemoModel, tags=["mongo"])
async def mongo_list_by_id(d_id: str):
    """
    使用 MongoDB 的示例
    :param d_id: 数据库中的ID，此例使用 demo 表
    :return:
    """
    if (demo := await mongo["demo"].find_one({"_id": d_id})) is not None:
        return demo
    raise HTTPException(status_code=404, detail="Demo {} not found!".format(d_id))


@router.get("/mongo/list", response_model=List[core.schemas.mongo.DemoBase], tags=["mongo"])
async def mongo_list_by_id():
    results = await mongo["demo"].find().to_list(1000)
    return results


@router.post("/mongo/add", response_model=DemoModel, tags=["mongo"])
async def mongo_add_by_id(demo: DemoModel = Body(...)):
    demo = jsonable_encoder(demo)
    new_demo = await mongo["demo"].insert_one(demo)
    created_demo = await mongo["demo"].find_one({"_id": new_demo.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_demo)


@router.post("/validate", tags=["validate"])
def test_validate(data: DemoRequests):
    return {"msg": "ok"}


@router.get("/cache", tags=["cache"])
def get_cache():
    return {"msg": settings.TEST_ENV}
