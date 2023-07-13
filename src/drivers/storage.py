import os
from typing import Dict, Any

import boto3
from dotenv import load_dotenv

from src.drivers.interfaces.storage_interface import StorageInterface


class Storage(StorageInterface):
    __storage: boto3

    def __init__(self) -> None:
        # load envs
        load_dotenv()

        self.__storage = self.connect()

    def connect(self) -> boto3:
        service = os.getenv("STORAGE")
        region_name = os.getenv("AWS_DEFAULT_REGION")
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        # connect buckets by s3
        s3 = boto3.client(service,
                          region_name=region_name,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

        return s3

    def list_buckets(self) -> Dict[str, str | int]:
        buckets = self.__storage.list_buckets()
        return buckets

    def get_object(self, bucket, path) -> Any:
        try:
            object_file = self.__storage.get_object(Bucket=bucket, Key=path)
            return object_file

        except Exception:
            return False
