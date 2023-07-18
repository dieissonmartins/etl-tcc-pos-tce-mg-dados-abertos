import os
from src.drivers.conn import Conn


class LoadDataOrgaos:
    def __init__(self) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))

        conn = Conn()
        self.__conn = conn.connect()

    def load(self, transform_html_data):
        for row in transform_html_data:

            orgao = self.get_orgao(row)

            if orgao:
                print('atualiza')
            else:
                print('não existe')

    def get_orgao(self, row):
        cursor = self.__conn.cursor()

        seq_orgao = row['seq_orgao']
        cod_orgao = row['cod_orgao']
        cod_municipio = row['cod_municipio']

        query = "SELECT id FROM orgaos WHERE seq_orgao = %s AND cod_orgao = %s AND cod_municipio = %s"

        where = (seq_orgao, cod_orgao, cod_municipio)

        smpt = cursor.execute(query, where)

        orgao = cursor.fetch()

        debug = orgao

        return orgao
