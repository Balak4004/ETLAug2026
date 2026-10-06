
import pandas as pd

df = pd.read_csv(r"G:\ETLAug2026\Data\emp.csv")
print(df.head())

# count of all rows in csv file
print(len(df))
print(df.shape[0])

# count of employees by dept wise
# reset_index to put result into dataframe
# name='emp_count' to rename eno as emp_count
# if eno contains NULL values: then ['eno'] will not count NULL eno values.
agg_data = df.groupby('deptno')['eno'].count().reset_index(name='emp_count')
print(agg_data)

# size() will count all rows
agg_data1 = df.groupby('deptno').size().reset_index(name='emp_count')
print(agg_data1)

# agg count min max avg sum
# in pandas for avg use mean
# round({'avg_sal':2}) .round() is used for numeric columns format
agg_data2 = df.groupby('deptno')['salary'].agg(emp_count='count',
                                               max_sal = 'max',
                                               min_sal = 'min',
                                               total_sal = 'sum',
                                               avg_sal = 'mean').reset_index().round({'avg_sal':2})
print(agg_data2)

# to rename the columns pass them as dict
agg_data3 = agg_data2.rename(columns={'deptno':'deptno','max_sal':'MaximumSal',
                          'min_sal':'MinimumSal','total_sal':'TotalSal',
                          'avg_sal':'AvergaeSal'})
print(agg_data3)

# write agg_data3 data to csv file --> G:\ETLAug2026\Pandas\emp_salary_summary.csv
agg_data3.to_csv('emp_salary_summary.csv',index=False)


df2 = pd.read_csv(r"G:\ETLAug2026\Data\emp.csv")
print(df2.head())

# group by more than one column
agg_df2 = df2.groupby(['deptno','location']).size().reset_index(name='emp_count')
print(agg_df2)

agg_df3 = df2.groupby(['deptno','location'])['eno'].count().reset_index(name='emp_count')
print(agg_df3)

# filter and group by
agg_df4 = df2[df2['deptno']==20].groupby(['deptno','location']).size().reset_index(name='emp_count')
print(agg_df4)

#  first filter and then group by and filter the group by data
df3 = pd.read_csv(r"G:\ETLAug2026\Data\emp.csv")
print(df3.head())

agg_df_2 = df3[df3['location']!='Chennai'].groupby('deptno')['salary'].agg(total_sal='sum').reset_index()
agg_df_2 = agg_df_2[agg_df_2['total_sal']>20000]
print(agg_df_2)

agg_df_3 = df3[df3['location']!='Chennai'].groupby(['deptno'])['salary'].sum().reset_index(name='Total_sal')
agg_df_3 = agg_df_3[agg_df_3['Total_sal']>20000]
print(agg_df_3)
