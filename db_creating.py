import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from argparse import ArgumentParser
from contextlib import closing

def create_db(db_name):
    try:
        with closing(psycopg2.connect(user='postgres',
                                        password='***',
                                        host='127.0.0.1',
                                        port='5432')) as connection:
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                sql_create_database = 'create database %s;'
                cursor.execute(sql_create_database % (db_name))
    except Error as error:
        print(error)

def createParser():
    parser = ArgumentParser()
    
    parser.add_argument('-d', '--database', default='lykke')

    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    create_db(namespace.database)