#Additional for snake
import psycopg2
from config import config
#"""--------------------------------------------------------------#
def create_tables():
    commands = (
        """
        CREATE TABLE users (
          user_id serial PRIMARY KEY,
          username VARCHAR (50) UNIQUE NOT NULL,
          password VARCHAR(20) NOT NULL
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

#create_tables()
#"""---------------------------------------------------------------------------#
def insert_game(username, password):
    sql = """
    INSERT INTO users(username, password)
    VALUES(%s, %s) RETURNING user_id; """
    

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, password))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id

#insert_game('admin', 'admin')
#"""#----------------------------------------------------------#

def drop_tables():
    commands = (
        """
        DROP TABLE users;
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

#drop_tables()