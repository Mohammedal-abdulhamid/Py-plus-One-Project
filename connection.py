import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DEFAULT_DB = os.getenv("DB_NAME")

def get_connection(dbname=DEFAULT_DB):
    return psycopg2.connect(
        dbname=dbname,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )