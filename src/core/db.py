from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# создаем сессию для работы с БД из предыдущего ДЗ
engine = create_engine("sqlite:///university_hw15.db", echo=False, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
