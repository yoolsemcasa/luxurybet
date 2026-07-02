from flask import signals

from database.init_db import init_database

from logs.logger import logger

from core.version import VERSION

from core.application import Application

from collector.aviator import AviatorCollector
from collector.mines import MinesCollector


app = Application()


# ==========================================
# Tarefas do Scheduler
# ==========================================

def heartbeat():

    logger.info("LuxuryBET Online")


def collector_job():

    resultados = app.collector_manager.execute()

    for game, data in resultados:

        if game == "AVIATOR":

            app.repository.save_aviator(
                data["multiplier"]
            )

        elif game == "MINES":

            app.repository.save_mines(
                data["mines"],
                data["board"]
            )

    logger.info(
        f"{len(resultados)} coletores executados."
    )

    stats = app.aviator_analyzer.analyze(100)

    if stats:

        logger.info("===== AVIATOR =====")

        logger.info(
            f"Rodadas: {stats['total']}"
        )

        logger.info(
            f"Média: {stats['average']}x"
        )

        logger.info(
            f"Maior: {stats['highest']}x"
        )

        logger.info(
            f"Menor: {stats['lowest']}x"
        )

        logger.info(
            f">=2x: {stats['above_2']}%"
        )

        logger.info(
            f">=5x: {stats['above_5']}%"
        )

        logger.info(
            f">=10x: {stats['above_10']}%"
        )
        mines_stats = app.mines_analyzer.analyze(100)

    if mines_stats:

        logger.info("===== MINES =====")

        logger.info(
        f"Rodadas: {mines_stats['total']}"
        )

        logger.info(
        f"Distribuição de minas: {mines_stats['mines']}"
        )

        logger.info(
        f"Posições menos frequentes: {mines_stats['safest']}"
        )

        logger.info(
        f"Posições mais frequentes: {mines_stats['riskiest']}"
        )

        logger.info("Coleta salva no banco.")

        logger.info(f"{len(resultados)} coletores executados.")

        logger.info("Coleta salva no banco.")

        signals = app.signal_engine.generate(
        stats,
        mines_stats
        )

    for signal in signals:

        logger.info(f"[{signal.level}] {signal.title}")

        logger.info(signal.message)

        app.notifier.send(
        signal.title,
        signal.message
        )


# ==========================================
# Inicialização do Sistema
# ==========================================

def startup():

    logger.info("=" * 60)

    logger.info(f"LuxuryBET v{VERSION}")

    logger.info("Inicializando sistema...")

    # Banco de Dados
    init_database()

    logger.info("Banco SQLite iniciado.")

    # Inicializa os serviços
    app.initialize()

    # Registra os coletores
    app.collector_manager.register(
        AviatorCollector()
    )

    app.collector_manager.register(
        MinesCollector()
    )

    # Scheduler
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