import os
from datetime import datetime
import logging


class LoadDataReceitas:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load empenhos')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_empenhos(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa novo empenho')

            self.create_empenho(row)

    def delete_empenhos(self, year, seq_orgao):
        logging.info('Deleta empenhos por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM empenhos WHERE num_anoexercicio = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_empenho(self, row):
        cursor = self.__conn.cursor()

        seq_empenho = row['seq_empenho']
        cod_municipio = row['cod_municipio']
        seq_orgao = row['seq_orgao']
        seq_unidade = row['seq_unidade']
        cod_unidade = row['cod_unidade']
        cod_subunidade = row['cod_subunidade']
        num_anoexercicio = row['num_anoexercicio']
        num_mesexercicio = row['num_mesexercicio']
        num_empenho = row['num_empenho']
        dat_empenho = row['dat_empenho']
        dsc_modalidade = row['dsc_modalidade']
        dsc_tipo_empenho = row['dsc_tipo_empenho']
        dsc_empenho = row['dsc_empenho']
        ind_dec_contrato = row['ind_dec_contrato']
        ind_dec_convenio = row['ind_dec_convenio']
        ind_dec_licitacao = row['ind_dec_licitacao']
        ind_dec_instr_conge = row['ind_dec_instr_conge']
        seq_contrato = row['seq_contrato']
        seq_termo_aditivo = row['seq_termo_aditivo']
        seq_convenio = row['seq_convenio']
        seq_licitacao = row['seq_licitacao']
        seq_dispensa = row['seq_dispensa']
        seq_instr_conge = row['seq_instr_conge']
        dsc_dotacao = row['dsc_dotacao']
        dsc_funcao = row['dsc_funcao']
        dsc_subfuncao = row['dsc_subfuncao']
        dsc_programa = row['dsc_programa']
        dsc_acao = row['dsc_acao']
        dsc_subacao = row['dsc_subacao']
        dsc_naturezadespesa = row['dsc_naturezadespesa']
        vlr_empenhado = row['vlr_empenhado']
        vlr_reforco = row['vlr_reforco']
        vlr_anulempenho = row['vlr_anulempenho']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO empenhos (seq_empenho, cod_municipio, seq_orgao, seq_unidade, cod_unidade, cod_subunidade," \
                " num_anoexercicio, num_mesexercicio, num_empenho, dat_empenho, dsc_modalidade, dsc_tipo_empenho," \
                " dsc_empenho, ind_dec_contrato, ind_dec_convenio, ind_dec_licitacao, ind_dec_instr_conge, seq_contrato," \
                " seq_termo_aditivo, seq_convenio, seq_licitacao, seq_dispensa, seq_instr_conge, dsc_dotacao, dsc_funcao," \
                " dsc_subfuncao, dsc_programa, dsc_acao, dsc_subacao, dsc_naturezadespesa, vlr_empenhado, vlr_reforco," \
                " vlr_anulempenho, num_versaoarq, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (seq_empenho, cod_municipio, seq_orgao, seq_unidade, cod_unidade, cod_subunidade, num_anoexercicio,
                  num_mesexercicio, num_empenho, dat_empenho, dsc_modalidade, dsc_tipo_empenho, dsc_empenho,
                  ind_dec_contrato, ind_dec_convenio, ind_dec_licitacao, ind_dec_instr_conge, seq_contrato,
                  seq_termo_aditivo, seq_convenio, seq_licitacao, seq_dispensa, seq_instr_conge, dsc_dotacao,
                  dsc_funcao, dsc_subfuncao, dsc_programa, dsc_acao, dsc_subacao, dsc_naturezadespesa, vlr_empenhado,
                  vlr_reforco, vlr_anulempenho, num_versaoarq, created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
