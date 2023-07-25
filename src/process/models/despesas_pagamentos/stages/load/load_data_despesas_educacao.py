import os
from datetime import datetime
import logging


class LoadDataDespesasPagamentos:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load despesas pagamentos')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_despesas_pagamentos(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa nova despesa pagamentos')

            self.create_despesa_pagamento(row)

    def delete_despesas_pagamentos(self, year, seq_orgao):
        logging.info('Deleta despesas pagamentos por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM despesas_pagamentos WHERE num_ano_referencia = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_despesa_pagamento(self, row):
        cursor = self.__conn.cursor()

        seq_pagamento = row['seq_pagamento']
        seq_orgao = row['seq_orgao']
        seq_unidade = row['seq_unidade']
        seq_empenho = row['seq_empenho']
        seq_rsp = row['seq_rsp']
        seq_liquidacao = row['seq_liquidacao']
        seq_orgao_empenho = row['seq_orgao_empenho']
        seq_unid_empenho = row['seq_unid_empenho']
        num_ano_referencia = row['num_ano_referencia']
        num_mes_referencia = row['num_mes_referencia']
        num_doc_resp = row['num_doc_resp']
        nom_resp = row['nom_resp']
        num_doc_credor = row['num_doc_credor']
        nom_credor = row['nom_credor']
        num_empenho = row['num_empenho']
        dat_empenho = row['dat_empenho']
        num_liquidacao = row['num_liquidacao']
        dat_liquidacao = row['dat_liquidacao']
        num_ord_pagamento = row['num_ord_pagamento']
        dat_pagamento = row['dat_pagamento']
        dsc_pagamento = row['dsc_pagamento']
        dsc_tipo_pagamento = row['dsc_tipo_pagamento']
        dsc_fonte_recurso = row['dsc_fonte_recurso']
        vlr_pag_fonte = row['vlr_pag_fonte']
        vlr_ret_fonte = row['vlr_ret_fonte']
        vlr_ant_fonte = row['vlr_ant_fonte']
        vlr_anu_fonte = row['vlr_anu_fonte']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO despesas_pagamentos (seq_pagamento, seq_orgao, seq_unidade, seq_empenho, seq_rsp, " \
                "seq_liquidacao, seq_orgao_empenho, seq_unid_empenho, num_ano_referencia, num_mes_referencia, " \
                "num_doc_resp, nom_resp, num_doc_credor, nom_credor, num_empenho, dat_empenho, num_liquidacao, " \
                "dat_liquidacao, num_ord_pagamento, dat_pagamento, dsc_pagamento, dsc_tipo_pagamento, dsc_fonte_recurso, " \
                "vlr_pag_fonte, vlr_ret_fonte, vlr_ant_fonte, vlr_anu_fonte, num_versaoarq, created_at, updated_at)  " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s, %s, %s)"

        values = (seq_pagamento, seq_orgao, seq_unidade, seq_empenho, seq_rsp, seq_liquidacao, seq_orgao_empenho,
                  seq_unid_empenho, num_ano_referencia, num_mes_referencia, num_doc_resp, nom_resp, num_doc_credor,
                  nom_credor, num_empenho, dat_empenho, num_liquidacao, dat_liquidacao, num_ord_pagamento,
                  dat_pagamento, dsc_pagamento, dsc_tipo_pagamento, dsc_fonte_recurso, vlr_pag_fonte, vlr_ret_fonte,
                  vlr_ant_fonte, vlr_anu_fonte, num_versaoarq, created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
