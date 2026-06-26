
import psycopg2


conn = psycopg2.connect("dbname=nc_plus_one_project")
conn.autocommit = True
cur = conn.cursor()

def run_file(file_path):
    with open(file_path, "r") as f:
        sql = f.read()

    cur.execute(sql)

    
  
