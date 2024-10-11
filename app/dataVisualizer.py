from flask import Flask, request, render_template
import sqlite3
import os
from dotenv import load_dotenv
from search_by_llm_query import *
from sql_utils import *


load_dotenv()

db_path = os.getenv('DB_PATH')
db_table = get_tables_and_columns(db_path)
client = OpenAI(
    api_key=os.getenv('TEST_API_KEY'),
    organization=os.getenv('ORGA_ID'),
    project=os.getenv('PROJECT_ID')
)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        sql_query = question_to_sql(question, client, sql_table)
        results, column_names = execute_query(sql_query)
        summary = summarize_data(results, client)

        return render_template('results.html')

    return render_template('index.html')


@app.route('/explore_database', methods=['GET', 'POST'])
def explore_database():
    # get info on table to display
    selected_table = request.form.get('table_name', list(db_table.keys())[0])
    columns = db_table[selected_table]

    # Define page size and number of elements
    page = int(request.args.get('page', 1))
    per_page = 25
    
    # Filters for each column 
    filters = {col: request.form.get(col, '') for col in columns}

    # search by keywords
    search_query = request.form.get('search_query', '')

    # Get filtered data 
    rows, total_rows = get_filtered_data(db_path, selected_table, columns, page, per_page, filters, search_query)

    return render_template('explore_database.html', 
                           rows=rows, 
                           columns=columns, 
                           page=page, 
                           per_page=per_page, 
                           total_rows=total_rows, 
                           filters=filters, 
                           search_query=search_query, 
                           tables=list(db_table.keys()), selected_table=selected_table)


if  __name__ == '__main__':
    app.run(debug=True)
