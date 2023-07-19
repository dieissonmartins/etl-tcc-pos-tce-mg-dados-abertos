import os
from datetime import datetime
import logging


class LoadDataOrgaos:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn.connect()

    def load(self, transform_html_data):

        logging.info('load orgão')

        for row in transform_html_data:

            orgao = self.get_orgao(row)

            if not orgao:
                logging.info('Importa novo orgão')
                self.create_orgao(row)
            else:
                logging.info('Atualiza orgão: ' + str(row['seq_orgao']))
                print('não existe')

    def get_orgao(self, row):

        logging.info('Verifica se orgão existe')

        cursor = self.__conn.cursor()

        seq_orgao = row['seq_orgao']
        cod_orgao = row['cod_orgao']
        cod_municipio = row['cod_municipio']

        query = "SELECT id FROM orgaos WHERE seq_orgao = %s AND cod_orgao = %s AND cod_municipio = %s"

        where = (seq_orgao, cod_orgao, cod_municipio)

        smpt = cursor.execute(query, where)

        return cursor.fetchone()

    def create_orgao(self, row):

        cursor = self.__conn.cursor()

        seq_orgao = row['seq_orgao']
        num_anoexercicio = row['num_anoexercicio']
        cod_orgao = row['cod_orgao']
        nom_orgao = row['nom_orgao']
        tipo_orgao = row['tipo_orgao']
        cod_municipio = row['cod_municipio']
        nom_municipio = row['nom_municipio']
        cod_uf = row['cod_uf']
        sgl_uf = row['sgl_uf']
        nom_uf = row['nom_uf']
        dsc_regiaoplanejamento = row['dsc_regiaoplanejamento']
        num_versao_arq = row['num_versao_arq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO orgaos (seq_orgao, num_anoexercicio, cod_orgao, nom_orgao, tipo_orgao, cod_municipio," \
                "nom_municipio, cod_uf, sgl_uf, nom_uf, dsc_regiaoplanejamento, num_versao_arq, created_at, updated_at)" \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (
            seq_orgao, num_anoexercicio, cod_orgao, nom_orgao, tipo_orgao, cod_municipio, nom_municipio, cod_uf, sgl_uf,
            nom_uf, dsc_regiaoplanejamento, num_versao_arq, created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
