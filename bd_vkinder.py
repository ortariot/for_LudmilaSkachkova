import psycopg2
from config import *
from vkbot import *
connection = psycopg2.connect(

    user='postgres',
    password='',
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
    '''передаёте в функцию аргументы и не используете их'''
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO seen_users (vk_user_id, vk_profile_id)   # здесь преданные аргументы не используются поскольку вы преедаёте в селект не переменные а просто строку.
            VALUES ('{result_id}', '{user_id}');""" )
        return cursor.fetchone()
    
def select(offset):
    '''передаёте в функцию аргумент offset и не используете его'''
    with connection.cursor() as cursor:
        cursor.execute(
            """select vk_profile_id from seen_users
                WHERE vk_profile_id IS NULL;"""
        )
        return cursor.fetchone()

def check(user_id):
    '''передаёте в функцию аргумент user_id и не используете его'''
    with connection.cursor() as cursor:
        cursor.execute(
            """select EXISTS vk_user_id from seen_users
                       WHERE vk_user_id = ?;""")
        return cursor.fetchone()
        '''код после return не будет выполнен'''
        if cursor.fetchone() == "True":
            insert_data_users(user_id)



