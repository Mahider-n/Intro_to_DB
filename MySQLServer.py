import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (update host/user/password to match your MySQL setup)
        connection = mysql.connector.connect(
            host="localhost",
            user="trial",
            password="trial12"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL server or create database. {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: Uncomment to see when connection closes
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
