from fastapi import APIRouter

from core.configs.logs import logger

router = APIRouter()


@router.get("/test")
@logger.catch
def test():
    return a+b
