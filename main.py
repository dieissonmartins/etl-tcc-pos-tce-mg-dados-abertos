from src.drivers.storage import Storage

# connect storage by s3
storage = Storage()

buckets = storage.list_buckets()

bucket_names = buckets['Buckets']

