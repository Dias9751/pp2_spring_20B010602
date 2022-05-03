# Lab 11 task 5
"""
create or replace procedure drop_row(
    name varchar
)
as $$
begin
    delete from phonebook where phonebook.username = name;
end;
$$
language plpgsql;
"""

import psycopg2
from config import config


def drop_row1(name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call drop_row(%s)', (name, ))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

drop_row1('Parrot')