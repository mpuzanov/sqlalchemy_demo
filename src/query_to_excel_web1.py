"""
Оборотка по лицевым
"""
from utils_format.excel2007_2 import query_to_excel2007_2
from db import DbManager

# Оборотка по лицевым
query = 'exec rep_10 @fin_id=:fin_id, @tip_id=:tip_id, @fin_id2=:fin_id2'
params = {"tip_id": 2, 'fin_id': 238, 'fin_id2': 238}
query_result = DbManager().get_execute_sql(query, params)
# print(query_result)

columns_lst = [
    {'field': 'start_date', 'name': 'Фин_период', 'width': 15},
    {'field': 'SALDO', 'name': 'Вх.сальдо', 'format': '#,##0.#0', 'width': 15, 'func': 'sum'},
    {'field': 'value', 'name': 'Начисл.', 'width': 15, 'func': 'sum'},
    {'field': 'Added', 'name': 'Разовые', 'width': 15, 'func': 'sum'},
    {'field': 'Discount', 'name': 'Льгота', 'width': 15, 'func': 'sum'},
    {'field': 'compens', 'name': 'Субсидия', 'width': 15, 'func': 'sum'},
    {'field': 'paid', 'name': 'Пост.нач.', 'width': 15, 'func': 'sum'},
    {'field': 'PaymAccount', 'name': 'Оплатил', 'width': 15, 'func': 'sum'},
    {'field': 'PaymAccount_peny', 'name': 'Из них пени', 'width': 15, 'func': 'sum'},
    {'field': 'Debt', 'name': 'Исх.сальдо', 'width': 15, 'func': 'sum'},
    {'field': 'Penalty_old', 'name': 'Пени прошл.', 'width': 15, 'func': 'sum'},
    {'field': 'Penalty_old_new', 'name': 'Пени с учетом оплаты', 'width': 15, 'func': 'sum'},
    {'field': 'Penalty_added', 'name': 'Пени разовые', 'width': 15, 'func': 'sum'},
    {'field': 'penalty_value', 'name': 'Пени текущие', 'width': 15, 'func': 'sum'},
    {'field': 'penalty_itog', 'name': 'Пени итог', 'width': 15, 'func': 'sum'},
    {'field': 'whole_payment', 'name': 'К оплате', 'width': 15, 'func': 'sum'},
    {'field': 'DatePaym', 'name': 'Дата опл.', 'width': 20},
    {'field': 'person_status', 'name': 'Статус пр.', 'width': 20},
    {'field': 'KolPeople', 'name': 'Кол.чел.', 'width': 15, 'func': 'sum'},
    {'field': 'proptype', 'name': 'Статус кв.', 'width': 15},
    {'field': 'status_id', 'name': 'Статус лиц.', 'width': 15},        
    {'field': 'lgota', 'name': 'Льготы', 'width': 15},
    {'field': 'total_sq', 'name': 'Площадь', 'width': 20, 'func': 'sum'},
    {'field': 'occ', 'name': 'Ед.лиц.', 'width': 15},
    {'field': 'streets', 'name': 'Улица', 'width': 30},
    {'field': 'nom_dom', 'name': '№д', 'width': 15},
    {'field': 'nom_kvr', 'name': '№ кв.', 'width': 15},
    {'field': 'index_postal', 'name': 'Индекс', 'width': 15},            
    {'field': 'id_els_gis', 'name': 'ЕЛС в ГИС ЖКХ', 'width': 20},
    {'field': 'id_nom_gis', 'name': 'Код помещения в ГИС ЖКХ', 'width': 20},
    {'field': 'id_jku_gis', 'name': 'УИ в ГИС ЖКХ', 'width': 20},
]

# xlsx (Excel 2007 и выше) - openpyxl, xlsxwriter
sheet_name = 'Оборотка_по_лицевым'
file_name = 'src/files/Оборотка_по_лицевым.xlsx'
query_to_excel2007_2(query_result,
                     file_name=file_name,
                     sheet_name=sheet_name,
                     startrow=2,
                     columns=columns_lst)

