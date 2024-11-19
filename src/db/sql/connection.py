import os
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker
from typing import Generator

from src.config import DB_NAME

SQL_DRIVER = "mysql+pymysql"
SQL_HOST = "localhost"
SQL_PORT = "3306"
SQL_DBNAME = DB_NAME


def generate_sql_url() -> str:
    """
    Create the SQL DB URL for sqlalchemy
    """
    user = os.getenv("SQL_USER", "")
    password = os.getenv("SQL_PASSWORD", "")
    return f"{SQL_DRIVER}://{user}:{password}@{SQL_HOST}:{SQL_PORT}/{SQL_DBNAME}"

SQL_URL = generate_sql_url()
print(SQL_URL)
SQL_ENGINE = sqlalchemy.create_engine(SQL_URL)

_SQL_SESSION_MAKER = sessionmaker(bind=SQL_ENGINE)

class SQLSession:
    def __init__(self):
        self._session = _SQL_SESSION_MAKER()

    def __enter__(self) -> Session:
        return self._session

    def __exit__(self, *_) -> None:
        self._session.close()
