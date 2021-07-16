""" 
запуск хранимых процедур
"""

from db import get_execute

sql = 'exec rep_10 @fin_id=:fin_id, @tip_id=:tip_id, @fin_id2=:fin_id2'
params = {"fin_id": 228, "tip_id": 2, "fin_id2": 228}

result = get_execute(sql, params)

# print(result)
for row in result:
    print(row.get('Occ'), row.get('Debt'))
