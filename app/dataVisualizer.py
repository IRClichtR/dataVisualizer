from flask import Flask, request, render_template
import sqlite3
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('TEST_API_KEY')

app = Flask(__name__)

def question_to_sql(question):
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Convert the following question into a SQL query: {question}",
            max_token=150
            )
    return response.choices[0].text.strip()


def summarize_data(results):
    sumary_prompt = f"Summarize the following data: {results}"
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=summary_prompt,
            max_token=150
            )
    return response.choice[0].text.strip()


def execute_query(sql_query):
    conn = sqlite3.connect('database.db')
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

        return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
