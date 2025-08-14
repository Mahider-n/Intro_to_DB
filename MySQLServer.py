import mysql.connector

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

    except mysql.connector.Error as err:
        print(f"Error: Could not connect to MySQL server or create database. {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
