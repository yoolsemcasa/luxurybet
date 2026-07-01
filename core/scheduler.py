import threading
import time

from logs.logger import logger


class Task:

    def __init__(self, name, interval, callback):

        self.name = name

        self.interval = interval

        self.callback = callback

        self.last_run = 0


class Scheduler:

    def __init__(self):

        self.running = False

        self.tasks = []

        self.thread = None

    def add_task(self, name, interval, callback):

        self.tasks.append(

            Task(name, interval, callback)

        )

        logger.info(f"Tarefa registrada: {name}")

    def loop(self):

        logger.info("Loop do Scheduler iniciado.")

        while self.running:

            now = time.time()

            for task in self.tasks:

                if now - task.last_run >= task.interval:

                    try:

                        task.callback()

                        task.last_run = now

                    except Exception as e:

                        logger.exception(e)

            time.sleep(0.2)

        logger.info("Loop do Scheduler encerrado.")

    def start(self):

        if self.running:

            return

        self.running = True

        self.thread = threading.Thread(

            target=self.loop,

            daemon=True

        )

        self.thread.start()

        logger.info("Scheduler iniciado.")

    def stop(self):

        self.running = False

        logger.info("Scheduler parado.")