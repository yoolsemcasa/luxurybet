from logs.logger import logger

from core.startup import scheduler, telegram


def shutdown():

    logger.info("Encerrando sistema...")

    telegram.stop()

    scheduler.stop()

    logger.info("LuxuryBET encerrado.")