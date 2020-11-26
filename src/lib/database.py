"""
https://help.aiven.io/en/articles/489573-getting-started-with-aiven-postgresqldaxmmll97fcuv7x6
"""
from lib.settings import *
from psycopg2.extras import RealDictCursor
import psycopg2 as pg2
from lib.common import *


def send_to_database(message: ResponseMetrics):
    connect = pg2.connect(host=POSTGRESQL_HOST,
                          port=POSTGRESQL_PORT,
                          user=POSTGRESQL_USER,
                          database=POSTGRESQL_DB_NAME,
                          password=POSTGRESQL_PASSWORD)

    with connect:
        with connect.cursor(cursor_factory=RealDictCursor) as cursor:
            insert_query = """insert into """ + POSTGRESQL_TABLE_NAME + \
                           """ (url, status_code, response_time) values (%s, %s, %s); """
            cursor.execute(insert_query, (message.url, message.status_code,
                                          message.response_time_seconds))


def request_db(query: str):
    """
    Function to send various queries for testing purpose.
    E.g. - select * from ...
    """
    connect = pg2.connect(host=POSTGRESQL_HOST,
                          port=POSTGRESQL_PORT,
                          user=POSTGRESQL_USER,
                          database=POSTGRESQL_DB_NAME,
                          password=POSTGRESQL_PASSWORD)
    with connect:
        with connect.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)
            dat = cursor.fetchall()
            return dat


def drop_if_exist_and_create_table():
    """
    Initialize empty table.
    Delete if it already exists.
    """
    connect = pg2.connect(host=POSTGRESQL_HOST,
                          port=POSTGRESQL_PORT,
                          user=POSTGRESQL_USER,
                          database=POSTGRESQL_DB_NAME,
                          password=POSTGRESQL_PASSWORD)
    with connect:
        with connect.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("drop table if exists " +
                           POSTGRESQL_TABLE_NAME
                           + ";")
            req = """create table  """ + POSTGRESQL_TABLE_NAME + \
                """ (id bigserial not null primary key, 
                     url text,
                     status_code text, 
                     response_time float); """
            cursor.execute(req)
