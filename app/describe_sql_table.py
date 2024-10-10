import sqlite3
import os


def get_tables_and_columns():

    conn = sqlite3.connect('sqlDB.db')
    cursor = conn.cursor()

    cursor.execute("SELECT tbl_name FROM sqlite_master WHERE type = 'table';")
    tables = cursor.fetchall()

    res = {}

    for table in tables:
        table_name = table[0]

        cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = cursor.fetchall()

        column_names = [col[1] for col in columns]
        res[table_name] = column_names

    conn.close

    return res

if __name__ == "__main__":
     
    res = get_tables_and_columns()
    print(res)
