import os
from typing import Dict
import pandas as pd
import logging


class ExtractDespesasPessoas:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai despesas pessoas')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = [
            'cod_municipio',
            'num_ano_referencia',
            'num_mes_referencia',
            'cod_nat_despesa',
            'dsc_nat_despesa',
            'vlr_executivo',
            'vlr_legislativo',
            'vlr_municipio',
            'num_versao_arq'
        ]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
