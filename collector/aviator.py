import random

from collector.base_collector import BaseCollector


class AviatorCollector(BaseCollector):

    def __init__(self):

        super().__init__("AVIATOR")

    def collect(self):

        return {
            "multiplier": round(random.uniform(1.00, 15.00), 2)
        }