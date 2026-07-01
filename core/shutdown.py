from logs.logger import logger

from core.startup import app


def shutdown():

    logger.info("Encerrando sistema...")

    app.telegram.stop()

    app.discord.stop()

    app.scheduler.stop()

    logger.info("LuxuryBET encerrado.")