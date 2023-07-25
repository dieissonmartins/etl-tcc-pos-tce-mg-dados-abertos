import os
from datetime import datetime
import logging


class LoadDataDespesasEducacao:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load despesas educacao')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_despesas_educacao(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa nova despesa educacao')

            self.create_despesa_educacao(row)

    def delete_despesas_educacao(self, year, seq_orgao):
        logging.info('Deleta despesas educacao por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM despesas_educacao WHERE num_ano_referencia = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_despesa_educacao(self, row):
        cursor = self.__conn.cursor()

        cod_municipio = row['cod_municipio']
        seq_orgao = row['seq_orgao']
        seq_unidade = row['seq_unidade']
        num_ano_referencia = row['num_ano_referencia']
        num_mes_referencia = row['num_mes_referencia']
        dsc_funcao = row['dsc_funcao']
        dsc_subfuncao = row['dsc_subfuncao']
        dsc_programa = row['dsc_programa']
        dsc_acao = row['dsc_acao']
        dsc_subacao = row['dsc_subacao']
        dsc_nat_despesa = row['dsc_nat_despesa']
        dsc_fonte_recurso = row['dsc_fonte_recurso']
        num_empenho = row['num_empenho']
        dat_empenho = row['dat_empenho']
        vlr_empenho = row['vlr_empenho']
        vlr_ref_empenho = row['vlr_ref_empenho']
        vlr_anu_empenho = row['vlr_anu_empenho']
        vlr_liquidado = row['vlr_liquidado']
        vlr_anu_liquidado = row['vlr_anu_liquidado']
        vlr_pagamento = row['vlr_pagamento']
        vlr_anu_pagamento = row['vlr_anu_pagamento']
        vlr_outras_baixas = row['vlr_outras_baixas']
        vlr_anu_outras_baixas = row['vlr_anu_outras_baixas']
        vlr_rsp_proc = row['vlr_rsp_proc']
        vlr_rsp_nao_proc = row['vlr_rsp_nao_proc']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO despesas_educacao (cod_municipio, seq_orgao, seq_unidade, num_ano_referencia, " \
                "num_mes_referencia, dsc_funcao, dsc_subfuncao, dsc_programa, dsc_acao, dsc_subacao, dsc_nat_despesa, " \
                "dsc_fonte_recurso, num_empenho, dat_empenho, vlr_empenho, vlr_ref_empenho, vlr_anu_empenho, " \
                "vlr_liquidado, vlr_anu_liquidado, vlr_pagamento, vlr_anu_pagamento, vlr_outras_baixas, " \
                "vlr_anu_outras_baixas, vlr_rsp_proc, vlr_rsp_nao_proc, num_versaoarq, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (
            cod_municipio, seq_orgao, seq_unidade, num_ano_referencia, num_mes_referencia, dsc_funcao, dsc_subfuncao, dsc_programa,
            dsc_acao, dsc_subacao, dsc_nat_despesa, dsc_fonte_recurso, num_empenho, dat_empenho, vlr_empenho,
            vlr_ref_empenho, vlr_anu_empenho, vlr_liquidado, vlr_anu_liquidado, vlr_pagamento, vlr_anu_pagamento,
            vlr_outras_baixas, vlr_anu_outras_baixas, vlr_rsp_proc, vlr_rsp_nao_proc, num_versaoarq,
            created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
