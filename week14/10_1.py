#Lab 11 Task 1
"""
create or replace function get_number(name varchar)
returns TABLE(username varchar, phone_number integer) as
$$
begin
    return query
    select phonebook.username, phonebook.phone_number from phonebook where phonebook.username = name;
end;
$$
language plpgsql;
"""
import psycopg2
from config import config

def get_num_of_p(username):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('get_number', (username, ))
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

get_num_of_p('Parrot')