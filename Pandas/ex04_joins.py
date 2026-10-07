
import pandas as pd

df_emp = pd.read_csv(r"G:\ETLAug2026\Data\emp1.csv")
print(df_emp)

df_dept = pd.read_csv(r"G:\ETLAug2026\Data\dept.csv")
print(df_dept)

# left join
df1 = df_emp.merge(df_dept,how='left', left_on = 'deptno',right_on='deptid')
print(df1)

# Right join

df2 = df_emp.merge(df_dept,how='right', left_on = 'deptno',right_on='deptid')
print(df2)

# full outer join
df3 = df_emp.merge(df_dept,how='outer', left_on = 'deptno',right_on='deptid')
print(df3)

# selecting only required columns from both dataframes
# way 1 before merge
df4 = df_emp[['eno','ename','deptno']].merge(df_dept[['deptid','deptname']], how='left',
                                             left_on = 'deptno',right_on='deptid')
print(df4)

# way 2 after merge
df5 = df_emp.merge(df_dept, how='left', left_on = 'deptno',right_on='deptid')
df5 = df5[['eno','ename','deptname']]
print(df5)

# If you want to join using two or more columns, pass a list of column names to on.
# df4 = df_emp.merge(df_dept,how='left',on=['deptno', 'location'])
# print(df4)