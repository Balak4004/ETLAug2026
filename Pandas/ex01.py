

import pandas as pd

df = pd.read_csv(r'G:\ETLAug2026\Data\emp.csv')
print(df.head())

df1 = (df[['eno',"ename"]])
print(df1.head())

# where condition
df2 = df[df['eno']==5]
print(df2)

df3 = df[df['eno']<=5]
print(df3)

# where with and (&) condition
df4 = df[(df['deptno']==10) & (df['salary']>2500)]
print(df4)

# where with or (|) condition
df5 = df[(df['eno']==21) | (df['ename']=='Seema')]
print(df5)

# Returns rows where 'ename' starts the letter 'S'
# Catch both 'J' and 'j' at the start of a name
df6 = df[df['ename'].str.lower().str.startswith('J', na=False)]
print(df6)

# Returns rows where 'ename' ends the letter 'S'
# Catch both 'H' and 'h' at the start of a name
df7 = df[df['ename'].str.lower().str.startswith('h', na=False)]
print(df7)

# Returns rows where 'ename' ends the letter 'S'
# Catch both 'D' and 'd' at the start of a name
df8 = df[df['ename'].str.lower().str.contains('k', na=False)]
print(df8)

# sorting by column
df9 = df[(df['deptno']==10) & (df['salary']>=2000)].sort_values(by='salary')
print(df9)

# sorting by column in descending order
df10 = df[(df['deptno']==10) & (df['salary']>=2000)].sort_values(by='salary', ascending=False)
print(df10)

# sorting by column in ascending and descending order
df11 = df.sort_values(by=['deptno','salary'], ascending=[True, False])
print(df11)

# change data type of columns
df12 = df.astype({'salary':'float', 'doj':'datetime64[ns]'}).head()
print(df12)
print(df12.dtypes)

# display date column as dd-mm-yyyy format
df13 = df.astype({'salary':'float', 'doj':'datetime64[ns]'}).head()
df13['doj'] = df13['doj'].dt.strftime('%d-%m-%Y')
print(df13)
print(df13.dtypes)

# select data between specific dates
df = df.astype({'doj':'datetime64[ns]'})
df14 = df.sort_values(by='doj', ascending=True)
df14 = df14[(df14['doj'] >= '2015-01-01') & (df14['doj'] <= '2016-12-31')]
df14 = df14.sort_values(by='deptno', ascending=True)
print(df14)

