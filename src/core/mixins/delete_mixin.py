from sqlalchemy import delete
from sqlalchemy.orm import Session

from src.core.mixins.base_mixin import BaseMixin


class DeleteMixin(BaseMixin):

    @classmethod
    def delete(cls, pk: int, session: Session) -> dict:
        """
        delete item
        """
        query = delete(cls.table).where(cls.table.id == pk)
        cls.execute_commit(query=query, session=session)
        return {'status': 'success'}
