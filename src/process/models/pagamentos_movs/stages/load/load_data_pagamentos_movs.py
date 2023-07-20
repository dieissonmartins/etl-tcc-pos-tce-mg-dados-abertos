import os
from datetime import datetime
import logging


class LoadDataPagamentosMovs:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load pagamentos')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_pagamentos(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa novo pagamento')

            self.create_pagamento(row)

    def delete_pagamentos(self, year, seq_orgao):
        logging.info('Deleta pagamentos por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM pagamentos_movs WHERE num_ano_referencia = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_pagamento(self, row):
        cursor = self.__conn.cursor()

        seq_mov_pagamento = row['seq_mov_pagamento']
        seq_pagamento = row['seq_pagamento']
        seq_orgao = row['seq_orgao']
        num_ano_referencia = row['num_ano_referencia']
        num_mes_referencia = row['num_mes_referencia']
        dsc_tipo_doc = row['dsc_tipo_doc']
        dsc_tipo_doc_livre = row['dsc_tipo_doc_livre']
        num_documento = row['num_documento']
        dat_emissao = row['dat_emissao']
        dsc_inst_financeira = row['dsc_inst_financeira']
        dsc_agencia = row['dsc_agencia']
        dsc_conta_bancaria = row['dsc_conta_bancaria']
        dsc_finalidade_conta = row['dsc_finalidade_conta']
        dsc_tipo_aplicacao = row['dsc_tipo_aplicacao']
        num_aplicacao = row['num_aplicacao']
        vlr_movimentacao = row['vlr_movimentacao']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO pagamentos_movs (seq_mov_pagamento, seq_pagamento, seq_orgao, num_ano_referencia, " \
                "num_mes_referencia, dsc_tipo_doc, dsc_tipo_doc_livre, num_documento, dat_emissao, dsc_inst_financeira, " \
                "dsc_agencia, dsc_conta_bancaria, dsc_finalidade_conta, dsc_tipo_aplicacao, num_aplicacao, " \
                "vlr_movimentacao, num_versaoarq, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (seq_mov_pagamento, seq_pagamento, seq_orgao, num_ano_referencia, num_mes_referencia, dsc_tipo_doc,
                  dsc_tipo_doc_livre, num_documento, dat_emissao, dsc_inst_financeira, dsc_agencia, dsc_conta_bancaria,
                  dsc_finalidade_conta, dsc_tipo_aplicacao, num_aplicacao, vlr_movimentacao, num_versaoarq, created_at,
                  updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
