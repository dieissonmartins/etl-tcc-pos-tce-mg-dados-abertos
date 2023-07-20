from typing import List, Dict
import logging


class TransformRawDataDespesas:
    def transform(self, extract_data):
        logging.info('Transforma receitas')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_orgao = int(row['seq_orgao'])
            cod_municipio = int(row['cod_municipio'])
            seq_unidade = str(row['seq_unidade'])
            cod_unidade = str(row['cod_unidade'])
            cod_subunidade = str(row['cod_subunidade'])
            num_anoexercicio = int(row['num_anoexercicio'])
            num_mesexercicio = int(row['num_mesexercicio'])
            dsc_funcao = str(row['dsc_funcao'])
            dsc_subfuncao = str(row['dsc_subfuncao'])
            dsc_programa = str(row['dsc_programa'])
            dsc_acao = str(row['dsc_acao'])
            dsc_subacao = str(row['dsc_subacao'])
            dsc_naturezadespesa = str(row['dsc_naturezadespesa'])
            dsc_fonterecurso = str(row['dsc_fonterecurso'])
            vlr_previsto = float(row['vlr_previsto'])
            vlr_acrescimo = float(row['vlr_acrescimo'])
            vlr_deducao = float(row['vlr_deducao'])
            vlr_empenhado = float(row['vlr_empenhado'])
            vlr_liquidado = float(row['vlr_liquidado'])
            vlr_pago = float(row['vlr_pago'])
            vlr_rspprocessado = float(row['vlr_rspprocessado'])
            vlr_rspnprocprocessado = float(row['vlr_rspnprocprocessado'])
            num_versaoarq = str(row['num_versao_arq'])

            row = {
                'seq_orgao': seq_orgao,
                'cod_municipio': cod_municipio,
                'seq_unidade': seq_unidade,
                'cod_unidade': cod_unidade,
                'cod_subunidade': cod_subunidade,
                'num_anoexercicio': num_anoexercicio,
                'num_mesexercicio': num_mesexercicio,
                'dsc_funcao': dsc_funcao,
                'dsc_subfuncao': dsc_subfuncao,
                'dsc_programa': dsc_programa,
                'dsc_acao': dsc_acao,
                'dsc_subacao': dsc_subacao,
                'dsc_naturezadespesa': dsc_naturezadespesa,
                'dsc_fonterecurso': dsc_fonterecurso,
                'vlr_previsto': vlr_previsto,
                'vlr_acrescimo': vlr_acrescimo,
                'vlr_deducao': vlr_deducao,
                'vlr_empenhado': vlr_empenhado,
                'vlr_liquidado': vlr_liquidado,
                'vlr_pago': vlr_pago,
                'vlr_rspprocessado': vlr_rspprocessado,
                'vlr_rspnprocprocessado': vlr_rspnprocprocessado,
                'num_versaoarq': num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
