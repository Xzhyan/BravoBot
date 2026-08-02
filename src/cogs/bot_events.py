import discord
from discord.ext import commands

# core
from core.logger import addlog


class BotEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        addlog('bot_events', "Bot online")

        # Exibe no terminal de forma personalizada quando o bot esta online
        print("-" * 50)
        print(f"Bot: {self.bot.user}")
        print(f"ID: {self.bot.user.id}")
        print(f"Servidores: {len(self.bot.guilds)}")
        print("-" * 50)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """Bot foi adicionado em um servidor"""

        response = f"Entrei no servidor: {guild.name}"
        addlog('bot_events', response)
        print(response)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """Bot foi removido de um servidor"""

        response = f"Saí do servidor: {guild.name}"
        addlog('bot_events', response)
        print(response)


async def setup(bot: commands.Bot):
    await bot.add_cog(BotEvents(bot))
