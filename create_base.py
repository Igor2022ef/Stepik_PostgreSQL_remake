# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# connection = psycopg2.connect(user="postgres", password="34567890")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = connection.cursor()
# sql_create_database = cursor.execute('create database sqlalchemy_stepik_online_bookstore')
# cursor.close()
# connection.close()