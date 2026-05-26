import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = 1508375532583129098
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(f"Welcome to the server, {member.mention}!")
        else:
            print(f"No system channel found for {member.guild.name}. Cannot send welcome message.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))