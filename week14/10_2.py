# Lab 11 task 2
"""
create or replace procedure add_number(
    username varchar,
    phone_number integer
)
as $$
declare
    return_user_id INT;
begin
    insert into phonebook(username, phone_number)
    values(username, phone_number)
    returning user_id into return_user_id;
end;
$$
language plpgsql;
"""

import psycopg2
from config import config


def add_number(name, number):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call add_number(%s, %s)', (name, number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

add_number("Baieke", 887855)