from logs.logger import logger

from core.scheduler import Scheduler

from bots.telegram_bot import TelegramBot
from bots.discord_bot import DiscordBot

from database.repository import Repository

from services.notifier import Notifier

from collector.manager import CollectorManager


class Application:

    def __init__(self):

        logger.info("Criando Application...")

        self.scheduler = Scheduler()

        self.telegram = TelegramBot()

        self.discord = DiscordBot()

        self.notifier = Notifier()

        self.collector_manager = CollectorManager()

        self.repository = Repository()

    def initialize(self):

        logger.info("Inicializando serviços...")

        # Bots
        self.telegram.start()

        self.discord.start()

        # Notifier
        self.notifier.register_telegram(self.telegram)

        self.notifier.register_discord(self.discord)