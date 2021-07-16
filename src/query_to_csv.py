"""
Результаты запроса сохраняем в формат CSV
"""
import csv
from io import StringIO

from db import DbManager

sql = 'exec rep_counter_exp @tip_str=:tip_str, @fin_id1=:fin_id'
params = {"tip_str": 2, 'fin_id': 233}

result = DbManager().get_execute_sql(query=sql, params=params)

# ======================================================
# CSV
file_name = 'files/data.csv'


def save_dict_to_csv(output, data):
    col_names = data[0].keys()

    writer = csv.DictWriter(
        output,
        fieldnames=col_names,
        extrasaction='ignore',
        delimiter=";"
    )

    writer.writeheader()  # сохранение полей в первой строке
    writer.writerows(data)

    # запись по одной строке
    # for row in data:
    #     writer.writerow(row)

    output.seek(0)
    return output


# Получение CSV в памяти (без сохранения в файл, можно послать пользователю)
# str_output = StringIO()
# save_dict_to_csv(str_output, result)
# print(str_output.read())

with open(file_name, 'w', encoding='utf8', newline="") as fp:
    save_dict_to_csv(fp, result)

with open(file_name, "r", encoding='utf8', newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
