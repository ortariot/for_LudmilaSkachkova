import psycopg2
from config import *
from vkbot import *
connection = psycopg2.connect(

    user='postgres',
    password='12345678',
    database='bd_vkinder'
)
connection.autocommit = True

def create_table_seen_users():

    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS seen_users(\
            id SERIAL PRIMARY KEY, \
						vk_user_id varchar(20), \
						vk_profile_id varchar(20);"
        )
        return cursor.fetchone()
    
def insert_seen_users(result_id, user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO seen_users (vk_user_id, vk_profile_id) 
            VALUES ('{result_id}', '{user_id}');""" )
        return cursor.fetchone()
    
def select(offset):
    with connection.cursor() as cursor:
        cursor.execute(
            """select vk_profile_id from seen_users
                WHERE vk_profile_id IS NULL;"""
        )
        return cursor.fetchone()

def check(user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """select EXISTS vk_user_id from seen_users
                       WHERE vk_user_id = ?;""")
        return cursor.fetchone()
        if cursor.fetchone() == "True":
            insert_data_users(user_id)



