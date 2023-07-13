from src.drivers.storage import Storage

# entry point
if __name__ == '__main__':

    # connect storage by s3
    storage = Storage()

    # get file
    file_zip = storage.get_object('testsdataeng', 'tcemg/22.zip')

    # if not file
    if not file_zip:
        print('file not exists')
