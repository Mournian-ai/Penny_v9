import asyncio
import os
from twitchio import Client
from shared.event_bus import event_bus

TOKEN = os.getenv("TWITCH_OAUTH_TOKEN")
CHANNEL = os.getenv("TWITCH_CHANNEL")


class TwitchBot(Client):
    def __init__(self):
        super().__init__(token=TOKEN)

    async def event_ready(self):
        event_bus.add_log("Connected to Twitch chat")
        if CHANNEL:
            await self.join_channels([CHANNEL])

    async def event_message(self, message):
        if message.echo:
            return
        event_bus.add_chat(f"{message.author.name}: {message.content}")


def start_bot():
    if not TOKEN or not CHANNEL:
        event_bus.add_log("Twitch credentials not configured")
        return
    bot = TwitchBot()
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start())
