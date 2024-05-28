# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import snowflake.connector as sf

def print_hi():
  print('hello')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    conn = sf.connect(
        user='PRADIP33Z',
        password='Hallowin@13',
        account='uh16987.ap-southeast-1'
    )
    conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
    conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")
    conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb")
    conn.cursor().execute("USE DATABASE testdb")
    conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema")
    conn.cursor().execute("USE SCHEMA testschema")
    conn.cursor().execute(
        "CREATE OR REPLACE TABLE "
        "test_table(col1 integer, col2 string)")
    conn.cursor().execute(
        "INSERT INTO test_table(col1, col2) "
        "VALUES(123, 'test string1'),(456, 'test string2')")
    col1, col2 = conn.cursor().execute("SELECT col1, col2 FROM test_table").fetchone()
    print('{0}, {1}'.format(col1, col2))
    print("emp table below")
    for(col1, col2) in  conn.cursor().execute("SELECT empid, salary FROM  pradipz.My_schema.emp order by empid"):
     print('{0}, {1}'.format(col1, col2))
    conn.close()
    --jfenfi
# See PyCharm help at https://www.jetbrains.com/he