import xlwings as xw
import pandas as pd

#wb=xw.Book()
#wb.save('test.xlsx')
#wbtest=xw.Book('data.xlsx')
#wb1=wbtest.sheets['Sheet1']
#wb1.range('A1').value='hello'
wb =xw.Book('Class.xlsx')
sheet= wb.sheets("ClassA")
#rg=sheet.range('A').value
#sheet.range('C2').value=' helloxlwings'
df =sheet.range('A1:C3').options(pd.DataFrame).value    #import pandas as pd
#print(df)
df=df[:2]
xw.view(df)
wb.close

