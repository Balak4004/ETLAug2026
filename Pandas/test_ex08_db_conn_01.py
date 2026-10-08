
import pandas as pd
from sqlalchemy import create_engine
import oracledb
# import allure

# create a connection
mysql_conn = create_engine("mysql+pymysql://root:admin%402024@localhost:3306/retaildwh")
print(mysql_conn)
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_20")
oracle_conn = create_engine("oracle+oracledb://hr:hr@localhost:1521/xe")
print(oracle_conn)

# @allure.title("Test Data Comparison Between oracle and mysql Tables")
#  @allure.description("Test Data Comparison Between oracle and mysql Tables")
def test_compare_data():
    source_query = "select * from product"
    df_source = pd.read_sql(source_query, oracle_conn)
    #print(df_source.head())

    target_query = "select * from product"
    df_target = pd.read_sql(target_query, mysql_conn)
    #print(df_target.head())

    assert df_source.equals(df_target), "Data mismatch between source and target tables"

