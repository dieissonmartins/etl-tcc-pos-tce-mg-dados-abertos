import os
from datetime import datetime
import logging


class LoadDataReceitas:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load receitas')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_receitas(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa nova receita')

            self.create_receita(row)

    def delete_receitas(self, year, seq_orgao):
        logging.info('Deleta receitas por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM receitas WHERE num_anoexercicio = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_receita(self, row):
        cursor = self.__conn.cursor()

        seq_orgao = row['seq_orgao']
        num_anoexercicio = row['num_anoexercicio']
        dsc_cateconomica = row['dsc_cateconomica']
        num_mesexercicio = row['num_mesexercicio']
        dsc_origem = row['dsc_origem']
        dsc_especie = row['dsc_especie']
        dsc_rubrica = row['dsc_rubrica']
        dsc_alinea = row['dsc_alinea']
        dsc_subalinea = row['dsc_subalinea']
        dsc_tipo = row['dsc_tipo']
        dsc_fonterecurso = row['dsc_fonterecurso']
        vlr_previsaoinicial = row['vlr_previsaoinicial']
        vlr_previsaoatualizada = row['vlr_previsaoatualizada']
        vlr_realizadoateperiodo = row['vlr_realizadoateperiodo']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO receitas (seq_orgao, num_anoexercicio, dsc_cateconomica, num_mesexercicio, dsc_origem, " \
                "dsc_especie, dsc_rubrica, dsc_alinea, dsc_subalinea, dsc_tipo, dsc_fonterecurso, vlr_previsaoinicial, " \
                "vlr_previsaoatualizada, vlr_realizadoateperiodo, num_versaoarq, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (seq_orgao, num_anoexercicio, dsc_cateconomica, num_mesexercicio, dsc_origem, dsc_especie, dsc_rubrica,
                  dsc_alinea, dsc_subalinea, dsc_tipo, dsc_fonterecurso, vlr_previsaoinicial, vlr_previsaoatualizada,
                  vlr_realizadoateperiodo, num_versaoarq, created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
