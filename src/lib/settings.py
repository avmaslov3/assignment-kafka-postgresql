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
