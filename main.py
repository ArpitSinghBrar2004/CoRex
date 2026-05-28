from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv("TOKEN")

if not token:
    print("TOKEN is missing in .env")
else:
    class Corex(commands.Bot):
        def __init__(self):
            intents = discord.Intents.default()
            intents.members = True
            super().__init__(
                command_prefix="!",
                intents=intents
            )

        async def setup_hook(self):
            await self.load_extension("cogs.utility")
            await self.load_extension("cogs.welcome")
            await self.load_extension("cogs.left")
            await self.load_extension("cogs.logs")
            print("Utility cog loaded")
            print("Welcome cog loaded")
            print("Left cog loaded")
            print("Logs cog loaded")
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} slash commands")

        async def on_ready(self):
            print(f"{self.user} has connected to Discord!")

    bot = Corex()
    bot.run(token)