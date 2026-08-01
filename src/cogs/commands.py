import discord
from discord import app_commands
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name='help',
        description="Mostrar a lista de comandos"
    )
    async def help(
        self,
        interaction: discord.Integration
    ):
        embed = discord.Embed(
            title="📚 Ajuda",
            description="Lista de comandos do bot",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="/help",
            value="Mostra esta mensagem.",
            inline=False
        )

        embed.add_field(
            name="/ping",
            value="Mostra a latência do bot.",
            inline=False
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Commands(bot)
    )
