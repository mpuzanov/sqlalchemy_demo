from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import text, inspect

engine = create_engine('mssql+pyodbc://sa:123@localhost:1433/kr1?driver=SQL+Server+Native+Client+11.0',
                       fast_executemany=True, echo=False)
meta = MetaData()

streets = Table(
    'Streets', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('prefix', String),
    Column('kod_fias', String),
    Column('full_name', String),
    Column('full_name2', String),
)

# s = streets.select().order_by('name').limit(50)
# conn = engine.connect()
# result = conn.execute(s)
# for row in result:
#     print(row)

# result = engine.execute("select id, name from towns")
# for row in result:
#     print(row)

# result = engine.execute("select id, name from towns")
# print(result.fetchall())

# result = engine.execute("select id, name from towns")
# print(result.fetchall())

# t = text("select id, name from towns where id=:id")
# result = engine.execute(t, id=3)
# print(result.fetchall())

print(engine.table_names())

print('-------------')  


# for t in meta.tables:
#     print(meta.tables[t])


# for t in meta.sorted_tables:
#     print(t.name)
