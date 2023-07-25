import datetime
import math
from typing import List, Dict
import logging


class TransformRawDataDespesasPagamentos:
    def transform(self, extract_data):
        logging.info('Transforma despesas pagamentos')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_pagamento = int(row['seq_pagamento'])
            seq_orgao = int(row['seq_orgao'])
            seq_unidade = int(row['seq_unidade'])
            seq_empenho = int(row['seq_empenho'])
            seq_rsp = int(row['seq_rsp'])
            seq_liquidacao = int(row['seq_liquidacao'])
            seq_orgao_empenho = int(row['seq_orgao_empenho'])
            seq_unid_empenho = int(row['seq_unid_empenho'])
            num_ano_referencia = int(row['num_ano_referencia'])
            num_mes_referencia = int(row['num_mes_referencia'])
            num_doc_resp = str(row['num_doc_resp'])
            nom_resp = str(row['nom_resp'])
            num_doc_credor = str(row['num_doc_credor'])
            nom_credor = str(row['nom_credor'])
            num_empenho = int(row['num_empenho'])

            # format field date
            dat_empenho = str(row['dat_empenho'])
            dat_empenho_arr = dat_empenho.split('/')
            year = int(dat_empenho_arr[2])
            month = int(dat_empenho_arr[1])
            day = int(dat_empenho_arr[0])
            dat_empenho = datetime.date(year, month, day)

            if not math.isnan(float(row['num_liquidacao'])):
                num_liquidacao = str(row['num_liquidacao'])
            else:
                num_liquidacao = 0

            # format field date
            dat_liquidacao = str(row['dat_liquidacao'])
            dat_liquidacao_arr = dat_liquidacao.split('/')
            if len(dat_liquidacao_arr) == 3:
                year = int(dat_liquidacao_arr[2])
                month = int(dat_liquidacao_arr[1])
                day = int(dat_liquidacao_arr[0])
                dat_liquidacao = datetime.date(year, month, day)
            else:
                dat_liquidacao = ''

            num_ord_pagamento = int(row['num_ord_pagamento'])

            # format field date
            dat_pagamento = str(row['dat_pagamento'])
            dat_pagamento_arr = dat_pagamento.split('/')
            year = int(dat_pagamento_arr[2])
            month = int(dat_pagamento_arr[1])
            day = int(dat_pagamento_arr[0])
            dat_pagamento = datetime.date(year, month, day)

            dsc_pagamento = str(row['dsc_pagamento'])
            dsc_tipo_pagamento = str(row['dsc_tipo_pagamento'])
            dsc_fonte_recurso = str(row['dsc_fonte_recurso'])
            vlr_pag_fonte = float(row['vlr_pag_fonte'])
            vlr_ret_fonte = float(row['vlr_ret_fonte'])
            vlr_ant_fonte = float(row['vlr_ant_fonte'])
            vlr_anu_fonte = float(row['vlr_anu_fonte'])
            num_versaoarq = int(row['num_versao_arq'])

            row = {
                'seq_pagamento': seq_pagamento,
                'seq_orgao': seq_orgao,
                'seq_unidade': seq_unidade,
                'seq_empenho': seq_empenho,
                'seq_rsp': seq_rsp,
                'seq_liquidacao': seq_liquidacao,
                'seq_orgao_empenho': seq_orgao_empenho,
                'seq_unid_empenho': seq_unid_empenho,
                'num_ano_referencia': num_ano_referencia,
                'num_mes_referencia': num_mes_referencia,
                'num_doc_resp': num_doc_resp,
                'nom_resp': nom_resp,
                'num_doc_credor': num_doc_credor,
                'nom_credor': nom_credor,
                'num_empenho': num_empenho,
                'dat_empenho': dat_empenho,
                'num_liquidacao': num_liquidacao,
                'dat_liquidacao': dat_liquidacao,
                'num_ord_pagamento': num_ord_pagamento,
                'dat_pagamento': dat_pagamento,
                'dsc_pagamento': dsc_pagamento,
                'dsc_tipo_pagamento': dsc_tipo_pagamento,
                'dsc_fonte_recurso': dsc_fonte_recurso,
                'vlr_pag_fonte': vlr_pag_fonte,
                'vlr_ret_fonte': vlr_ret_fonte,
                'vlr_ant_fonte': vlr_ant_fonte,
                'vlr_anu_fonte': vlr_anu_fonte,
                'num_versaoarq': num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
