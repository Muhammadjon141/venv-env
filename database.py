import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    def __init__(self) -> None:
        pass

    @staticmethod
    def select(query):
        db_connect = psql.connect(
            database = os.getenv('db_name'),
            user = os.getenv('db_user'),
            password = os.getenv('db_password'),
            host = os.getenv('db_host'),
            port = os.getenv('db_port')
        )

        cursor = db_connect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
if __name__ == "__main__":
    query = "SELECT * FROM products;"
    Database.select(query)