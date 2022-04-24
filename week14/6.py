# PhoneBook
import psycopg2
from config import config

def create_tables():
    commands = (
        """
        CREATE TABLE phonebook (
          user_id serial PRIMARY KEY,
          username VARCHAR (50) UNIQUE NOT NULL,
          phone_number SERIAL UNIQUE NOT NULL
        );
        """
    )  

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

create_tables()
