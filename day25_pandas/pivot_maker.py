import pandas as pd

df = pd.read_csv('/home/rishells/rcdev/100daysOfPython/day25_pandas/googleplaystore.csv')
df2 = pd.read_csv('/home/rishells/rcdev/100daysOfPython/day25_pandas/fomix.csv')
df3 = pd.read_csv('/home/rishells/rcdev/100daysOfPython/day25_pandas/becas.csv')
print(list(df3)) # Print columns
#print(len(df.App.unique())) # Print unique values of a column

#pivot = pd.pivot_table(df,index=['Content Rating','Category'], values=['Rating'],columns=['Type'],aggfunc='count')
#pivot = pd.pivot_table(df2,index=['ENTIDAD FEDERATIVA (SUJETO DE APOYO)'], values=['MONTO'], columns=['ENTIDAD FEDERATIVA (FOMIX)'], aggfunc='sum') # index = agrupacion, 
#fillna('0',inplace=True)
#print(pivot)
pivot = pd.pivot_table(df3,index=['Nivel','Género'],values=['Institución'], columns=['País Destino'],aggfunc='count')


writer = pd.ExcelWriter('/home/rishells/rcdev/100daysOfPython/day25_pandas/pivote3.xlsx')
pivot.to_excel(writer,'Fomix')
writer.save()