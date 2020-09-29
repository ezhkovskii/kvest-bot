import sqlite3
from sqlite3 import Error
from settings import current_datetime


def post_sql_query(sql_query):
    with sqlite3.connect('db.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error as e:
            print(e)
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS 
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        name TEXT,
                        reg_date TEXT);'''
    post_sql_query(users_query)


def register_user(user, username, name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        now = current_datetime()
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, name, reg_date) ' \
                             f'VALUES ({user}, "{username}", "{name}", "{now}");'
        post_sql_query(insert_to_db_query)


def query_all_user():
    user_check_query = f'SELECT * FROM USERS;'
    return post_sql_query(user_check_query)
    
    
