# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    """Connects to MySQL server and creates the alx_book_store database."""
    
    # --- IMPORTANT ---
    # Replace these placeholders with your actual MySQL connection details
    DB_HOST = "localhost"
    DB_USER = "your_username"
    DB_PASSWORD = "your_password"
    
    db_connection = None
    cursor = None
    
    try:
        # Establish a connection to the MySQL server
        db_connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        # Create a cursor object to execute SQL commands
        cursor = db_connection.cursor()
        
        # SQL command to create the database if it doesn't already exist
        # This prevents the script from failing if the database is already there
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle specific connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Error: Database does not exist.")
        else:
            # Handle other potential errors during connection or execution
            print(f"Failed to connect to the DB: {err}")
            
    finally:
        # Ensure the cursor and connection are closed properly
        if cursor:
            cursor.close()
            # print("Cursor closed.")
        if db_connection and db_connection.is_connected():
            db_connection.close()
            # print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()