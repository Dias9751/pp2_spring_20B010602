#Lab 11 Task 4
"""
create or replace function get_all_inf()
returns TABLE(user_id integer, username varchar, phone_number integer) as
$$
begin
    return query
    select phonebook.user_id, phonebook.username, phonebook.phone_number from phonebook order by phonebook.username limit 5;
end;
$$
language plpgsql;
"""
import psycopg2
from config import config

def get_all_inf():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('get_all_inf',)
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

get_all_inf()