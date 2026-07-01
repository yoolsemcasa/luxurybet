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

        logger.info(f"[NOTIFIER] {title}")

        texto = f"{title}\n\n{message}"

        if self.telegram:

            try:

                logger.info("Mensagem preparada para Telegram.")

                # Futuramente:
                # self.telegram.send_message(...)

            except Exception as e:

                logger.exception(e)

        if self.discord:

            try:

                logger.info("Mensagem preparada para Discord.")

                # Futuramente:
                # self.discord.send_message(...)

            except Exception as e:

                logger.exception(e)