from abc import ABC, abstractmethod

import json
import logging
import requests

# TODO: build this out.
class TFCMigrator(ABC):

    def __init__(self, api_source, api_target, log_level):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(log_level)
        self._api_source = api_source
        self._api_target = api_target

    @abstractmethod
    def migrate_all(self):
        return []

    @abstractmethod
    def delete_all(self):
        return []