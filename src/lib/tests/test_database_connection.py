from lib.database import request_db, drop_if_exist_and_create_table
import psycopg2
from psycopg2 import errors


def test_database_connection():
    try:
        request_db("SELECT url, status_code, response_time FROM METRICS;")
        db_version = request_db("SELECT VERSION()")
        assert len(db_version) == 1
    except psycopg2.OperationalError as e:
        raise psycopg2.OperationalError("Database connection error") from e
    except psycopg2.errors.UndefinedTable as e:
        raise psycopg2.errors.UndefinedTable("Table metrics doesn't exist - "
                                             "create table") from e

