from __future__ import annotations

import os
from typing import Dict, Any
import boto3
from dotenv import load_dotenv
import logging

from src.drivers.interfaces.storage_interface import StorageInterface


class Storage(StorageInterface):
    __storage: boto3
    __path: str

    def __init__(self) -> None:

        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

        # load envs
        load_dotenv()

        self.__storage = self.connect()

        self.__path = os.path.dirname(os.path.realpath(__file__))

    def connect(self) -> boto3:

        logging.info('Conecta no bucket')

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

    #def list_buckets(self) -> Dict[str, str | int]:
    #    buckets = self.__storage.list_buckets()
    #    return buckets

    def get_object(self, bucket, path) -> Any:
        try:
            object_file = self.__storage.get_object(Bucket=bucket, Key=path)
            return object_file

        except Exception:
            return False

    def download_file(self, bucket, key, path) -> Any:
        try:
            path = os.path.join(self.__path, path)
            object_file = self.__storage.download_file(Bucket=bucket, Key=key, Filename=path)

            return object_file

        except Exception:
            return False

    def is_file_local(self, path)-> bool:

        path_full = os.path.join(self.__path, path)

        check_file = os.path.isfile(path_full)

        return check_file