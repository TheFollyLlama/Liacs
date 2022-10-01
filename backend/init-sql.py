import psycopg2
import os

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=os.environ['DB_SCHEMA'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'])

cursor = conn.cursor()
cursor.execute(open("init.sql", "r").read())
conn.commit()
