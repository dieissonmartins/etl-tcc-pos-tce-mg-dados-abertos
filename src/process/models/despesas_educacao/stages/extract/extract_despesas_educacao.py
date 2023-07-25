import os
from typing import Dict
import pandas as pd
import logging


class ExtractDespesasEducacao:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai despesas educacao')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = [
            "cod_municipio",
            "seq_orgao",
            "seq_unidade",
            "num_ano_referencia",
            "num_mes_referencia",
            "dsc_funcao",
            "dsc_programa",
            "dsc_acao",
            "dsc_subacao",
            "dsc_nat_despesa",
            "dsc_fonte_recurso",
            "num_empenho",
            "dat_empenho",
            "vlr_empenho",
            "vlr_ref_empenho",
            "vlr_anu_empenho",
            "vlr_liquidado",
            "vlr_anu_liquidado",
            "vlr_pagamento",
            "vlr_anu_pagamento",
            "vlr_outras_baixas",
            "vlr_anu_outras_baixas",
            "vlr_rsp_proc",
            "vlr_rsp_nao_proc",
            "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
