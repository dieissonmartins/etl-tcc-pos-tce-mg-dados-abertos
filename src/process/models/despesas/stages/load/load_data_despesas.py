import os
from datetime import datetime
import logging


class LoadDataDespesas:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load despesas')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_despesas(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa nova despesa')

            self.create_despesa(row)

    def delete_despesas(self, year, seq_orgao):
        logging.info('Deleta despesas por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM despesas WHERE num_anoexercicio = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_despesa(self, row):
        cursor = self.__conn.cursor()

        seq_orgao = row['seq_orgao']
        cod_municipio = row['cod_municipio']
        seq_unidade = row['seq_unidade']
        cod_unidade = row['cod_unidade']
        cod_subunidade = row['cod_subunidade']
        num_anoexercicio = row['num_anoexercicio']
        num_mesexercicio = row['num_mesexercicio']
        dsc_funcao = row['dsc_funcao']
        dsc_subfuncao = row['dsc_subfuncao']
        dsc_programa = row['dsc_programa']
        dsc_acao = row['dsc_acao']
        dsc_subacao = row['dsc_subacao']
        dsc_naturezadespesa = row['dsc_naturezadespesa']
        dsc_fonterecurso = row['dsc_fonterecurso']
        vlr_previsto = row['vlr_previsto']
        vlr_acrescimo = row['vlr_acrescimo']
        vlr_deducao = row['vlr_deducao']
        vlr_empenhado = row['vlr_empenhado']
        vlr_liquidado = row['vlr_liquidado']
        vlr_pago = row['vlr_pago']
        vlr_rspprocessado = row['vlr_rspprocessado']
        vlr_rspnprocprocessado = row['vlr_rspnprocprocessado']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO despesas (seq_orgao cod_municipio, seq_unidade, cod_unidade, cod_subunidade, " \
                "num_anoexercicio, num_mesexercicio, dsc_funcao, dsc_subfuncao, dsc_programa, dsc_acao, dsc_subacao, " \
                "dsc_naturezadespesa, dsc_fonterecurso, vlr_previsto, vlr_acrescimo, vlr_deducao, vlr_empenhado, " \
                "vlr_liquidado, vlr_pago, vlr_rspprocessado, vlr_rspnprocprocessado, num_versaoarq, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (
            seq_orgao, cod_municipio, seq_unidade, cod_unidade, cod_subunidade, num_anoexercicio, num_mesexercicio,
            dsc_funcao, dsc_subfuncao, dsc_programa, dsc_acao, dsc_subacao, dsc_naturezadespesa, dsc_fonterecurso,
            vlr_previsto, vlr_acrescimo, vlr_deducao, vlr_empenhado, vlr_liquidado, vlr_pago, vlr_rspprocessado,
            vlr_rspnprocprocessado, num_versaoarq, created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
