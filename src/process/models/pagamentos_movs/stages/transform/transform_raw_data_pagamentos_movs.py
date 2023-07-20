from typing import List, Dict
import logging
from datetime import date


class TransformRawDataReceitas:
    def transform(self, extract_data):
        logging.info('Transforma receitas')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_mov_pagamento = int(row['seq_mov_pagamento'])
            seq_pagamento = int(row['seq_pagamento'])
            seq_orgao = int(row['seq_orgao'])
            num_ano_referencia = int(row['num_ano_referencia'])
            num_mes_referencia = int(row['num_mes_referencia'])
            dsc_tipo_doc = str(row['dsc_tipo_doc'])
            dsc_tipo_doc_livre = str(row['dsc_tipo_doc_livre'])
            num_documento = str(row['num_documento'])

            # format field date
            dat_emissao = str(row['dat_emissao'])
            dat_emissao_arr = dat_emissao.split('/')
            dat_emissao = date(int(dat_emissao_arr[2]), int(dat_emissao_arr[2]), int(dat_emissao_arr[0]))

            dsc_inst_financeira = str(row['dsc_inst_financeira'])
            dsc_agencia = str(row['dsc_agencia'])
            dsc_conta_bancaria = str(row['dsc_conta_bancaria'])
            dsc_finalidade_conta = str(row['dsc_finalidade_conta'])
            dsc_tipo_aplicacao = str(row['dsc_tipo_aplicacao'])
            num_aplicacao = int(row['num_aplicacao'])
            vlr_movimentacao = float(row['vlr_movimentacao'])
            num_versaoarq = float(row['num_versao_arq'])

            row = {
                "seq_mov_pagamento": seq_mov_pagamento,
                "seq_pagamento": seq_pagamento,
                "seq_orgao": seq_orgao,
                "num_ano_referencia": num_ano_referencia,
                "num_mes_referencia": num_mes_referencia,
                "dsc_tipo_doc": dsc_tipo_doc,
                "dsc_tipo_doc_livre": dsc_tipo_doc_livre,
                "num_documento": num_documento,
                "dat_emissao": dat_emissao,
                "dsc_inst_financeira": dsc_inst_financeira,
                "dsc_agencia": dsc_agencia,
                "dsc_conta_bancaria": dsc_conta_bancaria,
                "dsc_finalidade_conta": dsc_finalidade_conta,
                "dsc_tipo_aplicacao": dsc_tipo_aplicacao,
                "num_aplicacao": num_aplicacao,
                "vlr_movimentacao": vlr_movimentacao,
                "num_versaoarq": num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
