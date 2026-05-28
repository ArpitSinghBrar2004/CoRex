import discord
from discord.ext import commands
class Logs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        channel_id = 1508375532583129098
        channel = self.bot.get_channel(channel_id)
        if channel:
            embed = discord.Embed(
                title="Message Deleted",
                description=f"A message by {message.author.mention} was deleted in {message.channel.mention}.",
                color=discord.Color.orange()
            )
            embed.add_field(name="Content", value=message.content or "No content")
            embed.set_thumbnail(url=message.author.avatar.url if message.author.avatar else None)
            await channel.send(embed=embed)
        else:
            print(f"No system channel found for {message.guild.name}. Cannot log deleted message.")
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        channel_id = 1508375532583129098
        channel = self.bot.get_channel(channel_id)
        if channel:
            embed = discord.Embed(
                title="Message Edited",
                description=f"A message by {before.author.mention} was edited in {before.channel.mention}.",
                color=discord.Color.yellow()
            )
            embed.add_field(name="Before", value=before.content or "No content")
            embed.add_field(name="After", value=after.content or "No content")
            embed.set_thumbnail(url=before.author.avatar.url if before.author.avatar else None)
            await channel.send(embed=embed)
        else:
            print(f"No system channel found for {before.guild.name}. Cannot log edited message.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Logs(bot))