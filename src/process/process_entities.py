import os

from src.process.models.orgaos.stages.extract.extract_receitas import ExtractOrgaos
from src.process.models.orgaos.stages.load.load_data_orgaos import LoadDataOrgaos
from src.process.models.orgaos.stages.transform.transform_raw_data_orgaos import TransformRawDataOrgaos
from src.drivers.conn import Conn
import logging


class ProcessEntities:

    def __init__(self, path) -> None:
        self.__path = path

        conn = Conn()
        self.__conn = conn.connect()

    def run(self, entities):
        for files_path in entities.values():

            for file_path in files_path:
                file_path_arr = file_path.split("/")
                model = file_path_arr[3].split(".")[3]
                entity_id = file_path_arr[1]

                # etl orgaos
                self.pipeline_orgaos(file_path, model, entity_id)

                # etl receitas
                self.pipeline_receitas(file_path, model, entity_id)

        # TODO: matar conn banco de dados
        # self.__conn.connect.close()

    def pipeline_orgaos(self, file_path, model, entity_id):

        if not model == 'orgao':
            return

        logging.info('Início processar: ' + model)

        extract_orgaos = ExtractOrgaos(self.__path, file_path, model, entity_id)
        extract_html_data = extract_orgaos.extract()

        transform_raw_data = TransformRawDataOrgaos()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataOrgaos(self.__conn)
        load_data.load(transform_html_data)

    def pipeline_receitas(self, file_path, model, entity_id):

        if not model == 'receita':
            return

        logging.info('Início processar: ' + model)
