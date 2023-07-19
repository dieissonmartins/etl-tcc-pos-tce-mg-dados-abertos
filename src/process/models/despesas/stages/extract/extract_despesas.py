import os
from typing import Any, Dict
import pandas as pd
import logging


class ExtractDespesas:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai despesas')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = ["seq_orgao",
                     "cod_municipio",
                     "seq_unidade",
                     "cod_unidade",
                     "cod_subunidade",
                     "num_anoexercicio",
                     "num_mesexercicio",
                     "dsc_funcao",
                     "dsc_subfuncao",
                     "dsc_programa",
                     "dsc_acao",
                     "dsc_subacao",
                     "dsc_naturezadespesa",
                     "dsc_fonterecurso",
                     "vlr_previsto",
                     "vlr_acrescimo",
                     "vlr_deducao",
                     "vlr_empenhado",
                     "vlr_liquidado",
                     "vlr_pago",
                     "vlr_rspprocessado",
                     "vlr_rspnprocprocessado",
                     "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
