from database.init_db import init_database

from logs.logger import logger

from core.scheduler import Scheduler

from core.version import VERSION

from bots.telegram_bot import TelegramBot

from bots.discord_bot import DiscordBot

from services.notifier import Notifier


# ==========================
# Instâncias Globais
# ==========================

scheduler = Scheduler()

telegram = TelegramBot()

discord = DiscordBot()

notifier = Notifier()

# ==========================
# Tarefas do Scheduler
# ==========================

def heartbeat():

    logger.info("LuxuryBET Online")


# ==========================
# Inicialização do Sistema
# ==========================

def startup():

    logger.info("=" * 60)

    logger.info(f"LuxuryBET v{VERSION}")

    logger.info("Inicializando sistema...")

    # Banco de Dados
    init_database()

    logger.info("Banco SQLite iniciado.")

    # Bots
    telegram.start()

    discord.start()

    notifier.register_telegram(telegram)

    notifier.register_discord(discord)

    notifier.send(

    "LuxuryBET",

    "Sistema iniciado com sucesso."

    )

    # Scheduler
    scheduler.add_task(
        "heartbeat",
        10,
        heartbeat
    )

    scheduler.start()

    logger.info("Sistema iniciado.")

    logger.info("=" * 60)