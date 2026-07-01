from database.init_db import init_database

from logs.logger import logger

from core.version import VERSION

from core.application import Application

from collector.aviator import AviatorCollector
from collector.mines import MinesCollector


app = Application()


def heartbeat():

    logger.info("LuxuryBET Online")


def collector_job():

    resultados = app.collector_manager.execute()

    logger.info(resultados)


def startup():

    logger.info("=" * 60)

    logger.info(f"LuxuryBET v{VERSION}")

    logger.info("Inicializando sistema...")

    init_database()

    logger.info("Banco SQLite iniciado.")

    app.initialize()

    app.collector_manager.register(AviatorCollector())

    app.collector_manager.register(MinesCollector())

    app.scheduler.add_task(
        "heartbeat",
        10,
        heartbeat
    )

    app.scheduler.add_task(
        "collector",
        5,
        collector_job
    )

    app.scheduler.start()

    app.notifier.send(
        "LuxuryBET",
        "Sistema iniciado com sucesso."
    )

    logger.info("Sistema iniciado.")

    logger.info("=" * 60)