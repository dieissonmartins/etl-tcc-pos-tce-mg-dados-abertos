import os
from typing import Any
import pandas as pd


class ExtractOrgaos:

    def __init__(self, path, file_path, model, entity_id) -> None:
        self.__path = path
        self.__file_path = file_path
        self.__model = model
        self.__entity_id = entity_id
        self.__file = self.__path + '/src/drivers/tmp/' + self.__file_path

    def extract(self) -> Any:
        file = self.__file

        check_file = os.path.isfile(file)

        if not check_file:
            return []

        col_names = ["seq_orgao",
                     "num_anoexercicio",
                     "cod_orgao",
                     "nom_orgao",
                     "tipo_orgao",
                     "cod_municipio",
                     "nom_municipio",
                     "cod_uf",
                     "sgl_uf",
                     "nom_uf",
                     "dsc_regiaoplanejamento",
                     "num_versao_arq"]

        df = pd.read_csv(file, header=0, names=col_names, sep=';')

        rows = df.to_dict()

        return rows
