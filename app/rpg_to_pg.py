# app/rpg_to_pg.py

import psycopg2
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

rpg_connection = sqlite3.connect('rpg_db.sqlite3')
rpg_cursor = rpg_connection.cursor()

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
cursor.execute("SELECT * from character_table;")
result = cursor.fetchall()
print("RESULT:", len(result))


insertion_query  = """
INSERT INTO character_table (
    character_id,
    name,
    level,
    exp,
    hp,
    strength,
    intelligence,
    dexterity,
    wisdom)
VALUES %s
"""
execute_values(cursor, insertion_query, [
  (1,'Aliquid iste optio reiciendi',0,0,10,1,1,1,1),
  (2,'Optio dolorem ex a',0,0,10,1,1,1,1),
  (3,'Minus c',0,0,10,1,1,1,1),
  (4,'Sit ut repr',0,0,10,1,1,1,1),
  (5,'At id recusandae expl',0,0,10,1,1,1,1),
  (6,'Non nobis et of',0,0,10,1,1,1,1),
  (7,'Perferendis',0,0,10,1,1,1,1),
  (8,'Accusantium amet quidem eve',0,0,10,1,1,1,1),
  (9,'Sed nostrum inventore error m',0,0,10,1,1,1,1),
  (10,'Harum repellendus omnis od',0,0,10,1,1,1,1)])

cursor.close()
connection.commit()