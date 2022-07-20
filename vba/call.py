import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets('sheet1')
    sheet['A1'].value ="called from vba"