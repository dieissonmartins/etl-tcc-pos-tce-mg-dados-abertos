from src.drivers.storage import Storage

# connect storage by s3
storage = Storage()

file_zip = storage.get_object('testsdataeng', 'tcemg/2022.zip')

if file_zip:
    print('file exists')
else:
    print('file not exists')
