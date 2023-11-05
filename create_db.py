import pymysql

connection = pymysql.connect(
    host = "localhost",
    user="root",
    password="@delwar11@"
)

DB_NAME = "SCHOOL"

query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

cursor = connection.cursor()
cursor.execute(query)

print('Database created done!')