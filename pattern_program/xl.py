# Importing pandas
import pandas as pd

u2 = urllib.request.urlopen('http://finance.yahoo.com/q?s=aapl&ql=1')

for lines in u2.readlines():
    print (lines)
# The webpage URL whose table we want to extract
url = "https://www.geeksforgeeks.org/extended-operators-in-relational-algebra/"
  
# Assign the table data to a Pandas dataframe
table = pd.read_html(url)[0]
  
# Print the dataframe
print(table)
# Importing pandas
import pandas as pd
  
# The webpage URL whose table we want to extract
url = "https://www.geeksforgeeks.org/extended-operators-in-relational-algebra/"
  
# Assign the table data to a Pandas dataframe
table = pd.read_html(url)[0]
  
# Store the dataframe in Excel file
table.to_excel("data.xlsx")