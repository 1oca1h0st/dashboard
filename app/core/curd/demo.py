from sqlalchemy.orm import Session
from fastapi import Depends
from core.curd.deps import get_db
from core.models import demo


def get_demo(db: Session, t_id: int):
    """
    根据ID获取demo数据
    :param t_id: 获取的数据ID
    :param db: 数据库会话
    :return: 返回ID对应的数据信息
    """
    return db.query(demo.Demo).filter(demo.Demo.id == t_id).first()
