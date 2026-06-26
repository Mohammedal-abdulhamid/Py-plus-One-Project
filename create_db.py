import psycopg2

conn = psycopg2.connect(dbname="postgres")

# MUST be immediately after connection
conn.autocommit = True

cur = conn.cursor()

cur.execute("DROP DATABASE IF EXISTS nc_plus_one_project;")
cur.execute("CREATE DATABASE nc_plus_one_project;")

cur.close()
conn.close()