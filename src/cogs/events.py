import discord
from discord.ext import commands

# core
from core.logger import addlog


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        response = f"{member} entrou em {member.guild.name}"
        addlog('events', response)
        print(response)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        response = f"{member} saiu de {member.guild.name}"
        addlog('events', response)
        print(response)

async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))
