import os
from typing import Any, Dict
import pandas as pd
import logging


class ExtractReceitas:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai receitas')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = ["seq_orgao",
                     "num_anoexercicio",
                     "num_mesexercicio",
                     "dsc_cateconomica",
                     "dsc_origem",
                     "dsc_especie",
                     "dsc_rubrica",
                     "dsc_alinea",
                     "dsc_subalinea",
                     "dsc_tipo",
                     "dsc_fonterecurso",
                     "vlr_previsaoinicial",
                     "vlr_previsaoatualizada",
                     "vlr_realizadoateperiodo",
                     "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
