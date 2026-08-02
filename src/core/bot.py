import discord
from discord.ext import commands

# app_command_errors
from handlers.app_command_errors import ErrorHandler


class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
    
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        await self.load_cogs()

        # registra os handlers de error
        bot.tree.on_error = ErrorHandler().on_error

        # sincroniza os slash commands
        await self.tree.sync()
        print('[SUCCESS] slash commands carregados com sucesso')

    async def load_cogs(self):
        cogs = [
            'cogs.commands',
            'cogs.bot_events',
        ]

        for cog in cogs:
            await self.load_extension(cog)
            print(f"[SUCCESS] Cog carregada: {cog}")


bot = DiscordBot()
