
import pandas as pd
from sqlalchemy import create_engine
import oracledb


# create a connection
# @ for this %40
mysql_conn = create_engine("mysql+pymysql://root:admin%402024@localhost:3306/retaildwh")
print(mysql_conn)

# read data from mysql db table and store in dataframe
df_target = pd.read_sql("select * from product",mysql_conn)
pd.set_option('display.width', None)
print(df_target)

# read data from csv
df_source = pd.read_csv(r"G:\ETLAug2026\Data\product.csv")
print(df_source)

df_source1 = pd.read_csv(r"G:\ETLAug2026\Data\product1.csv")
print(df_source1)

# compare product_id in csv and mysql table
df_productid = df_source['product_id'].isin(df_target['product_id'])
print(df_productid)
# compare product_id in csv and mysql table
df_productid1 = df_source1['product_id'].isin(df_target['product_id'])
print(df_productid1)

# ~ to reverse True and False
df_productid1 = ~df_source1['product_id'].isin(df_target['product_id'])
print(df_source1[df_productid1])

# source is oracle and target is mysql
# mismatch between source and target for product_id
# create oracle connection
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_20")
oracle_conn = create_engine("oracle+oracledb://hr:hr@localhost:1521/xe")
df_oracle = pd.read_sql("select * from product",oracle_conn )
print(df_oracle.head())

df_prodid1 = ~df_oracle['product_id'].isin(df_target['product_id'])
print(df_oracle[df_prodid1])

df_prodid2 = ~df_target['product_id'].isin(df_oracle['product_id'])
print(df_target[df_prodid2])

# compare product_id for csv and mysql table
# in csv product_id are not in same order as in mysql table
df_source3 = pd.read_csv(r"G:\ETLAug2026\Data\product3.csv")
print(df_source3.head())

df_productid3 =~df_source3['product_id'].isin(df_target['product_id'])
#print(df_productid3)
print(df_source3[df_productid3])


# source is csv and target mysql comparing all columns
df_source2 = pd.read_csv(r"G:\ETLAug2026\Data\product2.csv")
print(df_source2.head())

df_equal = df_source2.equals(df_target)
print(df_equal)

#assert df_source2.equals(df_target), "Data mismatch between product2 and mysql product table"

df_compare_all = df_source2.compare(df_target)
print(df_compare_all)

df_compare_all2 = df_target.compare(df_source2)
print(df_compare_all2)



