import boto3
from dotenv import load_dotenv
import os

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
print(bucket_names)

# create new bucket
#new_bucket = s3.create_bucket(Bucket='bucker-by-boto3')

# delete bucket
#delete_bucket = s3.delete_bucket(Bucket='bucker-by-boto3')
