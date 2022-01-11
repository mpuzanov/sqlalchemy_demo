"""
Оборотка по услугам
"""
from utils_format.excel2007_2 import query_to_excel2007_2
from db import DbManager

# Оборотка по услугам
# rep_value_fin @fin_id1, @tip_id1, @build_id1, @sup_id
query = 'exec rep_value_fin @fin_id1=:fin_id, @tip_id1=:tip_id, @fin_id2=:fin_id2'
params = {"tip_id": 2, 'fin_id': 238, 'fin_id2': 239}
query_result = DbManager().get_execute_sql(query, params)
# print(query_result)
"""

"""
columns = {
    'row_num': '№ п/п',
    'start_date': 'Фин_период',
    'bldn_id': 'Код дома',
    'street': 'Улица',
    'nom_dom': 'Дом',
    'nom_kvr': 'Кварт.',
    'occ': 'Лицевой',
    'serv_name': 'Услуга',
    'unit_name': 'Ед. изм.',
    'SALDO': 'Нач. сальдо',
    'tarif': 'Тариф',
    'kol': 'Объём услуги',
    'kol_norma': 'Объём по норме',
    'kol_ipu': 'Объём ИПУ',
    'kol_opu': 'Объём ОПУ',
    'value': 'Начислено',
    'Discount': 'Льгота',
    'Added': 'Перерасчёты',
    'paid': 'Пост. начисл.',
    'PaymAccount': 'Оплачено',
    'PaymAccount_peny': 'из них пени',
    'Debt': 'Кон.сальдо',
    'metod': 'Метод',
    'occ_serv': 'Лиц.услуги',
    'compens': 'Субсидия',
    'tip_name': 'Тип фонда',

    # 'service_id': 'Код услуги',
    # 'paymaccount_serv': 'Оплачено по услуге',
    # 'kol_people': 'Кол граждан',
    # 'kol_people_serv': 'Кол граждан по услуге',
    # 'unit_id': 'Код ед.изм.',
}

columns_lst = [
    {'field': 'row_num', 'name': '№ п/п', 'width': 10},
    {'field': 'start_date', 'name': 'Фин_период', 'width': 15},
    {'field': 'bldn_id', 'name': 'Код дома', 'width': 10},
    {'field': 'street', 'name': 'Улица', 'width': 30},
    {'field': 'nom_dom', 'name': 'Дом', 'width': 15},
    {'field': 'nom_kvr', 'name': 'Кварт.', 'width': 15},
    {'field': 'occ', 'name': 'Лицевой', 'width': 15},
    {'field': 'serv_name', 'name': 'Услуга', 'width': 30},
    {'field': 'unit_name', 'name': 'Ед. изм.', 'width': 30},
    {'field': 'SALDO', 'name': 'Нач. сальдо',
        'format': '#,##0.#0', 'width': 15, 'func': 'sum'},
    {'field': 'tarif', 'name': 'Тариф', 'width': 15},
    {'field': 'kol', 'name': 'Объём услуги', 'width': 15},
    {'field': 'kol_norma', 'name': 'Объём по норме', 'width': 15},
    {'field': 'kol_ipu', 'name': 'Объём ИПУ', 'width': 15},
    {'field': 'kol_opu', 'name': 'Объём ОПУ', 'width': 15},
    {'field': 'value', 'name': 'Начислено', 'width': 15, 'func': 'sum'},
    {'field': 'Discount', 'name': 'Льгота', 'width': 15},
    {'field': 'Added', 'name': 'Перерасчёты', 'width': 15, 'func': 'sum'},
    {'field': 'paid', 'name': 'Пост. начисл.', 'width': 15, 'func': 'sum'},
    {'field': 'PaymAccount', 'name': 'Оплачено', 'width': 15, 'func': 'sum'},
    {'field': 'PaymAccount_peny', 'name': 'из них пени', 'width': 15, 'func': 'sum'},
    {'field': 'Debt', 'name': 'Кон.сальдо', 'width': 15, 'func': 'sum'},
    {'field': 'metod', 'name': 'Метод', 'width': 15},
    {'field': 'occ_serv', 'name': 'Лиц.услуги', 'width': 15},
    {'field': 'compens', 'name': 'Субсидия', 'width': 15},
    {'field': 'tip_name', 'name': 'Тип фонда', 'width': 30},
]


sheet_name = 'Оборотка по услугам выгрузка'
file_name = 'src/files/Оборотка_по_услугам.xlsx'
query_to_excel2007_2(query_result,
                     file_name=file_name,
                     sheet_name=sheet_name,
                     startrow=2,
                     columns=columns_lst)
