class ProcessEntities:

    def run(self, entities):
        for files_path in entities.values():

            for file_path in files_path:
                # etl orgaos
                self.pipeline_orgaos(file_path)

    def pipeline_orgaos(self, file_path):

        file_path_arr = file_path.split("/")

        model = file_path_arr[2]
        entity = file_path_arr[1]

        if not model == 'saude':
            return

        