#PhoneBook
import psycopg2
from config import config
 
def update_user(phone_number, username):
    sql = """
    update PhoneBook
    set phone_number = %s
    where username = %s;
    """
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone_number, username))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

update_user(874785469, 'Aidar')