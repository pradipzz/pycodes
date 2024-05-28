import snowflake.connector as sf
connection = sf.connect(
    user='PRADIP33Z',
    password='Hallowin@13',
    account='uh16987.ap-southeast-1'
    )
connection.cursor().execute("select * from pradipz.My_schema.emp")
connection.close()