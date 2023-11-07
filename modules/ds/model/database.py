import psycopg2
import pandas as pd

def connect_to_database():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="daredatachallenge",
        user="admin",
        password="admin",
    )
    print("Connected to the database!")
    return connection

def query_database(connection, query):
    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as error:
        print(f"Error: {error}")
