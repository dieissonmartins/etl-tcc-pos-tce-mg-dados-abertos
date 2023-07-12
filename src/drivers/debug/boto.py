import boto3
from dotenv import load_dotenv
import os
import logging

# load envs
load_dotenv()

service = os.getenv("STORAGE")
region_name = os.getenv("AWS_DEFAULT_REGION")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# connect buckets by s3
s3 = boto3.client(service,
                  region_name=region_name,
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# list buckets
buckets = s3.list_buckets()

bucket_names = buckets['Buckets']
# print(bucket_names)

# create new bucket
# new_bucket = s3.create_bucket(Bucket='bucker-by-boto3')

# delete bucket
# delete_bucket = s3.delete_bucket(Bucket='bucker-by-boto3')

local_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(local_path, 'tmp')

# create dir
try:
    os.mkdir(path)
except OSError as error:
    logging.error("not create dir")

# info
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Baixando arquivo...')

# download file
try:
    file = s3.download_file(Bucket='testsdataeng', Key='tcemg/2022.zip', Filename='tmp/2022.zip')
except:
    logging.error("not donwload file")
