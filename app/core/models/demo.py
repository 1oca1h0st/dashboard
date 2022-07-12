from sqlalchemy import Column, String, Integer

from core.db.mysql import Base


class Demo(Base):
    __tablename__ = "demo"

    id = Column(Integer, primary_key=True, unique=True)
    description = Column(String)
