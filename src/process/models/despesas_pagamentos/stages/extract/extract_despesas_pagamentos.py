import os
from typing import Dict
import pandas as pd
import logging


class ExtractDespesasPagamentos:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai despesas pegamentos')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = [
            'seq_pagamento',
            'seq_orgao',
            'seq_unidade',
            'seq_empenho',
            'seq_rsp',
            'seq_liquidacao',
            'seq_orgao_empenho',
            'seq_unid_empenho',
            'num_ano_referencia',
            'num_mes_referencia',
            'num_doc_resp',
            'nom_resp',
            'num_doc_credor',
            'nom_credor',
            'num_empenho',
            'dat_empenho',
            'num_liquidacao',
            'dat_liquidacao',
            'num_ord_pagamento',
            'dat_pagamento',
            'dsc_pagamento',
            'dsc_tipo_pagamento',
            'dsc_fonte_recurso',
            'vlr_pag_fonte',
            'vlr_ret_fonte',
            'vlr_ant_fonte',
            'vlr_anu_fonte',
            'num_versao_arq'
        ]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
