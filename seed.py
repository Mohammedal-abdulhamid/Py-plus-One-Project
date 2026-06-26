import psycopg2
import json

from run_file import run_file
run_file("db/scheema.sql")


def seed(filepath,table_name):
    
    conn = psycopg2.connect("dbname=nc_plus_one_project")
    cur = conn.cursor()
    with open(filepath) as f:
       data = json.load(f)
   
    conn = psycopg2.connect("dbname=nc_plus_one_project")
    cur = conn.cursor()

    columns = data[0].keys()
    columns_str = ", ".join(columns)
    values_template = ", ".join(["%s"] * len(columns))
    query = f"""
       INSERT INTO {table_name} ({columns_str})
       VALUES ({values_template})
       """
    print(data)
    for object in data :
        cur.execute(query, tuple(object.values()))
       
    conn.commit()


seed("db/data/users.json", "users")
seed("db/data/venues.json", "venues")
seed("db/data/events.json", "events")
seed("db/data/rsvps.json", "rsvps")
print("Seed completed successfully!")

   