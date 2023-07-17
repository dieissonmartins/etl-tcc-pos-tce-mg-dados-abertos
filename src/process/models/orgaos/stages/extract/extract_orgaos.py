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

        df = pd.read_csv(file)

        print(df.to_string())
