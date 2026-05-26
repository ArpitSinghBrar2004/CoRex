import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot =bot
    @app_commands.command(name="ping",description="Respond with the bot's latency")
    async def ping(self,interaction:discord.Interaction):
        latency = round(self.bot.latency *1000)
        embed = discord.Embed(
            title="Corex Status",
            description="CoreRex is responding successfully.",
            color=discord.Color(value=0x00BFFF)
        )
        embed.add_field(name="Latency",value=f"{latency}ms")
        await interaction.response.send_message(embed=embed)
async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))