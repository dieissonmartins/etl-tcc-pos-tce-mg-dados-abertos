# Import the required method
from zipfile36 import ZipFile
import os
import logging

local_path = os.path.dirname(os.path.realpath(__file__))

filepath = os.path.join(local_path, 'tmp/2022.zip')

with ZipFile(filepath, mode='r') as file:

    # get the list of files and print it
    files = file.namelist()

    # list fields
    for fl in files:

        # extract file
        extract_path = file.extract(fl, path=local_path + '/tmp/')

        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Extraindo arquivo ' + extract_path)