from flask import Flask, request, render_template
import sqlite3
from openai import OpenAI
import os
from dotenv import load_dotenv
from describe_sql_table import get_tables_and_columns

load_dotenv()

client = OpenAI(
    api_key=os.getenv('TEST_API_KEY'),
    organization=os.getenv('ORGA_ID'),
    project=os.getenv('PROJECT_ID')
)


app = Flask(__name__)


def question_to_sql(question):
    sql_table = get_tables_and_columns()

    response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"You're a helpful datascientist assistant. Convert the following question into a SQL query into the table and columns {sql_table}. Give only the sql query, no extra language added: {question}",
            temperature=0,
            )
    return response.choices[0].text.strip()


def summarize_data(results):
    summary_prompt = f"Summarize the following data: {results}"
    response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"You're a helpful datascientist assistant. {summary_prompt}",
            temperature=0.8,
    )
    return response.choices[0].text.strip()


def execute_query(sql_query):
    conn = sqlite3.connect('sqlDB.db')
    cursor = conn.cursor()
    cursor.execute(sql_query)

    results = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    conn.close()
    return results, column_names


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        sql_query = question_to_sql(question)
        results, column_names = execute_query(sql_query)
        summary = summarize_data(results)

        return render_template('results.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
