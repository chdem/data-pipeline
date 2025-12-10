import psycopg
from src.postgres.postgres_pool import *


def db_execute(fn, *args)-> psycopg.Cursor:
    try:
        with PostgresPool.get_conn() as conn:
            with conn.cursor() as cursor:
                return fn(cursor, *args)
    except psycopg.errors.SyntaxError as e:
        print("error sql", e)
    except psycopg.errors.UniqueViolation as e:
        print("Violation unique error", e)
    except psycopg.errors.OperationalError as e:
        print("Connection issue", e)
    except Exception as e:
        print("other error", e)

def db(func):
    def wrapper(*args, **kwargs):
        return db_execute(func, *args, **kwargs)
    return wrapper