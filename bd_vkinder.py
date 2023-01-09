import psycopg2
from config import *
from vkbot import *
connection = psycopg2.connect(

    user='postgres',
    password='12345678',
    database='bd_vkinder'
)
connection.autocommit = True

def create_table_applicant():

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS applicant (
                id_applicant SERIAL PRIMARY KEY,
                vk_id_applicant varchar(20) UNIQUE NOT null);
                """
        )
    print("[INFO] Table  was created.")

def create_table_seen_users():

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS seen_users(
            id_seen_users serial PRIMARY KEY,
            applicant_id INTEGER references applicant (id_applicant),
            vk_id_seen_users varchar(20) UNIQUE NOT null);"""
        )
    return cursor.fetchone()


def create_table_choice():
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS choice(
            id_choice serial PRIMARY KEY,
            applicant_id INTEGER references applicant (id_applicant),
            vk_id_choice varchar(20) UNIQUE NOT null);"""
        )
    return cursor.fetchone()


def insert_data_users(user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO applicant (vk_id_applicant)  
            VALUES ( '{user_id}');""")
        return cursor.fetchone()

def insert_data_seen_users(result_id, user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO seen_users (vk_id_seen_users, applicant_id,) 
            VALUES ('{result_id}', '{user_id}');""" )
        return cursor.fetchone()

def insert_data_choice(result_id, user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO choice (vk_id_seen_users, applicant_id,) 
            VALUES ('{result_id}', '{user_id}');""")
        return cursor.fetchone()


def select(offset):
    with connection.cursor() as cursor:
        cursor.execute(
            """select id_applicant from applicant a
                        JOIN seen_users su
                        ON a.id_applicant = su.applicant_id
                        WHERE su.applicant_id IS NULL;"""
        )
        return cursor.fetchone()

def check(user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """select EXISTS id_applicant from applicant a
                       WHERE id_applicant = ?;""")
        return cursor.fetchone()
        if cursor.fetchone() == "True":
            insert_data_users(user_id)



