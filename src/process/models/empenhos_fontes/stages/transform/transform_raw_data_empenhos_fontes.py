import datetime
from typing import List, Dict
import logging


class TransformRawDataEmpenhos:
    def transform(self, extract_data):
        logging.info('Transforma empenhos fontes')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_empenho_fonte = int(row['seq_empenho_fonte'])
            seq_empenho = int(row['seq_empenho'])
            seq_orgao = int(row['seq_orgao'])
            seq_unidade = int(row['seq_unidade'])
            num_ano_referencia = int(row['num_ano_referencia'])
            num_mes_referencia = int(row['num_mes_referencia'])
            dsc_fonte_recurso = str(row['dsc_fonte_recurso'])
            vlr_empenho = float(row['vlr_empenho'])
            vlr_reforco_emp = float(row['vlr_reforco_emp'])
            vlr_anulacao_emp = float(row['vlr_anulacao_emp'])
            vlr_liquidacao = float(row['vlr_liquidacao'])
            vlr_anu_liquidacao = float(row['vlr_anu_liquidacao'])
            vlr_pagamento = float(row['vlr_pagamento'])
            vlr_anu_pagamento = float(row['vlr_anu_pagamento'])
            vlr_outras_baixas = float(row['vlr_outras_baixas'])
            vlr_anu_outras_baixas = float(row['vlr_anu_outras_baixas'])
            num_versaoarq = int(row['num_versao_arq'])

            row = {
                'seq_empenho_fonte': seq_empenho_fonte,
                'seq_empenho': seq_empenho,
                'seq_orgao': seq_orgao,
                'seq_unidade': seq_unidade,
                'num_ano_referencia': num_ano_referencia,
                'num_mes_referencia': num_mes_referencia,
                'dsc_fonte_recurso': dsc_fonte_recurso,
                'vlr_empenho': vlr_empenho,
                'vlr_reforco_emp': vlr_reforco_emp,
                'vlr_anulacao_emp': vlr_anulacao_emp,
                'vlr_liquidacao': vlr_liquidacao,
                'vlr_anu_liquidacao': vlr_anu_liquidacao,
                'vlr_pagamento': vlr_pagamento,
                'vlr_anu_pagamento': vlr_anu_pagamento,
                'vlr_outras_baixas': vlr_outras_baixas,
                'vlr_anu_outras_baixas': vlr_anu_outras_baixas,
                'num_versaoarq': num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
