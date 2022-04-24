# PhoneBook
import psycopg2
import csv
from config import config

def insert_phonebook(username, phone_number):
    sql = """
    INSERT INTO PhoneBook(username, phone_number)
    VALUES(%s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, phone_number))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id

with open('num.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        insert_phonebook(row[0], int(row[1]))
"""
insert_phonebook('Askar', 87086221)
insert_phonebook('Aidar', 87089554)
insert_phonebook('Jenifer', 877479885)"""
