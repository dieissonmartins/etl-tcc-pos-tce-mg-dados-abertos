import datetime
from typing import List, Dict
import logging


class TransformRawDataEmpenhos:
    def transform(self, extract_data):
        logging.info('Transforma empenhos')

        ret = self.__filter_and_transform_data(extract_data)
        return ret

    def __filter_and_transform_data(self, data_content) -> List[Dict]:
        aux = []

        for row in data_content:
            seq_empenho = int(row['seq_empenho'])
            cod_municipio = int(row['cod_municipio'])
            seq_orgao = int(row['seq_orgao'])
            seq_unidade = int(row['seq_unidade'])
            cod_unidade = int(row['cod_unidade'])
            cod_subunidade = int(row['cod_subunidade'])
            num_anoexercicio = int(row['num_anoexercicio'])
            num_mesexercicio = int(row['num_mesexercicio'])
            num_empenho = int(row['num_empenho'])

            # format field date
            dat_empenho = str(row['dat_empenho'])
            dat_empenho_arr = dat_empenho.split('/')
            year = int(dat_empenho_arr[2])
            month = int(dat_empenho_arr[1])
            day = int(dat_empenho_arr[0])
            dat_empenho = datetime.date(year, month, day)

            dsc_modalidade = str(row['dsc_modalidade'])
            dsc_tipo_empenho = str(row['dsc_tipo_empenho'])
            dsc_empenho = str(row['dsc_empenho'])
            ind_dec_contrato = str(row['ind_dec_contrato'])
            ind_dec_convenio = str(row['ind_dec_convenio'])
            ind_dec_licitacao = str(row['ind_dec_licitacao'])
            ind_dec_instr_conge = str(row['ind_dec_instr_conge'])
            seq_contrato = int(row['seq_contrato'])
            seq_termo_aditivo = int(row['seq_termo_aditivo'])
            seq_convenio = int(row['seq_convenio'])
            seq_licitacao = int(row['seq_licitacao'])
            seq_dispensa = int(row['seq_dispensa'])
            seq_instr_conge = int(row['seq_instr_conge'])
            dsc_dotacao = str(row['dsc_dotacao'])
            dsc_funcao = str(row['dsc_funcao'])
            dsc_subfuncao = str(row['dsc_subfuncao'])
            dsc_programa = str(row['dsc_programa'])
            dsc_acao = str(row['dsc_acao'])
            dsc_subacao = str(row['dsc_subacao'])
            dsc_naturezadespesa = str(row['dsc_naturezadespesa'])
            vlr_empenhado = float(row['vlr_empenhado'])
            vlr_reforco = float(row['vlr_reforco'])
            vlr_anulempenho = float(row['vlr_anulempenho'])
            num_versaoarq = str(row['num_versao_arq'])

            row = {
                'seq_empenho': seq_empenho,
                'cod_municipio': cod_municipio,
                'seq_orgao': seq_orgao,
                'seq_unidade': seq_unidade,
                'cod_unidade': cod_unidade,
                'cod_subunidade': cod_subunidade,
                'num_anoexercicio': num_anoexercicio,
                'num_mesexercicio': num_mesexercicio,
                'num_empenho': num_empenho,
                'dat_empenho': dat_empenho,
                'dsc_modalidade': dsc_modalidade,
                'dsc_tipo_empenho': dsc_tipo_empenho,
                'dsc_empenho': dsc_empenho,
                'ind_dec_contrato': ind_dec_contrato,
                'ind_dec_convenio': ind_dec_convenio,
                'ind_dec_licitacao': ind_dec_licitacao,
                'ind_dec_instr_conge': ind_dec_instr_conge,
                'seq_contrato': seq_contrato,
                'seq_termo_aditivo': seq_termo_aditivo,
                'seq_convenio': seq_convenio,
                'seq_licitacao': seq_licitacao,
                'seq_dispensa': seq_dispensa,
                'seq_instr_conge': seq_instr_conge,
                'dsc_dotacao': dsc_dotacao,
                'dsc_funcao': dsc_funcao,
                'dsc_subfuncao': dsc_subfuncao,
                'dsc_programa': dsc_programa,
                'dsc_acao': dsc_acao,
                'dsc_subacao': dsc_subacao,
                'dsc_naturezadespesa': dsc_naturezadespesa,
                'vlr_empenhado': vlr_empenhado,
                'vlr_reforco': vlr_reforco,
                'vlr_anulempenho': vlr_anulempenho,
                'num_versaoarq': num_versaoarq
            }

            aux.append(row)

        ret = aux

        return ret
