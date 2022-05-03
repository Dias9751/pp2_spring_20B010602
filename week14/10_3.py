# Lab 11 task 3
"""
create or replace procedure add_numbers2(
    inf []
)
as $$
declare
    len integer := array_length(inf, 1);
    arr_indx integer := 1;
    return_user_id INT;
begin
    WHILE arr_indx <= len LOOP
        if (arr_indx == 2) then arr_indx = 3;
        end if;
        insert into phonebook(username, phone_number)
        values(inf[arr_indx-1][0], inf[arr_indx-1][1]::integer)
        returning user_id into return_user_id;
    END LOOP;
end;
$$
language plpgsql;
"""
# астындагысы дурыс
"""
create or replace procedure add_numbers2(
    username varchar,
    phone_number integer
)
as $$
declare
    return_user_id INT;
    i integer := 0;
begin
    while i <= 3 loop
        phone_number = phone_number + f;
        i = i +1;
    end loop;
    if (phone_number/1000 > 1 ) then insert into phonebook(username, phone_number)
                                      values(username, phone_number)
                                      returning user_id into return_user_id;
    end if;
end;
$$
language plpgsql;
"""
import psycopg2
from config import config


def add_number(db):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for i in range(len(db)):
            cur.execute('call add_numbers2(%s, %s)', (db[i][0], db[i][1]))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

arr = [['KZe', 70885], ['US', 1283], ['EAO', 9654]]
add_number(arr)