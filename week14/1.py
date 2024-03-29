# psql
# \l - list all databases
# \c database_name - connect to database
# \dt - list of all tables
# \q - quit

# create database database_name;
# create user name_of_user with password 'password';
# grant all privileges on database database_name to user_name; 
# grant all privileges on database pp2 to pp2;

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="onefit",
    user="onefit",
    password="onefit"
)

# select * from table where condition;

sql = "select id, user_type, subscription_id from authe_usertype where subscription_id=63"

cursor = conn.cursor()
cursor.execute(sql)
all_rows = cursor.fetchall()

for row in all_rows:
    print(row)

cursor.close()
conn.close()