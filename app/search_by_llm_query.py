import sqlite3
from openai import OpenAI
import os
from dotenv import load_dotenv



def question_to_sql(question, client, sql_table):
    response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"You're a helpful datascientist assistant. Convert the following question into a SQL query into the table and columns {sql_table}. Give only the sql query, no extra language added: {question}",
            temperature=0,
            )
    return response.choices[0].text.strip()


def summarize_data(results, client):
    summary_prompt = f"Summarize the following data: {results}"
    response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"You're a helpful datascientist assistant. {summary_prompt}",
            temperature=0.8,
    )
    return response.choices[0].text.strip()
