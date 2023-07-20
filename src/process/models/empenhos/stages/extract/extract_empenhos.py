import os
from typing import Dict
import pandas as pd
import logging


class ExtractEmpenhos:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Dict:
        logging.info('Extrai empenhos')

        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return {}

        col_names = ["seq_empenho",
                     "cod_municipio",
                     "seq_orgao",
                     "seq_unidade",
                     "cod_unidade",
                     "cod_subunidade",
                     "num_anoexercicio",
                     "num_mesexercicio",
                     "num_empenho",
                     "dat_empenho",
                     "dsc_modalidade",
                     "dsc_tipo_empenho",
                     "dsc_empenho",
                     "ind_dec_contrato",
                     "ind_dec_convenio",
                     "ind_dec_licitacao",
                     "ind_dec_instr_conge",
                     "seq_contrato",
                     "seq_termo_aditivo",
                     "seq_convenio",
                     "seq_licitacao",
                     "seq_dispensa",
                     "seq_instr_conge",
                     "dsc_dotacao",
                     "dsc_funcao",
                     "dsc_subfuncao",
                     "dsc_programa",
                     "dsc_acao",
                     "dsc_subacao",
                     "dsc_naturezadespesa",
                     "vlr_empenhado",
                     "vlr_reforco",
                     "vlr_anulempenho",
                     "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict(orient='records')

        return rows
