"""
Результаты запроса сохраняем в формат XML
"""
from db import DbManager
from lxml import etree

query = 'exec rep_counter_exp @tip_str=:tip_str, @fin_id1=:fin_id'
params = {"tip_str": 2, 'fin_id': 233}

query_result = DbManager().get_execute_sql(query, params)
# print(query_result)

file_name = 'files/data.xml'

root_name = 'items'
row_name = 'item'
attr_cols = ['occ', 'kol_people', 'service_id']
elem_cols = ['short_street', 'nom_dom', 'nom_kvr', 'serial_number', 'inspector_date', 'inspector_value']


def query_to_xml(root_name='items',
                 row_name='item',
                 attr_cols=[],
                 elem_cols=[]) -> str:
    """ 
    Получение результатов запроса в XML
    attr_cols - список полей для атрибутов
    elem_cols - список полей для элементов
    """
    root = etree.Element(root_name)
    for row in query_result:
        root_item = etree.SubElement(root, row_name)
        for col in elem_cols:
            etree.SubElement(root_item, col).text = str(row.get(col))
        for col in attr_cols:
            root_item.set(col, str(row.get(col)))

    xml_str = etree.tostring(root, pretty_print=True, encoding="utf-8", method="xml", xml_declaration=True).decode(
        encoding="utf-8")
    # with open(file_name, 'w', encoding='utf-8') as f:
    #     f.write(xml_str)
    return xml_str


xml_text = query_to_xml(root_name='root',
                        row_name='item',
                        attr_cols=attr_cols,
                        elem_cols=elem_cols)
print(xml_text)

with open(file_name, 'w', encoding='utf-8') as f:
    f.write(xml_text)
