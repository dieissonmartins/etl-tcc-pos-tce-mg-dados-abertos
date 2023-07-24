import os
from typing import Dict
import pandas as pd
import logging


class ExtractEmpenhosFontes:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai empenhos fontes')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = ["seq_empenho_fonte",
                     "seq_empenho",
                     "seq_orgao",
                     "seq_unidade",
                     "num_ano_referencia",
                     "num_mes_referencia",
                     "dsc_fonte_recurso",
                     "vlr_empenho",
                     "vlr_reforco_emp",
                     "vlr_anulacao_emp",
                     "vlr_liquidacao",
                     "vlr_anu_liquidacao",
                     "vlr_pagamento",
                     "vlr_anu_pagamento",
                     "vlr_outras_baixas",
                     "vlr_anu_outras_baixas",
                     "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
