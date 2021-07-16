"""
xlsx (Excel 2007 и выше) - openpyxl, xlsxwriter
"""
import openpyxl


def query_to_excel2007(query_result, file_name: str = 'file.xlsx', sheet_name: str = 'Лист 1'):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet_name

    header_list = query_result[0].keys()
    ws.append([i for i in header_list])  # добавляем заголовки
    row = 2
    for item in query_result:
        for col, col_name in enumerate(header_list):
            ws.cell(row=row, column=col+1, value=item.get(col_name))
        row += 1

    wb.save(file_name)
