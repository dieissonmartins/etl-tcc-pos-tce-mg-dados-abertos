from abc import ABC, abstractmethod

import boto3


class StorageInterface(ABC):

    @abstractmethod
    def connect_bucket(self) -> boto3:
        pass
