import os
import sqlite3
from describe_sql_table import get_tables_and_columns

def execute_query(sql_query):
    conn = sqlite3.connect('sqlDB.db')
    cursor = conn.cursor()
    cursor.execute(sql_query)

    results = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    conn.close()
    print(f'results = {results}')
    print(f'columns = {column_names}')
    # return results, column_names


sql_table = get_tables_and_columns()
print(sql_table)
query = input('Enter valid sql query about the table: ')
execute_query(query)
