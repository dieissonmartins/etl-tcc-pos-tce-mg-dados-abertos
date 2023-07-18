import os

from src.process.models.orgaos.stages.extract.extract_orgaos import ExtractOrgaos
from src.process.models.orgaos.stages.load.load_data_orgaos import LoadDataOrgaos
from src.process.models.orgaos.stages.transform.transform_raw_data_orgaos import TransformRawDataOrgaos


class ProcessEntities:

    def __init__(self, path) -> None:
        self.__path = path

    def run(self, entities):
        for files_path in entities.values():

            for file_path in files_path:
                # etl orgaos
                self.pipeline_orgaos(file_path)

    def pipeline_orgaos(self, file_path):
        file_path_arr = file_path.split("/")
        model = file_path_arr[3].split(".")[3]
        entity_id = file_path_arr[1]

        if not model == 'orgao':
            return

        extract_orgaos = ExtractOrgaos(self.__path, file_path, model, entity_id)
        extract_html_data = extract_orgaos.extract()

        transform_raw_data = TransformRawDataOrgaos()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataOrgaos()
        load_data.load(transform_html_data)