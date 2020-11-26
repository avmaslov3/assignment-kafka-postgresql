"""
Module to export settings from environmental variables which are set
using setenv.sh script.
"""
import os

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")
POSTGRESQL_URI = os.getenv("POSTGRESQL_URI")
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")
POSTGRESQL_TABLE_NAME = os.getenv("POSTGRESQL_TABLE_NAME")
FILE_SSL_CAFILE = os.getenv("FILE_SSL_CAFILE")
FILE_SSL_CERTFILE = os.getenv("FILE_SSL_CERTFILE")
FILE_SSL_KEYFILE = os.getenv("FILE_SSL_KEYFILE")

if not (KAFKA_TOPIC and KAFKA_SERVER and POSTGRESQL_URI and POSTGRESQL_HOST
        and POSTGRESQL_PORT and POSTGRESQL_USER and POSTGRESQL_PASSWORD and
        POSTGRESQL_DB_NAME and POSTGRESQL_TABLE_NAME and FILE_SSL_CAFILE and
        FILE_SSL_CERTFILE and FILE_SSL_KEYFILE):
    raise TypeError("Not all environmental variables are not set - run "
                    "./setenv.sh")