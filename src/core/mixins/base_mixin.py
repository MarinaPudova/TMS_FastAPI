from typing import Optional, TypeVar

from sqlalchemy.orm import Session

from src.core.db import Base

TableType = TypeVar('TableType', bound=Base)


class BaseMixin:

    table: TableType = None

    @staticmethod
    def execute_commit(query, session: Session, values: Optional[list] = None) -> None:
        session.execute(query, values)
        session.commit()
