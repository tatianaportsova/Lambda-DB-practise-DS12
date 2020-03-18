
# app/insert_titanic.py

import pandas
import psycopg2
import os
from dotenv import load_dotenv
import json
import sqlite3
from psycopg2.extras import execute_values

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME1", default="OOPS")
DB_USER = os.getenv("DB_USER1", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD1", default="OOPS")
DB_HOST = os.getenv("DB_HOST1", default="OOPS")

#connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
#print("CONNECTION:", connection)

#cursor = connection.cursor()
#print("CURSOR:", cursor)


def df_create(file_name):
    df = pandas.read_csv(file_name)
    # Replace apostrophes in name column to avoid SQL confusion
    df['Name'] = df['Name'].str.replace("'", '', regex=True)
    # Replace / and spaces in column names with underscores
    df.columns = df.columns.str.replace('/', "_")
    df.columns = df.columns.str.replace(' ', '_')
    return df

df = df_create('/Users/tt.sova/Desktop/titanic.csv')

# Instantiate connection to sqlite3
# Convert df to SQL
tconnection = sqlite3.connect('titanic.sqlite3')
df.to_sql('titanic', tconnection, if_exists='replace', index=False)
# Instantiate sqlite3 cursor
tcursor = tconnection.cursor()
# save SQL tabular data to result variable
result = tcursor.execute('SELECT * FROM titanic').fetchall()
# Instantiate postgresql connection & cursor
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = connection.cursor()

#
# TABLE CREATION
#
query = """
CREATE TABLE IF NOT EXISTS titanic (
        Survived INTEGER,
        Pclass INTEGER,
        Name VARCHAR(500),
        Sex VARCHAR(7),
        Age INTEGER,
        Siblings_Spouses_Abroad INTEGER,
        Parents_children_Abroad INTEGER,
        Fare REAL
        )
"""
cursor.execute(query)

#
# DATA INSERTION
#
# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
#insertion_query = """
#INSERT INTO titanic_table (
#    survived
#    ,pclass
#    ,name
#    ,sex
#    ,age
#    ,siblings_Spouses_Aboard
#    ,sarents_Children_Aboard
#    ,sare
#)
#VALUES %s
#"""
for row in result:
    insert_row = """
        INSERT INTO titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Abroad, Parents_Children_Abroad, Fare)
        VALUES """ + str(row[:]) + ';'
    cursor.execute(insert_row)
#data = list(df.itertuples())
#execute_values(tpg_curs, insertion_query, data)

cursor.close()
connection.commit()
