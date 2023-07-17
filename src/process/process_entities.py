class ProcessEntities:

    def run(self, entities, year):
        for models in entities.values():

            for file_path in models:
                self.pipeline_orgaos(file_path, year)

    def pipeline_orgaos(self, file_path, year):

        
