from sqlalchemy import update, select
from sqlalchemy.orm import Session

from src.core.mixins.base_mixin import BaseMixin


class UpdateMixin(BaseMixin):

    @classmethod
    def update_all(cls, pk: int, input_data: dict, session: Session) -> list:
        """
        update all fields in university-item
        """
        query = update(cls.table).where(cls.table.id == pk).values(**input_data)
        cls.execute_commit(query=query, session=session)
        result = session.execute(select(cls.table).where(cls.table.id == pk))
        return result.scalars().first()

    @classmethod
    def update_some_fields(cls, pk: int, input_data: dict, session: Session) -> list:
        """
        update some fields in university-item
        """
        # текущая инфо об университете
        obj = session.query(cls.table).get(pk).__dict__
        # составная инфо из существующих данных и измененных
        new_obj = {}
        for key, value in input_data.items():
            # если поле нужно изменять - берем новые данные
            if value is not None:
                new_obj[key] = value
            # если поле не нужно менять - используем старые
            else:
                new_obj[key] = obj[key]
        query = update(cls.table).where(cls.table.id == pk).values(**new_obj)
        cls.execute_commit(query=query, session=session)
        result = session.execute(select(cls.table).where(cls.table.id == pk))
        return result.scalars().first()
