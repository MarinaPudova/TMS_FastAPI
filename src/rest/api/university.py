from fastapi import APIRouter, status

from src.core.db import session
from src.core.managers.university_manager import UniversityManager
from src.rest.schemas.university_schema import (
    UniversityCommonSchema,
    UniversityListSchema,
    UniversityPartUpdateSchema
)

router = APIRouter()


# GET показать все объекты
@router.get(path="/universities", response_model=list[UniversityListSchema], status_code=status.HTTP_200_OK)
def read_base():
    """
    read information from base
    :return: list of date from DB
    """
    return UniversityManager.list(session=session)


# RETRIEVE вытянуть не все объекты, а 1 по id
@router.get(path="/universities/{search_id}", response_model=UniversityListSchema, status_code=status.HTTP_200_OK)
def read_base_id(search_id: int):
    """
    read information about search-id-university from base
    :return: date about search-id-university
    """
    return UniversityManager.retrieve(pk=search_id, session=session)


# POST - добавляем новую запись
@router.post(path="/new_university", status_code=status.HTTP_201_CREATED)
def create_uni(new_uni: UniversityCommonSchema):
    """
    create new university in DB
    :param new_uni: info about new item
    :return:
    """
    return UniversityManager.create(input_data=new_uni.__dict__, session=session)


# PUT - обновление всех полей
@router.put(path="/upd_university/{uni_id}", response_model=UniversityCommonSchema, status_code=status.HTTP_202_ACCEPTED)
def update_uni(uni_id: int, new_uni: UniversityCommonSchema):
    """
    update all fields in item
    :param uni_id: id uni for update
    :param new_uni: new information for making changes
    :return:
    """
    return UniversityManager.update_all(pk=uni_id, input_data=new_uni.__dict__, session=session)


# PATCH - обновление не всех полей
@router.patch(path="/upd_university/{uni_id}", response_model=UniversityCommonSchema, status_code=status.HTTP_202_ACCEPTED)
def update_field_uni(uni_id: int, new_uni: UniversityPartUpdateSchema):
    """
    update some fields in item
    :param uni_id: id uni for update
    :param new_uni: new information for making changes
    :return:
    """
    return UniversityManager.update_some_fields(pk=uni_id, input_data=new_uni.__dict__, session=session)


# DELETE - удаляем запись по ID
@router.delete(path="/del_university/{uni_id}", status_code=status.HTTP_200_OK)
def delete_uni(uni_id: int):
    """
    delete item by id
    :param uni_id: id uni for delete
    :return:
    """
    return UniversityManager.delete(pk=uni_id, session=session)
