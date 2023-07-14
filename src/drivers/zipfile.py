import os
from zipfile36 import ZipFile
import logging


class FileZip:

    def extract_file(self, path):

        local_path = os.path.dirname(os.path.realpath(__file__))

        filepath = os.path.join(local_path, path)

        with ZipFile(filepath, mode='r') as file:

            # get the list of files and print it
            files = file.namelist()

            # list fields
            for fl in files:

                if fl.startswith('2022/3100401/') and fl.endswith('.csv'):

                    # extract file
                    extract_path = file.extract(fl, path=local_path + '/tmp/')

                    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                    logging.info('Extraindo arquivo ' + extract_path)

                    folder_arr = extract_path.split("/")
