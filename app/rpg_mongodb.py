
# app/rpg_mongodb.py

import pymongo
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.rpg_collection # or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

# Create connection to rpg_db file
db_conn = sqlite3.connect('../rpg_db.sqlite3')
db_cursor = db_conn.cursor()
tables = db_cursor.execute("SELECT * FROM sqlite_master WHERE type='table';").fetchall() 
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#for table_name in tables:
#    table_name = table_name[0]
#    table = db_cursor.execute("SELECT * FROM %s;") # % table_name
#db_cursor.close()
#db.close()

db.collection.insert_one(tables) # can insert nested structures / documents!!!

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

