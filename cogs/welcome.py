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
            embed = discord.Embed(
                title="Welcome to the Server!",
                description=f"Hello {member.mention}, welcome to {member.guild.name}! We're glad to have you here. Feel free to introduce yourself and explore the channels. If you have any questions, don't hesitate to ask the moderators or other members. Enjoy your stay!",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
            
            await channel.send(embed=embed)

        else:
            print(f"No system channel found for {member.guild.name}. Cannot send welcome message.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))