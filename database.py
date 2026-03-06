import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="YOUR_HOST",
        user="YOUR_USER",
        password="YOUR_PASSWORD",
        database="YOUR_DATABASE"
    )