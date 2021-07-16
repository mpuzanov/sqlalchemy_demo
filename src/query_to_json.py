"""
Результаты запроса сохраняем в формат JSON
"""
import json
import datetime
import decimal
from uuid import UUID

from db import DbManager

sql = 'exec rep_counter_exp @tip_str=:tip_str, @fin_id1=:fin_id'
params = {"tip_str": 2, 'fin_id': 233}

result = DbManager().get_execute_sql(sql, params)


# ======================================================
# JSON

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        if isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


file_name = 'files/data.json'

"""
json.dumps, json.loads - работает со строками
json.dump, json.load - работает с файлами
"""

# 1. вывод на экран
# json_str = json.dumps(result, indent=4, ensure_ascii=False, cls=Encoder)

# 2. сохранение в файл
with open(file_name, 'w', encoding='utf8') as fp:
    json.dump(result, fp, indent=4, ensure_ascii=False, cls=Encoder)

# 3. выборочное сохранение
data = {"tip_str": params.get('tip_str'), "items": []}
for item in result:
    if item.get("kol_people") == 4:
        data["items"].append(dict(zip(result[0].keys(), item.values())))
json_str = json.dumps(data, indent=4, ensure_ascii=False, cls=Encoder)
# print(data)

# проверка и вывод JSON
parsed = json.loads(json_str)
print(json.dumps(parsed, indent=4, ensure_ascii=False))
