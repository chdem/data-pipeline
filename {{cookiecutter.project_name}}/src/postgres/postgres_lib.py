import psycopg
from postgres_pool import *


def db_execute(postgres_pool: PostgresPool, fn: function, *args)-> psycopg.Cursor:
    try:
        with postgres_pool.pool.connection() as conn:
            with conn.cursor() as cursor:
                return function(cursor, *args)
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