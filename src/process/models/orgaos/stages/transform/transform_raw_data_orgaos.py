from typing import List, Dict


class TransformRawDataOrgaos:
    def transform(self, extract_data):
        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:

            seq_orgao = int(row['seq_orgao'])
            num_anoexercicio = int(row['num_anoexercicio'])
            cod_orgao = int(row['cod_orgao'])

            row = {
                'seq_orgao': seq_orgao,
                'num_anoexercicio': num_anoexercicio,
                'cod_orgao': cod_orgao,
            }

            aux.append(row)

        ret = aux

        return []
