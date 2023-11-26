from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):

    @classmethod
    def list(cls, session: Session) -> list:
        """
        show all items from DB
        """
        query = select(cls.table)
        objects = session.execute(query)
        return list(objects.scalars().all())
