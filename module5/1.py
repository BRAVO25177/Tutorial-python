import pandas as pd

df=pd.read_csv('stud_data.csv')
print(df['CGPA'].mean())
print(df[df['CGPA']>9])
print(df[(df['Branch']=='CSE')&(df['CGPA']>9)])
print(df[df['CGPA']==df['CGPA'].max()])
avg_CGPA=df.groupby('Branch')['CGPA'].mean()
print(avg_CGPA)