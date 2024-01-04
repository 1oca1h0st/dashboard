from datetime import datetime

from sqlalchemy import DateTime, Column
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import as_declarative, Mapped


@as_declarative()
class Base:
    id: int
    __name__: str
    created_at: Mapped[DateTime] = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at: Mapped[DateTime] = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="最近一次更新时间")

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
