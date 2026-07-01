import discord

from bots.base_bot import BaseBot

from config import DISCORD_TOKEN

from logs.logger import logger


class DiscordBot(BaseBot):

    def __init__(self):

        super().__init__("Discord")

        self.client = None

    def run(self):

        if not DISCORD_TOKEN:

            logger.warning("DISCORD_TOKEN não configurado.")

            return

        intents = discord.Intents.default()

        intents.message_content = True

        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready():

            logger.info(f"Discord conectado como {self.client.user}")

        self.client.run(DISCORD_TOKEN)