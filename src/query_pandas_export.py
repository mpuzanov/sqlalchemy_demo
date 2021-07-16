"""
Выгрузки результатов запроса с помощью PANDAS
"""
import pandas as pd
from db import engine
from sqlalchemy import text
import json


sql = 'exec rep_counter_exp @tip_str=:tip_str, @fin_id1=:fin_id'
params = {"tip_str": 2, 'fin_id': 233}

df = pd.read_sql(text(sql), engine, params=params)

print(df.head())

# =============================================================================================
# Excel
# xlsx (Excel 2007 и выше) - openpyxl, xlsxwriter
# xls (Excel 2003) - import xlrd, xlwt

# file_name = 'pandas_data.xls'
# columns = ["street", "nom_dom", 'nom_kvr',
#            'serial_number', 'inspector_date', 'inspector_value']
# headers = ["Улица", "Дом", 'Квартира',
#            'Серийный номер', 'Дата показания', 'Значение']
# with pd.ExcelWriter(file_name) as writer:
#     df.to_excel(writer,
#                 sheet_name='counter_exp',
#                 index=False,
#                 startrow=6,
#                 columns=columns,
#                 header=headers,
#                 engine='xlwt')

# =============================================================================================
# CSV
# file_name = 'pandas_data.csv'
# df.to_csv(file_name, sep=";", index=False)

# =============================================================================================
# JSON
# file_name = 'pandas_data.json'
# df.to_json(file_name, orient="records", force_ascii=False, indent=4)

# result = df.to_json(orient="records", force_ascii=False)
# parsed = json.loads(result)
# print(json.dumps(parsed, indent=4, ensure_ascii=False))

# =============================================================================================
# # XML
# # pandas version 1.3.0., pip install lxml
# # https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.to_xml.html#pandas.DataFrame.to_xml
# file_name = 'pandas_data.xml'
# df.to_xml(file_name,
#           root_name='items',
#           row_name='item',
#           index=False,
#           attr_cols=['occ', 'kol_people', 'service_id'],
#           elem_cols=['short_street', 'nom_dom', 'nom_kvr', 'serial_number', 'inspector_date', 'inspector_value'])

# result = df.to_xml(root_name='items',
#                    row_name='item',
#                    index=False,
#                    attr_cols=['occ', 'kol_people', 'service_id'],
#                    elem_cols=['short_street', 'nom_dom', 'nom_kvr', 'serial_number', 'inspector_date', 'inspector_value'])
# print(result)
