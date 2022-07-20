import pandas as pd #df = dataframe
df =pd.read_excel(r'C:\Users\user\Downloads\New folder (3)\class.xlsx',engine="openpyxl")

#results = df.columns
#results = df.iloc[:5,2:5]
#results = df[df[''].str.contains('')]
#results = df[df[''].str.match('')]
#results=df.groupby('AGE')
#print(results.get_group('A').mean())