import os
from datetime import datetime
import logging


class LoadDataEmpenhos:
    def __init__(self, conn) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__conn = conn

    def load(self, transform_html_data, year):
        logging.info('load empenhos fontes')

        seq_orgao = transform_html_data[0]['seq_orgao']

        self.delete_empenhos_fontes(year, seq_orgao)

        for row in transform_html_data:
            logging.info('Importa novo empenho fonte')

            self.create_empenho_fonte(row)

    def delete_empenhos_fontes(self, year, seq_orgao):
        logging.info('Deleta empenhos fontes por ano')

        cursor = self.__conn.cursor()

        query = "DELETE FROM empenhos_fontes WHERE num_ano_referencia = %s AND seq_orgao = %s"

        where = (year, seq_orgao)

        cursor.execute(query, where)

    def create_empenho_fonte(self, row):
        cursor = self.__conn.cursor()

        seq_empenho_fonte = row['seq_empenho_fonte']
        seq_empenho = row['seq_empenho']
        seq_orgao = row['seq_orgao']
        seq_unidade = row['seq_unidade']
        num_ano_referencia = row['num_ano_referencia']
        num_mes_referencia = row['num_mes_referencia']
        dsc_fonte_recurso = row['dsc_fonte_recurso']
        vlr_empenho = row['vlr_empenho']
        vlr_reforco_emp = row['vlr_reforco_emp']
        vlr_anulacao_emp = row['vlr_anulacao_emp']
        vlr_liquidacao = row['vlr_liquidacao']
        vlr_anu_liquidacao = row['vlr_anu_liquidacao']
        vlr_pagamento = row['vlr_pagamento']
        vlr_anu_pagamento = row['vlr_anu_pagamento']
        vlr_outras_baixas = row['vlr_outras_baixas']
        vlr_anu_outras_baixas = row['vlr_anu_outras_baixas']
        num_versaoarq = row['num_versaoarq']
        created_at = datetime.now()
        updated_at = datetime.now()

        query = "INSERT INTO empenhos_fontes (seq_empenho_fonte, seq_empenho, seq_orgao, seq_unidade, num_ano_referencia, " \
                "num_mes_referencia, dsc_fonte_recurso, vlr_empenho, vlr_reforco_emp, vlr_anulacao_emp, vlr_liquidacao, " \
                "vlr_anu_liquidacao, vlr_pagamento, vlr_anu_pagamento, vlr_outras_baixas, vlr_anu_outras_baixas, " \
                "num_versaoarq, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (seq_empenho_fonte, seq_empenho, seq_orgao, seq_unidade, num_ano_referencia, num_mes_referencia,
                  dsc_fonte_recurso, vlr_empenho, vlr_reforco_emp, vlr_anulacao_emp, vlr_liquidacao, vlr_anu_liquidacao,
                  vlr_pagamento, vlr_anu_pagamento, vlr_outras_baixas, vlr_anu_outras_baixas, num_versaoarq,
                  created_at, updated_at)

        cursor.execute(query, values)

        self.__conn.commit()
