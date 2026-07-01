import random

from collector.base_collector import BaseCollector


class MinesCollector(BaseCollector):

    def __init__(self):

        super().__init__("MINES")

    def collect(self):

        return {
            "mines": random.randint(3, 7),
            "board": [random.randint(0, 1) for _ in range(25)]
        }