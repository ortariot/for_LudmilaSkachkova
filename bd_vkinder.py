import psycopg2
from config import *

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
                vk_id_applicant varchar(20) NOT null);
                """
        )
    print("[INFO] Table  was created.")


def create_table_seen_users():

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS seen_users(
            id_seen_users serial PRIMARY KEY,
            applicant_id INTEGER references applicant (id_applicant),
            vk_id_seen_users varchar(20) NOT null);"""
        )
    print("[INFO] Table was created.")


def insert_data_users(vk_id):

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO applicant (vk_id_applicant)  
            VALUES ( '{vk_id}');"""
        )


def insert_data_seen_users(vk_id_seen_users, applicant_id,  offset):

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO seen_users (vk_id_seen_users, applicant_id,) 
            VALUES ('{vk_id_seen_users}', '{applicant_id}')
            OFFSET '{offset}';"""
        )


def select(offset):

    with connection.cursor() as cursor:
        cursor.execute(
            """select id_applicant from applicant a
                        JOIN seen_users su
                        ON a.id_applicant = su.applicant_id
                        WHERE su.applicant_id IS NULL;"""
        )
        return cursor.fetchone()


def drop_applicant():

    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE IF EXISTS applicant CASCADE;"""
        )
        print('[INFO] Table was deleted.')


def drop_seen_users():

    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE  IF EXISTS seen_users CASCADE;"""
        )
        print('[INFO] Table  was deleted.')


def creating_database():
    drop_applicant()
    drop_seen_users()
    create_table_applicant()

