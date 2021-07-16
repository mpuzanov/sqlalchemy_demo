"""
Выборки из существующих таблиц в базе
"""
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

meta = MetaData()

streets = Table('streets', meta, autoload_with=engine)
print('streets:',[c.name for c in streets.columns])

towns = Table('towns', meta, autoload_with=engine)
print('towns:',[c.name for c in towns.columns])



# table = Table('Users', meta, autoload=True, autoload_with=engine, schema='dbo')
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()
# result = session.query(table).all()
# print(result[0])
