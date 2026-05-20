import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

def test_db_connection():
    try:
        
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
      
        cursor = connection.cursor()
        
       
        cursor.execute("SELECT version();")
        

        db_version = cursor.fetchone()
        
        print("\n==========================================")
        print("connect completely")
        print(f"DB version: {db_version[0]}")
        print("==========================================\n")
        
       
        cursor.close()
        connection.close()
        
    except Exception as error:
        print("\n==========================================")
        print(f"connect error: {error}")
        print("==========================================\n")


if __name__ == "__main__":
    test_db_connection()