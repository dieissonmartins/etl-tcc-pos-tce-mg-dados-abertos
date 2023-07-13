import os
from abc import ABC

import boto3
from dotenv import load_dotenv

from src.drivers.interfaces.storage_interface import StorageInterface


class Storage(StorageInterface, ABC):
    __bucket: boto3

    def __init__(self) -> None:
        # load envs
        load_dotenv()

        self.__bucket = self.connect_buckets()

    @property
    def connect_buckets(self) -> boto3:

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

        return s3