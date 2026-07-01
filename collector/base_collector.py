from abc import ABC, abstractmethod

from logs.logger import logger


class BaseCollector(ABC):

    def __init__(self, name):

        self.name = name

        self.enabled = True

    @abstractmethod
    def collect(self):
        pass

    def run(self):

        if not self.enabled:
            return

        logger.info(f"[{self.name}] Executando coleta...")

        return self.collect()