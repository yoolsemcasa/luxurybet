from logs.logger import logger

from core.scheduler import Scheduler

from bots.telegram_bot import TelegramBot
from bots.discord_bot import DiscordBot

from database.repository import Repository

from services.notifier import Notifier

from collector.manager import CollectorManager

from analyzer.aviator import AviatorAnalyzer
from analyzer.mines import MinesAnalyzer

from signals.signal_engine import SignalEngine

class Application:

    def __init__(self):

        logger.info("Criando Application...")

        self.scheduler = Scheduler()

        self.telegram = TelegramBot()

        self.discord = DiscordBot()

        self.notifier = Notifier()

        self.collector_manager = CollectorManager()

        self.repository = Repository()

        self.aviator_analyzer = AviatorAnalyzer(
        self.repository
        )

        self.mines_analyzer = MinesAnalyzer(
        self.repository
        )

        self.signal_engine = SignalEngine()

    def initialize(self):

        logger.info("Inicializando serviços...")

        # Bots
        self.telegram.start()

        self.discord.start()

        # Notifier
        self.notifier.register_telegram(self.telegram)

        self.notifier.register_discord(self.discord)