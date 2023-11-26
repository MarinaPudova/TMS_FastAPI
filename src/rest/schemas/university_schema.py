from typing import Optional

from pydantic import BaseModel


class UniversityCommonSchema(BaseModel):
    """
    common-schema-class for information about universities
    """
    name: str
    website: str
    country: str


class UniversityListSchema(BaseModel):
    """
    list-schema-class for information about universities
    """
    id: int
    name: str
    website: str
    country: str


class UniversityPartUpdateSchema(BaseModel):
    """
    part-update-schema-class for information about universities
    """
    name: Optional[str] = None
    website: Optional[str] = None
    country: Optional[str] = None
