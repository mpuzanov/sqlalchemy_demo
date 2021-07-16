from typing import Text
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
meta = MetaData()


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = {"schema": "dbo"}  # не обязательно
    id = Column(Integer, primary_key=True)
    login = Column(String)
    pswd = Column(String)
    Initials = Column(String)


Session = sessionmaker(bind=engine)
session = Session()

# def row2dict(row):
#     """ Строку таблицы в словарь """
#     d = {}
#     for column in row.__table__.columns:
#         d[column.name] = str(getattr(row, column.name))
#     return d
row2dict = lambda row: {col.name: str(getattr(row, col.name)) for col in row.__table__.columns}

# ============================================================================

result = session.query(Users).all()
print('Users:')
for row in result:
    print(f"id: {row.id}, login: {row.login}, Initials: {row.Initials}")
    print(row2dict(row))

print('=' * 80)

user = session.query(Users).filter_by(login='repview').first()
print('filter_find', user)

print('=' * 80)

# получаем список словарей из запроса
rows = session.execute(Text('select id, name, prefix from Streets'))
# list_of_dicts = [{key: value for (key, value) in row._asdict().items()} for row in rows]
list_of_dicts = [{key: value for (key, value) in dict(row).items()} for row in rows]
print(list_of_dicts)
# for row in list_of_dicts:
#    print(row)
# ==================================================================
print('=' * 80)

units = Table('Units', meta, autoload=True, autoload_with=engine, schema='dbo')
s = units.select()
print('текст запроса: \n', s)
print('данные:')
result = session.execute(units.select())
for row in result:
    print(row._asdict())
result.close()

print('=' * 80)


class Units(Base):
    __tablename__ = 'Units'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    short_id = Column(String)
    precision = Column(Integer)
    short_id2 = Column(String)


result = session.query(Units).all()
print('table:')
for row in result:
    print(row2dict(row))
