from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from core.controllers.scans import *
from core.controllers.tasks import *
from core.schemas.mongo.domains import DomainIn
from core.schemas.mongo.ips import IPIn

router = APIRouter()


@router.post("/domain/create")
async def create_domain_brute(domain: DomainIn):
    task_id = sub_domain_brute(domain.domain)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "task_id": str(task_id)
        }
    )


@router.post("/ip/create")
async def create_ip_scan(data: IPIn):
    ip = data.ip
    ports = data.ports
    task_id = await nmap_scan(ip, ports)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "task_id": str(task_id)
        }
    )


@router.get("/task/status/{task_id}")
async def get_task_status_by_id(task_id: str):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "detail": get_celery_task_status(task_id)
        }
    )


@router.get("/task/result/{task_id}")
async def get_task_result_by_id(task_id: str):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "detail": get_celery_task_result(task_id)
        }
    )
