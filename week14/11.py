#Additional for snake
import psycopg2
from config import config
#"""--------------------------------------------------------------#
def create_tables():
    commands = (
        """
        CREATE TABLE game_snake (
          user_id serial PRIMARY KEY,
          username VARCHAR (50) UNIQUE NOT NULL,
          level INTEGER,
          speed INTEGER,
          score INTEGER,
          FOREIGN KEY (username)
            REFERENCES users (username)
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
def insert_game(username, level, speed, score):
    sql = """
    INSERT INTO game_snake(username, level, speed, score)
    VALUES(%s, %s, %s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, level, speed, score))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id


#insert_game('admin', 1, 5, 0)
#"""----------------------------------------------------#
def update_user(level, speed, score, username):
    sql = """
    update game_snake
    set level = %s,
    speed = %s,
    score = %s
    where username = %s;
    """
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (level, speed, score, username))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

#update_user(1, 30, 0, 'admin')
#"""----------------------------------------------------------#