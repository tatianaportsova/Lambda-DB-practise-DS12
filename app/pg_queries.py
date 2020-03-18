import psycopg2

DB_NAME = "lyvosnye"
DB_USER = "lyvosnye"
DB_PASSWORD = "e_2m1YCwgD-Xa-lLybReed3VuYI87Dfm"
DB_HOST = "drona.db.elephantsql.com"

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:",connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')

result = cursor.fetchone()
print("RESULT:", result)

