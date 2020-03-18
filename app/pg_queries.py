import psycopg2

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:",connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')

result = cursor.fetchone()
print("RESULT:", result)

