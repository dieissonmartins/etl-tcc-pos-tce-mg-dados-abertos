from typing import List, Dict
import logging

class TransformRawDataOrgaos:
    def transform(self, extract_data):

        logging.info('Transforma orgão')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_orgao = int(row['seq_orgao'])
            num_anoexercicio = int(row['num_anoexercicio'])
            cod_orgao = str(row['cod_orgao'])
            nom_orgao = str(row['nom_orgao'])
            tipo_orgao = str(row['tipo_orgao'])
            cod_municipio = int(row['cod_municipio'])
            nom_municipio = str(row['nom_municipio'])
            cod_uf = str(row['cod_uf'])
            sgl_uf = str(row['sgl_uf'])
            nom_uf = str(row['nom_uf'])
            dsc_regiaoplanejamento = str(row['dsc_regiaoplanejamento'])
            num_versao_arq = str(row['num_versao_arq'])

            row = {
                'seq_orgao': seq_orgao,
                'num_anoexercicio': num_anoexercicio,
                'cod_orgao': cod_orgao,
                'nom_orgao': nom_orgao,
                'tipo_orgao': tipo_orgao,
                'cod_municipio': cod_municipio,
                'nom_municipio': nom_municipio,
                'cod_uf': cod_uf,
                'sgl_uf': sgl_uf,
                'nom_uf': nom_uf,
                'dsc_regiaoplanejamento': dsc_regiaoplanejamento,
                'num_versao_arq': num_versao_arq
            }

            aux.append(row)

        ret = aux

        return ret
