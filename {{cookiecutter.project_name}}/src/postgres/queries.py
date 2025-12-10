from src.postgres.postgres_lib import db

#exemple query to fetch users table
# @db
# def get_users_db(cursor, _):
#     cursor.execute("""
#         SELECT * FROM users;
#                     """)
#     return fetch_as_dicts(cursor)

def fetch_as_scalar(cursor):
    value = cursor.fetch_one()
    return value

def fetch_as_dicts(cursor):
    columns = [desc.name for desc in cursor.description]
    rows = cursor.fetchall()
    return  [dict(zip(columns, row)) for row in rows]