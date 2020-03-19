
## app/titanic_lecture_example.py
# app/pg_titanic.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME1", default="OOPS")
DB_USER = os.getenv("DB_USER1", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD1", default="OOPS")
DB_HOST = os.getenv("DB_HOST1", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)
# GOAL: load the data/titanic.csv file into a PG database table!
# CREATE THE TABLE
# discern which columns (pandas?)

query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  Survived INTEGER,
  Pclass INTEGER,
  Name VARCHAR(500),
  Sex VARCHAR(7),
  Age INTEGER,
  Siblings_Spouses_Abroad INTEGER,
  Parents_children_Abroad INTEGER,
  Fare REAL
);
"""
cursor.execute(query)
cursor.execute("SELECT * from passengers;")
result = cursor.fetchall()
print("PASSENGERS:", len(result))
if len(result) == 0:
    # INSERT RECORDS
    #CSV_FILEPATH = "data/titanic.csv"
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
    print("FILE EXISTS?", os.path.isfile(CSV_FILEPATH))
    df = pandas.read_csv(CSV_FILEPATH)
    print(df.head())
    # rows should be a list of tuples
    # [
    #   ('A rowwwww', 'null'),
    #   ('Another row, with JSONNNNN', json.dumps(my_dict)),
    #   ('Third row', "3")
    # ]
    # h/t Jesus and https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
    rows = list(df.itertuples(index=False, name=None))
    insertion_query = "INSERT INTO passengers (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Abroad, Parents_Children_Abroad, Fare) VALUES %s"
    execute_values(cursor, insertion_query, rows)
# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()