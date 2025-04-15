import pandas as pd

data={
    'Name':['John', 'Anna', 'Peter', 'Linda'],
    'Age':[10,12,13,14],
    'Grade':[1,2,3,4]
}

df=pd.DataFrame(data)
df.to_csv('students.csv',index=False)
df=pd.read_csv('students.csv')
print(df)