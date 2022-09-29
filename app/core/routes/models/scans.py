from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from core.controllers.scans import sub_domain_brute
from core.schemas.mongo.domains import DomainIn

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
