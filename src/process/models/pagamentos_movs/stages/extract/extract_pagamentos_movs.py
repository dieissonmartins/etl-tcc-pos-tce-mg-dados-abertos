import os
from typing import Dict
import pandas as pd
import logging


class ExtractPagamentosMovs:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai pagamentos movimentação')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = ["seq_mov_pagamento",
                     "seq_pagamento",
                     "seq_orgao",
                     "num_ano_referencia",
                     "num_mes_referencia",
                     "dsc_tipo_doc",
                     "dsc_tipo_doc_livre",
                     "num_documento",
                     "dat_emissao",
                     "dsc_inst_financeira",
                     "dsc_agencia",
                     "dsc_conta_bancaria",
                     "dsc_finalidade_conta",
                     "dsc_tipo_aplicacao",
                     "num_aplicacao",
                     "vlr_movimentacao",
                     "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
