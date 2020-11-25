import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
from lib.settings import *


def test_database_connection():
    try:
        connect = pg2.connect(host=POSTGRESQL_HOST,
                              port=POSTGRESQL_PORT,
                              user=POSTGRESQL_USER,
                              database=POSTGRESQL_DB_NAME,
                              password=POSTGRESQL_PASSWORD)
        c = connect.cursor(cursor_factory=RealDictCursor)
        c.execute("SELECT VERSION()")
        result = c.fetchone()
        print(result)
        return True
    except pg2.OperationalError as e:
        raise pg2.OperationalError("Database connection error") from e
        return False


