# src/database.py

import psycopg2
from psycopg2 import Error

DB_HOST = 'localhost'
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'

def connect_to_database():
    connection = None
    try:
        if DB_HOST is None or DB_NAME is None or DB_USER is None or DB_PASSWORD is None:
            raise ValueError("Database connection details are not set")
        
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        
        return connection
    
    except Error as e:
        print("Error while connecting to PostgreSQL:", e)
        return None

def query_database(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        query_results = cursor.fetchall()
        return query_results
    
    except Error as e:
        print("Error while querying database:", e)
        return None

def close_database_connection(connection):
    if connection and not connection.closed:
        connection.close()