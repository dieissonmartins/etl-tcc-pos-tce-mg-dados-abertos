from src.drivers.storage import Storage
import logging

from src.drivers.zipfile import FileZip
from src.process.process_entities import ProcessEntities

# entry point
if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # connect storage by s3
    storage = Storage()

    year = 2022
    bucket = 'testsdataeng'
    path_storage = 'tcemg/' + str(year) + '.zip'
    path_local = 'tmp/' + str(year) + '.zip'

    # get file
    file_zip = storage.get_object(bucket, path_storage)

    # if not file
    if not file_zip:
        logging.info('Arquivo ' + path_storage + 'não encotrado no bucket')
    else:

        is_file_local = storage.is_file_local(path_local)

        if not is_file_local:
            logging.info('Baixando novo arquivo')
            file = storage.download_file(bucket, path_storage, path_local)
        else:
            logging.info('Arquivo .zip ja exite')

            file_zip = FileZip()
            entities = file_zip.extract_file(path_local)

            process = ProcessEntities()
            process.run(entities, year)