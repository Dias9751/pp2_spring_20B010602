#PhoneBook
import psycopg2
from config import config
 
def drop_user(user_id, username):
    sql = """
    DELETE FROM PhoneBook where user_id = %s and username = %s
    """
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_id, username))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

drop_user(2, 'Aidar')