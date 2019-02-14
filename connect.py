from os import getenv

from psycopg2 import OperationalError
from psycopg2 import connect


CONNECTION_NAME = getenv("INSTANCE_CONNECTION_NAME")
DB_USER = getenv("POSTGRES_USER")
DB_PASSWORD = getenv("POSTGRES_PASSWORD")
DB_NAME = getenv("POSTGRES_DATABASE")

pg_config = {"user": DB_USER, "password": DB_PASSWORD, "dbname": DB_NAME}


def pg_connection(host):
    try:
        pg_config["host"] = host
        pg_con = connect(**pg_config)
        print("connecting to the web")
        return pg_con
    except OperationalError:
        pg_config["host"] = "localhost"
        pg_con = connect(**pg_config)
        print("connecting locally")
        return pg_con
    return pg_con