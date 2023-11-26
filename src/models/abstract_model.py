from sqlalchemy import Column, Integer

from src.core.db import Base


class AbstractModel(Base):
    """
    abstract class
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
