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


def question_to_sql(question):
    sql_table = get_tables_and_columns()

    response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"You're a helpful datascientist assistant. Convert the following question into a SQL query into the table and columns {sql_table}. Give only the sql query, no extra language added: {question}",
            temperature=0,
            )
    return response.choices[0].text.strip()
