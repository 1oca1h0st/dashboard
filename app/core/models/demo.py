from sqlalchemy import Column, String, Integer
from core.db.base_class import Base


class Demo(Base):
    __tablename__ = "demo"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(60))
    add_column = Column(String(255))