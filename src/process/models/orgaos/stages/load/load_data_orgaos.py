import pandas as pd
import os
from datetime import datetime

from src.drivers.conn import Conn


class LoadDataOrgaos:
    def __init__(self) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))

        self.__cursor = Conn().get_conn()

    def load(self, transform_html_data):
        for row in transform_html_data:
            item = row

            query = "SELECT * FROM orgaos"

            smpt = self.__cursor.execute(query)

            orgaos = self.__cursor.fetchall()

            debug = orgaos
