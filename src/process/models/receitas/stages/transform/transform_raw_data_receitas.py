from typing import List, Dict
import logging


class TransformRawDataReceitas:
    def transform(self, extract_data):
        logging.info('Transforma receitas')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_orgao = int(row['seq_orgao'])
            num_anoexercicio = int(row['num_anoexercicio'])
            dsc_cateconomica = str(row['dsc_cateconomica'])
            num_mesexercicio = str(row['num_mesexercicio'])
            dsc_origem = str(row['dsc_origem'])
            dsc_especie = str(row['dsc_especie'])
            dsc_rubrica = str(row['dsc_rubrica'])
            dsc_alinea = str(row['dsc_alinea'])
            dsc_subalinea = str(row['dsc_subalinea'])
            dsc_tipo = str(row['dsc_tipo'])
            dsc_fonterecurso = str(row['dsc_fonterecurso'])
            vlr_previsaoinicial = float(row['vlr_previsaoinicial'])
            vlr_previsaoatualizada = float(row['vlr_previsaoatualizada'])
            vlr_realizadoateperiodo = float(row['vlr_realizadoateperiodo'])
            num_versaoarq = str(row['num_versao_arq'])

            row = {
                "seq_orgao": seq_orgao,
                "num_anoexercicio": num_anoexercicio,
                "dsc_cateconomica": dsc_cateconomica,
                "num_mesexercicio": num_mesexercicio,
                "dsc_origem": dsc_origem,
                "dsc_especie": dsc_especie,
                "dsc_rubrica": dsc_rubrica,
                "dsc_alinea": dsc_alinea,
                "dsc_subalinea": dsc_subalinea,
                "dsc_tipo": dsc_tipo,
                "dsc_fonterecurso": dsc_fonterecurso,
                "vlr_previsaoinicial": vlr_previsaoinicial,
                "vlr_previsaoatualizada": vlr_previsaoatualizada,
                "vlr_realizadoateperiodo": vlr_realizadoateperiodo,
                "num_versaoarq": num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
