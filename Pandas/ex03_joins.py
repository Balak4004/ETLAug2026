
import pandas as pd

df1 = pd.read_csv(r"G:\ETLAug2026\Data\emp.csv")
print(df1.head())
df2 = pd.read_csv(r"G:\ETLAug2026\Data\dept.csv")
print(df2.head())
df3 = pd.read_csv(r"G:\ETLAug2026\Data\location.csv")
print(df3.head())

merge1 = df1.merge(df2, how='inner', on='deptno')
print(merge1.head())
merge2 = merge1.merge(df3,how='inner',on='location')
print(merge2.head(10))
