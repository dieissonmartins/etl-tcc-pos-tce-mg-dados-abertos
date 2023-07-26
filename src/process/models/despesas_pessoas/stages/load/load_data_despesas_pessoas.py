import os
from datetime import datetime
import logging


class LoadDataDespesasPessoas:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load despesas pessoas')

        cod_municipio = transform_html_data[0]['cod_municipio']

        self.delete_despesas_pessoas(year, cod_municipio)

        for row in transform_html_data:
            logging.info('Importa nova despesa pessoa')

            self.create_despesa_pessoa(row)

    def delete_despesas_pessoas(self, year, cod_municipio):
        logging.info('Deleta despesas pessoas por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM despesas_pessoas WHERE num_ano_referencia = %s AND cod_municipio = %s"

        where = (year, cod_municipio)

        cursor.execute(query, where)

    def create_despesa_pessoa(self, row):
        cursor = self.__conn.cursor()

        cod_municipio = row['cod_municipio']
        num_ano_referencia = row['num_ano_referencia']
        num_mes_referencia = row['num_mes_referencia']
        cod_nat_despesa = row['cod_nat_despesa']
        dsc_nat_despesa = row['dsc_nat_despesa']
        vlr_executivo = row['vlr_executivo']
        vlr_legislativo = row['vlr_legislativo']
        vlr_municipio = row['vlr_municipio']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO despesas_pessoas (cod_municipio, num_ano_referencia, num_mes_referencia, cod_nat_despesa, " \
                "dsc_nat_despesa, vlr_executivo, vlr_legislativo, vlr_municipio, num_versaoarq, created_at, updated_at)" \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (
            cod_municipio, num_ano_referencia, num_mes_referencia, cod_nat_despesa, dsc_nat_despesa, vlr_executivo,
            vlr_legislativo, vlr_municipio, num_versaoarq, created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
