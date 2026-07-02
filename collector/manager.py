from logs.logger import logger


class CollectorManager:

    def __init__(self):

        self.collectors = []

    def register(self, collector):

        self.collectors.append(collector)

        logger.info(f"Collector registrado: {collector.name}")

    def execute(self):

        logger.info("Executando coletores...")

        results = []

        for collector in self.collectors:

            data = collector.run()

            if data:

                results.append(

                    (

                        collector.name,

                        data

                    )

                )

        return results