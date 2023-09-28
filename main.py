# Реализовать фастапи приложение в докере со всеми видами запросов
# (get, retrieve (это вытянуть не все обьекты, а 1 по id), update (put, patch), post, delete)


# import requests
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


app = FastAPI(title="My first app")

# создаем сессию для работы с БД из предыдущего ДЗ
engine = create_engine("sqlite:///university_hw15.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class University(Base):
    """
    class for information about universities DB
    """
    __tablename__ = "university"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    website = Column(String(100), nullable=False)
    country = Column(String(50), nullable=False)


class UniversityAPI(BaseModel):
    """
    class for information about universities API
    """
    name: str
    website: str
    country: str


# GET показать все объекты
@app.get('/read_all')
def read_base():
    """
    read information from base
    :return:
    """
    return session.query(University).all()


# RETRIEVE вытянуть не все объекты, а 1 по id
@app.get('/read_uni_id/{search_id}')
def read_base(search_id: int):
    """
    read information from base
    :return:
    """
    return session.get(University, search_id).__dict__


# PUT - обновление всех полей
@app.put("/upd_uni/{uni_id}")
def update_uni(uni_id: int, new_uni: UniversityAPI):
    """

    :param uni_id:
    :param new_uni:
    :return:
    """
    old_uni = session.query(University).get(ident=uni_id)
    old_uni.country = new_uni.country
    old_uni.website = new_uni.website
    old_uni.name = new_uni.name
    session.add(old_uni)
    session.commit()


# PATCH - обновление не всех полей
@app.patch("/upd_uni_field/{uni_id}")
def update_field_uni(uni_id: int, new_uni: UniversityAPI):
    """

    :param uni_id:
    :param new_uni:
    :return:
    """
    old_uni = session.query(University).get(ident=uni_id)
    # string - как в приложеньке прописано
    old_uni.country = old_uni.country if new_uni.country == "string" else new_uni.country
    old_uni.website = old_uni.website if new_uni.website == "string" else new_uni.website
    old_uni.name = old_uni.name if new_uni.name == "string" else new_uni.name
    session.add(old_uni)
    session.commit()
    return "successful update"


# POST - добавляем новую запись
@app.post("/add_new_uni")
def create_uni(new_uni: UniversityAPI):
    """

    :param new_uni:
    :return:
    """
    add_uni = University()
    add_uni.country = new_uni.country
    add_uni.website = new_uni.website
    add_uni.name = new_uni.name
    session.add(add_uni)
    session.commit()
    return "successful add"


# DELETE - удаляем запись по ID
@app.delete("/del_by_id/{uni_id}")
def delete_uni(uni_id: int):
    """

    :param uni_id:
    :return:
    """
    del_uni = session.query(University).get(ident=uni_id)
    session.delete(del_uni)
    session.commit()
    return "successful delete"


# "country": "Germany",
# "id": 1,
# "name": "AKAD Hochschulen für Berufstätige, Fachhochschule Leipzig",
# website": "http://www.akad.de/"
