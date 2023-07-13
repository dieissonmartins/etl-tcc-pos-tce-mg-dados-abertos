from abc import ABC, abstractmethod
from typing import Dict

import boto3


class StorageInterface(ABC):

    @abstractmethod
    def connect(self) -> boto3:
        pass

    @abstractmethod
    def list_buckets(self) -> Dict[str, str | int]:
        pass
