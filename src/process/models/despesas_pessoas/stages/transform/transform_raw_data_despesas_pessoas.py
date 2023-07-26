from typing import List, Dict
import logging


class TransformRawDataDespesasPessoas:
    def transform(self, extract_data):
        logging.info('Transforma despesas pessoas')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            cod_municipio = int(row['cod_municipio'])
            num_ano_referencia = int(row['num_ano_referencia'])
            num_mes_referencia = int(row['num_mes_referencia'])
            cod_nat_despesa = int(row['cod_nat_despesa'])
            dsc_nat_despesa = str(row['dsc_nat_despesa'])
            vlr_executivo = float(row['vlr_executivo'])
            vlr_legislativo = float(row['vlr_legislativo'])
            vlr_municipio = float(row['vlr_municipio'])
            num_versaoarq = str(row['num_versao_arq'])

            row = {
                'cod_municipio': cod_municipio,
                'num_ano_referencia': num_ano_referencia,
                'num_mes_referencia': num_mes_referencia,
                'cod_nat_despesa': cod_nat_despesa,
                'dsc_nat_despesa': dsc_nat_despesa,
                'vlr_executivo': vlr_executivo,
                'vlr_legislativo': vlr_legislativo,
                'vlr_municipio': vlr_municipio,
                'num_versaoarq': num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
