import xlwings as wx

def main():
    wb = xlwings.Book.caller()
    sheet = wb.sheets('sheet1')
    sheet['A1'].value ="called from vba"

wb = wx.Book('vba.xlsx',password='pass')
ws=wb.sheets('Sheet1')
wc=ws.range('A10').value ="hello"

print(wc)

