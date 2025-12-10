import os
from dotenv import load_dotenv
from psycopg_pool import ConnectionPool

def get_db_port():
    return os.getenv("POSTGRES_PORTS", "5432").split(":")[0]

class PostgresPool:
    pool: ConnectionPool = None

    @staticmethod
    def init_pool():
        if PostgresPool.pool is None:
            load_dotenv()
            user = os.getenv("POSTGRES_USER")
            password = os.getenv("POSTGRES_PASSWORD")
            host = os.getenv("POSTGRES_CONTAINER_NAME", "localhost")
            port = get_db_port()
            dbname = os.getenv("POSTGRES_DB")
            database_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
            print(database_url)
            PostgresPool.pool = ConnectionPool(database_url, max_size=5, min_size=1)



    @staticmethod
    def get_conn():
        if PostgresPool.pool is None:
            PostgresPool.init_pool()
        return PostgresPool.pool.connection()

    def close(self):
        """Ferme le pool"""
        PostgresPool.close()  #comment je gère ça en static