from logs.logger import logger


class Notifier:

    def __init__(self):

        self.telegram = None
        self.discord = None

    def register_telegram(self, bot):

        self.telegram = bot

        logger.info("Telegram registrado no Notifier.")

    def register_discord(self, bot):

        self.discord = bot

        logger.info("Discord registrado no Notifier.")

    def send(self, title, message):

        logger.info(f"[EVENTO] {title}")

        texto = f"{title}\n\n{message}"

        if self.telegram:

            logger.info("Evento disponível para Telegram.")

            # Futuramente:
            # self.telegram.send_message(chat_id, texto)

        if self.discord:

            logger.info("Evento disponível para Discord.")

            # Futuramente:
            # self.discord.send_message(canal_id, texto)