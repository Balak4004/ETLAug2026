
import pandas as pd


df1 = pd.read_csv(r"G:\ETLAug2026\Data\emp2.csv")
print(df1)
df2 = pd.read_csv(r"G:\ETLAug2026\Data\emp3.csv")
print(df2)

# union all
df_unionall = pd.concat([df1,df2], axis=0)
print(df_unionall)

# union
df_unionall = pd.concat([df1,df2], axis=0).drop_duplicates()
print(df_unionall)

# for getting intersection like sql use inner
df_intersect = df1.merge(df2,how='inner')
print(df_intersect)