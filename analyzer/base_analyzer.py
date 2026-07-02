from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):

    def __init__(self, repository):

        self.repository = repository

    @abstractmethod
    def analyze(self):
        pass