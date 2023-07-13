from src.drivers.storage import Storage

# connect storage by s3
storage = Storage()

bukects = storage.list_buckets()
