from typing import Any

from dotenv import load_dotenv
import logging
from mysql import connector
import os


class Conn:
    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

        # load envs
        load_dotenv()

        # elf.__conn = self.connect()

    def connect(self) -> Any:
        logging.info('Conecta no banco de dados')

        user = os.getenv("DB_USERNAME")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_DATABASE")

        conn = connector.connect(user=user, password=password, host=host, database=database)

        return conn

    def get_conn(self):
        return self.__conn
