from datetime import datetime
from typing import List, Dict
import logging


class TransformRawDataDespesasEducacao:
    def transform(self, extract_data):
        logging.info('Transforma despesas educacao')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            cod_municipio = int(row['cod_municipio'])
            seq_orgao = int(row['seq_orgao'])
            seq_unidade = int(row['seq_unidade'])
            num_ano_referencia = int(row['num_ano_referencia'])
            num_mes_referencia = str(row['num_mes_referencia'])
            dsc_funcao = str(row['dsc_funcao'])
            dsc_programa = str(row['dsc_programa'])
            dsc_acao = str(row['dsc_acao'])
            dsc_subacao = str(row['dsc_subacao'])
            dsc_nat_despesa = str(row['dsc_nat_despesa'])
            dsc_fonte_recurso = str(row['dsc_fonte_recurso'])
            num_empenho = int(row['num_empenho'])

            # format field date
            dat_empenho = str(row['dat_empenho'])
            dat_empenho_arr = dat_empenho.split('/')
            year = int(dat_empenho_arr[2])
            month = int(dat_empenho_arr[1])
            day = int(dat_empenho_arr[0])
            dat_empenho = datetime.date(year, month, day)

            vlr_empenho = float(row['vlr_empenho'])
            vlr_ref_empenho = float(row['vlr_ref_empenho'])
            vlr_anu_empenho = float(row['vlr_anu_empenho'])
            vlr_liquidado = float(row['vlr_liquidado'])
            vlr_anu_liquidado = float(row['vlr_anu_liquidado'])
            vlr_pagamento = float(row['vlr_pagamento'])
            vlr_anu_pagamento = float(row['vlr_anu_pagamento'])
            vlr_outras_baixas = float(row['vlr_outras_baixas'])
            vlr_anu_outras_baixas = float(row['vlr_anu_outras_baixas'])
            vlr_rsp_proc = float(row['vlr_rsp_proc'])
            vlr_rsp_nao_proc = float(row['vlr_rsp_nao_proc'])
            num_versaoarq = int(row['num_versaoarq'])

            row = {
                'cod_municipio': cod_municipio,
                'seq_orgao': seq_orgao,
                'seq_unidade': seq_unidade,
                'num_ano_referencia': num_ano_referencia,
                'num_mes_referencia': num_mes_referencia,
                'dsc_funcao': dsc_funcao,
                'dsc_programa': dsc_programa,
                'dsc_acao': dsc_acao,
                'dsc_subacao': dsc_subacao,
                'dsc_nat_despesa': dsc_nat_despesa,
                'dsc_fonte_recurso': dsc_fonte_recurso,
                'num_empenho': num_empenho,
                'dat_empenho': dat_empenho,
                'vlr_empenho': vlr_empenho,
                'vlr_ref_empenho': vlr_ref_empenho,
                'vlr_anu_empenho': vlr_anu_empenho,
                'vlr_liquidado': vlr_liquidado,
                'vlr_anu_liquidado': vlr_anu_liquidado,
                'vlr_pagamento': vlr_pagamento,
                'vlr_anu_pagamento': vlr_anu_pagamento,
                'vlr_outras_baixas': vlr_outras_baixas,
                'vlr_anu_outras_baixas': vlr_anu_outras_baixas,
                'vlr_rsp_proc': vlr_rsp_proc,
                'vlr_rsp_nao_proc': vlr_rsp_nao_proc,
                'num_versaoarq': num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
