from src.process.models.despesas.stages.extract.extract_despesas import ExtractDespesas
from src.process.models.despesas.stages.load.load_data_despesas import LoadDataDespesas
from src.process.models.despesas.stages.transform.transform_raw_data_despesas import TransformRawDataDespesas
from src.process.models.despesas_educacao.stages.extract.extract_despesas_educacao import ExtractDespesasEducacao
from src.process.models.despesas_educacao.stages.load.load_data_despesas_educacao import LoadDataDespesasEducacao
from src.process.models.despesas_educacao.stages.transform.transform_raw_data_despesas_educacao import \
    TransformRawDataDespesasEducacao
from src.process.models.despesas_pagamentos.stages.extract.extract_despesas_pagamentos import ExtractDespesasPagamentos
from src.process.models.despesas_pagamentos.stages.load.load_data_despesas_pagamentos import LoadDataDespesasPagamentos
from src.process.models.despesas_pagamentos.stages.transform.transform_raw_data_despesas_pagamentos import \
    TransformRawDataDespesasPagamentos
from src.process.models.despesas_pessoas.stages.extract.extract_despesas_pessoas import ExtractDespesasPessoas
from src.process.models.despesas_pessoas.stages.load.load_data_despesas_pessoas import LoadDataDespesasPessoas
from src.process.models.despesas_pessoas.stages.transform.transform_raw_data_despesas_pessoas import \
    TransformRawDataDespesasPessoas
from src.process.models.despesas_saude.stages.extract.extract_despesas_saude import ExtractDespesasSaude
from src.process.models.despesas_saude.stages.load.load_data_despesas_saude import LoadDataDespesasSaude
from src.process.models.despesas_saude.stages.transform.transform_raw_data_despesas_saude import \
    TransformRawDataDespesasSaude
from src.process.models.empenhos.stages.extract.extract_empenhos import ExtractEmpenhos
from src.process.models.empenhos.stages.load.load_data_empenhos import LoadDataEmpenhos
from src.process.models.empenhos.stages.transform.transform_raw_data_empenhos import TransformRawDataEmpenhos
from src.process.models.empenhos_fontes.stages.extract.extract_empenhos_fontes import ExtractEmpenhosFontes
from src.process.models.empenhos_fontes.stages.load.load_data_empenhos_fontes import LoadDataEmpenhosFontes
from src.process.models.empenhos_fontes.stages.transform.transform_raw_data_empenhos_fontes import \
    TransformRawDataEmpenhosFontes
from src.process.models.orgaos.stages.extract.extract_orgaos import ExtractOrgaos
from src.process.models.orgaos.stages.load.load_data_orgaos import LoadDataOrgaos
from src.process.models.orgaos.stages.transform.transform_raw_data_orgaos import TransformRawDataOrgaos
from src.drivers.conn import Conn
import logging

from src.process.models.pagamentos_movs.stages.extract.extract_pagamentos_movs import ExtractPagamentosMovs
from src.process.models.pagamentos_movs.stages.load.load_data_pagamentos_movs import LoadDataPagamentosMovs
from src.process.models.pagamentos_movs.stages.transform.transform_raw_data_pagamentos_movs import \
    TransformRawDataPagamentosMovs
from src.process.models.receitas.stages.extract.extract_receitas import ExtractReceitas
from src.process.models.receitas.stages.load.load_data_receitas import LoadDataReceitas
from src.process.models.receitas.stages.transform.transform_raw_data_receitas import TransformRawDataReceitas


class ProcessEntities:

    def __init__(self, path, year) -> None:
        self.__path = path
        self.__year = year

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

                # etl despesas
                self.pipeline_despesas(file_path, model, entity_id)

                # etl movimentacoes
                self.pipeline_movimentacoes(file_path, model, entity_id)

                # etl empenhos
                self.pipeline_empenhos(file_path, model, entity_id)

                # etl empenhos fontes
                self.pipeline_empenhos_fontes(file_path, model, entity_id)

                # etl despesas educacao
                self.pipeline_despesas_educacao(file_path, model, entity_id)

                # etl despesas pagamentos
                self.pipeline_despesas_pagamentos(file_path, model, entity_id)

                # etl despesas pessoas
                self.pipeline_despesas_pessoas(file_path, model, entity_id)

                # etl despesas saude
                self.pipeline_despesas_saude(file_path, model, entity_id)

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

        extract_receitas = ExtractReceitas(self.__path, file_path, model, entity_id)
        extract_html_data = extract_receitas.extract()

        transform_raw_data = TransformRawDataReceitas()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataReceitas(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_despesas(self, file_path, model, entity_id):

        if not model == 'despesa':
            return

        logging.info('Início processar: ' + model)

        extract_despesas = ExtractDespesas(self.__path, file_path, model, entity_id)
        extract_html_data = extract_despesas.extract()

        transform_raw_data = TransformRawDataDespesas()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataDespesas(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_movimentacoes(self, file_path, model, entity_id):

        if not model == 'movPagamento':
            return

        logging.info('Início processar: ' + model)

        extract_despesas = ExtractPagamentosMovs(self.__path, file_path, model, entity_id)
        extract_html_data = extract_despesas.extract()

        transform_raw_data = TransformRawDataPagamentosMovs()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataPagamentosMovs(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_empenhos(self, file_path, model, entity_id):

        if not model == 'empenho':
            return

        logging.info('Início processar: ' + model)

        extract_empenhos = ExtractEmpenhos(self.__path, file_path, model, entity_id)
        extract_html_data = extract_empenhos.extract()

        transform_raw_data = TransformRawDataEmpenhos()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataEmpenhos(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_empenhos_fontes(self, file_path, model, entity_id):

        if not model == 'empenhoFonte':
            return

        logging.info('Início processar: ' + model)

        extract_empenhos = ExtractEmpenhosFontes(self.__path, file_path, model, entity_id)
        extract_html_data = extract_empenhos.extract()

        transform_raw_data = TransformRawDataEmpenhosFontes()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataEmpenhosFontes(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_despesas_educacao(self, file_path, model, entity_id):

        if not model == 'educacao':
            return

        logging.info('Início processar: ' + model)

        extract_empenhos = ExtractDespesasEducacao(self.__path, file_path, model, entity_id)
        extract_html_data = extract_empenhos.extract()

        transform_raw_data = TransformRawDataDespesasEducacao()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataDespesasEducacao(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_despesas_pagamentos(self, file_path, model, entity_id):

        if not model == 'pagamento':
            return

        logging.info('Início processar: ' + model)

        extract_empenhos = ExtractDespesasPagamentos(self.__path, file_path, model, entity_id)
        extract_html_data = extract_empenhos.extract()

        transform_raw_data = TransformRawDataDespesasPagamentos()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataDespesasPagamentos(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_despesas_pessoas(self, file_path, model, entity_id):

        if not model == 'despPessoal':
            return

        logging.info('Início processar: ' + model)

        extract_empenhos = ExtractDespesasPessoas(self.__path, file_path, model, entity_id)
        extract_html_data = extract_empenhos.extract()

        transform_raw_data = TransformRawDataDespesasPessoas()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataDespesasPessoas(self.__conn)
        load_data.load(transform_html_data, self.__year)

    def pipeline_despesas_saude(self, file_path, model, entity_id):

        if not model == 'saude':
            return

        logging.info('Início processar: ' + model)

        extract_empenhos = ExtractDespesasSaude(self.__path, file_path, model, entity_id)
        extract_html_data = extract_empenhos.extract()

        transform_raw_data = TransformRawDataDespesasSaude()
        transform_html_data = transform_raw_data.transform(extract_html_data)

        load_data = LoadDataDespesasSaude(self.__conn)
        load_data.load(transform_html_data, self.__year)
