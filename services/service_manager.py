from logs.logger import logger


class ServiceManager:

    def __init__(self):

        self.services = []

    def register(self, service):

        self.services.append(service)

        logger.info(f"Serviço registrado: {service.name}")

    def start_all(self):

        logger.info("Iniciando serviços...")

        for service in self.services:

            service.start()

    def stop_all(self):

        logger.info("Finalizando serviços...")

        for service in self.services:

            service.stop()