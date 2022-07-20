from pickle import TRUE
import openpyxl

book = openpyxl.load_workbook(r'C:\Users\user\Downloads\New folder (3)\class.xlsx')
sheet = book["ClassA"]
for row in sheet.iter_rows(min_row=1,max_row=5,min_col=3,max_col=6,values_only=TRUE):
    print(row)