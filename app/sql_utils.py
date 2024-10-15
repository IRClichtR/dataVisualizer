import sqlite3
import os



def get_tables_and_columns(db_path):

    conn = sqlite3.connect(db_path)
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

    conn.close()

    return res


def execute_query(sql_query, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql_query)

    results = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    conn.close()

    return results, column_names


def get_filtered_data(db_path, table_name, columns, page, per_page, filters, search_query):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    query = f'SELECT * FROM {table_name} WHERE 1=1'
    params = []

    for column, value in filters.items():
        if value and column in columns:
            query += f' AND {column} LIKE ?'
            params.append(f'%{value}%')

    if search_query:
        query += ' AND ('
        query += 'OR '.join([f'{col} LIKE ?' for col in columns])
        query += ')'
        params.extend([f'%{search_query}%'] * len(columns))

    if page == 1:
        offset = per_page
    else:
        offset = (page - 1) * per_page
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])

    cursor.execute(query, params)
    rows = cursor.fetchall()

    cursor.execute(f'SELECT COUNT(*) FROM {table_name} WHERE 1=1')
    total_rows = cursor.fetchone()[0]

    conn.close()

    return rows, total_rows
