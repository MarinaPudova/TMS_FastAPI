from sqlalchemy import Column, String

from src.models.abstract_model import AbstractModel


class University(AbstractModel):
    """
    class for information about universities DB
    """
    __tablename__ = "university"
    name = Column(String(150), nullable=False)
    website = Column(String(100), nullable=False)
    country = Column(String(50), nullable=False)
