import os
from zipfile36 import ZipFile
import logging
import uuid

class FileZip:

    def extract_file(self, path):

        local_path = os.path.dirname(os.path.realpath(__file__))

        filepath = os.path.join(local_path, path)

        with ZipFile(filepath, mode='r') as file:

            # get the list of files and print it
            files = file.namelist()

            aux = {}

            # list fields
            for fl in files:

                if fl.startswith('2022/3145307/') and fl.endswith('.csv'):
                    # extract file
                    extract_path = file.extract(fl, path=local_path + '/tmp/')

                    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                    logging.info('Extraindo arquivo ' + extract_path)

                    folder_arr = fl.split("/")

                    entity_key = str(folder_arr[1])

                    if entity_key in aux:
                        aux[entity_key].append(fl)
                    else:
                        aux[entity_key] = [fl]

        entities = aux

        return entities
