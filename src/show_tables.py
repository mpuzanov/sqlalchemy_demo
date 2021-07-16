"""
получение списка таблиц в базе
"""
from db import engine
from sqlalchemy import inspect, MetaData



print('1 вариант','='*60)
# 1 вариант работает быстрее второго
inspector = inspect(engine)
schemas = inspector.get_schema_names(default_schema_name='dbo')

for schema in schemas:
    print(f"schema: {schema}")
    if schema == 'dbo':
        for table_name in inspector.get_table_names(schema=schema):
            print(f"Table:{table_name}")
            # for column in inspector.get_columns(table_name, schema=schema):
            #     print(f"Column: {column}")

print('2 вариант','='*60)

metadata = MetaData()
metadata.reflect(bind=engine)
for table in metadata.sorted_tables:
    print(table)
