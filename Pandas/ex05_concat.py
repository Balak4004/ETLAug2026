
# concat() in pandas is used to combine two or more DataFrames.
# The main difference from merge() is:

# merge() → combines DataFrames based on matching column values (like SQL JOIN).
# concat() → combines DataFrames vertically (rows) or horizontally (columns).

# axis=0  → down ↓  → rows
# axis=1  → across → → columns

import pandas as pd

df_emp = pd.read_csv(r"G:\ETLAug2026\Data\emp1.csv")
df_dept = pd.read_csv(r"G:\ETLAug2026\Data\dept.csv")
df_loc = pd.read_csv(r"G:\ETLAug2026\Data\location.csv")

df1 = pd.concat([df_emp,df_dept],axis=0)
print(df1)

df2 = pd.concat([df_emp,df_dept], axis=1)
print(df2)

# concat 3 data frames
df3 = pd.concat([df_emp,df_dept,df_loc],axis=1)
print(df3)

# concat 3 data frames
# display all columns in output
df4 = pd.concat([df_emp,df_dept,df_loc],axis=1)
pd.set_option('display.width', None)
print(df4)