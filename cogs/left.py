import discord
from discord.ext import commands
class Left(commands.Cog):
    def __init__(self ,bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_remove(self,member: discord.Member):
        channel_id = 1508375532583129098
        channel = self.bot.get_channel(channel_id)
        if channel:
            embed = discord.Embed(
                title="Goodbye!",
                description=f"{member.mention} has left the server. We're sorry to see you go!",
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
            await channel.send(embed=embed)
        else:
            print(f"No system channel found for {member.guild.name}. Cannot send goodbye message.")
async def setup(bot: commands.Bot):
    await bot.add_cog(Left(bot))