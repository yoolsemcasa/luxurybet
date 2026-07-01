import telebot

from bots.base_bot import BaseBot

from config import TELEGRAM_TOKEN

from logs.logger import logger


class TelegramBot(BaseBot):

    def __init__(self):

        super().__init__("Telegram")

        self.bot = None

    def run(self):

        if not TELEGRAM_TOKEN:

            logger.warning("TELEGRAM_TOKEN não configurado.")

            return

        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)

        logger.info("Bot Telegram conectado.")

    def send_message(self, chat_id, text):

        if self.bot:

            self.bot.send_message(chat_id, text)