import snowflake.connector
import os

conn = snowflake.connector.connect(
    user = 'PANDA',
    password = os.getenv('SNOWSQL_PWD'),
    account = 'JSA18243',
    warehouse = 'PANDA_WH',
    database = 'PANDA_DB',
    schema = 'PANDA_SCHEMA'
)

cur = conn.cursor()

try:
    cur.execute('select * from members')

    results = cur.fetchall()

    for result in results:
        print(result)

finally:
    cur.close()
conn.close()