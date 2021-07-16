"""
Результаты запроса сохраняем в формат Excel
"""
from utils_format import query_to_excel2003, query_to_excel2007
from db import DbManager

query = 'exec rep_counter_exp @tip_str=:tip_str, @fin_id1=:fin_id'
params = {"tip_str": 2, 'fin_id': 233}

query_result = DbManager().get_execute_sql(query, params)
# print(query_result)

# # # xlsx (Excel 2007 и выше) - openpyxl, xlsxwriter
# file_name = 'src/files/data.xlsx'
# query_to_excel2007(query_result, file_name)


# xls (Excel 2003) - import xlrd, xlwt
file_name = 'files/data.xls'

# список полей с наименованиями для вывода
columns = {
    'row_num': '№ п/п',
    'occ': 'Лицевой счёт',
    'street': 'Улица',
    'nom_dom': 'Дом',
    'Корпус': 'Корпус',
    'nom_kvr': 'Квартира',
    'type': 'Тип',
    'serial_number': 'Серийный номер',
    'date_create': 'Дата установки',
    'PeriodCheck': 'Период поверки',
    'value_pred': 'Показания предыдущие',
    'Показания предыдущие (ночь)': 'Показания предыдущие (ночь)',
    'inspector_value': 'Текущие показания',
    'Показания текущие (ночь)': 'Показания текущие (ночь)',
    'inspector_date': 'Дата текущих показаний',
    'actual_value': 'Фактический расход',
    'Фактический расход (ночь)': 'Фактический расход (ночь)',
}

with open(file_name, 'wb') as f:
    xls = query_to_excel2003(query_result,
                       sheet_name='Лист 1',
                       startrow=6,
                       columns=columns
                       )
    f.write(xls)
