from threading import Thread

from logs.logger import logger


class BaseBot:

    def __init__(self, name):

        self.name = name

        self.running = False

        self.thread = None

    def run(self):
        pass

    def start(self):

        self.running = True

        self.thread = Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

        logger.info(f"{self.name} iniciado.")

    def stop(self):

        self.running = False

        logger.info(f"{self.name} parado.")