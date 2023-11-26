from sqlalchemy.orm import Session

from src.core.mixins.base_mixin import BaseMixin


class CreateMixin(BaseMixin):

    @classmethod
    def create(cls, input_data, session: Session):
        """
        create new item in DB
        """
        new_item = cls.table(**input_data)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item
