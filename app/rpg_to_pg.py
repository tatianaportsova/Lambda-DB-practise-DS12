# app/rpg_to_pg.py

import psycopg2
import pandas
import os
from dotenv import load_dotenv
import json
import sqlite3
from psycopg2.extras import execute_values

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME2", default="OOPS")
DB_USER = os.getenv("DB_USER2", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD2", default="OOPS")
DB_HOST = os.getenv("DB_HOST2", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

db_conn = sqlite3.connect('../rpg_db.sqlite3')
db_cursor = db_conn.cursor()
characters = db_cursor.execute("SELECT * from charactercreator_character;").fetchall()

query = """
CREATE TABLE IF NOT EXISTS character_table (
  character_id INTEGER,
  name varchar(40) NOT NULL,
  level INTEGER,
  exp INTEGER,
  hp INTEGER,
  strength INTEGER,
  intelligence INTEGER,
  dexterity INTEGER,
  wisdom INTEGER
);
"""
cursor.execute(query)
#cursor.execute("SELECT * from character_table;")
#result = cursor.fetchall()
#print("RESULT:", len(result))

# Inject into elephantSQL table
for character in characters:
    insert_character =  """
        INSERT INTO character_table (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[:]) + ';'
    cursor.execute(insert_character)

cursor.close()
connection.commit()
