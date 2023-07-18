from typing import List, Dict


class TransformRawDataOrgaos:
    def transform(self, extract_data):
        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = {}

        for data in data_content.items():
            debug = data

            debug2 = ''

        ret = aux

        return []
