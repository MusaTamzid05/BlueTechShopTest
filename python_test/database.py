import os
from helper import get_postgres_host
import os
import psycopg2

class Database:
    USER_NAME =  os.environ["POSTGRES_USER"]
    USER_PASSWORD  = os.environ["POSTGRES_PASSWORD"]
    DB_NAME  = os.environ["POSTGRES_DB"]
    DB_HOST =  get_postgres_host()

    @staticmethod
    def get_connection():

        try:
            return psycopg2.connect(
                    dbname = Database.DB_NAME ,
                    user = Database.USER_NAME ,
                    password = Database.USER_PASSWORD ,
                    host = get_postgres_host()
                    )

        except psycopg2.OperationalError as e:
            print("Database connection failed")
            print(e)

        return None


