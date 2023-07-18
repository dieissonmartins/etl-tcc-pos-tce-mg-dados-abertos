import os

from mysql import connector
from dotenv import load_dotenv

# load envs
load_dotenv()

user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")

conn = connector.connect(user=user, password=password, host=host, database=database)

cursor = conn.cursor()

query = "SELECT * FROM orgaos"

smpt = cursor.execute(query)

orgaos = cursor.fetchall()

conn.close()
